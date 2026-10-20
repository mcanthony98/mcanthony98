"""The /services/seo.html page. Same idea as the websites page: proof first, few words.
All numbers are Google Search Console totals from the RevOps app (Oct 2026)."""
from kit import BASE, bar_chart, chart_block, icon, line_chart
from content import QUOTES, kiboko_clicks_weekly


def debluc_rank(w=480):
    return chart_block("Average position on Google (lower is better)",
                       line_chart(w=w, points=[("May", 23.4), ("Jun", 19.6), ("Jul", 18.6), ("Aug", 15.3), ("Sep", 9.6), ("Oct", 8.9)],
                                  color="money", h=200, fmt="{:.0f}", invert=True, ymin=6, ymax=26),
                       sub="page 3 &rarr; page 1", source="Google Search Console, 2026")


def debluc_clicks(w=480):
    return chart_block("Clicks from Google",
                       bar_chart(w=w, bars=[("May", 3, "muted"), ("Jun", 6, "money"), ("Jul", 17, "money"), ("Aug", 22, "money")], h=200, ymax=26),
                       sub="7&times; in 3 months", source="Google Search Console, 2026")


def _unused_snaptours_ctr(w=480):
    return chart_block("Searchers who click through",
                       line_chart(w=w, points=[("Aug", 2.7), ("Sep", 8.5), ("Oct", 9.5)], color="money", h=200, fmt="{:.1f}%", ymin=0, ymax=11),
                       sub="2.7% &rarr; 9.5%", source="Google Search Console (CTR), 2026")


INCLUDED = [
    ("Fix the site", [("bolt", "Technical SEO", "Speed, broken pages, duplicate pages and sitemaps. Fixed in the code, not listed in a PDF."),
                      ("funnel", "Hacked-site cleanup", "Spam pages removed, security holes closed, Google told the site is safe again.")]),
    ("Win the searches", [("search", "Keyword research", "The exact words your buyers type when they&rsquo;re ready to pay."),
                          ("code", "On-page SEO", "Titles, headings, page copy and product descriptions rewritten for people and Google."),
                          ("users", "Local SEO", "Google Business Profile, reviews and directories, so you show up in &ldquo;near me&rdquo; and Maps.")]),
    ("Prove it works", [("chart", "Tracking", "Google Search Console, GA4 and Microsoft Clarity, set up properly."),
                        ("mail", "Monthly report", "One page: what moved, what it brought you, what&rsquo;s next."),
                        ("wa", "Leads, not just traffic", "Every WhatsApp tap, call and form from Google is counted.")]),
]

FAQ = [
    ("How long does SEO take?", "Fixes can show in 2 to 4 weeks, like Kiboko. Bigger ranking gains usually take 2 to 4 months. You see progress in the monthly report from month one."),
    ("Can you guarantee number one on Google?", "No honest SEO can. I can guarantee a site Google can read, pages that match what buyers search, and honest numbers every month."),
    ("How much does SEO cost?", "An audit is KES 25,000. Monthly SEO starts from KES 35,000. Local SEO setup is KES 15,000."),
    ("Do you build backlinks?", "Only real ones: directories, partners, suppliers and press. No link farms. They get sites punished."),
]


def build(page, write, contact, r="../"):
    groups = "".join(
        f'<div class="inc reveal"><h3>{g}</h3>' + "".join(
            f'<div class="inc-item"><span class="ic">{icon(i)}</span><div><h4>{t}</h4><p>{d}</p></div></div>' for i, t, d in items) + "</div>"
        for g, items in INCLUDED)
    flow = "".join(f'<div class="fl reveal"><span class="ic">{icon(i)}</span><b>{t}</b><small>{s}</small></div>' + ('<span class="fl-arrow">' + icon("arrow") + "</span>" if n < 4 else "")
                   for n, (i, t, s) in enumerate([("search", "Searched", "a buyer types it"), ("chart", "Shown", "you&rsquo;re on page one"), ("cursor", "Clicked", "your title wins the click"),
                                                  ("code", "Convinced", "the page answers them"), ("wa", "Contacted", "WhatsApp, call or form")]))
    quotes = "".join(f'<blockquote class="quote reveal"><div class="mark">&ldquo;</div><p>{q}</p><footer><i>{n[0]}</i><div><strong>{n}</strong><span>{ro}</span></div></footer></blockquote>'
                     for q, n, ro in QUOTES)
    pk = [("SEO audit", "Starter", "Find out exactly what&rsquo;s holding you back.", "KES 25,000", "", ["Full technical check", "Keyword and competitor gaps", "Ranked list of fixes", "Walkthrough call"], False),
          ("Monthly SEO", "Most chosen", "Steady growth you can see in enquiries.", "KES 35,000", " / month", ["Technical fixes every month", "2 new or improved pages a month", "Google Business Profile care", "Monthly report on leads", "3-month minimum"], True),
          ("Local SEO setup", "One-off", "Show up in &ldquo;near me&rdquo; and Maps.", "KES 15,000", "", ["Google Business Profile set up", "Photos, services and hours", "Review request plan", "Top local directories"], False)]
    pkgs = "".join(f"""<div class="pkg reveal{' hot' if hot else ''}"><span class="badge">{badge}</span><h3>{nm}</h3><p class="for">{fr}</p>
<div class="wprice">From <b>{amt}<span style="font-size:15px;font-weight:500;letter-spacing:0">{per}</span></b></div><ul>{''.join(f"<li>{icon('check')}<span>{x}</span></li>" for x in items)}</ul>
<a class="btn {'btn-primary' if hot else 'btn-ghost'}" href="#contact">Get started {icon('arrow')}</a></div>""" for nm, badge, fr, amt, per, items, hot in pk)
    faq = "".join(f'<details><summary>{q}<i></i></summary><div class="ans"><p>{a}</p></div></details>' for q, a in FAQ)
    serp = f"""<div class="serpcard">
  <div class="sq">{icon("search")}<span>best [what you sell] in Nairobi</span></div>
  <div class="sr you"><small>yourbusiness.co.ke &middot; example</small><b>Your Business | The best [what you sell] in Nairobi</b><p>The answer your buyer was looking for, with prices, reviews and one tap to WhatsApp&hellip;</p></div>
  <div class="sr dim"><small>competitor.co.ke</small><b>Your competitor</b><p>Competing for the same customer&hellip;</p></div>
  <div class="sr dim"><small>directory.com</small><b>Top 10 list</b><p>A list you&rsquo;re not on yet&hellip;</p></div>
</div>"""

    body = f"""
<section class="hero page-hero">
  <div class="container hero-grid">
    <div>
      <div class="crumbs reveal"><a href="{r}index.html">Mark Anthony Maina</a><span>/</span><a href="{r}services/index.html">Services</a><span>/</span><span>SEO</span></div>
      <div class="kicker reveal">SEO &middot; Technical, on-page &amp; local</div>
      <h1 class="reveal d1">Get found on Google by people <span class="serif">ready to buy.</span></h1>
      <p class="lead reveal d2">Not more traffic. The <strong>right</strong> traffic. I fix what stops Google trusting your site, rewrite the pages that should rank, and report on enquiries, not vanity numbers.</p>
      <div class="btn-row reveal d3"><a class="btn btn-primary" href="#contact">Get a free SEO check {icon("arrow")}</a><a class="btn btn-ghost" href="#results">See the results</a></div>
    </div>
    <div class="reveal d2" style="position:relative">
      {serp}
      <a class="wchip" href="{r}work/kiboko.html" style="bottom:-30px"><b>4&times;</b><span>Google clicks in a month<br><u>See the Kiboko story</u></span></a>
    </div>
  </div>
</section>

<section class="section" id="results" style="padding-top:clamp(56px,7vw,90px)">
  <div class="container">
    <div class="section-head split"><div class="reveal"><div class="kicker">Results</div><h2>SEO results I&rsquo;ve <span class="serif">delivered.</span></h2></div>
    <p class="lead reveal d1">Straight from each client&rsquo;s Google Search Console. Click through to see the live sites.</p></div>
    <a class="wfeature reveal" href="{r}work/kiboko.html">
      <div class="wf-body" style="border-right:1px solid var(--line)"><div class="anim">{kiboko_clicks_weekly(w=520)}</div></div>
      <div class="wf-body">
        <span class="wtag">Case study &middot; Safari company</span>
        <h3>Kiboko Tours &amp; Travel</h3>
        <p>Fading on Google for a year. We fixed the site and rebuilt the homepage. Four weeks later:</p>
        <div class="wf-stats"><div><b>4&times;</b>Google clicks</div><div><b>3&times;</b>click-through rate</div><div><b>36&rarr;17</b>Google position</div></div>
        <span class="link-arrow">Read the case study {icon("arrow")}</span>
      </div>
    </a>
    <div class="seo-grid">
      <a class="seo-card reveal" href="https://www.debluchairessentials.co.ke/" target="_blank" rel="noopener">
        <div class="seo-top"><div><span class="wtag">Online store &middot; Nairobi</span><h3>Debluc Hair Essentials</h3></div><div class="seo-big"><b>p3&rarr;p1</b><small>on Google</small></div></div>
        <div class="seo-charts"><div class="anim">{debluc_rank(w=360)}</div><div class="anim">{debluc_clicks(w=360)}</div></div>
        <p>All 30 pages and the full catalogue rewritten for what Kenyans search. Average position went from 23 to 9, and clicks rose 7&times; in three months.</p>
        <span class="wlink">Visit site {icon("arrow")}</span>
      </a>
      <div class="seo-card reveal d1">
        <div class="seo-top"><div><span class="wtag">SEO audit &middot; Safari company</span><h3>What an audit finds</h3></div><div class="seo-big"><b>10</b><small>findings in one audit</small></div></div>
        <p>A real audit from September 2026 (client kept private). The site looked fine. Google saw something else:</p>
        <ul class="seo-finds">
          <li><b>18 of 18</b> destination pages in the sitemap quietly sent visitors to the homepage. One was the site&rsquo;s #2 page on Google, with zero clicks.</li>
          <li><b>9 of 20</b> safari packages were dead ends, including 5 linked on every page.</li>
          <li><b>No Google Analytics</b> had ever been installed, so nobody knew where bookings came from.</li>
        </ul>
        <a class="wlink" href="#contact">Get your site checked {icon("arrow")}</a>
      </div>
    </div>
  </div>
</section>

<section class="section section-white">
  <div class="container">
    <div class="section-head center reveal"><div class="kicker">What&rsquo;s included</div><h2>Not just rankings. <span class="serif">Customers.</span></h2>
    <p class="lead">I fix the site, win the searches that matter, and prove it with numbers.</p></div>
    <div class="incs">{groups}</div>
  </div>
</section>

<section class="section section-dark">
  <div class="container">
    <div class="section-head center reveal"><div class="kicker">How SEO makes money</div><h2>Five steps from search <span class="serif">to sale.</span></h2>
    <p class="lead">Most SEO stops at step 2. I work on all five.</p></div>
    <div class="flowrow">{flow}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head split"><div class="reveal"><div class="kicker">Pricing</div><h2>Clear prices. <span class="serif">No surprises.</span></h2></div>
    <p class="lead reveal d1">Start with an audit, or go straight to monthly SEO. Fixed price, agreed before we start.</p></div>
    <div class="pkgs">{pkgs}</div>
  </div>
</section>

<section class="section section-white">
  <div class="container">
    <div class="section-head reveal"><div class="kicker">Kind words</div><h2>What clients <span class="serif">say.</span></h2></div>
    <div class="wquotes">{quotes}</div>
  </div>
</section>

<section class="section" style="padding-top:calc(var(--section) * .6)">
  <div class="container narrow">
    <div class="section-head center reveal"><h2>Quick answers</h2></div>
    <div class="faq reveal">{faq}</div>
  </div>
</section>
{contact(r, title='Let&rsquo;s get you <span class="serif">found.</span>', lead="Send me your website. I&rsquo;ll check it for free and tell you the 3 things holding you back on Google.", topic_default="SEO")}
"""
    ld = [{"@context": "https://schema.org", "@type": "Service", "name": "SEO services",
           "description": "Technical, on-page and local SEO with monthly reporting tied to enquiries.",
           "provider": {"@type": "Person", "name": "Mark Anthony Maina", "url": BASE}, "areaServed": ["KE", "GB", "US"],
           "url": BASE + "services/seo.html"},
          {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
              {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a.replace("&rsquo;", "'")}} for q, a in FAQ]}]
    write("services/seo.html", page("services/seo.html", "SEO Services: Get Found on Google by Buyers | Mark Anthony Maina",
          "SEO that brings enquiries: technical, on-page and local SEO. Kiboko got 4x the Google clicks in a month; Debluc went from page 3 to page 1.",
          body, r, "services", ld))
