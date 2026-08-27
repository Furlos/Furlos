<p align="center">
  <img src="./assets/hero.svg" width="100%" alt="Furlos — Python Backend Engineer" />
</p>

<p align="center">
  <b>Python backend • APIs • PostgreSQL • async systems • AI integrations • automation</b>
</p>

<p align="center">
  <a href="https://github.com/Furlos?tab=repositories">Repositories</a> ·
  <a href="https://github.com/Furlos/alfabank-AI-bot">AI Banking Assistant</a> ·
  <a href="https://github.com/Furlos/vtb_optimization">PostgreSQL Optimization</a> ·
  <a href="https://github.com/Furlos/Marzban_bot">Backend Automation</a>
</p>

---

## `> whoami`

I build backend systems in **Python** — from API and database layers to async workers, integrations, bots and AI-powered services.

I like projects where backend engineering is visible: clear boundaries, predictable data flow, useful abstractions, observability, deployment and performance rather than just “it runs on my machine”.

```python
class Furlos:
    focus = ["Python", "Backend", "PostgreSQL", "AI integrations"]
    building = ["APIs", "services", "automation", "data-heavy systems"]
    principles = ["simple > clever", "measure > guess", "ship > overthink"]
```

<p align="center">
  <img src="./assets/backend-map.svg" width="100%" alt="Backend engineering constellation" />
</p>

## ⚙️ Backend toolbox

<table>
<tr>
<td valign="top" width="33%">

**Core**

`Python` · `asyncio` · `OOP`  
`REST APIs` · `service design`  
`Telegram automation`

</td>
<td valign="top" width="33%">

**Data & infrastructure**

`PostgreSQL` · `SQL`  
`Docker` · `Docker Compose`  
`Linux` · `Git`

</td>
<td valign="top" width="33%">

**AI & integrations**

`LLM services` · `AI APIs`  
`bot ↔ service architecture`  
`external API integrations`

</td>
</tr>
</table>

<p align="center">
  <img src="./assets/request-flow.svg" width="100%" alt="Request lifecycle" />
</p>

## 🚀 Selected engineering work

<table>
<tr>
<td width="50%" valign="top">

### 🤖 [Alfabank AI Bot](https://github.com/Furlos/alfabank-AI-bot)

AI assistant for small business in Telegram. The project is split into a **Telegram bot**, an **AI service** and an **LLM/model layer**, and is packaged with Docker Compose.

`Python` `AI/LLM` `Telegram` `Docker`

</td>
<td width="50%" valign="top">

### 🐘 [PostgreSQL OLAP Optimization](https://github.com/Furlos/vtb_optimization)

Performance lab for analytical workloads over millions of synthetic banking records. Uses **BRIN / partial / composite indexes**, materialized views and repeatable query timing to compare raw OLAP queries with optimized paths.

`Python` `PostgreSQL` `OLAP` `Performance`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### ⚙️ [Marzban Bot](https://github.com/Furlos/Marzban_bot)

Backend + Telegram automation project with a separated **backend service**, **bot layer** and Docker Compose environment.

`Python` `Backend` `Telegram` `Docker`

</td>
<td width="50%" valign="top">

### 📝 [MemoPad](https://github.com/Furlos/MemoPad)

Local notes web app with authentication and CRUD flows, built with Flask and SQLite.

`Python` `Flask` `SQLite` `Web`

</td>
</tr>
</table>

## 🧬 How I think about backend

```text
client request
    │
    ▼
validate ──► authorize ──► domain logic ──► persistence
    │                            │              │
    │                            └──► integrations
    │
    └──► useful errors + logs + metrics

            then measure the slow path and make it faster.
```

I’m especially interested in **Python backend development**, database-heavy systems, service architecture, optimization and practical AI integration.

---

<p align="center">
  <sub>Built as code, not as a screenshot. Every visual on this page is an SVG stored in this repository.</sub>
</p>
