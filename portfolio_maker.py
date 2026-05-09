import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

# ── Data file ──────────────────────────────────────────────────────────────────
DATA_FILE = "portfolio_data.json"

DEFAULT_DATA = {
    "hero": {
        "name_line1": "Yosef",
        "name_line2": "Setiawan",
        "subtitle": "Game & App Developer · Python · Depok, Indonesia",
        "description": "I made and modified app and games on how i always imagined them to be, like snakes that coop play with no collision , sudoku that tells on what number each box can have , or wheel spinner with score system, etc.",
        "availability_tag": "◆ Available for work",
        "itchio_url": "https://cloudbv.itch.io",
        "show_availability": True,
    },
    "projects": [
        {
            "title": "Snake Classic (with a twist)",
            "type": "Game · Python / Pygame",
            "desc": "Snake, but with a twist where there is no collision, instead you and your friend keep going and eating until the arena is full , just like how i always wanted a snake game to be.",
            "tags": "Python,Pygame,Browser,PC",
            "tag_colors": "cyan,cyan,red,red",
            "link": "https://cloudbv.itch.io/snake-classic",
        },
        {
            "title": "Sudoku Classic (with a twist)",
            "type": "Game · Python / Pygame",
            "desc": "Sudoku but instead of writing the available number using some pencil tool (ive always found that annoying), the game just automatically does it for you.",
            "tags": "Python,Pygame,Browser,PC",
            "tag_colors": "cyan,cyan,red,red",
            "link": "https://cloudbv.itch.io/sudoku-classic-with-a-twist",
        },
        {
            "title": "Wheel Spinner with Score System",
            "type": "App · Python / Tkinter",
            "desc": "A classroom tool built for real teaching use. score system where the more you score the less change you will be picked, score tracking, attendance toggling, CSV export, and auto-backups. Used it myself while teaching high school.",
            "tags": "Python,Tkinter,Tool,PC",
            "tag_colors": "cyan,cyan,gold,gold",
            "link": "",
        },
        {
            "title": "Modded Arcuz 2",
            "type": "Mod · Flash / JPEXS",
            "desc": "Arcuz 2 the way I always wanted it , homing projectiles, doubled XP, better drops, 100% crafting, buffed skills, secret shop for found only item. A complete overhaul mod.",
            "tags": "Modding,Flash,Browser",
            "tag_colors": "gold,gold,red",
            "link": "https://cloudbv.itch.io/modded-arcuz-2",
        },
    ],
    "about": {
        "paragraphs": [
            "I'm a <strong>self-taught Python developer</strong> and indie game creator based in Depok, West Java. My background is in <strong>Industrial Engineering</strong> (President University, 2023) — which means I think in systems, processes, and optimization.",
            "I got into programming because I was tired of simple mobile games being ruined by ads and paywalls. So I started building my own — clean, focused, and actually fun.",
            "I also spent a year <strong>teaching Python and Informatika</strong> to high school students, which taught me how to explain complex things simply.",
            "Currently expanding into <strong>data science and machine learning</strong> through Kaggle, while continuing to build and publish games and tools.",
        ],
        "english_note": "English: C2 Proficient (EF SET 76/100)",
        "skills": [
            {"name": "Game Dev (Python/Pygame)", "level": "Primary",      "pct": 85, "color": "red"},
            {"name": "App Dev (Tkinter)",         "level": "Strong",       "pct": 80, "color": "red"},
            {"name": "Python (General)",           "level": "Strong",       "pct": 82, "color": "cyan"},
            {"name": "Data Analysis / Pandas",     "level": "Intermediate", "pct": 65, "color": "cyan"},
            {"name": "Machine Learning",           "level": "Intermediate", "pct": 60, "color": "gold"},
            {"name": "SQL",                        "level": "Intermediate", "pct": 55, "color": "gold"},
            {"name": "Web (HTML/CSS)",             "level": "Basic",        "pct": 45, "color": "gray"},
        ],
    },
    "certs": [
        {
            "issuer": "freeCodeCamp",
            "note": "3 certs · ~900hrs",
            "items": [
                {"name": "Data Analysis with Python",      "date": "May 2024"},
                {"name": "Scientific Computing with Python","date": "Apr 2024"},
                {"name": "Responsive Web Design",          "date": "Feb 2024"},
            ],
        },
        {
            "issuer": "Kaggle",
            "note": "17 certs",
            "items": [
                {"name": "Machine Learning Explainability",        "date": "Dec 2024"},
                {"name": "Computer Vision",                        "date": "Dec 2024"},
                {"name": "Intro to Deep Learning",                 "date": "Dec 2024"},
                {"name": "Geospatial Analysis",                    "date": "Dec 2024"},
                {"name": "Time Series",                            "date": "Dec 2024"},
                {"name": "Intro to AI Ethics",                     "date": "Dec 2024"},
                {"name": "Feature Engineering",                    "date": "Nov 2024"},
                {"name": "Intermediate Machine Learning",          "date": "Oct 2024"},
                {"name": "Game AI & Reinforcement Learning",       "date": "Oct 2024"},
                {"name": "Advanced SQL",                           "date": "Oct 2024"},
                {"name": "Data Cleaning · Data Visualization",    "date": "Sep–Oct 2024"},
                {"name": "Intro to ML · Pandas · SQL · Python",   "date": "Aug 2024"},
            ],
        },
        {
            "issuer": "EF SET",
            "note": "English",
            "items": [
                {"name": "C2 Proficient — Score 76/100", "date": "Aug 2024"},
            ],
        },
    ],
    "contact": {
        "email": "yosefsetiawan2001@gmail.com",
        "links": [
            {"label": "itch.io",  "url": "https://cloudbv.itch.io"},
            {"label": "GitHub",   "url": "https://github.com/cloudBV"},
        ],
        "tagline": "Got a project, a job, or just want to say hi?",
    },
    "footer": {
        "name": "Yosef Setiawan",
        "year": "2026",
        "location": "Depok, Indonesia",
    },
}

# ── Load / Save ────────────────────────────────────────────────────────────────
def load_data():
    import copy
    base = copy.deepcopy(DEFAULT_DATA)
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                saved = json.load(f)
            for key in base:
                if key in saved:
                    base[key] = saved[key]
        except Exception:
            pass
    return base

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# ── HTML Generator ─────────────────────────────────────────────────────────────
def generate_html(data):
    hero    = data["hero"]
    projects= data["projects"]
    about   = data["about"]
    certs   = data["certs"]
    contact = data["contact"]
    footer  = data["footer"]

    # ── projects html ──
    def tag_html(tag, color):
        return f'<span class="tag tag-{color}">{tag}</span>'

    def project_card(p):
        raw_link = p["link"].strip()
        if raw_link and not raw_link.startswith(("http://", "https://")):
            raw_link = "https://" + raw_link
        link_open  = f'<a href="{raw_link}" target="_blank" class="project-card reveal">' if raw_link else '<div class="project-card reveal">'
        link_close = '</a>' if raw_link else '</div>'
        arrow      = '<span class="project-link">↗</span>' if raw_link else ''
        tags_html  = ""
        tags   = [t.strip() for t in p["tags"].split(",") if t.strip()]
        colors = [c.strip() for c in p["tag_colors"].split(",") if c.strip()]
        for i, t in enumerate(tags):
            c = colors[i] if i < len(colors) else "gray"
            tags_html += tag_html(t, c)
        return f"""
      {link_open}
        {arrow}
        <div class="project-type">{p['type']}</div>
        <div class="project-title">{p['title']}</div>
        <p class="project-desc">{p['desc']}</p>
        <div class="project-tags">{tags_html}</div>
      {link_close}"""

    projects_html = "\n".join(project_card(p) for p in projects)

    # ── about paragraphs ──
    paras_html = "\n".join(f"        <p>{para}</p>" for para in about["paragraphs"])
    if about.get("english_note"):
        paras_html += f'\n        <p style="color: var(--cyan); margin-top: 1.5rem;">{about["english_note"]}</p>'

    # ── skills ──
    def skill_row(s):
        color_class = "" if s["color"] == "red" else f' {s["color"]}' if s["color"] in ("cyan","gold") else ""
        bg_style    = " background: var(--gray);" if s["color"] == "gray" else ""
        return f"""
        <div class="skill-row">
          <div class="skill-label"><span>{s['name']}</span><span>{s['level']}</span></div>
          <div class="skill-bar"><div class="skill-fill{color_class}" style="width: {s['pct']}%;{bg_style}"></div></div>
        </div>"""

    skills_html = "\n".join(skill_row(s) for s in about["skills"])

    # ── certs ──
    def cert_group(g):
        items_html = "\n".join(
            f'          <div class="cert-item"><span>{i["name"]}</span><span class="cert-date">{i["date"]}</span></div>'
            for i in g["items"]
        )
        return f"""
      <div class="cert-group reveal">
        <div class="cert-issuer">{g['issuer']} <span class="cert-count">{g['note']}</span></div>
{items_html}
      </div>"""

    certs_html = "\n".join(cert_group(g) for g in certs)

    # ── contact links ──
    contact_links_html = "\n".join(
        f'        <a href="{lk["url"]}" target="_blank" class="contact-link">{lk["label"]}</a>'
        for lk in contact["links"]
    )

    # ── availability tag ──
    avail_html = ""
    if hero.get("show_availability"):
        avail_html = f'      <div class="hero-tag">{hero["availability_tag"]}</div>\n'

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{hero['name_line1']} {hero['name_line2']} — {hero['subtitle'].split('·')[0].strip()}</title>
  <link href="https://fonts.googleapis.com/css2?family=Space+Mono:ital,wght@0,400;0,700;1,400&family=Syne:wght@400;700;800&display=swap" rel="stylesheet" />
  <style>
    :root {{
      --bg:       #0d0d0f;
      --bg2:      #13131a;
      --surface:  #1a1a26;
      --red:      #e94560;
      --gold:     #f5a623;
      --cyan:     #00d2ff;
      --white:    #f0f0f0;
      --gray:     #888;
      --border:   #2a2a3a;
    }}
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ scroll-behavior: smooth; }}
    body {{
      background: var(--bg);
      color: var(--white);
      font-family: 'Space Mono', monospace;
      line-height: 1.6;
      overflow-x: hidden;
    }}
    body::before {{
      content: '';
      position: fixed;
      inset: 0;
      background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.04'/%3E%3C/svg%3E");
      pointer-events: none;
      z-index: 999;
      opacity: 0.4;
    }}
    nav {{
      position: fixed;
      top: 0; left: 0; right: 0;
      z-index: 100;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 1.2rem 3rem;
      background: rgba(13,13,15,0.85);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
    }}
    .nav-logo {{
      font-family: 'Syne', sans-serif;
      font-weight: 800;
      font-size: 1.1rem;
      color: var(--cyan);
      letter-spacing: 0.05em;
      text-decoration: none;
    }}
    .nav-links {{ display: flex; gap: 2rem; list-style: none; }}
    .nav-links a {{
      color: var(--gray);
      text-decoration: none;
      font-size: 0.75rem;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      transition: color 0.2s;
    }}
    .nav-links a:hover {{ color: var(--cyan); }}
    #hero {{
      min-height: 100vh;
      display: flex;
      align-items: center;
      padding: 8rem 3rem 4rem;
      position: relative;
      overflow: hidden;
    }}
    .hero-grid {{
      position: absolute;
      inset: 0;
      background-image:
        linear-gradient(var(--border) 1px, transparent 1px),
        linear-gradient(90deg, var(--border) 1px, transparent 1px);
      background-size: 60px 60px;
      opacity: 0.3;
      mask-image: radial-gradient(ellipse at 50% 50%, black 30%, transparent 80%);
    }}
    .hero-glow {{
      position: absolute;
      width: 600px; height: 600px;
      background: radial-gradient(circle, rgba(233,69,96,0.12) 0%, transparent 70%);
      top: 50%; left: 60%;
      transform: translate(-50%, -50%);
      pointer-events: none;
    }}
    .hero-content {{ position: relative; max-width: 900px; }}
    .hero-tag {{
      display: inline-block;
      font-size: 0.7rem;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: var(--red);
      border: 1px solid var(--red);
      padding: 0.3rem 0.8rem;
      margin-bottom: 1.5rem;
      animation: fadeUp 0.6s ease both;
    }}
    .hero-name {{
      font-family: 'Syne', sans-serif;
      font-weight: 800;
      font-size: clamp(3rem, 8vw, 7rem);
      line-height: 1;
      letter-spacing: -0.02em;
      margin-bottom: 0.5rem;
      animation: fadeUp 0.6s 0.1s ease both;
    }}
    .hero-name span {{ color: var(--red); }}
    .hero-subtitle {{
      font-family: 'Syne', sans-serif;
      font-size: clamp(1rem, 2.5vw, 1.5rem);
      color: var(--gold);
      font-weight: 700;
      margin-bottom: 1.5rem;
      animation: fadeUp 0.6s 0.2s ease both;
    }}
    .hero-desc {{
      font-size: 0.85rem;
      color: var(--gray);
      max-width: 520px;
      margin-bottom: 2.5rem;
      animation: fadeUp 0.6s 0.3s ease both;
    }}
    .hero-btns {{ display: flex; gap: 1rem; flex-wrap: wrap; animation: fadeUp 0.6s 0.4s ease both; }}
    .btn {{
      display: inline-block;
      padding: 0.75rem 1.8rem;
      font-family: 'Space Mono', monospace;
      font-size: 0.75rem;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      text-decoration: none;
      transition: all 0.2s;
      cursor: pointer;
      border: none;
    }}
    .btn-primary {{ background: var(--red); color: white; }}
    .btn-primary:hover {{ background: #ff6b84; transform: translateY(-2px); }}
    .btn-outline {{ background: transparent; color: var(--cyan); border: 1px solid var(--cyan); }}
    .btn-outline:hover {{ background: var(--cyan); color: var(--bg); transform: translateY(-2px); }}
    .hero-scroll {{
      position: absolute;
      bottom: 2rem;
      left: 50%;
      transform: translateX(-50%);
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0.5rem;
      color: var(--gray);
      font-size: 0.65rem;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      animation: fadeUp 0.6s 0.6s ease both;
    }}
    .scroll-line {{
      width: 1px; height: 40px;
      background: linear-gradient(to bottom, var(--gray), transparent);
      animation: scrollPulse 1.5s ease-in-out infinite;
    }}
    section {{ padding: 6rem 3rem; max-width: 1100px; margin: 0 auto; }}
    .section-label {{
      font-size: 0.65rem;
      letter-spacing: 0.25em;
      text-transform: uppercase;
      color: var(--red);
      margin-bottom: 0.5rem;
      display: flex;
      align-items: center;
      gap: 0.8rem;
    }}
    .section-label::after {{
      content: '';
      flex: 1;
      max-width: 60px;
      height: 1px;
      background: var(--red);
    }}
    .section-title {{
      font-family: 'Syne', sans-serif;
      font-weight: 800;
      font-size: clamp(1.8rem, 4vw, 3rem);
      margin-bottom: 3rem;
      line-height: 1.1;
    }}
    .projects-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 1.5rem;
    }}
    .project-card {{
      background: var(--surface);
      border: 1px solid var(--border);
      padding: 2rem;
      position: relative;
      overflow: hidden;
      transition: transform 0.2s, border-color 0.2s;
      text-decoration: none;
      color: inherit;
      display: block;
    }}
    .project-card::before {{
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0;
      height: 2px;
      background: var(--red);
      transform: scaleX(0);
      transform-origin: left;
      transition: transform 0.3s;
    }}
    .project-card:hover {{ transform: translateY(-4px); border-color: var(--red); }}
    .project-card:hover::before {{ transform: scaleX(1); }}
    .project-type {{ font-size: 0.6rem; letter-spacing: 0.2em; text-transform: uppercase; color: var(--gold); margin-bottom: 0.8rem; }}
    .project-title {{ font-family: 'Syne', sans-serif; font-weight: 700; font-size: 1.2rem; margin-bottom: 0.8rem; color: var(--white); }}
    .project-desc {{ font-size: 0.78rem; color: var(--gray); line-height: 1.7; margin-bottom: 1.2rem; }}
    .project-tags {{ display: flex; flex-wrap: wrap; gap: 0.5rem; }}
    .tag {{ font-size: 0.6rem; letter-spacing: 0.1em; text-transform: uppercase; padding: 0.25rem 0.6rem; border: 1px solid var(--border); color: var(--gray); }}
    .tag-cyan {{ border-color: var(--cyan); color: var(--cyan); }}
    .tag-red {{ border-color: var(--red); color: var(--red); }}
    .tag-gold {{ border-color: var(--gold); color: var(--gold); }}
    .project-link {{ position: absolute; top: 1.5rem; right: 1.5rem; color: var(--gray); font-size: 0.8rem; transition: color 0.2s; }}
    .project-card:hover .project-link {{ color: var(--red); }}
    .about-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: start; }}
    .about-text p {{ font-size: 0.85rem; color: var(--gray); margin-bottom: 1rem; line-height: 1.8; }}
    .about-text p strong {{ color: var(--white); }}
    .skills-list {{ display: flex; flex-direction: column; gap: 1.2rem; }}
    .skill-row {{ display: flex; flex-direction: column; gap: 0.4rem; }}
    .skill-label {{ display: flex; justify-content: space-between; font-size: 0.7rem; letter-spacing: 0.1em; text-transform: uppercase; }}
    .skill-label span:first-child {{ color: var(--white); }}
    .skill-label span:last-child {{ color: var(--gray); }}
    .skill-bar {{ height: 2px; background: var(--border); position: relative; }}
    .skill-fill {{ position: absolute; top: 0; left: 0; height: 100%; background: var(--red); transition: width 1s ease; }}
    .skill-fill.cyan {{ background: var(--cyan); }}
    .skill-fill.gold {{ background: var(--gold); }}
    .certs-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; }}
    .cert-group {{ background: var(--surface); border: 1px solid var(--border); padding: 1.5rem; }}
    .cert-issuer {{
      font-family: 'Syne', sans-serif;
      font-weight: 700;
      font-size: 0.85rem;
      color: var(--gold);
      margin-bottom: 1rem;
      padding-bottom: 0.8rem;
      border-bottom: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .cert-count {{ font-family: 'Space Mono', monospace; font-size: 0.65rem; color: var(--gray); }}
    .cert-item {{ font-size: 0.72rem; color: var(--gray); padding: 0.3rem 0; border-bottom: 1px solid rgba(255,255,255,0.03); display: flex; justify-content: space-between; }}
    .cert-item:last-child {{ border-bottom: none; }}
    .cert-date {{ color: var(--border); font-size: 0.65rem; }}
    #contact {{ text-align: center; padding: 6rem 3rem; position: relative; }}
    .contact-glow {{
      position: absolute;
      width: 400px; height: 400px;
      background: radial-gradient(circle, rgba(0,210,255,0.08) 0%, transparent 70%);
      top: 50%; left: 50%;
      transform: translate(-50%, -50%);
      pointer-events: none;
    }}
    .contact-inner {{ position: relative; max-width: 600px; margin: 0 auto; }}
    .contact-inner .section-label {{ justify-content: center; }}
    .contact-inner .section-label::after {{ display: none; }}
    .contact-email {{
      font-family: 'Syne', sans-serif;
      font-size: clamp(1rem, 2.5vw, 1.6rem);
      font-weight: 800;
      color: var(--cyan);
      text-decoration: none;
      display: block;
      margin: 1.5rem 0;
      transition: color 0.2s;
      word-break: break-all;
    }}
    .contact-email:hover {{ color: var(--red); }}
    .contact-links {{ display: flex; justify-content: center; gap: 1.5rem; flex-wrap: wrap; margin-top: 2rem; }}
    .contact-link {{
      font-size: 0.7rem;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      color: var(--gray);
      text-decoration: none;
      padding-bottom: 2px;
      border-bottom: 1px solid var(--border);
      transition: color 0.2s, border-color 0.2s;
    }}
    .contact-link:hover {{ color: var(--cyan); border-color: var(--cyan); }}
    footer {{
      border-top: 1px solid var(--border);
      padding: 2rem 3rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.65rem;
      color: var(--gray);
      letter-spacing: 0.1em;
    }}
    .divider {{
      width: 100%;
      height: 1px;
      background: linear-gradient(to right, transparent, var(--border), transparent);
    }}
    @keyframes fadeUp {{
      from {{ opacity: 0; transform: translateY(20px); }}
      to   {{ opacity: 1; transform: translateY(0); }}
    }}
    @keyframes scrollPulse {{
      0%, 100% {{ opacity: 1; }}
      50% {{ opacity: 0.3; }}
    }}
    .reveal {{ opacity: 0; transform: translateY(30px); transition: opacity 0.7s ease, transform 0.7s ease; }}
    .reveal.visible {{ opacity: 1; transform: translateY(0); }}
    @media (max-width: 700px) {{
      nav {{ padding: 1rem 1.5rem; }}
      .nav-links {{ gap: 1rem; }}
      #hero {{ padding: 7rem 1.5rem 4rem; }}
      section {{ padding: 4rem 1.5rem; }}
      .about-grid {{ grid-template-columns: 1fr; gap: 2rem; }}
      footer {{ flex-direction: column; gap: 0.5rem; text-align: center; }}
    }}
  </style>
</head>
<body>

  <nav>
    <a href="#hero" class="nav-logo">cloudbv</a>
    <ul class="nav-links">
      <li><a href="#projects">Projects</a></li>
      <li><a href="#about">About</a></li>
      <li><a href="#certs">Certs</a></li>
      <li><a href="#contact">Contact</a></li>
    </ul>
  </nav>

  <div id="hero">
    <div class="hero-grid"></div>
    <div class="hero-glow"></div>
    <div class="hero-content">
{avail_html}      <h1 class="hero-name">{hero['name_line1']}<br><span>{hero['name_line2']}</span></h1>
      <p class="hero-subtitle">{hero['subtitle']}</p>
      <p class="hero-desc">{hero['description']}</p>
      <div class="hero-btns">
        <a href="#projects" class="btn btn-primary">See My Work</a>
        <a href="{hero['itchio_url']}" target="_blank" class="btn btn-outline">itch.io →</a>
      </div>
    </div>
    <div class="hero-scroll">
      <div class="scroll-line"></div>
      scroll
    </div>
  </div>

  <section id="projects">
    <div class="section-label reveal">Projects</div>
    <h2 class="section-title reveal">Things I've Built</h2>
    <div class="projects-grid">
{projects_html}
    </div>
  </section>

  <div class="divider"></div>

  <section id="about">
    <div class="section-label reveal">About</div>
    <h2 class="section-title reveal">Who I Am</h2>
    <div class="about-grid">
      <div class="about-text reveal">
{paras_html}
      </div>
      <div class="skills-list reveal">
{skills_html}
      </div>
    </div>
  </section>

  <div class="divider"></div>

  <section id="certs">
    <div class="section-label reveal">Credentials</div>
    <h2 class="section-title reveal">Certifications</h2>
    <div class="certs-grid">
{certs_html}
    </div>
  </section>

  <div class="divider"></div>

  <div id="contact">
    <div class="contact-glow"></div>
    <div class="contact-inner">
      <div class="section-label reveal">Contact</div>
      <h2 class="section-title reveal" style="text-align:center">Let's Talk</h2>
      <p class="reveal" style="color: var(--gray); font-size: 0.8rem; margin-bottom: 1rem;">{contact['tagline']}</p>
      <a href="mailto:{contact['email']}" class="contact-email reveal">{contact['email']}</a>
      <div class="contact-links reveal">
{contact_links_html}
      </div>
    </div>
  </div>

  <footer>
    <span>© {footer['year']} {footer['name']}</span>
    <span>Built with HTML · Hosted on GitHub Pages</span>
    <span>{footer['location']}</span>
  </footer>

  <script>
    const reveals = document.querySelectorAll('.reveal');
    const observer = new IntersectionObserver((entries) => {{
      entries.forEach((entry, i) => {{
        if (entry.isIntersecting) {{
          setTimeout(() => entry.target.classList.add('visible'), i * 80);
          observer.unobserve(entry.target);
        }}
      }});
    }}, {{ threshold: 0.1 }});
    reveals.forEach(el => observer.observe(el));

    const skillFills = document.querySelectorAll('.skill-fill');
    const skillObserver = new IntersectionObserver((entries) => {{
      entries.forEach(entry => {{
        if (entry.isIntersecting) {{
          skillObserver.unobserve(entry.target);
        }}
      }});
    }}, {{ threshold: 0.5 }});
    skillFills.forEach(el => {{
      const targetWidth = el.style.width;
      el.style.width = '0';
      setTimeout(() => el.style.width = targetWidth, 300);
      skillObserver.observe(el);
    }});
  </script>

</body>
</html>"""
    return html


# ── Styles ─────────────────────────────────────────────────────────────────────
BG       = "#0d0d0f"
SURFACE  = "#1a1a26"
BORDER   = "#2a2a3a"
RED      = "#e94560"
GOLD     = "#f5a623"
CYAN     = "#00d2ff"
WHITE    = "#f0f0f0"
GRAY     = "#888888"

def style_widget(w, **kw):
    try: w.configure(**kw)
    except Exception: pass

def make_label(parent, text, color=WHITE, font=("Courier", 9), bg=BG, **kw):
    l = tk.Label(parent, text=text, fg=color, bg=bg, font=font, **kw)
    return l

def make_entry(parent, textvariable=None, width=50):
    e = tk.Entry(parent, textvariable=textvariable, width=width,
                 bg=SURFACE, fg=WHITE, insertbackground=WHITE,
                 relief="flat", bd=4, font=("Courier", 9))
    return e

def make_text(parent, height=4, width=60):
    t = tk.Text(parent, height=height, width=width,
                bg=SURFACE, fg=WHITE, insertbackground=WHITE,
                relief="flat", bd=4, font=("Courier", 9),
                wrap="word", undo=True)
    return t

def make_button(parent, text, command, color=RED):
    return tk.Button(parent, text=text, command=command,
                     bg=color, fg=WHITE, relief="flat",
                     font=("Courier", 9, "bold"),
                     padx=12, pady=6, cursor="hand2",
                     activebackground=WHITE, activeforeground=BG)

def make_frame(parent, **kw):
    return tk.Frame(parent, bg=BG, **kw)

def make_lframe(parent, text, color=GOLD):
    lf = tk.LabelFrame(parent, text=text, fg=color, bg=BG,
                       font=("Courier", 9, "bold"), bd=1,
                       relief="solid", labelanchor="nw")
    return lf

def scrollable_frame(parent):
    canvas = tk.Canvas(parent, bg=BG, highlightthickness=0)
    sb = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
    inner = make_frame(canvas)
    def _on_resize(event):  # pylint: disable=unused-argument
        canvas.configure(scrollregion=canvas.bbox("all"))
    inner.bind("<Configure>", _on_resize)
    canvas.create_window((0, 0), window=inner, anchor="nw")
    canvas.configure(yscrollcommand=sb.set)
    canvas.pack(side="left", fill="both", expand=True)
    sb.pack(side="right", fill="y")

    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    canvas.bind_all("<MouseWheel>", _on_mousewheel)
    return inner


# ══════════════════════════════════════════════════════════════════════════════
# TAB: HERO
# ══════════════════════════════════════════════════════════════════════════════
class HeroTab:
    def __init__(self, parent, data):
        self.data = data
        self.frame = make_frame(parent)
        self._build()

    def _build(self):
        f = self.frame
        h = self.data["hero"]

        lf = make_lframe(f, "  HERO SECTION  ")
        lf.pack(fill="x", padx=20, pady=20)
        inner = make_frame(lf)
        inner.pack(fill="x", padx=10, pady=10)

        fields = [
            ("Name Line 1",    "name_line1"),
            ("Name Line 2 (red)", "name_line2"),
            ("Subtitle",       "subtitle"),
            ("itch.io URL",    "itchio_url"),
            ("Availability Tag Text", "availability_tag"),
        ]
        self.vars = {}
        for row, (label, key) in enumerate(fields):
            make_label(inner, label + ":", color=CYAN).grid(row=row, column=0, sticky="w", pady=4, padx=6)
            var = tk.StringVar(value=h.get(key, ""))
            self.vars[key] = var
            make_entry(inner, textvariable=var, width=55).grid(row=row, column=1, sticky="ew", pady=4, padx=6)

        # show availability checkbox
        self.show_avail = tk.BooleanVar(value=h.get("show_availability", True))
        cb = tk.Checkbutton(inner, text="Show availability tag", variable=self.show_avail,
                            bg=BG, fg=WHITE, selectcolor=SURFACE,
                            activebackground=BG, activeforeground=CYAN,
                            font=("Courier", 9))
        cb.grid(row=len(fields), column=1, sticky="w", pady=4, padx=6)

        make_label(inner, "Hero Description:", color=CYAN).grid(row=len(fields)+1, column=0, sticky="nw", pady=4, padx=6)
        self.desc_text = make_text(inner, height=4, width=55)
        self.desc_text.insert("1.0", h.get("description", ""))
        self.desc_text.grid(row=len(fields)+1, column=1, sticky="ew", pady=4, padx=6)

    def save_to_data(self):
        h = self.data["hero"]
        for key, var in self.vars.items():
            h[key] = var.get()
        h["description"] = self.desc_text.get("1.0", "end-1c")
        h["show_availability"] = self.show_avail.get()


# ══════════════════════════════════════════════════════════════════════════════
# TAB: PROJECTS
# ══════════════════════════════════════════════════════════════════════════════
class ProjectsTab:
    def __init__(self, parent, data):
        self.data = data
        self.frame = make_frame(parent)
        self._build()

    def _build(self):
        # top bar
        top = make_frame(self.frame)
        top.pack(fill="x", padx=20, pady=(15,0))
        make_label(top, "PROJECTS", color=RED, font=("Courier", 10, "bold")).pack(side="left")
        make_button(top, "+ Add Project", self._add_project, color=CYAN).pack(side="right")

        # scrollable list
        scroll_outer = make_frame(self.frame)
        scroll_outer.pack(fill="both", expand=True, padx=20, pady=10)
        self.list_inner = scrollable_frame(scroll_outer)
        self._refresh_list()

    def _refresh_list(self):
        for widget in self.list_inner.winfo_children():
            widget.destroy()
        for i, p in enumerate(self.data["projects"]):
            self._project_row(i, p)

    def _project_row(self, idx, p):
        lf = make_lframe(self.list_inner, f"  Project {idx+1}: {p['title']}  ")
        lf.pack(fill="x", pady=6, padx=4)
        inner = make_frame(lf)
        inner.pack(fill="x", padx=8, pady=6)

        fields = [
            ("Title",       "title",     50),
            ("Type",        "type",      50),
            ("itch.io Link (leave blank if no link)", "link", 50),
            ("Tags (comma separated)", "tags", 50),
            ("Tag Colors (cyan/red/gold/gray, comma separated)", "tag_colors", 50),
        ]
        field_vars: dict = {}
        for row, (label, key, width) in enumerate(fields):
            make_label(inner, label+":", color=CYAN).grid(row=row, column=0, sticky="w", pady=3, padx=4)
            var = tk.StringVar(value=p.get(key, ""))
            field_vars[key] = var
            make_entry(inner, textvariable=var, width=width).grid(row=row, column=1, sticky="ew", pady=3, padx=4)

        make_label(inner, "Description:", color=CYAN).grid(row=len(fields), column=0, sticky="nw", pady=3, padx=4)
        desc_box = make_text(inner, height=3, width=52)
        desc_box.insert("1.0", p.get("desc", ""))
        desc_box.grid(row=len(fields), column=1, sticky="ew", pady=3, padx=4)

        # buttons
        btn_row = make_frame(inner)
        btn_row.grid(row=len(fields)+1, column=1, sticky="e", pady=6)

        _i = idx
        def save_this():
            proj = self.data["projects"][_i]
            for k, v in field_vars.items():
                proj[k] = v.get()
            proj["desc"] = desc_box.get("1.0", "end-1c")
            messagebox.showinfo("Saved", f"Project {_i+1} saved!")

        def move_up(i=idx):
            if i > 0:
                self.data["projects"][i], self.data["projects"][i-1] = \
                    self.data["projects"][i-1], self.data["projects"][i]
                self._refresh_list()

        def move_down(i=idx):
            if i < len(self.data["projects"])-1:
                self.data["projects"][i], self.data["projects"][i+1] = \
                    self.data["projects"][i+1], self.data["projects"][i]
                self._refresh_list()

        def delete_this(i=idx):
            if messagebox.askyesno("Delete", f"Delete project '{self.data['projects'][i]['title']}'?"):
                self.data["projects"].pop(i)
                self._refresh_list()

        make_button(btn_row, "↑",        move_up,    BORDER).pack(side="left", padx=2)
        make_button(btn_row, "↓",        move_down,  BORDER).pack(side="left", padx=2)
        make_button(btn_row, "Save",     save_this,  CYAN ).pack(side="left", padx=2)
        make_button(btn_row, "Delete",   delete_this, RED  ).pack(side="left", padx=2)

    def _add_project(self):
        self.data["projects"].append({
            "title": "New Project",
            "type": "App · Python / Tkinter",
            "desc": "Description here.",
            "tags": "Python,Tkinter",
            "tag_colors": "cyan,cyan",
            "link": "",
        })
        self._refresh_list()

    def save_to_data(self):
        pass  # projects saved per-row


# ══════════════════════════════════════════════════════════════════════════════
# TAB: ABOUT
# ══════════════════════════════════════════════════════════════════════════════
class AboutTab:
    def __init__(self, parent, data):
        self.data = data
        self.frame = make_frame(parent)
        self._build()

    def _build(self):
        scroll_outer = make_frame(self.frame)
        scroll_outer.pack(fill="both", expand=True, padx=20, pady=10)
        inner = scrollable_frame(scroll_outer)

        # paragraphs
        lf_para = make_lframe(inner, "  BIO PARAGRAPHS (one per box)  ")
        lf_para.pack(fill="x", pady=10, padx=4)
        self.para_boxes = []
        para_inner = make_frame(lf_para)
        para_inner.pack(fill="x", padx=8, pady=6)

        for i, para in enumerate(self.data["about"]["paragraphs"]):
            make_label(para_inner, f"Paragraph {i+1}:", color=CYAN).pack(anchor="w", pady=(6,0))
            tb = make_text(para_inner, height=3, width=70)
            tb.insert("1.0", para)
            tb.pack(fill="x", pady=2)
            self.para_boxes.append(tb)

        # english note
        lf_eng = make_lframe(inner, "  ENGLISH NOTE  ")
        lf_eng.pack(fill="x", pady=6, padx=4)
        eng_inner = make_frame(lf_eng)
        eng_inner.pack(fill="x", padx=8, pady=6)
        make_label(eng_inner, "Text:", color=CYAN).pack(side="left", padx=4)
        self.eng_var = tk.StringVar(value=self.data["about"].get("english_note", ""))
        make_entry(eng_inner, textvariable=self.eng_var, width=55).pack(side="left", padx=4)

        # skills
        lf_sk = make_lframe(inner, "  SKILLS  ")
        lf_sk.pack(fill="x", pady=6, padx=4)
        sk_inner = make_frame(lf_sk)
        sk_inner.pack(fill="x", padx=8, pady=6)

        header = make_frame(sk_inner)
        header.pack(fill="x")
        for txt, _ in [("Skill Name",20),("Level",12),("% (0-100)",8),("Color (red/cyan/gold/gray)",20)]:
            make_label(header, txt, color=GOLD, font=("Courier",8,"bold")).pack(side="left", padx=4)

        self.skill_rows = []
        for s in self.data["about"]["skills"]:
            row = make_frame(sk_inner)
            row.pack(fill="x", pady=2)
            name_v  = tk.StringVar(value=s["name"])
            level_v = tk.StringVar(value=s["level"])
            pct_v   = tk.StringVar(value=str(s["pct"]))
            color_v = tk.StringVar(value=s["color"])
            make_entry(row, textvariable=name_v,  width=22).pack(side="left", padx=2)
            make_entry(row, textvariable=level_v, width=13).pack(side="left", padx=2)
            make_entry(row, textvariable=pct_v,   width=6 ).pack(side="left", padx=2)
            make_entry(row, textvariable=color_v, width=10).pack(side="left", padx=2)
            self.skill_rows.append((name_v, level_v, pct_v, color_v))

    def save_to_data(self):
        self.data["about"]["paragraphs"] = [tb.get("1.0","end-1c") for tb in self.para_boxes]
        self.data["about"]["english_note"] = self.eng_var.get()
        skills = []
        for name_v, level_v, pct_v, color_v in self.skill_rows:
            try: pct = int(pct_v.get())
            except: pct = 50
            skills.append({"name": name_v.get(), "level": level_v.get(), "pct": pct, "color": color_v.get()})
        self.data["about"]["skills"] = skills


# ══════════════════════════════════════════════════════════════════════════════
# TAB: CERTS
# ══════════════════════════════════════════════════════════════════════════════
class CertsTab:
    def __init__(self, parent, data):
        self.data = data
        self.frame = make_frame(parent)
        self._build()

    def _build(self):
        top = make_frame(self.frame)
        top.pack(fill="x", padx=20, pady=(15,0))
        make_label(top, "CERTIFICATIONS", color=RED, font=("Courier",10,"bold")).pack(side="left")
        make_button(top, "+ Add Issuer", self._add_issuer, color=CYAN).pack(side="right")

        scroll_outer = make_frame(self.frame)
        scroll_outer.pack(fill="both", expand=True, padx=20, pady=10)
        self.list_inner = scrollable_frame(scroll_outer)
        self._refresh()

    def _refresh(self):
        for widget in self.list_inner.winfo_children():
            widget.destroy()
        for i, g in enumerate(self.data["certs"]):
            self._group_row(i, g)

    def _group_row(self, idx, g):
        lf = make_lframe(self.list_inner, f"  {g['issuer']}  ")
        lf.pack(fill="x", pady=6, padx=4)
        inner = make_frame(lf)
        inner.pack(fill="x", padx=8, pady=6)

        # issuer + note
        top = make_frame(inner)
        top.pack(fill="x")
        make_label(top, "Issuer:", color=CYAN).pack(side="left", padx=4)
        issuer_v = tk.StringVar(value=g["issuer"])
        make_entry(top, textvariable=issuer_v, width=20).pack(side="left", padx=4)
        make_label(top, "Note:", color=CYAN).pack(side="left", padx=4)
        note_v = tk.StringVar(value=g["note"])
        make_entry(top, textvariable=note_v, width=20).pack(side="left", padx=4)

        # cert items
        make_label(inner, "Certs (Name | Date):", color=GOLD).pack(anchor="w", pady=(8,2))
        item_frame = make_frame(inner)
        item_frame.pack(fill="x")
        item_widgets: list = []

        def _add_item_row(name="", date=""):
            row = make_frame(item_frame)
            row.pack(fill="x", pady=1)
            nv = tk.StringVar(value=name)
            dv = tk.StringVar(value=date)
            make_entry(row, textvariable=nv, width=38).pack(side="left", padx=2)
            make_label(row, "|", color=GRAY).pack(side="left")
            make_entry(row, textvariable=dv, width=12).pack(side="left", padx=2)
            def rm(r=row, nv=nv, dv=dv):
                item_widgets.remove((nv,dv))
                r.destroy()
            make_button(row, "✕", rm, BORDER).pack(side="left", padx=2)
            item_widgets.append((nv, dv))

        for item in g["items"]:
            _add_item_row(item["name"], item["date"])

        make_button(inner, "+ Add Cert", _add_item_row, GOLD).pack(anchor="w", pady=4)

        # save / delete
        btn_row = make_frame(inner)
        btn_row.pack(anchor="e", pady=4)

        _i2 = idx
        def save_group():
            self.data["certs"][_i2]["issuer"] = issuer_v.get()
            self.data["certs"][_i2]["note"]   = note_v.get()
            self.data["certs"][_i2]["items"]  = [{"name": n.get(), "date": d.get()} for n,d in item_widgets if n.get()]
            messagebox.showinfo("Saved", f"Issuer '{issuer_v.get()}' saved!")

        def del_group(i=idx):
            if messagebox.askyesno("Delete", f"Delete issuer '{self.data['certs'][i]['issuer']}'?"):
                self.data["certs"].pop(i)
                self._refresh()

        make_button(btn_row, "Save",   save_group, CYAN).pack(side="left", padx=2)
        make_button(btn_row, "Delete", del_group,  RED ).pack(side="left", padx=2)

    def _add_issuer(self):
        self.data["certs"].append({"issuer": "New Issuer", "note": "", "items": []})
        self._refresh()

    def save_to_data(self):
        pass  # saved per-group


# ══════════════════════════════════════════════════════════════════════════════
# TAB: CONTACT
# ══════════════════════════════════════════════════════════════════════════════
class ContactTab:
    def __init__(self, parent, data):
        self.data = data
        self.frame = make_frame(parent)
        self._build()

    def _build(self):
        c = self.data["contact"]
        fo = self.data["footer"]

        scroll_outer = make_frame(self.frame)
        scroll_outer.pack(fill="both", expand=True, padx=20, pady=10)
        inner = scrollable_frame(scroll_outer)

        # contact
        lf = make_lframe(inner, "  CONTACT  ")
        lf.pack(fill="x", pady=10, padx=4)
        cf = make_frame(lf)
        cf.pack(fill="x", padx=8, pady=8)

        fields = [("Email", "email"), ("Tagline", "tagline")]
        self.contact_vars = {}
        for row, (label, key) in enumerate(fields):
            make_label(cf, label+":", color=CYAN).grid(row=row, column=0, sticky="w", pady=4, padx=4)
            var = tk.StringVar(value=c.get(key,""))
            self.contact_vars[key] = var
            make_entry(cf, textvariable=var, width=50).grid(row=row, column=1, sticky="ew", pady=4, padx=4)

        # links
        make_label(cf, "Social Links:", color=GOLD).grid(row=2, column=0, sticky="nw", pady=4, padx=4)
        self.links_frame = make_frame(cf)
        self.links_frame.grid(row=2, column=1, sticky="ew", pady=4, padx=4)
        self.link_widgets = []
        for lk in c.get("links", []):
            self._add_link_row(lk["label"], lk["url"])
        make_button(cf, "+ Add Link", self._add_link_row, GOLD).grid(row=3, column=1, sticky="w", pady=4, padx=4)

        # footer
        lf2 = make_lframe(inner, "  FOOTER  ")
        lf2.pack(fill="x", pady=10, padx=4)
        ff = make_frame(lf2)
        ff.pack(fill="x", padx=8, pady=8)

        footer_fields = [("Name", "name"), ("Year", "year"), ("Location", "location")]
        self.footer_vars = {}
        for row, (label, key) in enumerate(footer_fields):
            make_label(ff, label+":", color=CYAN).grid(row=row, column=0, sticky="w", pady=4, padx=4)
            var = tk.StringVar(value=fo.get(key,""))
            self.footer_vars[key] = var
            make_entry(ff, textvariable=var, width=40).grid(row=row, column=1, sticky="ew", pady=4, padx=4)

    def _add_link_row(self, label="", url=""):
        row = make_frame(self.links_frame)
        row.pack(fill="x", pady=2)
        lv = tk.StringVar(value=label)
        uv = tk.StringVar(value=url)
        make_label(row, "Label:", color=CYAN).pack(side="left", padx=2)
        make_entry(row, textvariable=lv, width=12).pack(side="left", padx=2)
        make_label(row, "URL:", color=CYAN).pack(side="left", padx=2)
        make_entry(row, textvariable=uv, width=30).pack(side="left", padx=2)
        def rm(r=row, lv=lv, uv=uv):
            self.link_widgets.remove((lv,uv))
            r.destroy()
        make_button(row, "✕", rm, BORDER).pack(side="left", padx=2)
        self.link_widgets.append((lv, uv))

    def save_to_data(self):
        for key, var in self.contact_vars.items():
            self.data["contact"][key] = var.get()
        self.data["contact"]["links"] = [
            {"label": lv.get(), "url": uv.get()} for lv,uv in self.link_widgets if lv.get()
        ]
        for key, var in self.footer_vars.items():
            self.data["footer"][key] = var.get()


# ══════════════════════════════════════════════════════════════════════════════
# MAIN APP
# ══════════════════════════════════════════════════════════════════════════════
class App:
    def __init__(self, win):
        self.root = win
        self.root.title("Portfolio Generator — cloudbv")
        self.root.configure(bg=BG)
        self.root.geometry("860x700")
        self.root.minsize(700, 500)

        self.data = load_data()
        self._build_ui()

    def _build_ui(self):
        # title bar
        title_bar = make_frame(self.root)
        title_bar.pack(fill="x", padx=0, pady=0)
        title_bar.configure(bg=SURFACE)
        make_label(title_bar, "  ◆ PORTFOLIO GENERATOR", color=CYAN,
                   font=("Courier", 11, "bold"), bg=SURFACE).pack(side="left", pady=12)
        make_label(title_bar, "cloudbv  ", color=GRAY,
                   font=("Courier", 9), bg=SURFACE).pack(side="right", pady=12)

        # ttk style for notebook
        style = ttk.Style()
        style.theme_use("default")
        style.configure("TNotebook",        background=BG,      borderwidth=0)
        style.configure("TNotebook.Tab",    background=SURFACE, foreground=GRAY,
                        font=("Courier", 9, "bold"), padding=[14, 6])
        style.map("TNotebook.Tab",
                  background=[("selected", BG)],
                  foreground=[("selected", CYAN)])

        nb = ttk.Notebook(self.root)
        nb.pack(fill="both", expand=True, padx=0, pady=0)

        self.hero_tab    = HeroTab(nb, self.data)
        self.proj_tab    = ProjectsTab(nb, self.data)
        self.about_tab   = AboutTab(nb, self.data)
        self.certs_tab   = CertsTab(nb, self.data)
        self.contact_tab = ContactTab(nb, self.data)

        nb.add(self.hero_tab.frame,    text="  HERO  ")
        nb.add(self.proj_tab.frame,    text="  PROJECTS  ")
        nb.add(self.about_tab.frame,   text="  ABOUT  ")
        nb.add(self.certs_tab.frame,   text="  CERTS  ")
        nb.add(self.contact_tab.frame, text="  CONTACT  ")

        # bottom bar
        bot = make_frame(self.root)
        bot.configure(bg=SURFACE)
        bot.pack(fill="x", side="bottom")

        make_button(bot, "💾  Save Data",       self._save,    GOLD ).pack(side="left",  padx=12, pady=10)
        make_button(bot, "⚡  Generate HTML",   self._generate, RED  ).pack(side="right", padx=12, pady=10)
        self.status = make_label(bot, "Ready.", color=GRAY, bg=SURFACE)
        self.status.pack(side="right", padx=12)

    def _collect_all(self):
        self.hero_tab.save_to_data()
        self.about_tab.save_to_data()
        self.contact_tab.save_to_data()
        # proj and certs tabs save per-row

    def _save(self):
        self._collect_all()
        save_data(self.data)
        self.status.config(text="Data saved ✓", fg=CYAN)
        self.root.after(3000, lambda: self.status.config(text="Ready.", fg=GRAY))

    def _generate(self):
        self._collect_all()
        save_data(self.data)
        try:
            html = generate_html(self.data)
            with open("index.html", "w", encoding="utf-8") as f:
                f.write(html)
            self.status.config(text="index.html generated ✓", fg=GOLD)
            messagebox.showinfo("Done!", "index.html has been generated in the same folder as this script.\n\nJust drop it into your GitHub repo — done!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        self.root.after(4000, lambda: self.status.config(text="Ready.", fg=GRAY))


if __name__ == "__main__":
    main_window = tk.Tk()
    app = App(main_window)
    main_window.mainloop()
