"""Shared building blocks: icons, SVG charts, page shell, header, footer, contact.

Jekyll ignores folders that start with "_", so nothing in _src/ is published.
Run `python _src/build.py` from the repo root to regenerate every page.
"""
import html
import json

BASE = "https://mcanthony98.github.io/mcanthony98/"
EMAIL = "mmaina.online@gmail.com"
WHATSAPP = "https://wa.me/254799830928"
LINKEDIN = "https://www.linkedin.com/in/mark-maina-web-dev/"
GITHUB = "https://github.com/mcanthony98"
GANIAM = "https://ganiamtech.com/"
FONTS = ("https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,600;12..96,700;12..96,800"
         "&family=Instrument+Serif:ital@1&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500&display=swap")

esc = html.escape

# ---------------------------------------------------------------- icons
_P = {
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "down": '<path d="M6 9l6 6 6-6"/>',
    "check": '<path d="M20 6L9 17l-5-5"/>',
    "check-circle": '<circle cx="12" cy="12" r="9"/><path d="M8.5 12.5l2.5 2.5 5-5.5"/>',
    "funnel": '<path d="M3 4h18l-7 8.5V19l-4 2v-8.5L3 4z"/>',
    "bolt": '<path d="M13 2L4 14h7l-1 8 9-12h-7l1-8z"/>',
    "bot": '<rect x="4" y="8" width="16" height="12" rx="3"/><path d="M12 8V4M9 14h.01M15 14h.01M8 4h8"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/>',
    "cursor": '<path d="M5 3l14 7-6 2-2 6L5 3z"/>',
    "code": '<path d="M8 6l-6 6 6 6M16 6l6 6-6 6"/>',
    "chart": '<path d="M3 3v18h18"/><path d="M7 15l4-4 3 3 5-6"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
    "wa": '<path d="M20.5 11.6a8.5 8.5 0 0 1-12.6 7.4L3.5 20.5 5 16.3A8.5 8.5 0 1 1 20.5 11.6z"/><path d="M9 8.8c.3 2.9 2.4 5 5.2 5.6l1.1-1.2 1.9.8-.4 1.8c-4.4.3-8.4-3.4-8.6-7.9l1.7-.5.9 1.8-1.2 1.2"/>',
    "in": '<rect x="3" y="3" width="18" height="18" rx="3"/><path d="M8 10v7M8 7v.01M12 17v-4a2 2 0 0 1 4 0v4M12 10v7"/>',
    "gh": '<path d="M9 19c-4.3 1.4-4.3-2.5-6-3m12 5v-3.5c0-1 .1-1.4-.5-2 2.8-.3 5.5-1.4 5.5-6a4.6 4.6 0 0 0-1.3-3.2 4.2 4.2 0 0 0-.1-3.2s-1.1-.3-3.5 1.3a12.3 12.3 0 0 0-6.2 0C6.5 2.8 5.4 3.1 5.4 3.1a4.2 4.2 0 0 0-.1 3.2A4.6 4.6 0 0 0 4 9.5c0 4.6 2.7 5.7 5.5 6-.6.6-.6 1.2-.5 2V21"/>',
    "alert": '<path d="M12 3l10 18H2L12 3z"/><path d="M12 10v5M12 18v.01"/>',
    "users": '<circle cx="9" cy="8" r="4"/><path d="M2 21a7 7 0 0 1 14 0M16 4a4 4 0 0 1 0 8M22 21a7 7 0 0 0-4-6.3"/>',
    "grad": '<path d="M2 9l10-5 10 5-10 5L2 9z"/><path d="M6 11v5c3 2.5 9 2.5 12 0v-5M22 9v6"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.7 3.8 5.7 3.8 9s-1.3 6.3-3.8 9c-2.5-2.7-3.8-5.7-3.8-9S9.5 5.7 12 3z"/>',
    "cal": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
}


def icon(name, cls=""):
    c = f' class="{cls}"' if cls else ""
    return (f'<svg{c} viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{_P[name]}</svg>')


# ---------------------------------------------------------------- charts
COLORS = {"violet": "#6552e0", "violet2": "#8676ff", "money": "#10a765", "money2": "#3ddc97",
          "red": "#e0474c", "red2": "#ff8b8f", "amber": "#e89b1c", "sky": "#8fb4e8", "muted": "#c9c6d8"}
_uid = [0]


def _id(prefix):
    _uid[0] += 1
    return f"{prefix}{_uid[0]}"


def line_chart(points, color="violet", w=480, h=240, fmt="{:,.0f}", ymin=None, ymax=None, invert=False,
               note=None, label_last_only=False):
    """points: [(label, value)]. invert=True puts lower values higher (e.g. Google position)."""
    pad_l, pad_r, pad_t, pad_b = 12, 16, 30, 30
    vals = [v for _, v in points]
    lo = min(vals) if ymin is None else ymin
    hi = max(vals) if ymax is None else ymax
    if hi == lo:
        hi += 1
    iw, ih = w - pad_l - pad_r, h - pad_t - pad_b
    n = len(points)

    def xy(i, v):
        x = pad_l + (iw * i / (n - 1) if n > 1 else iw / 2)
        t = (v - lo) / (hi - lo)
        y = pad_t + (t * ih if invert else (1 - t) * ih)
        return round(x, 1), round(y, 1)

    pts = [xy(i, v) for i, (_, v) in enumerate(points)]
    col = COLORS[color]
    gid = _id("g")
    d = "M" + " L".join(f"{x},{y}" for x, y in pts)
    area = d + f" L{pts[-1][0]},{pad_t + ih} L{pts[0][0]},{pad_t + ih} Z"
    grid = "".join(f'<line x1="{pad_l}" x2="{w - pad_r}" y1="{pad_t + ih * k / 3:.1f}" y2="{pad_t + ih * k / 3:.1f}"/>' for k in range(4))
    dots, labels = [], []
    for i, ((lab, v), (x, y)) in enumerate(zip(points, pts)):
        dots.append(f'<circle class="dot" cx="{x}" cy="{y}" r="4.5" fill="{col}" stroke="#fff" stroke-width="2"/>')
        anchor = "start" if i == 0 else ("end" if i == n - 1 else "middle")
        labels.append(f'<text x="{x}" y="{h - 8}" text-anchor="{anchor}">{lab}</text>')
        if not label_last_only or i in (0, n - 1):
            ty = y - 12 if y - 12 > 12 else y + 22
            labels.append(f'<text class="val fade" x="{x}" y="{ty}" text-anchor="{anchor}">{fmt.format(v)}</text>')
    extra = ""
    if note:
        extra = f'<text class="fade" x="{w - pad_r}" y="14" text-anchor="end">{note}</text>'
    return (f'<svg class="chart" viewBox="0 0 {w} {h}" role="img" aria-label="line chart">'
            f'<defs><linearGradient id="{gid}" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="{col}" stop-opacity=".28"/>'
            f'<stop offset="1" stop-color="{col}" stop-opacity="0"/></linearGradient></defs>'
            f'<g class="grid">{grid}</g><path class="area" d="{area}" fill="url(#{gid})"/>'
            f'<path class="draw" d="{d}" pathLength="1" fill="none" stroke="{col}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
            f'{"".join(dots)}{"".join(labels)}{extra}</svg>')


def bar_chart(bars, w=480, h=240, fmt="{:,.0f}", ymax=None):
    """bars: [(label, value, color)]"""
    pad_l, pad_r, pad_t, pad_b = 8, 8, 34, 30
    hi = ymax or max(v for _, v, _ in bars) * 1.08
    n = len(bars)
    iw, ih = w - pad_l - pad_r, h - pad_t - pad_b
    slot = iw / n
    bw = min(96, slot * .56)
    out = []
    grid = "".join(f'<line x1="{pad_l}" x2="{w - pad_r}" y1="{pad_t + ih * k / 3:.1f}" y2="{pad_t + ih * k / 3:.1f}"/>' for k in range(4))
    for i, (lab, v, c) in enumerate(bars):
        bh = ih * v / hi
        x = pad_l + slot * i + (slot - bw) / 2
        y = pad_t + ih - bh
        out.append(f'<rect class="bar" style="transition-delay:{i * .12:.2f}s" x="{x:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{bh:.1f}" rx="8" fill="{COLORS[c]}"/>')
        out.append(f'<text class="val fade" x="{x + bw / 2:.1f}" y="{y - 10:.1f}" text-anchor="middle">{fmt.format(v)}</text>')
        out.append(f'<text x="{x + bw / 2:.1f}" y="{h - 8}" text-anchor="middle">{lab}</text>')
    return (f'<svg class="chart" viewBox="0 0 {w} {h}" role="img" aria-label="bar chart">'
            f'<g class="grid">{grid}</g>{"".join(out)}</svg>')


def hbar_chart(rows, w=480, fmt="{:,.1f}", row_h=36, label_w=130, vmax=None):
    """rows: [(label, value, color[, display])] horizontal bars."""
    rows = [tuple(x) + (None,) * (4 - len(x)) for x in rows]
    hi = vmax or max(x[1] for x in rows)
    h = len(rows) * row_h + 6
    bw_max = w - label_w - 70
    out = []
    for i, (lab, v, c, disp) in enumerate(rows):
        y = i * row_h + 4
        bw = max(4, bw_max * v / hi)
        out.append(f'<text x="0" y="{y + row_h / 2 + 1:.1f}" dominant-baseline="middle">{lab}</text>')
        out.append(f'<rect x="{label_w}" y="{y + 5}" width="{bw_max}" height="{row_h - 12}" rx="6" fill="{COLORS["muted"]}" opacity=".18"/>')
        out.append(f'<rect class="hbar" style="transition-delay:{i * .08:.2f}s" x="{label_w}" y="{y + 5}" width="{bw:.1f}" height="{row_h - 12}" rx="6" fill="{COLORS[c]}"/>')
        out.append(f'<text class="val fade" x="{label_w + bw + 10:.1f}" y="{y + row_h / 2 + 1:.1f}" dominant-baseline="middle" >{disp or fmt.format(v)}</text>')
    return f'<svg class="chart" viewBox="0 0 {w} {h}" role="img" aria-label="bar chart">{"".join(out)}</svg>'


def chart_block(title, svg, sub="", source="", legend=None):
    leg = ""
    if legend:
        leg = '<div class="chart-legend">' + "".join(f'<span><i style="background:{COLORS[c]}"></i>{t}</span>' for t, c in legend) + "</div>"
    src = f'<div class="chart-source">{source}</div>' if source else ""
    return (f'<div class="anim"><div class="chart-title"><span>{title}</span><small>{sub}</small></div>'
            f'{svg}{leg}{src}</div>')


def sparkline(vals, color="money2", w=62, h=26):
    lo, hi = min(vals), max(vals)
    n = len(vals)
    pts = " ".join(f"{w * i / (n - 1):.1f},{h - 3 - (h - 6) * (v - lo) / ((hi - lo) or 1):.1f}" for i, v in enumerate(vals))
    return (f'<svg viewBox="0 0 {w} {h}"><polyline points="{pts}" fill="none" stroke="{COLORS[color]}" '
            f'stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def browser(img, url, alt, r=""):
    return (f'<div class="browser"><div class="browser-bar"><div class="dots"><i></i><i></i><i></i></div>'
            f'<span>{esc(url)}</span></div>'
            f'<picture><source type="image/webp" srcset="{r}assets/img/work/{img}-720.webp 720w, {r}assets/img/work/{img}-1400.webp 1400w" sizes="(max-width: 960px) 100vw, 640px">'
            f'<img src="{r}assets/img/work/{img}.jpg" alt="{esc(alt)}" loading="lazy" width="1400" height="875"></picture></div>')


# ---------------------------------------------------------------- page shell
def head(title, desc, path, extra_ld=None, r=""):
    url = BASE + path
    ld = ""
    for block in (extra_ld or []):
        ld += f'<script type="application/ld+json">{json.dumps(block, ensure_ascii=False)}</script>\n'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="author" content="Mark Anthony Maina">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}assets/img/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0b0d18">
<link rel="icon" href="{r}assets/img/favicon.png">
<link rel="apple-touch-icon" href="{r}assets/img/mark-square-160.webp">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="{r}assets/css/site.css">
{ld}</head>
"""


def header(services, r="", active="", light=False):
    drop = "".join(
        f'<a href="{r}services/{s["slug"]}.html"><span class="ic">{icon(s["icon"])}</span>'
        f'<span><strong>{esc(s["name"])}</strong><small>{esc(s["menu"])}</small></span></a>' for s in services)
    msub = "".join(f'<a href="{r}services/{s["slug"]}.html">{esc(s["name"])}</a>' for s in services)

    def a(href, label, key):
        cls = ' class="active"' if key == active else ""
        return f'<a href="{href}"{cls}>{label}</a>'

    home = f"{r}index.html"
    return f"""<header class="header {'on-light' if light else 'on-dark'}">
  <div class="container header-inner">
    <a class="brand" href="{home}"><img src="{r}assets/img/mark-square-160.webp" alt="Mark Anthony Maina" width="38" height="38"><span>Mark Anthony Maina<small>RevOps &amp; Automation</small></span></a>
    <nav class="nav" aria-label="Main">
      <div class="nav-drop"><button type="button" aria-expanded="false">Services {icon("down")}</button><div class="drop">{drop}</div></div>
      {a(f"{r}work/index.html", "Work &amp; results", "work")}
      {a(f"{home}#how", "How I work", "how")}
      {a(f"{home}#about", "About", "about")}
    </nav>
    <a class="btn btn-primary btn-desk" href="#contact">Book a free call {icon("arrow")}</a>
    <button class="menu-btn" type="button" aria-label="Menu" aria-expanded="false"><span></span></button>
  </div>
</header>
<div class="mobile-nav">
  <a href="{home}">Home</a>
  <a href="{r}services/index.html">Services</a>
  <div class="sub">{msub}</div>
  <a href="{r}work/index.html">Work &amp; results</a>
  <a href="{home}#how">How I work</a>
  <a href="{home}#about">About</a>
  <a class="btn btn-primary" href="#contact">Book a free call {icon("arrow")}</a>
</div>
"""


def contact(r="", title=None, lead=None, topic_default=""):
    title = title or 'Let&rsquo;s talk about your <span class="serif">numbers.</span>'
    lead = lead or ("Tell me what you sell and where you think it&rsquo;s going wrong. I&rsquo;ll reply within one working day, "
                    "and the first call is free. If I&rsquo;m not the right person for it, I&rsquo;ll tell you who is.")
    topics = ["Not sure yet, help me find the leak", "RevOps / funnel audit", "Marketing automation", "AI sales agent",
              "SEO", "CRO / landing pages", "Website", "Analytics & tracking"]
    opts = "".join(f'<option{" selected" if t == topic_default else ""}>{t}</option>' for t in topics)
    return f"""<section class="section contact" id="contact">
  <div class="container contact-grid">
    <div class="reveal">
      <div class="kicker">Contact</div>
      <h2>{title}</h2>
      <p class="lead">{lead}</p>
      <div class="contact-ways">
        <a href="mailto:{EMAIL}"><span class="ic">{icon("mail")}</span><span><small>Email me directly</small><strong>{EMAIL}</strong></span></a>
        <a href="{WHATSAPP}" target="_blank" rel="noopener"><span class="ic">{icon("wa")}</span><span><small>WhatsApp (Ganiam Tech)</small><strong>+254 799 830 928</strong></span></a>
        <a href="{LINKEDIN}" target="_blank" rel="noopener"><span class="ic">{icon("in")}</span><span><small>LinkedIn</small><strong>Mark Anthony Maina</strong></span></a>
      </div>
    </div>
    <form class="form reveal d1" data-mailto="{EMAIL}">
      <h3>Get a free 20-minute call</h3>
      <p>No pitch deck. We look at your funnel together and I tell you the first thing I&rsquo;d fix.</p>
      <div class="row2">
        <div class="field"><label for="f-name">Your name</label><input id="f-name" name="name" required autocomplete="name"></div>
        <div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" required autocomplete="email"></div>
      </div>
      <div class="row2">
        <div class="field"><label for="f-company">Business / website</label><input id="f-company" name="company" autocomplete="organization"></div>
        <div class="field"><label for="f-topic">I need help with</label><select id="f-topic" name="topic">{opts}</select></div>
      </div>
      <div class="field"><label for="f-msg">What are you trying to fix?</label><textarea id="f-msg" name="message" required placeholder="e.g. We get enquiries on WhatsApp but most never buy, and I can't tell why."></textarea></div>
      <button class="btn btn-primary" type="submit">Send it over {icon("arrow")}</button>
      <p class="fine">Opens your email app with everything filled in. Nothing is stored on this site.</p>
    </form>
  </div>
</section>
"""


def footer(services, cases, r=""):
    sv = "".join(f'<li><a href="{r}services/{s["slug"]}.html">{esc(s["name"])}</a></li>' for s in services)
    cs = "".join(f'<li><a href="{r}work/{c["slug"]}.html">{esc(c["client"])}</a></li>' for c in cases)
    return f"""<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <a class="brand" href="{r}index.html"><img src="{r}assets/img/mark-square-160.webp" alt="" width="38" height="38"><span>Mark Anthony Maina<small>RevOps &amp; Automation</small></span></a>
        <p class="footer-big">A funnel you can&rsquo;t measure is a funnel you can&rsquo;t fix.</p>
        <p>Nairobi, Kenya. Working with teams in Africa, the UK and the US.<br>Client work runs through <a href="{GANIAM}" target="_blank" rel="noopener" style="color:#fff">Ganiam Tech</a>.</p>
      </div>
      <div><h4>Services</h4><ul>{sv}</ul></div>
      <div><h4>Case studies</h4><ul>{cs}<li><a href="{r}work/index.html">All work &rarr;</a></li></ul></div>
      <div><h4>Contact</h4><ul>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><a href="{WHATSAPP}" target="_blank" rel="noopener">WhatsApp</a></li>
        <li><a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a></li>
        <li><a href="{GITHUB}" target="_blank" rel="noopener">GitHub</a></li>
        <li><a href="{GANIAM}" target="_blank" rel="noopener">ganiamtech.com</a></li>
      </ul></div>
    </div>
    <div class="footer-bottom"><span>&copy; <span id="year">2026</span> Mark Anthony Maina &middot; Ganiam Tech</span><span>Built by hand. Every number on this site is from a real client account.</span></div>
  </div>
</footer>
<script src="{r}assets/js/site.js" defer></script>
</body>
</html>
"""


def other_services(services, current, r=""):
    links = "".join(
        f'<a href="{r}services/{s["slug"]}.html"><span class="ic">{icon(s["icon"])}</span>{esc(s["name"])}</a>'
        for s in services if s["slug"] != current)
    return f"""<section class="section-tight section-white">
  <div class="container">
    <div class="kicker">Also part of the same engine</div>
    <h3 style="margin-bottom:22px">Everything I do connects. Pick the piece you need, or let me find it.</h3>
    <div class="other-svcs">{links}</div>
  </div>
</section>
"""
