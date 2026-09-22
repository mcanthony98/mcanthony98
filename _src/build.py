"""Build every page of the portfolio. Run from the repo root:  python _src/build.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from kit import (BASE, EMAIL, GANIAM, LINKEDIN, GITHUB, WHATSAPP, browser, contact, esc, footer, head, header,
                 icon, other_services, sparkline)
from content import (AGENT_DIAGRAM, CASE, CASES, CLIENTS, EXTRA_PROOF, QUOTES, SEARV_DIAGRAM, SERVICES, SITES,
                     SVC, SYSTEMS)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FEATURED = ["kiboko", "debluc", "snapshot", "ai-sales-agent"]

PERSON = {
    "@context": "https://schema.org", "@type": "Person", "name": "Mark Anthony Maina", "url": BASE,
    "image": BASE + "assets/img/mark-hero.jpg", "email": "mailto:" + EMAIL,
    "jobTitle": "RevOps & Marketing Automation Consultant",
    "worksFor": {"@type": "Organization", "name": "Ganiam Tech", "url": GANIAM},
    "address": {"@type": "PostalAddress", "addressLocality": "Nairobi", "addressCountry": "KE"},
    "knowsAbout": ["Revenue Operations", "Marketing Automation", "n8n", "AI Sales Agents", "SEO",
                   "Conversion Rate Optimization", "GA4", "Google Tag Manager", "Web Development"],
    "sameAs": [LINKEDIN, GITHUB, GANIAM],
}


def write(path, html):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    print("built", path)


# ---------------------------------------------------------------- shared sections
def leak_funnel():
    rows = [("Visitors", 100, "1,000", ""), ("Engaged", 52, "520", ""), ("Viewed the offer", 24, "240", ""),
            ("Enquired", 9, "22", ""), ("Got a reply the same day", 4, "9", "leak"), ("Paid", 2, "3", "")]
    out = "".join(f'<div class="f-row {c}"><span class="lbl">{l}</span><div class="f-bar"><i style="--w:{max(w, 2.5)}%"></i></div>'
                  f'<span class="val">{v}</span></div>' for l, w, v, c in rows)
    return f"""<div class="leak-card anim">
  <div class="chart-title"><span>Where a typical funnel loses money</span><small>illustration</small></div>
  <div class="funnel">{out}</div>
  <div class="leak-note">{icon("alert")}<span><strong>A real one:</strong> in one audit, 68 enquiries arrived in 12 months and every single one was still marked &ldquo;new&rdquo;. Nobody could say which became customers.</span></div>
</div>"""


def case_card(c, r="", flip=False):
    metrics = "".join(f'<div><b class="{cls}">{v}</b>{esc_html(lbl)}</div>' for v, lbl, cls in c["metrics"])
    if c["shot"] and c["slug"] != "searv":
        visual = f'<div class="shot">{browser(c["shot"], c["url"], c["client"] + " website", r)}</div><div class="chart-card">{c["chart"](w=360)}</div>'
    elif c["slug"] == "ai-sales-agent":
        visual = f'<div class="chart-card">{AGENT_DIAGRAM}</div><div class="chart-card">{c["chart"](w=400)}</div>'
    else:
        visual = f'<div class="chart-card">{SEARV_DIAGRAM}</div><div class="chart-card">{c["chart"](w=400)}</div>'
    tags = " &middot; ".join(c["services"])
    return f"""<a class="case reveal{' flip' if flip else ''}" href="{r}work/{c['slug']}.html">
  <div class="case-body">
    <div class="case-meta"><span>{c['client']}</span><span>{c['industry']} &middot; {c['where']}</span></div>
    <h3>{c['card_title']}</h3>
    <p>{c['summary']}</p>
    <div class="case-metrics">{metrics}</div>
    <span class="link-arrow">Read the case study {icon("arrow")}</span>
    <div class="case-meta" style="margin:18px 0 0">{tags}</div>
  </div>
  <div class="case-visual">{visual}</div>
</a>"""


def esc_html(s):
    return s  # copy already contains safe entities


def systems_grid():
    cards = []
    for name, sub, text, flow, tags, res, res_sub in SYSTEMS:
        t = "".join(f"<span>{x}</span>" for x in tags)
        cards.append(f"""<article class="sys reveal">
  <div class="sys-top"><div><h3>{name}</h3><div class="sub">{sub}</div></div><div class="result">{res}<small>{res_sub}</small></div></div>
  <p>{text}</p>
  <div class="flow">{flow}</div>
  <div class="tags">{t}</div>
</article>""")
    return '<div class="sys-grid">' + "".join(cards) + "</div>"


def quotes_block(single=False):
    q, name, role = QUOTES[0]
    big = f"""<blockquote class="quote big reveal"><div><div class="mark">&ldquo;</div><p>{q}</p></div>
  <footer><i>{name[0]}</i><div><strong>{name}</strong><span>{role}</span></div></footer></blockquote>"""
    if single:
        return f'<div class="quotes">{big}</div>'
    rest = "".join(f"""<blockquote class="quote reveal d1"><div class="mark">&ldquo;</div><p>{q}</p>
  <footer><i>{n[0]}</i><div><strong>{n}</strong><span>{ro}</span></div></footer></blockquote>""" for q, n, ro in QUOTES[1:])
    cta = f"""<div class="quote reveal d2" style="background:var(--violet-soft);border-color:transparent">
  <div class="kicker" style="margin-bottom:12px">Your turn</div>
  <p style="font-family:var(--display);font-size:24px;line-height:1.25;letter-spacing:-.02em;margin-top:0">Want to be the next case study on this page?</p>
  <footer><a class="btn btn-primary" href="#contact">Book a free call {icon("arrow")}</a></footer></div>"""
    return f'<div class="quotes">{big}{rest}{cta}</div>'


def faq_block(items):
    out = "".join(f'<details><summary>{q}<i></i></summary><div class="ans"><p>{a}</p></div></details>' for q, a in items)
    return f'<div class="faq reveal">{out}</div>'


def svc_cards(r=""):
    out = []
    for i, s in enumerate(SERVICES):
        feat = i == 0
        tag = '<span class="tag">Flagship</span>' if feat else ""
        out.append(f"""<a class="svc reveal{' feature' if feat else ''}" href="{r}services/{s['slug']}.html">{tag}
  <span class="ic">{icon(s['icon'])}</span>
  <h3>{s['name'] if not feat else 'RevOps: I find where your money leaks, and plug it'}</h3>
  <p>{s['card']}</p>
  <span class="outcome"><span>{s['outcome']}</span>{icon("arrow")}</span>
</a>""")
    out.append(f"""<a class="svc reveal svc-cta" href="#contact">
  <span class="ic">{icon('users')}</span>
  <h3>Not sure which one you need?</h3>
  <p>That&rsquo;s normal. Book a free 20-minute call and we&rsquo;ll look at your numbers together. I&rsquo;ll tell you the first thing I&rsquo;d fix, even if it&rsquo;s not me who fixes it.</p>
  <span class="outcome"><span>Book a free call</span>{icon("arrow")}</span>
</a>""")
    return '<div class="svc-grid">' + "".join(out) + "</div>"


LOOP = [("Pull", "Real numbers from GA4, Search Console, ads, CRM and the actual sales record."),
        ("Diagnose", "Name one failing stage: demand, visibility, conversion, follow-up or retention."),
        ("Prioritise", "Rank the three cheapest fixes by expected revenue, not by what&rsquo;s fun to build."),
        ("Ship", "Build it and put it live. Tracking, page, automation, integration."),
        ("Report", "One page: what changed, what moved, what it was worth, what&rsquo;s next."),
        ("Close the loop", "Check against banked money, because analytics and revenue aren&rsquo;t the same number.")]


def loop_block():
    items = "".join(f"<li class=\"reveal\"><h4>{t}</h4><p>{d}</p></li>" for t, d in LOOP)
    return f'<ol class="loop">{items}</ol>'


def page(path, title, desc, body, r="", active="", ld=None):
    return head(title, desc, path, ld, r) + "<body>\n" + header(SERVICES, r, active) + "<main>" + body + "</main>\n" + footer(SERVICES, CASES, r)


# ---------------------------------------------------------------- home
def build_home():
    r = ""
    marquee = "".join(f"<span>{c}</span>" for c in CLIENTS * 2)
    featured = "".join(case_card(CASE[s], r, flip=i % 2 == 1) for i, s in enumerate(FEATURED))
    faq = faq_block([
        ("What do you actually do, in one sentence?", "I help businesses make more money from the customers they&rsquo;re already attracting, by fixing the path from first click to paid invoice: the website, the tracking, the follow-up, the automations and the AI."),
        ("Can I hire you for just one thing, like a website or SEO?", "Yes. Every service has its own page and its own fixed scope. I&rsquo;ll just tell you honestly if the thing you asked for isn&rsquo;t the thing that&rsquo;s actually holding you back."),
        ("Do you work with businesses outside Kenya?", "Yes. I work with clients in Kenya, the UK and the US, remotely, across East African, UK and US hours."),
        ("How much does it cost?", "Projects are fixed-price, agreed before we start. Ongoing work is a monthly retainer. On the first call I&rsquo;ll give you a straight number, not a range designed to find out your budget."),
        ("What if our data is a mess, or tracking was never set up?", "That&rsquo;s normal. Month one is usually instrumentation: installing the measurement, defining what a lead and a sale mean, and cleaning out bots and staff visits. I say it up front so it never feels like a month of nothing."),
        ("Is it just you, or an agency?", "It&rsquo;s me, doing the work myself. Client projects are contracted through Ganiam Tech, my agency, so you get a proper company behind the invoice and the same person on every call."),
    ])
    body = f"""
<section class="hero">
  <div class="container hero-grid">
    <div>
      <div class="pill reveal"><i></i>Taking new projects &middot; Worldwide</div>
      <h1 class="reveal d1 hero-h1">I help businesses<br><span class="nowrap">make <span class="serif">money online.</span></span></h1>
      <p class="lead reveal d2">Hi, I&rsquo;m Mark. Not traffic, not likes: <strong>money.</strong> I build the systems between a stranger&rsquo;s first click and cash in your bank (the website, the tracking, the automations, the AI agents) and then I show you the numbers, so you know it worked.</p>
      <div class="btn-row reveal d3">
        <a class="btn btn-primary" href="#contact">Book a free 20-min call {icon("arrow")}</a>
        <a class="btn btn-ghost" href="#results">See the results</a>
      </div>
      <div class="hero-proof reveal d3">
        <div><b>+47%</b>conversions, same ad spend</div>
        <div><b>+74%</b>organic traffic in a month</div>
        <div><b>&lt; 60s</b>enquiry to AI quote</div>
      </div>
    </div>
    <div class="portrait reveal d2">
      <div class="portrait-frame">
        <picture><source type="image/webp" srcset="assets/img/mark-hero-560.webp 560w, assets/img/mark-hero-900.webp 900w" sizes="(max-width: 960px) 90vw, 470px">
        <img src="assets/img/mark-hero.jpg" alt="Mark Anthony Maina" width="900" height="1125" fetchpriority="high"></picture>
      </div>
      <div class="chip chip-a"><span class="chip-ic">{icon("cal")}</span><div><b>8 years</b><small>building for the web, since 2018</small></div></div>
      <div class="chip chip-b"><span class="chip-ic">{icon("code")}</span><div><b>150+</b><small>sites, platforms &amp; automations shipped</small></div></div>
      <div class="chip chip-c"><span class="chip-ic">{icon("globe")}</span><div><b>Worldwide</b><small>taking clients globally</small></div></div>
    </div>
  </div>
</section>
<div class="marquee" aria-label="Clients"><div class="marquee-label">Businesses I&rsquo;ve built for</div><div class="marquee-track">{marquee}</div></div>

<section class="section-tight">
  <div class="container">
    <div class="stats reveal">
      <div class="stat"><b data-count="8">8</b><span>revenue systems built from scratch: CRMs, AI agents, quote engines</span><em>in production</em></div>
      <div class="stat"><b data-count="6">6</b><span>growth clients run on my own RevOps platform</span><em>live, API-synced</em></div>
      <div class="stat"><b data-count="121">121</b><span>pages fixed for Google in a single week</span><em>Kiboko</em></div>
      <div class="stat"><b data-count="4" data-suffix=" yrs">4 yrs</b><span>longest client relationship, and still going</span><em>Snapshot, since 2022</em></div>
    </div>
  </div>
</section>

<section class="section" style="padding-top:calc(var(--section) * .5)">
  <div class="container leak-grid">
    <div class="reveal">
      <div class="kicker">The real problem</div>
      <h2>You probably don&rsquo;t have a traffic problem. You have a <span class="serif">leak.</span></h2>
      <p class="lead">Somewhere between the first click and the paid invoice, people are falling out. Usually at a stage nobody owns: the WhatsApp chat that never got answered, the quote sent two days late, the page that confused them.</p>
      <ul class="bullets">
        <li>{icon("check-circle")}<span><strong>Your agency</strong> stops at traffic. <strong>Your sales team</strong> starts at the enquiry. Nobody owns the middle.</span></li>
        <li>{icon("check-circle")}<span>I measure every stage, find the one losing the most money, and fix that first.</span></li>
        <li>{icon("check-circle")}<span>Then next month&rsquo;s numbers tell us if I was right. No vibes, no vanity metrics.</span></li>
      </ul>
      <a class="link-arrow" href="services/revops.html">How RevOps works {icon("arrow")}</a>
    </div>
    <div class="reveal d1">{leak_funnel()}</div>
  </div>
</section>

<section class="section section-white" id="services">
  <div class="container">
    <div class="section-head split">
      <div class="reveal"><div class="kicker">What I do</div><h2>Seven ways I help you make more <span class="serif">money.</span></h2></div>
      <p class="lead reveal d1">Most businesses hire one specialist per slice and spend the year translating between them. I cover the whole path. Pick the piece you need, or let me find the one that matters most.</p>
    </div>
    {svc_cards(r)}
  </div>
</section>

<section class="section section-dark" id="results">
  <div class="container">
    <div class="section-head split">
      <div class="reveal"><div class="kicker">Results</div><h2>Real clients. Real numbers. <span class="serif">Receipts.</span></h2></div>
      <p class="lead reveal d1">Every chart on this site comes from a real client account: Search Console, GA4, their database. Where something is an estimate, it says so. Where results are still coming in, it says that too.</p>
    </div>
    <div class="cases">{featured}</div>
    <div class="center" style="margin-top:44px"><a class="btn btn-ghost" href="work/index.html">See all work and systems {icon("arrow")}</a></div>
  </div>
</section>

<section class="section" id="how">
  <div class="container">
    <div class="section-head split">
      <div class="reveal"><div class="kicker">How I work</div><h2>One loop. Every client. Every <span class="serif">month.</span></h2></div>
      <p class="lead reveal d1">Trying to optimise everything at once is how retainers quietly turn into busywork. So every month I find the single stage failing hardest, fix that one thing, and prove whether it moved.</p>
    </div>
    {loop_block()}
  </div>
</section>

<section class="section section-dark" id="systems">
  <div class="container">
    <div class="section-head split">
      <div class="reveal"><div class="kicker">Systems I&rsquo;ve built</div><h2>Not mockups. Working <span class="serif">machines.</span></h2></div>
      <p class="lead reveal d1">Databases, webhooks, scheduled jobs, AI agents and error handling. Most of these exist because an off-the-shelf tool couldn&rsquo;t do the job at a price the client could pay. So I built it.</p>
    </div>
    {systems_grid()}
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head center reveal"><div class="kicker">Why it works</div><h2>An engineer who thinks like an <span class="serif">owner.</span></h2>
    <p class="lead">Most marketers can&rsquo;t build. Most developers don&rsquo;t think about margins. I do both, which means nothing gets lost in translation.</p></div>
    <div class="duo">
      <div class="duo-card eng reveal">
        <div class="kicker">The technical side</div>
        <h3>I write the code.</h3>
        <p>When a tool can&rsquo;t do it, I build it. When an integration breaks, I debug it instead of raising a ticket.</p>
        <ul class="duo-list">
          <li><b>Build</b><span>PHP &amp; Laravel, JavaScript, React &amp; Next.js, Node, MySQL, WordPress, Shopify, Odoo</span></li>
          <li><b>Automate</b><span>n8n, webhooks, REST APIs, cron jobs &amp; queues, WhatsApp via Evolution API</span></li>
          <li><b>AI</b><span>Claude, OpenAI and Gemini APIs. Agents that fail closed, never guess</span></li>
          <li><b>Measure</b><span>GA4, Tag Manager, Search Console, Clarity, Google Ads &amp; Meta APIs</span></li>
        </ul>
        <div class="code-snip"><span class="c">// every new lead, any channel</span>
<span class="k">on</span>(<span class="s">'lead.created'</span>, lead =&gt; {{
  reply(lead, {{ within: <span class="s">'60s'</span>, from: catalogue }})
  crm.tag(lead, {{ stage: <span class="s">'new'</span>, source: lead.utm }})
  <span class="k">if</span> (!agent.sure) handover(lead, team)  <span class="c">// fail closed</span>
  followUp(lead, {{ touches: 5, stopOn: <span class="s">'reply'</span> }})
}})</div>
      </div>
      <div class="duo-card biz reveal d1">
        <div class="kicker">The business side</div>
        <h3>I think in money.</h3>
        <p style="color:var(--muted)">Before I touch anything, I want to know what a lead is worth to you. That decides what&rsquo;s worth fixing.</p>
        <ul class="duo-list">
          <li><b>Unit economics</b><span>Average order, margin, close rate, and what one more lead is worth</span></li>
          <li><b>Funnel math</b><span>Where the biggest leak is, in shillings or dollars, not percentages</span></li>
          <li><b>Priorities</b><span>The three cheapest fixes ranked by revenue, not by what&rsquo;s fun</span></li>
          <li><b>Revenue truth</b><span>Checked against what actually hit the bank, not just GA4</span></li>
        </ul>
        <div class="calc">
          <div><span>Monthly visitors</span><span>3,000</span></div>
          <div><span>Conversion 2% &rarr; 3%</span><span>+30 leads</span></div>
          <div><span>Close rate 20%</span><span>+6 customers</span></div>
          <div><span>Average deal KES 25,000</span><span>+KES 150,000 / month</span></div>
        </div>
        <p style="font-size:13px;color:var(--muted);margin:10px 0 0">Example math. One point of conversion, from traffic you already have.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-white" id="about">
  <div class="container about-grid">
    <div class="about-photo reveal">
      <div class="frame"><picture><source type="image/webp" srcset="assets/img/mark-studio-480.webp 480w, assets/img/mark-studio-800.webp 800w" sizes="(max-width: 960px) 90vw, 420px">
      <img src="assets/img/mark-studio.jpg" alt="Mark Anthony Maina" loading="lazy" width="800" height="1000"></picture></div>
      <div class="caption"><span>Mark Anthony Maina</span><span>Nairobi, Kenya</span></div>
    </div>
    <div class="about-text">
      <div class="kicker reveal">About</div>
      <p class="big reveal">Hi there, I&rsquo;m Mark. I started out building websites. Then I kept watching good websites fail to make money, so I followed the money.</p>
      <ol class="path reveal">
        <li><b>Websites</b><span>I built sites for businesses. They looked good. Some sold, most didn&rsquo;t.</span></li>
        <li><b>SEO &amp; Google Ads</b><span>So I learned how to bring the right people to them.</span></li>
        <li><b>CRO</b><span>Then how to turn those visitors into enquiries.</span></li>
        <li><b>Data</b><span>Then how to see exactly where the leads were getting lost.</span></li>
        <li><b>Automation &amp; AI</b><span>Then how to make sure no lead ever gets forgotten again.</span></li>
        <li><b>RevOps, today</b><span>Now I own the whole path, from first click to money in the bank.</span></li>
      </ol>
      <p class="reveal">My old LinkedIn banner said <em>&ldquo;Building websites that don&rsquo;t just look good. They sell.&rdquo;</em> Still true. It just turned out the website was one stage out of five.</p>
      <p class="reveal">That&rsquo;s the difference. Most people you&rsquo;ll hire do one slice and hand the rest to someone else. I write the code, set up the tracking, build the automations, and report on the one number that matters: did you make more money?</p>
      <a class="ganiam reveal" href="{GANIAM}" target="_blank" rel="noopener"><span class="gt">GT</span><p><strong>Ganiam Tech</strong> is my Nairobi growth agency. Client projects are contracted through it: same person doing the work, a proper company behind the invoice. <span class="link-arrow" style="display:inline-flex">ganiamtech.com {icon("arrow")}</span></p></a>
      <div class="edu reveal"><span>BSc Electrical &amp; Electronics Engineering, JKUAT</span><span>Diploma, Business IT, Strathmore</span><span>Clients in Kenya, UK &amp; US</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal"><div class="kicker">Kind words</div><h2>From people who chose to work with <span class="serif">me.</span></h2></div>
    {quotes_block()}
  </div>
</section>

<section class="section section-white" style="padding-top:calc(var(--section) * .7)">
  <div class="container narrow">
    <div class="section-head center reveal"><div class="kicker">Questions</div><h2>Frequent <span class="serif">questions.</span></h2></div>
    {faq}
  </div>
</section>
{contact(r)}
"""
    ld = [PERSON, {"@context": "https://schema.org", "@type": "ProfessionalService", "name": "Mark Anthony Maina · Ganiam Tech",
                   "url": BASE, "areaServed": ["KE", "GB", "US"], "email": EMAIL,
                   "address": {"@type": "PostalAddress", "addressLocality": "Nairobi", "addressCountry": "KE"},
                   "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Services", "itemListElement": [
                       {"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["name"], "url": BASE + "services/" + s["slug"] + ".html"}} for s in SERVICES]}}]
    write("index.html", page("", "Mark Anthony Maina | I help businesses make money online. RevOps, Automation & AI",
                             "I help businesses make money online: RevOps, marketing automation, AI sales agents, SEO, CRO and websites that sell. Real client results, real numbers. Based in Nairobi, working worldwide.",
                             body, r, "home", ld))


# ---------------------------------------------------------------- service page
def hero_visual(s, r):
    slug = s["slug"]
    if slug == "revops":
        return leak_funnel().replace('class="leak-card anim"', 'class="leak-card anim" style="color:var(--text)"')
    if slug == "marketing-automation":
        lines = [("09:41:02", "new lead &middot; website form &middot; <b>google-ads</b>", ""),
                 ("09:41:03", "crm.upsert &rarr; stage=<b>new</b> owner=<b>sales</b>", ""),
                 ("09:41:05", "whatsapp.reply &rarr; sent", "ok"),
                 ("09:41:05", "email.reply &rarr; sent", "ok"),
                 ("09:41:06", "team.alert &rarr; telegram", "ok"),
                 ("+1 day", "no reply &rarr; follow-up #2 queued", ""),
                 ("+3 days", "follow-up #3 &middot; stops if they reply", "")]
        rows = "".join(f'<div style="display:grid;grid-template-columns:78px 1fr auto;gap:10px;padding:9px 0;border-bottom:1px solid rgba(255,255,255,.07)">'
                       f'<span style="color:rgba(232,234,255,.45)">{t}</span><span>{m}</span><span class="ok">{"&#10003;" if ok else ""}</span></div>' for t, m, ok in lines)
        return f"""<div class="hero-visual reveal d2"><div class="hv-head"><b>Speed-to-lead workflow</b><span>example run</span></div>
<div class="flow" style="margin:0;font-size:12.5px">{rows}</div>
<div class="hv-head" style="margin:14px 0 0"><span>Lead answered in</span><b style="font-family:var(--display);font-size:26px;color:var(--money-2)">3 seconds</b></div></div>"""
    if slug == "ai-sales-agents":
        def bub(t, me=False):
            st = ("margin-left:auto;background:#1f6f4a;border-radius:16px 16px 4px 16px" if me else "background:rgba(255,255,255,.08);border-radius:16px 16px 16px 4px")
            return f'<div style="max-width:82%;padding:11px 14px;font-size:14.5px;line-height:1.45;{st}">{t}</div>'
        chat = (bub("Hi, is the rosemary &amp; mint conditioner in stock? How much?") +
                bub("Hi! Yes, it&rsquo;s in stock at KES 550. Want me to set up delivery? Just share your area.", True) +
                bub("Westlands. Can I pay on delivery?") +
                bub("You can, M-Pesa on delivery works. I&rsquo;ve noted your order: 1 &times; conditioner to Westlands. Anything else? &#128522;", True))
        return f"""<div class="hero-visual reveal d2"><div class="hv-head"><b>WhatsApp &middot; AI agent</b><span>example conversation</span></div>
<div style="display:grid;gap:10px">{chat}</div>
<div class="hv-head" style="margin:16px 0 0"><span>Stage: <b style="color:var(--money-2)">ready to buy</b> &middot; admin alerted</span><span>replied in seconds</span></div></div>"""
    if slug == "seo":
        return f'<div class="hero-visual reveal d2">{CASE["debluc"]["chart"](w=440)}</div>'
    if slug == "cro":
        return f'<div class="hero-visual reveal d2">{CASE["snapshot"]["chart"](w=440)}</div>'
    if slug == "web-development":
        return f'<div class="reveal d2">{browser("bil", "bodyanditslanguage.com", "Body & Its Language website", r)}</div>'
    if slug == "analytics-tracking":
        ev = [("private_enquiry", "Package enquiry form"), ("custom_trip_enquiry", "Custom trip form"),
              ("whatsapp_click", "Tap to WhatsApp"), ("form_blocked", "Spam caught")]
        rows = "".join(f'<div style="display:grid;grid-template-columns:1fr auto;gap:10px;padding:11px 0;border-bottom:1px solid rgba(255,255,255,.07)">'
                       f'<span><span class="mono" style="color:var(--lavender);font-size:13px">{e}</span><br><small style="color:rgba(232,234,255,.5)">{d}</small></span>'
                       f'<span style="align-self:center;font-size:12px;padding:4px 10px;border-radius:99px;background:rgba(61,220,151,.14);color:var(--money-2)">live &#10003;</span></div>' for e, d in ev)
        return f"""<div class="hero-visual reveal d2"><div class="hv-head"><b>GA4 key events &middot; Kiboko</b><span>shipped Sep 2026</span></div>{rows}
<p style="font-size:13.5px;margin:14px 0 0;color:rgba(232,234,255,.6)">Before this, 68 enquiries in a year were invisible to analytics. Now every one is tied to its source.</p></div>"""
    return ""


def proof_card(key, r):
    if key in EXTRA_PROOF:
        c = EXTRA_PROOF[key]
        viz = c["visual"](r)
        href = f'{r}work/{c["slug"]}.html'
        return f"""<a class="proof reveal" href="{href}"><div class="viz">{viz}</div><div class="body">
<div class="case-meta"><span>{c['client']}</span><span>{c['industry']}</span></div><h3>{c['card_title']}</h3><p>{c['summary']}</p>
<span class="link-arrow">See how it works {icon("arrow")}</span></div></a>"""
    c = CASE[key]
    metrics = " &middot; ".join(f"<strong>{v}</strong> {l}" for v, l, _ in c["metrics"][:2])
    return f"""<a class="proof reveal" href="{r}work/{c['slug']}.html"><div class="viz">{c['chart']()}</div><div class="body">
<div class="case-meta"><span>{c['client']}</span><span>{c['industry']} &middot; {c['where']}</span></div><h3>{c['card_title']}</h3>
<p>{c['summary']}</p><p style="font-size:14px;color:var(--text)">{metrics}</p>
<span class="link-arrow">Read the case study {icon("arrow")}</span></div></a>"""


WHY = [("01", "One person, whole funnel", "No handoffs between a designer, a developer, an SEO and an automation freelancer. I see how each piece affects the next."),
       ("02", "I build, not just advise", "You don&rsquo;t get a slide deck of recommendations. You get working pages, tracking and automations, live."),
       ("03", "Judged on money", "Every piece of work is tied to a number that matters: leads, sales, booked calls. If it doesn&rsquo;t move, we change course.")]


def build_service(s):
    r = "../"
    pains = "".join(f'<div class="pain reveal"><i>&times;</i><span>{p}</span></div>' for p in s["pains"])
    deliv = "".join(f'<div class="deliv reveal"><div class="n">{i + 1:02d}</div><h4>{t}</h4><p>{d}</p></div>' for i, (t, d) in enumerate(s["deliv"]))
    steps = "".join(f'<div class="step reveal"><div class="when">{w}</div><div><h4>{t}</h4><p>{d}</p></div></div>' for w, t, d in s["steps"])
    proof = "".join(proof_card(k, r) for k in s["proof"])
    tools = "".join(f"<span>{t}</span>" for t in s["tools"])
    why = "".join(f'<div class="why reveal"><b>{n}</b><h4>{t}</h4><p>{d}</p></div>' for n, t, d in WHY)
    pk = []
    for i, (name, badge, fr, items, time) in enumerate(s["pkgs"]):
        hot = i == 1
        li = "".join(f"<li>{icon('check')}<span>{x}</span></li>" for x in items)
        pk.append(f"""<div class="pkg reveal{' hot' if hot else ''}"><span class="badge">{badge}</span><h3>{name}</h3><p class="for">{fr}</p><ul>{li}</ul>
<div class="time"><span>Timeline</span><strong>{time}</strong></div>
<a class="btn {'btn-primary' if hot else 'btn-ghost'}" href="#contact">Ask about this {icon("arrow")}</a></div>""")
    forl = "".join(f"<li>{icon('check-circle')}<span>{x}</span></li>" for x in s["for"])
    topic = {"revops": "RevOps / funnel audit", "marketing-automation": "Marketing automation", "ai-sales-agents": "AI sales agent",
             "seo": "SEO", "cro": "CRO / landing pages", "web-development": "Website", "analytics-tracking": "Analytics & tracking"}[s["slug"]]
    body = f"""
<section class="hero page-hero">
  <div class="container hero-grid">
    <div>
      <div class="crumbs reveal"><a href="{r}index.html">Mark Anthony Maina</a><span>/</span><a href="{r}services/index.html">Services</a><span>/</span><span>{s['name']}</span></div>
      <div class="kicker reveal">{s['kicker']}</div>
      <h1 class="reveal d1">{s['h1']}</h1>
      <p class="lead reveal d2">{s['lead']}</p>
      <ul class="for-list reveal d2">{forl}</ul>
      <div class="btn-row reveal d3"><a class="btn btn-primary" href="#contact">Book a free 20-min call {icon("arrow")}</a><a class="btn btn-ghost" href="#proof">See the proof</a></div>
    </div>
    <div>{hero_visual(s, r)}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal"><div class="kicker">Sound familiar?</div><h2>If any of this sounds like your business&hellip;</h2></div>
    <div class="pain-grid">{pains}</div>
    <p class="pain-close reveal">{s['pain_close']}</p>
  </div>
</section>

<section class="section section-white">
  <div class="container">
    <div class="section-head split"><div class="reveal"><div class="kicker">What you get</div><h2>What I actually <span class="serif">deliver.</span></h2></div>
    <p class="lead reveal d1">Real, working things. Not a report that sits in your inbox.</p></div>
    <div class="deliv-grid">{deliv}</div>
  </div>
</section>

<section class="section section-dark">
  <div class="container">
    <div class="section-head split"><div class="reveal"><div class="kicker">How it works</div><h2>From first call to <span class="serif">live.</span></h2></div>
    <p class="lead reveal d1">Clear steps, clear dates. You always know what I&rsquo;m doing this week and why.</p></div>
    <div class="steps">{steps}</div>
  </div>
</section>

<section class="section" id="proof">
  <div class="container">
    <div class="section-head split"><div class="reveal"><div class="kicker">Proof</div><h2>Here&rsquo;s where I&rsquo;ve done it <span class="serif">before.</span></h2></div>
    <p class="lead reveal d1">Real client accounts, real data. Click through for the full story, charts and all.</p></div>
    <div class="proof-grid">{proof}</div>
  </div>
</section>

<section class="section-tight section-white">
  <div class="container">
    <div class="kicker reveal">Tools I use for this</div>
    <div class="tool-row reveal">{tools}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head center reveal"><div class="kicker">Why me</div><h2>Why hire me instead of an <span class="serif">agency?</span></h2></div>
    <div class="why-grid">{why}</div>
  </div>
</section>

<section class="section section-white">
  <div class="container">
    <div class="section-head split"><div class="reveal"><div class="kicker">Ways to work together</div><h2>Pick a starting <span class="serif">point.</span></h2></div>
    <p class="lead reveal d1">Fixed price, agreed before we start. You&rsquo;ll get a straight number on the first call, not a range.</p></div>
    <div class="pkgs">{''.join(pk)}</div>
  </div>
</section>

<section class="section">
  <div class="container">{quotes_block(single=True)}</div>
</section>

<section class="section section-white" style="padding-top:calc(var(--section) * .6)">
  <div class="container narrow">
    <div class="section-head center reveal"><div class="kicker">Questions</div><h2>Before you ask&hellip;</h2></div>
    {faq_block(s['faq'])}
  </div>
</section>
{other_services(SERVICES, s['slug'], r)}
{contact(r, topic_default=topic)}
"""
    ld = [{"@context": "https://schema.org", "@type": "Service", "name": s["name"], "description": s["desc"],
           "provider": {"@type": "Person", "name": "Mark Anthony Maina", "url": BASE}, "areaServed": ["KE", "GB", "US"],
           "url": BASE + f"services/{s['slug']}.html"},
          {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
              {"@type": "Question", "name": q.replace("&rsquo;", "'"), "acceptedAnswer": {"@type": "Answer", "text": a.replace("&rsquo;", "'")}} for q, a in s["faq"]]}]
    write(f"services/{s['slug']}.html", page(f"services/{s['slug']}.html", s["title"], s["desc"], body, r, "services", ld))


def build_services_index():
    r = "../"
    body = f"""
<section class="hero page-hero">
  <div class="container">
    <div class="crumbs reveal"><a href="{r}index.html">Mark Anthony Maina</a><span>/</span><span>Services</span></div>
    <div class="kicker reveal">Services</div>
    <h1 class="reveal d1" style="max-width:900px">Everything between the first click and the <span class="serif">paid invoice.</span></h1>
    <p class="lead reveal d2">Each service has its own page with the full detail, proof and ways to work together. Not sure which one you need? That&rsquo;s literally what the free call is for.</p>
  </div>
</section>
<section class="section section-white"><div class="container">{svc_cards(r)}</div></section>
<section class="section"><div class="container">
  <div class="section-head split"><div class="reveal"><div class="kicker">How I work</div><h2>One loop. Every <span class="serif">client.</span></h2></div>
  <p class="lead reveal d1">Whatever the service, the method is the same: measure, find the biggest leak, fix it, prove it.</p></div>
  {loop_block()}
</div></section>
{contact(r)}
"""
    write("services/index.html", page("services/", "Services | RevOps, Automation, AI Agents, SEO, CRO & Web | Mark Anthony Maina",
                                      "RevOps, marketing automation, AI sales agents, SEO, CRO, websites and analytics. One person covering the whole path from first click to paid invoice.",
                                      body, r, "services"))


# ---------------------------------------------------------------- case study page
def build_case(c, idx):
    r = "../"
    stats = "".join(f'<div><b class="{cls}">{v}</b>{l}</div>' for v, l, cls in c["stats"])
    if c["slug"] == "ai-sales-agent":
        top = f'<div class="figure dark" style="background:var(--ink-2);border-radius:26px;padding:26px;box-shadow:var(--shadow-lg)">{AGENT_DIAGRAM}</div>'
    elif c["slug"] == "searv":
        top = f'<div class="figure dark" style="background:var(--ink-2);border-radius:26px;padding:26px;box-shadow:var(--shadow-lg)">{SEARV_DIAGRAM}</div>'
    else:
        top = browser(c["shot"], c["url"], c["client"] + " website", r)
    site = f'<div><small>Website</small><a href="https://www.{c["url"]}" target="_blank" rel="noopener">{c["url"]}</a></div>' if c["url"] else ""
    svcs = "<br>".join(c["services"])
    nxt = CASES[(idx + 1) % len(CASES)]
    related = [s for s in SERVICES if c["slug"] in s["proof"] or (c["slug"] == "searv" and "bil" in s["proof"])]
    rel = "".join(f'<a href="{r}services/{s["slug"]}.html"><span class="ic">{icon(s["icon"])}</span>{s["name"]}</a>' for s in related)
    body = f"""
<section class="hero page-hero" style="padding-bottom:clamp(110px, 12vw, 170px)">
  <div class="container">
    <div class="crumbs reveal"><a href="{r}index.html">Mark Anthony Maina</a><span>/</span><a href="{r}work/index.html">Work</a><span>/</span><span>{c['client']}</span></div>
    <div class="kicker reveal">Case study &middot; {c['industry']} &middot; {c['where']}</div>
    <h1 class="reveal d1" style="max-width:980px">{c['h1']}</h1>
    <p class="lead reveal d2" style="max-width:760px">{c['lead']}</p>
    <div class="cs-stats reveal d3">{stats}</div>
  </div>
</section>
<div class="container cs-shot reveal">{top}</div>
<section class="section">
  <div class="container cs-layout">
    <aside class="cs-aside">
      <div><small>Client</small>{c['client']}</div>
      <div><small>Industry</small>{c['industry']}</div>
      <div><small>Location</small>{c['where']}</div>
      <div><small>When</small>{c['year']}</div>
      <div><small>What I did</small>{svcs}</div>
      {site}
      <a class="btn btn-primary" href="#contact">Want this for you? {icon("arrow")}</a>
    </aside>
    <article class="cs-body anim">{c['body'](r)}</article>
  </div>
</section>
<section class="section-tight section-white"><div class="container">
  <div class="kicker">Services used here</div>
  <div class="other-svcs" style="margin-bottom:40px">{rel}</div>
  <a class="next-case" href="{r}work/{nxt['slug']}.html"><div><small>Next case study</small><h3>{nxt['card_title']}</h3></div><span class="arrow">{icon("arrow")}</span></a>
</div></section>
{contact(r)}
"""
    write(f"work/{c['slug']}.html", page(f"work/{c['slug']}.html", f"{strip(c['card_title'])} | {strip(c['client'])} case study | Mark Anthony Maina",
                                         strip(c["summary"]), body, r, "work"))


def strip(s):
    import html as _h
    import re
    return _h.unescape(re.sub("<[^>]+>", "", s))


def build_work_index():
    r = "../"
    cards = "".join(case_card(c, r, flip=i % 2 == 1) for i, c in enumerate(CASES))
    links = {"kiboko": "https://www.kibokotoursandtravel.com", "debluc": "https://www.debluchairessentials.co.ke",
             "snapshot": "https://www.snapshotteambuilding.com", "ganiam": GANIAM}
    sites = "".join(f'<a class="site reveal" href="{links[img]}" target="_blank" rel="noopener">{browser(img, u, n, r)}<h4>{n}</h4><p>{d}</p></a>'
                    if img in links else
                    f'<div class="site reveal">{browser(img, u, n, r)}<h4>{n}</h4><p>{d}</p></div>' for img, n, u, d in SITES)
    body = f"""
<section class="hero page-hero">
  <div class="container">
    <div class="crumbs reveal"><a href="{r}index.html">Mark Anthony Maina</a><span>/</span><span>Work</span></div>
    <div class="kicker reveal">Work &amp; results</div>
    <h1 class="reveal d1" style="max-width:940px">The proof. Clients, numbers and the <span class="serif">systems</span> behind them.</h1>
    <p class="lead reveal d2">Case studies with the real data, the websites I&rsquo;ve built, and the machines running quietly behind them. Where results are still coming in, I say so.</p>
  </div>
</section>
<section class="section section-dark" style="padding-top:clamp(40px,5vw,70px)"><div class="container"><div class="cases">{cards}</div></div></section>
<section class="section section-white"><div class="container">
  <div class="section-head split"><div class="reveal"><div class="kicker">Websites</div><h2>Sites that do a <span class="serif">job.</span></h2></div>
  <p class="lead reveal d1">Every one built with tracking, lead capture and SEO structure from day one. Design is how it looks; conversion is how it works.</p></div>
  <div class="gallery">{sites}</div>
  <p style="margin-top:28px;color:var(--muted);font-size:15px">Earlier work includes Jacich Safaris (booking flow + GA4), Mommy&amp;Me Baby Shop (Shopify with UGC video), JW Law Advocates (lead-gen legal site), and company profiles and sites for SARL, Wafftech and Soland Enterprises.</p>
</div></section>
<section class="section section-dark"><div class="container">
  <div class="section-head split"><div class="reveal"><div class="kicker">Systems</div><h2>The machines behind the <span class="serif">results.</span></h2></div>
  <p class="lead reveal d1">Most of these exist because an off-the-shelf tool couldn&rsquo;t do the job at a price the client could pay.</p></div>
  {systems_grid()}
</div></section>
{contact(r)}
"""
    write("work/index.html", page("work/", "Work & Results: Case Studies, Websites & Systems | Mark Anthony Maina",
                                  "Case studies with real client data: +47% conversions, +74% organic traffic, a full safari-site recovery audit, AI WhatsApp sales agents and more.",
                                  body, r, "work"))


if __name__ == "__main__":
    build_home()
    build_services_index()
    for s in SERVICES:
        build_service(s)
    for i, c in enumerate(CASES):
        build_case(c, i)
    build_work_index()
