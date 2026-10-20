"""The /services/web-development.html page. Built on its own (not the shared service template)
because it is sent to website clients directly: sites first, few words."""
from kit import BASE, icon
from content import CASE, QUOTES, SVC

# (image, name, what it is, where, live url or None)
SITES = [
    ("sarl", "SARL", "Construction &amp; interiors company", "Kenya", "https://sarl.co.ke/"),
    ("kareithi", "Kareithi Properties", "Land and property listings", "Kenya", "https://kareithiproperties.com/"),
    ("kundi", "Kundi Home", "German kitchens showroom", "UK", "https://kundi.ganiamtech.com/"),
    ("sierra", "Sierra Restaurants", "Restaurant group, with its own admin", "Kenya", "https://www.sierrarestaurants.com/"),
    ("metro", "Metro Design Build", "Design &amp; build contractor", "UK", "https://metro-design-build.netlify.app/services"),
    ("bil", "Body &amp; Its Language", "Health coaching, quiz to booked call", "USA", "https://bodyanditslanguage.com/"),
    ("debluc", "Debluc Hair Essentials", "Online store on Odoo", "Kenya", "https://www.debluchairessentials.co.ke/"),
    ("signvita", "Signvita", "Climate &amp; agri-tech company", "Kenya", "https://signvita.co.ke/"),
    ("snapteam", "Snapshot Team Building", "Corporate events", "Kenya", "https://www.snapshotteambuilding.com/"),
    ("snaptours", "Snapshot Tours &amp; Safaris", "Safari company", "Kenya", "https://snapshottoursandsafaris.com/"),
    ("boblegal", "Bob Legal", "Law firm", "Kenya", "https://boblegal.org/"),
    ("esteem", "Esteem Consultancy", "Mental wellness", "Kenya", "https://esteemconsultancy.org/"),
    ("ffm", "Food for Ministers", "Charity", "", "https://foodforministers.com/"),
    ("wafftech", "Wafftech Services", "Engineering services", "Kenya", "https://wafftechservices.co.ke/"),
    ("kiliki", "Kiliki Beekeepers", "Honey producer", "Kenya", None),
]

INCLUDED = [
    ("Build it", [("code", "Custom design", "Made around your business and your customers. Never a template."),
                  ("funnel", "Admin portal", "Change text, photos, prices and posts yourself. No developer needed.")]),
    ("Get it seen", [("search", "SEO", "Set up so Google can find you and show you to buyers."),
                     ("chart", "Tracking", "Google Search Console, GA4 and Microsoft Clarity: see who visits and what they do."),
                     ("bolt", "Domain &amp; hosting", "Your name online, fast and secure, registered in your name.")]),
    ("Get reached", [("mail", "Business email", "you@yourbusiness.com, set up on your own domain."),
                     ("wa", "WhatsApp, calls &amp; forms", "One tap to reach you, from any page."),
                     ("users", "CRM", "Every enquiry saved in one place, so no customer is forgotten.")]),
]

FAQ = [
    ("How much does a website cost?", "From KES 35,000 for a one-page site, KES 100,000 for a full business website, and from KES 150,000 for a website with custom features, AI automations and integrations. You get one fixed price before we start."),
    ("How long does it take?", "1 to 2 days for a one-page site and about 1 week for a business website. Custom builds depend on the features you need."),
    ("Are there any hidden costs?", "No. There are no other costs. Your website is live and maintained for one full year. After that, it&rsquo;s KES 10,000 a year to renew your domain, hosting and maintenance."),
    ("Can I update it myself?", "Yes. Every site comes with an admin portal, and I show you how to use it."),
    ("Is the domain and email in my name?", "Yes. Your domain, hosting, email and data always belong to you."),
]


def build(page, write, contact, r="../"):
    k = CASE["kiboko"]
    cards = "".join(
        (f'<a class="wsite reveal" href="{u}" target="_blank" rel="noopener">' if u else '<div class="wsite reveal">')
        + f'<div class="wshot"><img src="{r}assets/img/sites/{img}.webp" alt="{n} website" loading="lazy" width="1000" height="625"></div>'
        + f'<div class="wmeta"><div><h4>{n}</h4><p>{d}</p></div>{f'<span class="wtag">{c}</span>' if c else ''}</div>'
        + (f'<span class="wlink">Visit site {icon("arrow")}</span></a>' if u else '</div>')
        for img, n, d, c, u in SITES)
    groups = "".join(
        f'<div class="inc reveal"><h3>{g}</h3>' + "".join(
            f'<div class="inc-item"><span class="ic">{icon(i)}</span><div><h4>{t}</h4><p>{d}</p></div></div>' for i, t, d in items) + "</div>"
        for g, items in INCLUDED)
    flow = "".join(f'<div class="fl reveal"><span class="ic">{icon(i)}</span><b>{t}</b><small>{s}</small></div>' + ('<span class="fl-arrow">' + icon("arrow") + "</span>" if n < 4 else "")
                   for n, (i, t, s) in enumerate([("search", "Found", "on Google"), ("code", "Trusted", "on your website"), ("wa", "Reached", "WhatsApp, call or form"),
                                                  ("users", "Saved", "in your CRM"), ("chart", "Measured", "so you know what works")]))
    quotes = "".join(f'<blockquote class="quote reveal"><div class="mark">&ldquo;</div><p>{q}</p><footer><i>{n[0]}</i><div><strong>{n}</strong><span>{ro}</span></div></footer></blockquote>'
                     for q, n, ro in QUOTES)
    pk = [("One-page site", "One offer, one page.", "KES 35,000", ["Custom design", "WhatsApp, call and form", "Domain, hosting and tracking", "Ready in 1 to 2 days"], False),
          ("Business website", "For most growing businesses.", "KES 100,000", ["Up to 8 pages", "Admin portal", "SEO, domain, hosting and business email", "GA4, Search Console and Clarity", "Ready in 1 week"], True),
          ("Custom website", "Built around how your business works.", "KES 150,000", ["Everything in Business", "Custom features and customizations", "AI automations", "Integrations: payments, CRM, bookings and more"], False)]
    pkgs = "".join(f"""<div class="pkg reveal{' hot' if hot else ''}"><span class="badge">{badge}</span><h3>{nm}</h3><p class="for">{fr}</p>
<div class="wprice">From <b>{amt}</b></div><ul>{''.join(f"<li>{icon('check')}<span>{x}</span></li>" for x in items)}</ul>
<a class="btn {'btn-primary' if hot else 'btn-ghost'}" href="#contact">Get a quote {icon('arrow')}</a></div>""" for (nm, fr, amt, items, hot), badge in zip(pk, ["Starter", "Most chosen", "Advanced"]))
    faq = "".join(f'<details><summary>{q}<i></i></summary><div class="ans"><p>{a}</p></div></details>' for q, a in FAQ)

    body = f"""
<section class="hero page-hero">
  <div class="container hero-grid">
    <div>
      <div class="crumbs reveal"><a href="{r}index.html">Mark Anthony Maina</a><span>/</span><a href="{r}services/index.html">Services</a><span>/</span><span>Websites</span></div>
      <div class="kicker reveal">Custom websites &middot; Kenya, UK, USA</div>
      <h1 class="reveal d1">Not just a website. <span class="serif">A system that brings you customers.</span></h1>
      <p class="lead reveal d2">I build custom websites made for your business, then handle everything around them: so people <strong>find you</strong>, <strong>trust you</strong> and <strong>reach you</strong>.</p>
      <div class="btn-row reveal d3"><a class="btn btn-primary" href="#contact">Get a free quote {icon("arrow")}</a><a class="btn btn-ghost" href="#sites">See sites I&rsquo;ve built</a></div>
    </div>
    <div class="reveal d2" style="position:relative">
      <div class="wshot" style="border-radius:12px;box-shadow:0 40px 80px -40px rgba(0,0,0,.8)"><img src="{r}assets/img/sites/kiboko.webp" alt="Kiboko Tours website" width="1000" height="625"></div>
      <div class="wphone"><img src="{r}assets/img/sites/kiboko-m.webp" alt="Kiboko Tours on mobile" width="400" height="800"></div>
      <a class="wchip" href="{r}work/kiboko.html"><b>4&times;</b><span>Google clicks in a month<br><u>See the Kiboko story</u></span></a>
    </div>
  </div>
</section>

<section class="section" id="sites" style="padding-top:clamp(56px,7vw,90px)">
  <div class="container">
    <div class="section-head split"><div class="reveal"><div class="kicker">My work</div><h2>Websites I&rsquo;ve <span class="serif">built.</span></h2></div>
    <p class="lead reveal d1">Real businesses in Kenya, the UK and the USA. Click any site to see it live.</p></div>
    <a class="wfeature reveal" href="{r}work/kiboko.html">
      <div class="wshot"><img src="{r}assets/img/sites/kiboko.webp" alt="Kiboko Tours &amp; Travel website" loading="lazy" width="1000" height="625"></div>
      <div class="wf-body">
        <span class="wtag">Case study &middot; Kenya</span>
        <h3>Kiboko Tours &amp; Travel</h3>
        <p>A safari company fading on Google. We fixed the site and rebuilt the homepage. Four weeks later:</p>
        <div class="wf-stats"><div><b>4&times;</b>Google clicks</div><div><b>3&times;</b>click-through rate</div><div><b>36&rarr;17</b>Google position</div></div>
        <span class="link-arrow">Read the case study {icon("arrow")}</span>
      </div>
    </a>
    <div class="wgrid">{cards}</div>
    <p class="reveal" style="margin-top:22px;color:var(--muted);font-size:15px">Also: <a class="link-arrow" style="display:inline-flex" href="https://outboundexports.co.ke/" target="_blank" rel="noopener">Outbound Exports</a>, Jacich Safaris, JW Law Advocates, Timkent Spares, Mommy&amp;Me Baby Shop and more.</p>
  </div>
</section>

<section class="section section-white">
  <div class="container">
    <div class="section-head center reveal"><div class="kicker">Everything around the website</div><h2>I don&rsquo;t just build it. <span class="serif">I make it work.</span></h2>
    <p class="lead">Creating it, getting it seen, and making sure customers can reach you. All in one place.</p></div>
    <div class="incs">{groups}</div>
  </div>
</section>

<section class="section section-dark">
  <div class="container">
    <div class="section-head center reveal"><div class="kicker">It&rsquo;s a system</div><h2>A website that <span class="serif">works while you sleep.</span></h2></div>
    <div class="flowrow">{flow}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head split"><div class="reveal"><div class="kicker">Pricing</div><h2>Clear prices. <span class="serif">No surprises.</span></h2></div>
    <p class="lead reveal d1">One fixed price before we start. Every site includes its first year of domain, hosting and maintenance. No hidden costs.</p></div>
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
{contact(r, title='Let&rsquo;s build your <span class="serif">website.</span>', lead="Tell me about your business. You&rsquo;ll get a clear plan and one fixed price, usually the same day.", topic_default="Website")}
"""
    s = SVC["web-development"]
    ld = [{"@context": "https://schema.org", "@type": "Service", "name": "Custom website design and development",
           "description": "Custom websites with admin portal, SEO, domain and hosting, business email, tracking and CRM.",
           "provider": {"@type": "Person", "name": "Mark Anthony Maina", "url": BASE}, "areaServed": ["KE", "GB", "US"],
           "url": BASE + "services/web-development.html"},
          {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
              {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}]
    write("services/web-development.html", page("services/web-development.html",
          "Custom Website Design &amp; Development | Mark Anthony Maina".replace("&amp;", "&"),
          "Custom websites for businesses in Kenya, the UK and the USA, with admin portal, SEO, domain, business email, tracking and CRM. See 16+ sites I've built.",
          body, r, "services", ld))
