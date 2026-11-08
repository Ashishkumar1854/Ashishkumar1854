#!/usr/bin/env python3
"""Fill the README's merged-PR section with data from the GitHub API.

The section can include pull requests from private repositories. The
GITHUB_TOKEN used here must be able to read those repositories (a classic PAT
with the `repo` scope, saved as the GH_PAT secret).

Environment variables:
  GITHUB_TOKEN   token that can read your private repos (required)
  GH_USERNAME    GitHub login whose PRs to list (default: Ashishkumar1854)
  SHOW_REPO_NAME "true" shows private repo names; anything else hides them
                 as "Private repo" (default: hide)
  README_PATH    file to update (default: README.md)
  SAMPLE_JSON    path to a saved API response; used instead of calling the API
"""
import datetime as dt
import html
import json
import urllib.parse
import os
import re
import sys
import urllib.request

START = "<!-- PR-SECTION:START -->"
END = "<!-- PR-SECTION:END -->"
TOP_N = 10

QUERY = """
query($q: String!, $cursor: String) {
  search(query: $q, type: ISSUE, first: 50, after: $cursor) {
    pageInfo { hasNextPage endCursor }
    nodes {
      ... on PullRequest {
        title body url number mergedAt additions deletions changedFiles headRefName
        repository { nameWithOwner isPrivate }
        commits(first: 20) { nodes { commit { messageHeadline } } }
      }
    }
  }
}
"""


def fetch_prs(token, username, since):
    q = f"is:pr is:merged author:{username} merged:>={since}"
    prs, cursor = [], None
    while True:
        payload = json.dumps({"query": QUERY, "variables": {"q": q, "cursor": cursor}}).encode()
        req = urllib.request.Request(
            "https://api.github.com/graphql",
            data=payload,
            headers={"Authorization": f"bearer {token}", "User-Agent": "readme-pr-section"},
        )
        with urllib.request.urlopen(req) as resp:
            data = json.load(resp)
        if "errors" in data:
            sys.exit(f"GitHub API error: {data['errors']}")
        search = data["data"]["search"]
        prs.extend(n for n in search["nodes"] if n)
        if not search["pageInfo"]["hasNextPage"] or len(prs) >= 300:
            return prs
        cursor = search["pageInfo"]["endCursor"]


def clean(text, limit):
    """Shorten text to one line and escape it for HTML."""
    text = re.sub(r"<[^>]+>", "", text or "")
    text = re.sub(r"\s+", " ", text).strip()
    text = text if len(text) <= limit else text[: limit - 1].rstrip() + "…"
    return html.escape(text, quote=True)


def summary_line(body):
    """First real sentence of the PR description, skipping headings, checklists and images."""
    for line in (body or "").splitlines():
        line = line.strip()
        if not line or line.startswith(("#", "- [", "* [", "![", "<!--", "```", "|", ">")):
            continue
        line = re.sub(r"^[-*]\s+", "", line)
        line = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", line)  # keep link text, drop URL
        return clean(line.replace("`", "").replace("*", ""), 140)
    return ""


def norm(text):
    return re.sub(r"[^a-z0-9]", "", (text or "").lower())


def commit_headlines(pr):
    """Commit subjects of the PR, without merge commits or duplicates."""
    seen, out = set(), []
    for node in (pr.get("commits") or {}).get("nodes", []):
        line = (node.get("commit") or {}).get("messageHeadline", "").strip()
        if not line or line.lower().startswith("merge ") or norm(line) in seen:
            continue
        seen.add(norm(line))
        out.append(line)
    return out


def describe(pr):
    """Return (title, summary) that say what the PR did.

    GitHub fills the title with the branch name ("Ashish mod") when a PR has
    several commits, and long titles are cut with "…" and continued in the body.
    """
    title, body = pr["title"], pr.get("body") or ""
    if title.endswith("…") and body.startswith("…"):
        rest, _, body = body[1:].partition("\n")
        title = title[:-1] + rest
    commits = commit_headlines(pr)
    generic = norm(title) == norm(pr.get("headRefName")) or len(norm(title)) < 12
    if generic and commits:
        title, commits = commits[0], commits[1:]
    summary = summary_line(body)  # already cleaned
    if not summary and commits:
        extra = len(commits) - 2
        more = f" (+{extra} more commit{'s' if extra > 1 else ''})" if extra > 0 else ""
        summary = clean("; ".join(commits[:2]), 140 - len(more)) + more
    return clean(title, 90), summary


def repo_label(pr, show_names):
    repo = pr["repository"]
    name = html.escape(repo["nameWithOwner"])
    if repo["isPrivate"]:
        return f"🔒 {name}" if show_names else "🔒 Private repo"
    return f'<a href="https://github.com/{name}">{name}</a>'


def title_cell(pr):
    title = describe(pr)[0]
    # Links to private PRs give visitors a 404, so only public PRs are linked.
    return title if pr["repository"]["isPrivate"] else f'<a href="{html.escape(pr["url"])}">{title}</a>'


def nice_date(iso):
    """'2026-11-06T…' -> '06 Nov 2026' with non-breaking spaces so it stays on one line."""
    return dt.date.fromisoformat(iso[:10]).strftime("%d %b %Y").replace(" ", "&nbsp;")


def changes(pr):
    return f"<code>+{pr['additions']:,}</code>&nbsp;<code>-{pr['deletions']:,}</code>"


def banner(month_name, merged_this_month, merged_year):
    """Animated typing heading, same style as the banner at the top of the profile."""
    lines = [
        "🔀 Merged Pull Requests",
        f"🚀 {merged_this_month} PRs merged in {month_name}",
        f"🔥 {merged_year} PRs merged in the last 12 months",
    ]
    params = {
        "font": "JetBrains Mono", "weight": "700", "size": "30", "pause": "1200",
        "color": "3FB950", "background": "00000000", "center": "true", "vCenter": "true",
        "width": "800", "height": "60", "lines": ";".join(lines),
    }
    url = "https://readme-typing-svg.demolab.com?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    return [
        '<div align="center">',
        f'  <img src="{html.escape(url)}" alt="Merged Pull Requests" />',
        "</div>",
    ]


def render(prs, show_names, today):
    prs = sorted(prs, key=lambda p: p["mergedAt"], reverse=True)
    month_start = today.replace(day=1).isoformat()
    this_month = [p for p in prs if p["mergedAt"][:10] >= month_start]
    month_name = today.strftime("%B %Y")

    lines = [START, ""]
    lines += banner(month_name, len(this_month), len(prs))
    lines.append("")
    lines.append(
        "> Most of these pull requests are in private client repositories, so the links and code "
        "are not public. This list is updated automatically every day from the GitHub API."
    )
    lines.append("")

    added = sum(p["additions"] for p in this_month)
    removed = sum(p["deletions"] for p in this_month)
    lines.append(
        f"**{month_name}:** {len(this_month)} PRs merged · `+{added:,}` / `-{removed:,}` lines · "
        f"**Last 12 months:** {len(prs)} PRs merged"
    )
    lines.append("")

    if this_month:
        # Prefer PRs that have a real description; fall back to the biggest overall.
        described = [p for p in this_month if describe(p)[1]] or this_month
        top = max(described, key=lambda p: p["additions"] + p["deletions"])
        lines.append(f"### ⭐ Top PR of {month_name}")
        lines.append("")
        lines.append(f"**{title_cell(top)}** — {repo_label(top, show_names)}")
        summary = describe(top)[1]
        if summary:
            lines.append("")
            lines.append(f"> {summary}")
        lines.append("")
        lines.append(
            f"Merged {nice_date(top['mergedAt'])} · {top['changedFiles']} files · "
            f"`+{top['additions']:,}` / `-{top['deletions']:,}`"
        )
        lines.append("")

    recent = prs[:TOP_N]
    if not recent:
        lines += ["_No merged pull requests found yet._", "", END]
        return "\n".join(lines)

    # HTML table, because markdown tables can't merge cells: PRs merged on the
    # same day share one date cell (rowspan).
    lines.append(f"### 🕒 Last {len(recent)} merged PRs")
    lines.append("")
    lines.append("<table>")
    lines.append(
        "  <tr><th>Merged</th><th>Pull request</th><th>What it does</th>"
        "<th>Repo</th><th>Changes</th></tr>"
    )
    for i, p in enumerate(recent):
        day = p["mergedAt"][:10]
        cells = []
        if i == 0 or recent[i - 1]["mergedAt"][:10] != day:
            span = sum(1 for q in recent[i:] if q["mergedAt"][:10] == day)
            cells.append(f'<td rowspan="{span}" align="center"><b>{nice_date(p["mergedAt"])}</b></td>')
        cells += [
            f"<td>{title_cell(p)}</td>",
            f"<td>{describe(p)[1] or '—'}</td>",
            f"<td>{repo_label(p, show_names)}</td>",
            f"<td>{changes(p)}</td>",
        ]
        lines.append("  <tr>" + "".join(cells) + "</tr>")
    lines.append("</table>")
    lines += ["", END]
    return "\n".join(lines)


def main():
    username = os.environ.get("GH_USERNAME", "Ashishkumar1854")
    show_names = os.environ.get("SHOW_REPO_NAME", "").lower() == "true"
    readme_path = os.environ.get("README_PATH", "README.md")
    today = dt.date.today()

    sample = os.environ.get("SAMPLE_JSON")
    if sample:
        with open(sample) as f:
            prs = json.load(f)
    else:
        token = os.environ.get("GITHUB_TOKEN")
        if not token:
            sys.exit("GITHUB_TOKEN is not set")
        prs = fetch_prs(token, username, (today - dt.timedelta(days=365)).isoformat())

    with open(readme_path) as f:
        readme = f.read()
    if START not in readme or END not in readme:
        sys.exit(f"README is missing the {START} / {END} markers")

    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    updated = pattern.sub(lambda _: render(prs, show_names, today), readme)
    with open(readme_path, "w") as f:
        f.write(updated)
    print(f"Wrote {len(prs)} PRs to {readme_path}")


if __name__ == "__main__":
    main()
