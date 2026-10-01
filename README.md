<div align="center">

<img src="https://raw.githubusercontent.com/Ashishkumar1854/Ashishkumar1854/main/assets/banners.gif" width="100%" alt="Ashish Kumar Banner"/>

</div>

<!-- Animated Typing Header -->
<div align="center">
<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=28&pause=800&color=6E57E0&background=00000000&center=true&vCenter=true&multiline=false&repeat=true&width=900&height=55&lines=%F0%9F%91%8B+Hey%2C+I'm+Ashish+Kumar;%F0%9F%9A%80+Full+Stack+Developer+%7C+MERN+%7C+SaaS;%F0%9F%8F%86+National+Hackathon+Finalist;%E2%9A%A1+Building+Production-Ready+Products" alt="Typing SVG" />
</div>

<br/>

<!-- Status Badges Row -->
<div align="center">

[![Micro1 Certified](https://img.shields.io/badge/%F0%9F%9B%A1%EF%B8%8F_Micro1-Certified_Talent-3FB950?style=for-the-badge&labelColor=0D1117)](https://micro1.ai)&nbsp;
[![Hackathon](https://img.shields.io/badge/%F0%9F%8F%86_NCIIPC--AICTE-Top_230_%2F_26K_Teams-FF6B6B?style=for-the-badge&labelColor=0D1117)](https://github.com/Ashishkumar1854)&nbsp;
[![CIH](https://img.shields.io/badge/%F0%9F%A5%87_CIH_2.0-National_Finalist-BB9AF7?style=for-the-badge&labelColor=0D1117)](https://github.com/Ashishkumar1854)&nbsp;
[![Profile Views](https://komarev.com/ghpvc/?username=Ashishkumar1854&label=Profile+Views&color=7AA2F7&style=for-the-badge&labelColor=0D1117)](https://github.com/Ashishkumar1854)

</div>

<br/>

---

## 🧑‍💻 About Me

```yaml
🧑 Name: Ashish Kumar
💼 Role: Full Stack Developer |  AI Agenet Developer | SaaS Product builder
🏢 Experience: 1 year production experience across full-stack engineering roles
🎓 Education: B.Tech IT — Rungta College of Engineering (Graduated 2026)
📍 Location: Raipur, Chhattisgarh, India 🇮🇳
🌐 Portfolio: https://ashishportfolio.aigateway.in
💡 Focus: Multi-Tenant SaaS · REST APIs · PostgreSQL · Docker · AWS EC2
🎯 Stats: 200 Coding Problems · 80% Acceptance Rate
```

---

## 💼 Production Experience

### Full Stack Engineer — Botivate Services LLP
`Aug 2026 - Present` · Raipur, India

Sole full-stack engineer across 4 production systems spanning B2B SaaS, multi-tenant ERP, and AI-powered platforms. Owned the entire software lifecycle — architecture, development, deployment, and infra — end-to-end.

**🏭 Jewellery Factory — Multi-Tenant B2B Jewellery Platform** *(Next.js 15, PostgreSQL, Prisma, AWS EC2 + S3 + CloudFront)*
- Designed and built a 4-role multi-tenant SaaS from scratch: Manufacturer, Purchase Manager (Head Office), Store Manager, and Kiosk — each with strict data isolation via route guards and cookie-based HMAC-SHA256 auth.
- Architected a full order lifecycle covering Kiosk (walk-in), Catalog (B2B), and Custom Design orders, with per-branch approval flows, real-time order chat, and Mark Completed handover — all on a single polymorphic `order_messages` table.
- Integrated AI Features microservice (Python + Docker, deployed on Hugging Face): catalog image generation, virtual try-on (2-step OpenAI pipeline → transparent PNG), AI product description, and OpenCLIP-powered visual similarity search backed by PostgreSQL `pgvector` — replaced Qdrant with zero extra infra.
- Migrated all media from Cloudinary to AWS S3 + CloudFront with presigned direct-upload; set up CORS and IAM correctly across 4 separate origin configs.
- Shipped automated Karigar (artisan) assignment flow for order-to-dispatch, PIN-walled per-branch restock ordering, and retailer intelligence/analytics dashboard.
- Deployed on AWS EC2 via Docker with auto-migration on container start; database on AWS RDS Postgres; configured Nginx + Certbot TLS for custom production domains.

**🏢 HR FMS — Enterprise HR & Payroll System** *(Next.js + Node.js/Express, PostgreSQL, Supabase)*
- Built a 5-role HR platform (Employee, HOD, HR Specialist, Admin, Canteen Manager) with full RBAC — route guards enforce data scope at the DB query level (`WHERE employee_id = user.id`).
- Delivered 18+ HR modules end-to-end: biometric attendance with GPS + face-capture watermarking, monthly payroll engine (base + OT at 1.5× + advance EMI deductions), leave management (multi-stage HOD→HR approval), PF/ESIC compliance, gate pass, canteen, resignation workflow, and job vacancy + application portal.
- Built a CSV/BioTime device sync pipeline to import biometric punch data from physical attendance hardware into the system nightly.
- Generated downloadable payslips, salary-difference reports, and zero-basic-salary audit reports directly from the backend as structured Excel/PDF.

**📦 Real Estate CRM & ERP** *(React + Vite, Supabase, Hono)*
- Built a multi-vertical CRM for Real Estate, Insurance, and Mutual Fund operations with automated lead numbering (L-RE-0001, L-IN-0001, L-MF-0001) and conditional vertical-specific fields.
- Delivered telecalling workflow: Pending Tracker → Call Outcome (Received/Expected/Not Interested/Need Meeting) → Customer Master auto-conversion, with a full chronological audit trail.
- Added Excel bulk import, one-click caller performance reports (by lead type, caller, and month), and a fully mobile-responsive layout with boundary-clamped dropdowns and momentum scrolling.

**🏪 Procurement & Inventory Management System** *(Node.js, Express, Prisma, PostgreSQL, React + Vite, AWS S3)*
- Built an end-to-end procurement platform covering a 7-stage indent lifecycle: Indent Creation → Department Head Approval → Vendor Quotation Collection → Three-Party Comparative Approval → Purchase Order Generation → Store In (Goods Receipt) → Store Out (Material Issuance).
- Implemented automated delay tracking at each stage, real-time inventory updates on receipt and issue events, and WhatsApp Business API notifications for purchase order and approval alerts.
- Built vendor management with rate comparison engine supporting multi-vendor quotation history, rate revision cycles, and price benchmarking before PO award.
- Designed JSON-based role permissions for modular page-level access control, and integrated AWS S3 for document storage (indents, POs, bills, and delivery receipts).

**🚗 Car Detailing ERP** *(Next.js, Supabase, PostgreSQL)*
- Designed and built a full detailing studio ERP: job orders, delivery tracking, finance, sales, and workforce modules under a single dashboard.
- Implemented an attendance and salary engine: WebRTC camera frame capture → HTML5 Canvas watermark stamping (Name + Timestamp + GPS coords) → Cloudinary upload pipeline, plus a monthly payroll calculator with OT and EMI deductions.

### Product Engineer - Full Stack SaaS — Phoneo
`May 2026 - Jul 2026` · Bhilai, India

- Architected KarigarHQ, a multi-tenant Repair ERP with 4 role tiers and branch-level data isolation.
- Built the complete 9-stage repair lifecycle from customer intake through billing, payment, and handover.
- Reduced deployment time from 45 minutes to under 5 minutes using GitHub Actions, Docker, Nginx, and AWS EC2.
- Added 20 backend integration tests covering authentication, RBAC, tenant isolation, inventory, billing, and workflow transitions.

### Frontend Developer — Phoneo
`Feb 2026 - Apr 2026` · Bhilai, India

- Launched the React.js and Next.js marketing website that supported onboarding of 4,300 mobile shops across 100 cities.
- Integrated lead capture, demo scheduling, and CTA funnels with backend REST APIs, reducing manual sales outreach by 60%.
- Fixed a live demo-booking production issue within 2 hours with zero client downtime and no data loss.

### Web Developer — Rungta College Incubation Center
`Feb 2023 - Nov 2024` · Bhilai, India

- Founded and led a startup product through 4 major full-stack release cycles over 21 months.
- Maintained Git workflows and PR review standards across a 4-person team with zero production rollbacks.

---

## 🚀 Featured Projects

<table>
<tr>
<td width="50%" valign="top">

### 🛠️ KarigarHQ — Repair ERP SaaS

**Multi-Tenant SaaS · 4-Tier RBAC · 9-Stage Lifecycle**

> Repair business ERP with branch-level data isolation, automated workflows, and containerized deployment.

- 👤 4-Role tier: Super Admin → Owner → Admin → Technician
- ⚙️ Full 9-stage job lifecycle automation
- 🐳 Docker + GitHub Actions CI/CD on AWS EC2
- 📉 Deploy time: **45 min → <5 min**
- ✅ 20 backend integration tests

[![Architecture](https://img.shields.io/badge/Enterprise-Multi--Tenant_ERP-4F46E5?style=flat-square&labelColor=0D1117)](https://github.com/AshishOrgs)
[![Status](https://img.shields.io/badge/Status-Production_Active-3FB950?style=flat-square&labelColor=0D1117)](#)

![React](https://img.shields.io/badge/React-0D1117?style=flat-square&logo=react&logoColor=61DAFB)
![Node.js](https://img.shields.io/badge/Node.js-0D1117?style=flat-square&logo=node.js&logoColor=339933)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-0D1117?style=flat-square&logo=postgresql&logoColor=4169E1)
![Docker](https://img.shields.io/badge/Docker-0D1117?style=flat-square&logo=docker&logoColor=2496ED)
![AWS](https://img.shields.io/badge/AWS_EC2-0D1117?style=flat-square&logo=amazonaws&logoColor=FF9900)

</td>
<td width="50%" valign="top">

### 🤖 AiGateway — Multi-Tenant AI SaaS

**Turborepo Monorepo · LLM Agents · n8n Automation**

> AI-powered lead research platform with autonomous scoring agents and human-in-the-loop validation.

- 🏗️ Turborepo: 3 Next.js apps + Python FastAPI microservices
- 🧠 n8n + OpenAI/Gemini lead scoring agent (0–100)
- 🔒 Human-in-the-loop gate before CRM insertion
- 🗄️ Tenant-aware MongoDB + PostgreSQL schema isolation

[![GitHub Repo](https://img.shields.io/badge/🔗_GitHub-aiGateway-0D1117?style=flat-square&logo=github&labelColor=0D1117)](https://github.com/Ashishkumar1854/aiGateway)
[![Portfolio Live](https://img.shields.io/badge/🌐_Portfolio-aigateway.in-0D1117?style=flat-square&labelColor=0D1117&color=8A2BE2)](https://ashishportfolio.aigateway.in)

![Next.js](https://img.shields.io/badge/Next.js_14-0D1117?style=flat-square&logo=next.js&logoColor=white)
![n8n](https://img.shields.io/badge/n8n-0D1117?style=flat-square&logo=n8n&logoColor=FF6584)
![Turborepo](https://img.shields.io/badge/Turborepo-0D1117?style=flat-square&logo=turborepo&logoColor=EF4444)
![MongoDB](https://img.shields.io/badge/MongoDB-0D1117?style=flat-square&logo=mongodb&logoColor=47A248)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🗳️ Secure Biometric Voting System

**OpenCV Face Recognition · 97% Accuracy · ACID-Compliant**

> Tamper-proof digital voting with computer vision authentication to eliminate proxy voting.

- 👁️ OpenCV + FastAPI face recognition — **97% accuracy**
- 🔐 ACID-compliant session state + encrypted audit trail
- 🚫 Zero proxy voting in live authentication flow

[![Demo](https://img.shields.io/badge/🔗_Live_Demo-LinkedIn-0D1117?style=flat-square&labelColor=0D1117&color=0A66C2)](https://www.linkedin.com/posts/ashishkumar1854_electioncommissionofindia-blockchainvoting-activity-7346224352129875970-zjVA)
[![GitHub Repo](https://img.shields.io/badge/🔗_GitHub-Voting_Repo-0D1117?style=flat-square&logo=github&labelColor=0D1117)](https://github.com/Ashishkumar1854/FaceBaseed-Faster-and-Secure-Voting-system)

![React](https://img.shields.io/badge/React-0D1117?style=flat-square&logo=react&logoColor=61DAFB)
![Python](https://img.shields.io/badge/Python-0D1117?style=flat-square&logo=python&logoColor=3776AB)
![Node.js](https://img.shields.io/badge/Node.js-0D1117?style=flat-square&logo=node.js&logoColor=339933)

</td>
<td width="50%" valign="top">

### 📱 Phoneo — SaaS Marketing Platform

**B2B SaaS · 4,300+ Shops · 100 Cities**

> High-converting seller acquisition platform for mobile retail stores with lead capture & funnel optimization.

- 🏪 Serving **4,300+ mobile stores** across 100 cities
- 🔄 Maintaining the live SaaS platform used by **50 active retailers**
- 📈 Lead capture & demo booking funnels — **60% friction reduction**
- 🔧 Fixed critical production bugs in **<2 hours**, zero downtime

[![Live Site](https://img.shields.io/badge/🔗_Live_Site-seller.phoneo.in-0D1117?style=flat-square&labelColor=0D1117&color=00C7B7)](https://seller.phoneo.in)
[![Status](https://img.shields.io/badge/Status-Live_Production-3FB950?style=flat-square&labelColor=0D1117)](#)

![React](https://img.shields.io/badge/React-0D1117?style=flat-square&logo=react&logoColor=61DAFB)
![Next.js](https://img.shields.io/badge/Next.js-0D1117?style=flat-square&logo=next.js&logoColor=white)
![REST API](https://img.shields.io/badge/REST_APIs-0D1117?style=flat-square&logo=postman&logoColor=FF6C37)

</td>
</tr>
</table>

---

## 🛠️ Tech Stack

<div align="center">

### ⚡ Languages

[![Languages](https://skillicons.dev/icons?i=js,ts,python,java,mysql&theme=dark)](https://skillicons.dev)

### 🖥️ Frontend

[![Frontend](https://skillicons.dev/icons?i=react,nextjs,redux,tailwind,html,css&theme=dark)](https://skillicons.dev)

![Axios](https://img.shields.io/badge/Axios-0D1117?style=flat-square&logo=axios&logoColor=5A29E4)

### ⚙️ Backend & APIs

[![Backend](https://skillicons.dev/icons?i=nodejs,express,fastapi,flask&theme=dark)](https://skillicons.dev)

![Socket.io](https://img.shields.io/badge/Socket.io-0D1117?style=flat-square&logo=socket.io&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-0D1117?style=flat-square&logo=jsonwebtokens&logoColor=white)
![WebSockets](https://img.shields.io/badge/WebSockets-0D1117?style=flat-square&logo=socketdotio&logoColor=white)
![Webhooks](https://img.shields.io/badge/Webhooks-0D1117?style=flat-square&logo=webhook&logoColor=white)

### 🗄️ Databases & ORM

[![Databases](https://skillicons.dev/icons?i=postgresql,mongodb,prisma,redis,mysql,firebase&theme=dark)](https://skillicons.dev)

### 🔁 Automation & Integrations

![OpenAI](https://img.shields.io/badge/OpenAI-0D1117?style=for-the-badge&logo=openai&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Gemini-0D1117?style=for-the-badge&logo=googlegemini&logoColor=8E75B2)
![LLMs](https://img.shields.io/badge/LLMs-0D1117?style=for-the-badge&logo=huggingface&logoColor=FFD21E)
![n8n](https://img.shields.io/badge/n8n-0D1117?style=for-the-badge&logo=n8n&logoColor=FF6584)
![WhatsApp Business API](https://img.shields.io/badge/WhatsApp_Business_API-0D1117?style=for-the-badge&logo=whatsapp&logoColor=25D366)
![RAG](https://img.shields.io/badge/RAG_Pipelines-0D1117?style=for-the-badge&logo=openai&logoColor=white)

### 🐳 DevOps & Infrastructure

[![DevOps](https://skillicons.dev/icons?i=docker,githubactions,aws,nginx,git&theme=dark)](https://skillicons.dev)

![Nginx](https://img.shields.io/badge/Nginx-0D1117?style=flat-square&logo=nginx&logoColor=009639)
![Turborepo](https://img.shields.io/badge/Turborepo-0D1117?style=flat-square&logo=turborepo&logoColor=EF4444)

### 🧰 Tools & Platforms

[![Tools](https://skillicons.dev/icons?i=postman,vscode,vercel,netlify&theme=dark)](https://skillicons.dev)

</div>

---

## 🏆 Achievements & Certifications

<table>
<tr>
<td>🥇</td>
<td><strong>National Finalist - NCIIPC-AICTE Pentathon 2025</strong></td>
<td>Top <strong>230 / 26,000 teams</strong> • India's Premier Cybersecurity Hackathon</td>
</tr>
<tr>
<td>🏆</td>
<td><strong>National Finalist - CIH 2.0 National Hackathon 2025</strong></td>
<td>Recognized for breakthrough tech innovation at the national stage</td>
</tr>
<tr>
<td>🛡️</td>
<td><strong>Micro1 Certified Developer</strong></td>
<td>AI-driven rigorous technical vetting on global talent platform</td>
</tr>
<tr>
<td>📊</td>
<td><strong>AMCAT — Top 15 Percentile</strong></td>
<td>Excelled in quantitative, logical & domain assessments</td>
</tr>
<tr>
<td>🌐</td>
<td><strong>OSS Contributor</strong></td>
<td><a href="https://github.com/wtasg/meetonline/pull/316">PR #316 Merged</a> @ wtasg/meetonline — Favicon, branding & HTML optimization</td>
</tr>
</table>

---

## 📊 GitHub Stats & Analytics

<p align="center">

[![Trophies](https://github-profile-trophy.vercel.app/?username=Ashishkumar1854&theme=tokyonight&no-frame=true&no-background=true&margin-w=10&column=6)](https://github.com/Ashishkumar1854)

</p>

<p align="center">

[![Ashish's GitHub Stats](https://github-readme-stats.vercel.app/api?username=Ashishkumar1854&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0D1117&count_private=true&include_all_commits=true&hide=contribs&rank_icon=github&custom_title=Ashish%27s+GitHub+Stats)](https://github.com/Ashishkumar1854)
[![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=Ashishkumar1854&layout=compact&theme=tokyonight&hide_border=true&bg_color=0D1117&langs_count=8&custom_title=Top+Languages)](https://github.com/Ashishkumar1854)

</p>

<p align="center">

[![GitHub Streak](https://streak-stats.demolab.com/?user=Ashishkumar1854&theme=tokyonight&hide_border=true&background=0D1117&date_format=j%20M%5B%20Y%5D)](https://git.io/streak-stats)

</p>

<p align="center">

[![Ashish's github activity graph](https://github-readme-activity-graph.vercel.app/graph?username=Ashishkumar1854&theme=tokyo-night&hide_border=true&bg_color=0D1117&custom_title=Contribution+Activity+Graph)](https://github.com/ashutosh00710/github-readme-activity-graph)

</p>

---

## 🤝 Let's Connect

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Ashish_Kumar-0D1117?style=for-the-badge&logo=linkedin&logoColor=0A66C2&labelColor=0D1117)](https://linkedin.com/in/ashishkumar1854)
[![Portfolio](https://img.shields.io/badge/Portfolio-aigateway.in-0D1117?style=for-the-badge&logo=vercel&logoColor=BB9AF7&labelColor=0D1117)](https://ashishportfolio.aigateway.in)
[![Email](https://img.shields.io/badge/Email-ashishyadav.dev%40gmail.com-0D1117?style=for-the-badge&logo=gmail&logoColor=EA4335&labelColor=0D1117)](mailto:ashishyadav.dev@gmail.com)
[![LeetCode](https://img.shields.io/badge/LeetCode-Ashishkumar1854-0D1117?style=for-the-badge&logo=leetcode&logoColor=FFA116&labelColor=0D1117)](https://leetcode.com/Ashishkumar1854)
[![HackerRank](https://img.shields.io/badge/HackerRank-Ashishkumar-0D1117?style=for-the-badge&logo=hackerrank&logoColor=00EA64&labelColor=0D1117)](https://hackerrank.com/Ashishkumar)
[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Ashishkumar-0D1117?style=for-the-badge&logo=geeksforgeeks&logoColor=2F8D46&labelColor=0D1117)](https://geeksforgeeks.org/user/ashishkumar1854)

</div>

<br/>

<p align="center">

![Footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer&text=Thanks+for+visiting!+%E2%AD%90+Star+my+repos+if+you+like+them!&fontSize=16&fontColor=fff&animation=twinkling&fontAlignY=65)

</p>
