"""All copy and data. Every number here comes from a real client account
(RevOps app, Search Console, GA4, client databases) or Mark's own records.
Estimates are labelled as estimates on the page."""
from kit import (bar_chart, browser, chart_block, esc, hbar_chart, icon, line_chart)

# ================================================================ SERVICES
SERVICES = [
    {
        "slug": "revops", "icon": "funnel", "name": "RevOps & Funnel Fixing",
        "menu": "Find where the money leaks, then plug it",
        "card": "I map the whole path from first click to money in the bank, find the one stage losing you the most, and fix it. Every month.",
        "outcome": "More revenue from the same traffic",
        "title": "RevOps & Funnel Fixing | Mark Anthony Maina",
        "desc": "Revenue operations for service businesses and ecommerce: I map your funnel from first click to paid invoice, find the biggest leak and fix it every month.",
        "kicker": "RevOps · Funnel diagnostics",
        "h1": 'Find where your money is <span class="serif">leaking.</span> Then plug it.',
        "lead": "Most businesses don&rsquo;t need more traffic. They need to stop losing the people who already showed up. I map your funnel from first click to money in the bank, put a real number on every stage, and fix the one stage costing you the most. Then I prove it moved.",
        "for": ["Service businesses and online stores already making sales",
                "Leads coming in by website, WhatsApp, calls or DMs",
                "Nobody can say exactly where deals die"],
        "pains": ["You&rsquo;re paying for ads or SEO and can&rsquo;t say which one actually pays you back.",
                  "Enquiries land on WhatsApp and nobody knows what happened to half of them.",
                  "Your agency sends reports full of impressions. None of them mention revenue.",
                  "Five tools, five vendors, and every problem is somebody else&rsquo;s fault."],
        "pain_close": "Here&rsquo;s the thing: it&rsquo;s almost never the whole funnel that&rsquo;s broken. It&rsquo;s one stage. Find that one, and everything else gets cheaper.",
        "deliv": [("Funnel map", "Every step from stranger to paying customer, drawn for how you actually sell: forms, WhatsApp, calls, checkout."),
                  ("Baseline scorecard", "A real number on every stage, pulled from GA4, Search Console, your CRM and your actual sales record."),
                  ("The named bottleneck", "One stage, in writing, with the evidence and what it&rsquo;s costing you per month."),
                  ("Fixes, shipped", "Tracking, pages, automations, follow-up. Whatever the diagnosis calls for, built and live. Not a PDF of suggestions."),
                  ("One-page monthly report", "What changed, what moved, what it was worth, what&rsquo;s next. Readable in two minutes."),
                  ("Revenue truth", "Analytics conversions and banked money are different numbers. I reconcile them with your sales side.")],
        "steps": [("Week 1", "Access and instrumentation", "I get read access to everything (never passwords), install what&rsquo;s missing and agree what a lead and a sale actually mean."),
                  ("Week 2", "Baseline and diagnosis", "The full funnel with real numbers, and the one stage I&rsquo;m going after first."),
                  ("Weeks 3&ndash;4", "First fix live", "Built, shipped and tracked, so next month&rsquo;s numbers can prove it worked or tell us it didn&rsquo;t."),
                  ("Every month", "Pull, diagnose, fix, report", "Same loop, every client, every month. Max three fixes at a time, so nothing turns into busywork.")],
        "proof": ["kiboko", "debluc"],
        "tools": ["GA4", "Google Tag Manager", "Search Console", "Microsoft Clarity", "Looker Studio", "n8n", "WhatsApp Business", "HubSpot", "Odoo", "My own RevOps app (API sync)"],
        "pkgs": [("Funnel Audit", "One-off", "You want to know what&rsquo;s broken before you commit.",
                  ["Full funnel map and baseline", "The named bottleneck with evidence", "Top 3 fixes ranked by revenue impact", "Walkthrough call"], "About 2 weeks"),
                 ("Monthly RevOps", "Most popular", "You want someone to own the number, not just the tasks.",
                  ["Everything in the audit", "Fixes built and shipped every month", "Tracking and automations maintained", "One-page report + monthly call"], "3-month minimum"),
                 ("Fractional Head of Growth", "Embedded", "You want a senior operator inside your team.",
                  ["Owns the whole growth function", "Works with your team and vendors", "Weekly check-ins", "Board-ready reporting"], "6-month minimum")],
        "faq": [("What if our tracking is a mess, or was never set up?", "That&rsquo;s the normal case, not the exception. Month one is instrumentation: installing the measurement, defining conversions, filtering out spam and your own team&rsquo;s visits. I say this up front so it never feels like a month of nothing."),
                ("How soon will I see results?", "You&rsquo;ll see the diagnosis in two weeks, and the first fix goes live in month one. Revenue movement depends on the stage: follow-up fixes can move numbers in days, SEO fixes take weeks. I&rsquo;ll tell you which kind we&rsquo;re dealing with before we start."),
                ("Do you replace my marketing team or agency?", "No. I usually sit between them and sales, the part nobody owns. I can work alongside your people and hold everyone to the same scorecard."),
                ("What do you need from me?", "Access (role-based, never passwords), an honest look at your sales numbers, and 30 minutes a month. That&rsquo;s it.")],
    },
    {
        "slug": "marketing-automation", "icon": "bolt", "name": "Marketing Automation",
        "menu": "n8n, email and WhatsApp that run themselves",
        "card": "Follow-ups, quote chasing, cart recovery, CRM updates, team alerts. Built in n8n and real code so they keep running after I leave.",
        "outcome": "Hours back every week, zero leads forgotten",
        "title": "Marketing Automation (n8n, Email, WhatsApp) | Mark Anthony Maina",
        "desc": "n8n marketing automation engineer: speed-to-lead, nurture sequences, WhatsApp and email follow-up, CRM sync and alerts that keep running after handover.",
        "kicker": "Marketing automation · n8n",
        "h1": 'Follow-up that never forgets, never sleeps and never calls in <span class="serif">sick.</span>',
        "lead": "I build the automations that do the boring, money-critical work: replying to new leads, chasing quotes, recovering carts, updating the CRM and pinging your team when something needs a human. Built in n8n and real code, with error handling, so it keeps running long after I hand it over.",
        "for": ["Teams answering leads by hand, late, or not at all",
                "Anyone copy-pasting between forms, sheets, CRM and inbox",
                "Businesses that tried Zapier and outgrew it"],
        "pains": ["New leads wait hours for a reply, and by then they&rsquo;ve bought from someone else.",
                  "Follow-up only happens if somebody remembers. Usually nobody does.",
                  "Your CRM is always out of date because updating it is a manual job.",
                  "An automation someone built last year broke quietly and nobody noticed for weeks."],
        "pain_close": "Most leads don&rsquo;t die because they said no. They die because nobody followed up. That&rsquo;s a systems problem, and systems problems have systems fixes.",
        "deliv": [("Speed-to-lead responder", "Every new enquiry gets a useful reply in under a minute, day or night, on the channel they used."),
                  ("Nurture &amp; quote-chasing sequences", "Email and WhatsApp follow-ups that stop the moment someone replies or books."),
                  ("Cart &amp; chat recovery", "Abandoned carts and stalled WhatsApp chats picked back up automatically."),
                  ("CRM sync &amp; lead routing", "Leads land in the right pipeline stage with the right owner, deduplicated, with their source attached."),
                  ("Team alerts", "WhatsApp, Telegram or email pings when a hot lead arrives or something needs a human."),
                  ("Monitoring that fails safe", "Logs, retries, health checks, and AI steps that fail closed. Broken things get noticed, not ignored.")],
        "steps": [("Day 1&ndash;3", "Map the manual work", "We list every repetitive task between lead and sale, and what each one costs in time and lost deals."),
                  ("Week 1", "Design the flows", "Triggers, messages, branches and edge cases on one page, agreed before I build anything."),
                  ("Weeks 2&ndash;3", "Build, test, go live", "Built in n8n (self-hosted or cloud) plus code where needed, tested with real data, then switched on."),
                  ("After launch", "Hand over or keep running", "Documented so your team can own it, or I monitor and improve it on a small retainer.")],
        "proof": ["searv", "ai-sales-agent"],
        "tools": ["n8n", "Webhooks &amp; REST APIs", "Evolution API (WhatsApp)", "Gmail / SMTP", "HubSpot", "GoHighLevel", "Odoo", "Google Sheets", "PHP / MySQL", "Claude, OpenAI &amp; Gemini APIs", "Telegram"],
        "pkgs": [("Single workflow", "Fixed scope", "One painful manual process, automated properly.",
                  ["e.g. form &rarr; CRM &rarr; WhatsApp + email reply", "Error handling and logging", "Documentation", "30 days of fixes"], "About 1 week"),
                 ("Lead-to-sale system", "Most popular", "Every enquiry captured, answered and followed up.",
                  ["All enquiry channels into one pipeline", "Reply in under 60 seconds", "5-touch follow-up sequence", "Pipeline dashboard"], "About 2&ndash;3 weeks"),
                 ("Automation retainer", "Ongoing", "A steady stream of new automations, and someone watching the old ones.",
                  ["2&ndash;3 new automations a month", "Monitoring and fixes", "Monthly report", "Priority support"], "Monthly")],
        "faq": [("Why n8n instead of Zapier or Make?", "It handles complex logic, can be self-hosted (so your costs don&rsquo;t explode per task), and when it isn&rsquo;t enough I drop into real code. I&rsquo;ll still use Zapier or Make if that&rsquo;s what your team already runs."),
                ("Can you fix automations someone else built?", "Yes, and it&rsquo;s a common starting point. I audit what&rsquo;s running, document what each workflow actually does, kill the ones that duplicate or silently fail, and rebuild the fragile parts."),
                ("Who owns it when you&rsquo;re done?", "You do. Your accounts, your n8n instance, your data. You get documentation written for a non-developer."),
                ("What happens when something breaks?", "It tells someone. Everything I build logs its runs and alerts on failure, and AI steps fail closed: if the AI isn&rsquo;t sure, a human gets it.")],
    },
    {
        "slug": "ai-sales-agents", "icon": "bot", "name": "AI Sales Agents",
        "menu": "WhatsApp & web agents that sell 24/7",
        "card": "An AI salesperson on your WhatsApp and website. It answers from your real catalogue, qualifies, takes the order and hands over to a human when it should.",
        "outcome": "Replies in seconds, not hours",
        "title": "AI Sales Agents for WhatsApp & Web | Mark Anthony Maina",
        "desc": "AI WhatsApp and website sales agents that answer from your real catalogue, qualify leads, capture orders and escalate to a human. Built with Claude, n8n and your CRM.",
        "kicker": "AI agents · WhatsApp · Web",
        "h1": 'An AI salesperson that replies in <span class="serif">seconds.</span> Day or night.',
        "lead": "I build AI agents that live on your WhatsApp and website. They answer questions from your real catalogue and prices, qualify the lead, take the order or book the call, and hand the chat to a human the second they&rsquo;re out of their depth. In your voice, not a robot&rsquo;s.",
        "for": ["Businesses that sell through WhatsApp or chat",
                "Teams answering the same 20 questions all day",
                "Anyone losing late-night and weekend enquiries"],
        "pains": ["A customer messages at 11pm. You reply at 9am. They already bought elsewhere.",
                  "Your team spends half the day answering the same price and stock questions.",
                  "You tried a chatbot once. It was a menu of buttons and customers hated it.",
                  "You&rsquo;re scared an AI will make things up and embarrass you."],
        "pain_close": "Speed wins the sale. An agent that replies in seconds, from your real data, and knows when to call a human, is the cheapest salesperson you&rsquo;ll ever hire.",
        "deliv": [("The agent", "On WhatsApp (Business API or Evolution API) and/or your website, trained on your products, prices, policies and tone."),
                  ("Live catalogue sync", "Prices, stock, SKUs and images pulled from Odoo, WooCommerce, Shopify or a sheet, so answers are never out of date."),
                  ("Qualification &amp; tagging", "Every conversation tagged by sales stage and source, so you know which chats turn into money."),
                  ("Orders &amp; bookings", "Captures the order details or books straight into your calendar."),
                  ("Human handover", "Escalates to your team with the full context the moment it can&rsquo;t answer, and alerts an admin."),
                  ("Follow-up &amp; reporting", "Stalled chats get nudged on a schedule. You get a weekly view of conversations, orders and drop-offs.")],
        "steps": [("Week 1", "Knowledge and rules", "We gather your catalogue, FAQs and policies, and write down what the agent must never say or promise."),
                  ("Week 2", "Build and connect", "Agent, catalogue sync, CRM and alerts wired together, tested against real past conversations."),
                  ("Week 3", "Soft launch", "It drafts, your team approves. Once it&rsquo;s getting things right, it goes live on its own."),
                  ("Ongoing", "Tune and report", "I review conversations, fix weak answers and report on what the agent actually sold.")],
        "proof": ["ai-sales-agent", "searv"],
        "tools": ["Claude API", "OpenAI", "Google Gemini", "Evolution API", "WhatsApp Business", "n8n", "PHP / MySQL", "Odoo JSON-RPC", "WooCommerce", "Webhooks"],
        "pkgs": [("FAQ &amp; lead agent", "Starter", "Answers questions and captures leads for your team.",
                  ["Website or WhatsApp", "Trained on your FAQs and offers", "Lead capture to CRM or sheet", "Human handover"], "About 1&ndash;2 weeks"),
                 ("Sales agent", "Most popular", "Sells from your catalogue and captures orders.",
                  ["WhatsApp + website", "Live catalogue and stock sync", "Order capture and admin alerts", "Follow-ups and stage tagging"], "About 2&ndash;3 weeks"),
                 ("Agent + missed-lead recovery", "Full system", "Every enquiry, every channel, answered in under 60 seconds.",
                  ["All channels into one inbox", "AI first reply, 24/7", "5-touch follow-up", "Monthly tuning and report"], "Setup + monthly")],
        "faq": [("Will it make things up?", "It only answers from the knowledge and catalogue we give it, and it&rsquo;s built to fail closed: if it isn&rsquo;t sure, it hands over to a human instead of guessing."),
                ("Which languages can it handle?", "English and Swahili out of the box, and most major languages. It can match how your customers actually write, including mixed Kenyan English."),
                ("What does it cost to run?", "Usually a few dollars to a few tens of dollars a month in AI usage for an SME, plus WhatsApp costs. I&rsquo;ll estimate it from your real message volume before we start."),
                ("Will customers know it&rsquo;s AI?", "That&rsquo;s your call, and I recommend being upfront. Customers mostly care that they got a fast, correct answer.")],
    },
    {
        "slug": "seo", "icon": "search", "name": "SEO",
        "menu": "Technical, on-page and local search",
        "card": "Technical fixes, pages rewritten for buying searches, and local SEO. Judged on enquiries and sales, not on a rankings screenshot.",
        "outcome": "Found by people ready to buy",
        "title": "SEO Services: Technical, On-Page & Local | Mark Anthony Maina",
        "desc": "SEO that ends in sales: technical SEO audits and fixes, on-page optimisation for buying searches, local SEO and Google Business Profile, reported against leads and revenue.",
        "kicker": "SEO · Technical · Local",
        "h1": 'Get found on Google by people who are ready to <span class="serif">buy.</span>',
        "lead": "Not &ldquo;more traffic.&rdquo; The right traffic. I fix the technical problems that stop Google trusting your site, rewrite the pages that should be ranking, and go after the searches that actually turn into enquiries and sales. Then I report on those, not on vanity numbers.",
        "for": ["Businesses whose customers search before they buy",
                "Sites that look good but nobody finds",
                "Anyone burned by an SEO report that meant nothing"],
        "pains": ["You have a good website and almost nobody finds it.",
                  "You&rsquo;re stuck on page two for the searches that make money.",
                  "Traffic is up, but enquiries aren&rsquo;t. Wrong visitors.",
                  "Your site got hacked or spammed once, and Google never really forgave it."],
        "pain_close": "SEO usually fails for one of three reasons: Google can&rsquo;t read the site properly, the pages don&rsquo;t match what buyers search, or nobody off-site vouches for you. I find out which one it is first.",
        "deliv": [("Technical audit &amp; fixes", "Indexing, canonicals, redirects, sitemaps, speed, hacked-page cleanup. Fixed in the code, not listed in a PDF."),
                  ("Buying-intent keyword map", "The searches your customers use when they&rsquo;re ready to pay, mapped to the pages that should win them."),
                  ("On-page optimisation", "Titles, headings, copy, product descriptions and internal links, rewritten for people and Google."),
                  ("Local SEO", "Google Business Profile, reviews, directory listings and location pages for &ldquo;near me&rdquo; buyers."),
                  ("Product &amp; merchant SEO", "Google Merchant Center, product schema and shopping visibility for online stores."),
                  ("Reporting that means something", "Search Console and GA4 tied to leads and sales, not a screenshot of rankings.")],
        "steps": [("Week 1", "Audit", "Search Console, GA4, a full crawl and a look at your competitors. You get the problems ranked by what they cost you."),
                  ("Weeks 2&ndash;3", "Technical fixes", "The things that stop Google trusting the site get fixed first, because nothing else works until they are."),
                  ("Month 1&ndash;2", "Pages and content", "Money pages rewritten, internal links built, new pages only where there&rsquo;s real search demand."),
                  ("Month 2+", "Authority and local", "Business profile, reviews, listings and partner links, then monthly reporting against enquiries.")],
        "proof": ["debluc", "kiboko"],
        "tools": ["Google Search Console", "GA4", "Screaming Frog", "PageSpeed / Lighthouse", "Google Business Profile", "Merchant Center", "Schema.org", "WordPress", "Odoo Website", "Custom PHP"],
        "pkgs": [("SEO audit", "One-off", "You want the honest picture and a plan.",
                  ["Technical crawl and indexing review", "Keyword and competitor gaps", "Prioritised fix list with impact", "Walkthrough call"], "About 1 week"),
                 ("Fix &amp; optimise", "Most popular", "You want the problems actually fixed.",
                  ["Everything in the audit", "Technical fixes implemented", "Money pages rewritten", "Tracking for enquiries from search"], "About 3&ndash;4 weeks"),
                 ("Monthly SEO", "Ongoing", "You want steady growth you can see in enquiries.",
                  ["Content and on-page every month", "Local and off-page authority", "Technical monitoring", "Monthly report tied to leads"], "3-month minimum")],
        "faq": [("How long until SEO works?", "Technical fixes can show up in weeks. New rankings usually take 2&ndash;4 months. I&rsquo;ll show you leading indicators (impressions, positions, indexed pages) so you&rsquo;re never waiting blind."),
                ("Can you guarantee first place on Google?", "No, and be careful with anyone who does. What I can promise is a site Google can read, pages that match buyer searches, and honest numbers every month."),
                ("Do you write the content?", "Yes, for money pages and product descriptions. For long-form blog content I&rsquo;ll brief it tightly or write it, depending on what the plan needs."),
                ("Do you build backlinks?", "I build real ones: business profiles, directories, partners, suppliers, press. No link farms, because those end in penalties.")],
    },
    {
        "slug": "cro", "icon": "cursor", "name": "CRO & Landing Pages",
        "menu": "More sales from the traffic you already have",
        "card": "Where I started. Heatmaps, recordings and funnel data to find why people leave, then pages and tests that make them stay and buy.",
        "outcome": "+47% conversions on a real ad page",
        "title": "Conversion Rate Optimisation & Landing Pages | Mark Anthony Maina",
        "desc": "CRO and landing pages: I find why visitors leave using analytics, heatmaps and recordings, then build and A/B test pages that convert. +47% conversions on a Google Ads page.",
        "kicker": "CRO · Landing pages · A/B testing",
        "h1": 'More sales from the traffic you already <span class="serif">pay for.</span>',
        "lead": "This is where I started, and it&rsquo;s still the fastest lever on most funnels. I find out exactly why visitors leave (analytics, heatmaps, session recordings), fix the page, and A/B test until the number moves. Doubling conversions is usually cheaper than doubling traffic.",
        "for": ["Businesses running Google or Meta ads",
                "Sites with traffic but few enquiries or sales",
                "Teams redesigning based on opinions, not data"],
        "pains": ["Your ads get clicks, but hardly anyone enquires or buys.",
                  "Mobile visitors bounce in seconds and you don&rsquo;t know why.",
                  "The ad promises one thing and the landing page talks about something else.",
                  "Every redesign is somebody&rsquo;s opinion. Nobody measures if it worked."],
        "pain_close": "If 100 people land on your page and 2 enquire, getting that to 3 is a 50% jump in leads, without spending another shilling on ads.",
        "deliv": [("CRO audit", "Funnel data, heatmaps and recordings, turned into a ranked list of what&rsquo;s stopping people buying."),
                  ("Landing pages built for one job", "Fast, mobile-first pages with one offer, one action and proof in the right places."),
                  ("Message match", "The ad, the headline and the offer finally say the same thing."),
                  ("A/B testing programme", "Headlines, offers, forms and layouts tested properly, with enough traffic to trust the result."),
                  ("Form &amp; checkout fixes", "Fewer fields, clearer steps, WhatsApp and call options for people who&rsquo;d rather talk."),
                  ("Conversion tracking", "Every enquiry, call and WhatsApp click tracked, so we know which change did what.")],
        "steps": [("Week 1", "Watch real visitors", "Analytics and session recordings show where people hesitate, get confused and leave."),
                  ("Week 1&ndash;2", "Hypotheses", "A short list of changes, each with a reason and a number we expect to move."),
                  ("Weeks 2&ndash;3", "Build and launch", "New page or changes shipped with tracking, often as an A/B test against the old version."),
                  ("Ongoing", "Test, keep, repeat", "Winners stay, losers go, and we move to the next biggest leak.")],
        "proof": ["snapshot", "kiboko"],
        "tools": ["Microsoft Clarity", "Hotjar", "GA4", "Google Tag Manager", "Google Ads", "Meta Pixel", "Unbounce", "WordPress", "Figma", "Custom HTML/CSS/JS"],
        "pkgs": [("CRO audit", "One-off", "You want to know why your page isn&rsquo;t converting.",
                  ["Funnel and recording analysis", "Ranked list of fixes", "Mock-ups of the top changes", "Walkthrough call"], "About 1 week"),
                 ("Landing page build", "Most popular", "You need a page that turns ad clicks into leads.",
                  ["Copy, design and build", "Message-matched to your ads", "Tracking installed", "A/B test ready"], "About 1&ndash;2 weeks"),
                 ("Testing programme", "Ongoing", "You want conversion rates that keep going up.",
                  ["Monthly test roadmap", "Tests built and run", "Results you can trust", "Monthly report"], "Monthly")],
        "faq": [("How much traffic do I need for A/B testing?", "For proper tests, a few hundred conversions a month helps. With less, I use recordings and before/after comparisons instead, and I&rsquo;ll be honest about how sure we can be."),
                ("Do you design the pages too?", "Yes. Copy, design and build. Pretty matters, but every design choice has a job to do."),
                ("Can you work on my existing site?", "Yes. WordPress, Shopify, Odoo, Webflow or custom code. Often the fastest win is fixing the page you already have."),
                ("How long does a landing page take?", "Usually one to two weeks from brief to live, including tracking.")],
    },
    {
        "slug": "web-development", "icon": "code", "name": "Websites that Sell",
        "menu": "Fast sites with the sales machinery built in",
        "card": "Custom websites and stores with tracking, WhatsApp, lead capture, payments and SEO structure built in from day one.",
        "outcome": "A site that earns, not just looks good",
        "title": "Web Design & Development: Websites that Sell | Mark Anthony Maina",
        "desc": "Web design and development for businesses that want sales, not a brochure: fast, mobile-first websites and stores with tracking, WhatsApp, payments and SEO built in.",
        "kicker": "Web design · Development · Ecommerce",
        "h1": 'Websites that don&rsquo;t just look good. They <span class="serif">sell.</span>',
        "lead": "I design and build fast, mobile-first websites and online stores with the sales machinery already inside: lead capture, WhatsApp, booking, payments, tracking and SEO structure. Because a beautiful site that nobody measures is just an expensive brochure.",
        "for": ["New businesses that need to sell online fast",
                "Old sites that look dated and don&rsquo;t convert",
                "Stores that need payments, stock and WhatsApp to work together"],
        "pains": ["Your website looks fine but it doesn&rsquo;t bring in any business.",
                  "It&rsquo;s slow on phones, which is where most of your customers are.",
                  "Your last developer vanished and nobody can change anything.",
                  "You can&rsquo;t tell how many enquiries the site actually produces."],
        "pain_close": "I build every site as the first stage of a funnel, not as a design project. It launches already tracked, already ranking-ready and already connected to the way you sell.",
        "deliv": [("Design that fits your buyer", "Custom design built around what your customers need to see before they buy."),
                  ("The right platform", "WordPress, WooCommerce, Shopify, Odoo, Laravel or Next.js. Chosen for your business, not my habits."),
                  ("Fast and mobile-first", "Built for phones and slow networks first, because that&rsquo;s where most of your customers are."),
                  ("Conversion built in", "Clear offers, WhatsApp, forms, booking and payments including M-Pesa, Paystack and Pesapal."),
                  ("Tracking from day one", "GA4, Tag Manager, Search Console and Clarity installed and tested before launch."),
                  ("Handover you can live with", "Training, documentation and a site your team can actually edit.")],
        "steps": [("Week 1", "Plan", "What the site must achieve, who it&rsquo;s for, the pages, the offer and the platform."),
                  ("Weeks 1&ndash;2", "Design", "Homepage and key pages designed and signed off before build."),
                  ("Weeks 2&ndash;4", "Build", "Development, content, SEO structure, integrations and tracking."),
                  ("Launch +30 days", "Launch and tune", "Go live, watch real visitors, fix what the data shows.")],
        "proof": ["bil", "snapshot"],
        "tools": ["WordPress", "WooCommerce", "Shopify", "Odoo Website", "PHP / Laravel", "Next.js / React", "MySQL", "M-Pesa, Paystack, Pesapal", "GA4 &amp; GTM", "Figma"],
        "pkgs": [("Landing page", "Fast", "One offer, one page, one job.",
                  ["Copy, design and build", "Mobile-first and fast", "Tracking and WhatsApp", "Ad-ready"], "About 1&ndash;2 weeks"),
                 ("Business website", "Most popular", "A full site that brings in enquiries.",
                  ["5&ndash;10 pages, custom design", "SEO structure and local SEO setup", "Lead capture + WhatsApp + booking", "Tracking and training"], "About 3&ndash;5 weeks"),
                 ("Online store", "Ecommerce", "Sell online with payments and stock sorted.",
                  ["Store build and product setup", "Local and card payments", "Order notifications", "Merchant Center and tracking"], "About 4&ndash;6 weeks")],
        "faq": [("How long does a website take?", "Landing pages take 1&ndash;2 weeks. Full websites take 3&ndash;5 weeks. Online stores take 4&ndash;6 weeks, mostly depending on how fast product content arrives."),
                ("Which platform will you use?", "Whatever suits how you&rsquo;ll run it. WordPress if your team wants to edit easily, Shopify or WooCommerce for stores, Odoo if you want the site tied to your stock and accounts, custom code when nothing else fits."),
                ("Do you write the content?", "I write conversion copy for the key pages and help structure the rest. You bring the knowledge of your business, I turn it into pages that sell."),
                ("What happens after launch?", "Thirty days of fixes are included. After that you can run it yourself, or keep me on to grow it through SEO, CRO and automation.")],
    },
    {
        "slug": "analytics-tracking", "icon": "chart", "name": "Analytics & Tracking",
        "menu": "GA4, Tag Manager and dashboards you can trust",
        "card": "GA4, Tag Manager, Search Console and Clarity set up properly, the actions that matter tracked, and a dashboard you can read in two minutes.",
        "outcome": "Know which marketing makes money",
        "title": "GA4, Tag Manager & Marketing Dashboards | Mark Anthony Maina",
        "desc": "Analytics and tracking setup: GA4, Google Tag Manager, Search Console, Clarity, WhatsApp click and lead tracking, ads conversion imports, and dashboards you can trust.",
        "kicker": "Analytics · Tracking · Dashboards",
        "h1": 'Know which marketing makes you money. Stop <span class="serif">guessing.</span>',
        "lead": "I set up GA4, Tag Manager, Search Console and Clarity properly, track the actions that actually matter (calls, WhatsApp clicks, form fills, bookings, purchases), clean out the spam and your own team&rsquo;s visits, and build a dashboard you can read in two minutes.",
        "for": ["Businesses spending on marketing without clear answers",
                "Teams that don&rsquo;t trust their GA4 numbers",
                "Anyone selling through WhatsApp or phone calls"],
        "pains": ["GA4 is installed, but nobody trusts it or knows what to look at.",
                  "You can&rsquo;t tell which channel brings the customers who actually pay.",
                  "Most of your sales happen on WhatsApp, and analytics sees none of it.",
                  "Your numbers are full of bots and your own staff logging in."],
        "pain_close": "Bad data is worse than no data, because you make confident decisions on it. Fixing measurement is the least exciting thing I do, and the thing everything else depends on.",
        "deliv": [("Measurement plan", "What counts as a lead, a sale and a win for your business, written down and agreed."),
                  ("GA4 + Tag Manager setup or repair", "Clean property, proper events and key events, consent-aware, tested in debug mode."),
                  ("The actions that matter", "WhatsApp clicks, calls, forms, bookings and purchases tracked with their source."),
                  ("Ads conversion imports", "Google Ads and Meta get real conversion data, so their algorithms optimise for buyers."),
                  ("Clean data", "Internal traffic, bots and spam filtered out, so the numbers mean something."),
                  ("Dashboards", "Looker Studio or a custom dashboard with GA4, Search Console and Clarity synced by API.")],
        "steps": [("Days 1&ndash;3", "Audit", "What&rsquo;s installed, what&rsquo;s broken, what&rsquo;s missing, and what the data currently lies about."),
                  ("Week 1", "Plan", "The events, key events and reports your business actually needs. Nothing more."),
                  ("Week 2", "Implement and test", "Tags, events, filters and imports built and verified in debug and in real reports."),
                  ("Week 3", "Dashboard and handover", "One dashboard, a short walkthrough and a guide to what to look at each week.")],
        "proof": ["kiboko", "debluc"],
        "tools": ["GA4", "Google Tag Manager", "Search Console", "Microsoft Clarity", "Hotjar", "Looker Studio", "Google Ads", "Meta Pixel &amp; CAPI", "GA4 Data API", "BigQuery"],
        "pkgs": [("Tracking audit", "One-off", "You want to know if your data can be trusted.",
                  ["Full GA4 / GTM review", "What&rsquo;s broken and what&rsquo;s missing", "Fix list in priority order", "Walkthrough call"], "About 3&ndash;5 days"),
                 ("Tracking setup", "Most popular", "You want it done properly, once.",
                  ["Measurement plan", "GA4 + GTM + key events", "WhatsApp, call and form tracking", "Ads conversion imports"], "About 1&ndash;2 weeks"),
                 ("Dashboard + monthly insights", "Ongoing", "You want the numbers read for you.",
                  ["API-synced dashboard", "Monthly insights report", "Tracking maintained", "Alerts when something breaks"], "Monthly")],
        "faq": [("Can you track WhatsApp enquiries?", "Yes. I track the click to WhatsApp with its source, tag the pre-filled message so we know which page or ad it came from, and where possible connect chat outcomes back to the funnel."),
                ("We already have GA4. Do we need this?", "Maybe not. The audit tells you. Most setups I see are installed but untrusted: missing key events, polluted by internal visits, or double counting."),
                ("Do you handle cookie consent?", "Yes, consent-aware setups with Consent Mode where your market requires it."),
                ("Will I be able to read the dashboard myself?", "That&rsquo;s the whole point. One page, the few numbers that matter, and a note on what changed.")],
    },
]
SVC = {s["slug"]: s for s in SERVICES}


# ================================================================ CHARTS (real data)
def kiboko_impressions(w=480):
    return chart_block("Google impressions per month",
                       line_chart(w=w, points=[("Jan", 6384), ("Mar", 3833), ("Jun", 1350), ("Aug", 807)], color="red", h=210),
                       sub="-87% since January", source="Source: Google Search Console, clean months, 2026")


def kiboko_position(w=480):
    return chart_block("Average Google position (lower is better)",
                       line_chart(w=w, points=[("Jan", 20.8), ("Mar", 15.4), ("Jun", 25.2), ("Aug", 36.2)], color="amber", h=210,
                                  fmt="{:.1f}", invert=True, ymin=10, ymax=40),
                       sub="15.4 &rarr; 36.2", source="Source: Google Search Console")


def kiboko_weight(w=480):
    return chart_block("Homepage weight by file type (MB)",
                       hbar_chart(w=w, rows=[("JPG images", 1.6, "red"), ("PNG images", 1.5, "red"), ("CSS", .8, "amber"),
                                   ("SVG", .5, "amber"), ("JavaScript", .5, "amber")], label_w=110, vmax=1.8),
                       sub="5.0 MB total", source="Measured 22 Sep 2026 · 70 assets on one page")


def kiboko_enquiries(w=480):
    return chart_block("Where 68 real enquiries went (12 months)",
                       hbar_chart(w=w, rows=[("Marked &lsquo;new&rsquo;", 68, "red"), ("Quoted", 0, "muted"), ("Deposit", 0, "muted")],
                                  fmt="{:,.0f}", label_w=120, vmax=70),
                       sub="100% untouched in the system", source="Source: Kiboko booking database, Sep 2025 &ndash; Aug 2026")


def debluc_organic(w=480):
    return chart_block("Organic search sessions",
                       bar_chart(w=w, bars=[("July", 19, "muted"), ("August", 33, "money")], h=220, ymax=40),
                       sub="+74% in one month", source="Source: GA4 traffic acquisition, 2026")


def debluc_engagement(w=480):
    return chart_block("Engagement rate",
                       line_chart(w=w, points=[("Jul", 47), ("Aug", 55), ("Sep", 62)], color="money", h=210, fmt="{:.0f}%", ymin=40, ymax=66),
                       sub="47% &rarr; 62%", source="Source: GA4 · Sep = 1&ndash;12 Sep")


def debluc_direct(w=480):
    return chart_block("&lsquo;Direct&rsquo; traffic after removing staff logins",
                       bar_chart(w=w, bars=[("July", 71, "amber"), ("August", 32, "violet")], h=200, ymax=80),
                       sub="cleaner data, not lost visitors", source="Source: GA4 · internal /web/login sessions excluded")


def snapshot_lift(w=480):
    return chart_block("Conversions from the Google Ads landing page",
                       bar_chart(w=w, bars=[("Old page", 100, "muted"), ("New page", 147, "money")], h=220, fmt="{:,.0f}", ymax=160),
                       sub="indexed to 100 · +47%", source="A/B test against the previous page")


def searv_speed(w=480):
    return chart_block("Time from enquiry to a priced quote",
                       hbar_chart(w=w, rows=[("By hand (typical)", 1440, "muted", "~1 day"), ("SEARV", 1, "money", "&lt; 60 s")],
                                  label_w=130, vmax=1440),
                       sub="&lt; 60 seconds", source="Manual figure is a typical 1-day turnaround (estimate)")


def agent_speed(w=480):
    return chart_block("First reply to a WhatsApp enquiry",
                       hbar_chart(w=w, rows=[("Human, busy day", 180, "muted", "~3 hours"), ("AI agent", .2, "money2", "seconds")],
                                  label_w=130, vmax=180),
                       sub="hours &rarr; seconds", source="Human figure is a typical 3-hour wait (estimate)")


AGENT_DIAGRAM = """<svg class="diagram" viewBox="0 0 640 300" role="img" aria-label="AI sales agent architecture">
<path class="wire" d="M116 70 H176"/><path class="wire" d="M296 70 H346"/><path class="wire" d="M406 100 V150"/>
<path class="wire" d="M466 70 H516"/><path class="wire" d="M346 180 H296"/><path class="wire" d="M406 210 V240 H236 V210"/>
<path class="wire" d="M466 180 H516"/>
<rect class="box" x="10" y="40" width="106" height="60" rx="12"/><text x="63" y="66" text-anchor="middle">Customer</text><text class="sm" x="63" y="84" text-anchor="middle">WhatsApp</text>
<rect class="box" x="176" y="40" width="120" height="60" rx="12"/><text x="236" y="66" text-anchor="middle">Evolution API</text><text class="sm" x="236" y="84" text-anchor="middle">webhook</text>
<rect class="box hi" x="346" y="40" width="120" height="60" rx="12"/><text x="406" y="66" text-anchor="middle">Claude agent</text><text class="sm" x="406" y="84" text-anchor="middle">PHP 8 · MySQL</text>
<rect class="box ok" x="516" y="40" width="114" height="60" rx="12"/><text x="573" y="66" text-anchor="middle">Reply / order</text><text class="sm" x="573" y="84" text-anchor="middle">in seconds</text>
<rect class="box" x="346" y="150" width="120" height="60" rx="12"/><text x="406" y="176" text-anchor="middle">Catalogue</text><text class="sm" x="406" y="194" text-anchor="middle">Odoo JSON-RPC</text>
<rect class="box" x="176" y="150" width="120" height="60" rx="12"/><text x="236" y="176" text-anchor="middle">n8n scheduler</text><text class="sm" x="236" y="194" text-anchor="middle">follow-ups</text>
<rect class="box ok" x="516" y="150" width="114" height="60" rx="12"/><text x="573" y="176" text-anchor="middle">Escalate</text><text class="sm" x="573" y="194" text-anchor="middle">human + alert</text>
<text class="sm" x="320" y="268" text-anchor="middle">every chat tagged by sales stage and source · abandoned chats swept on a schedule</text>
</svg>"""

SEARV_DIAGRAM = """<svg class="diagram" viewBox="0 0 640 170" role="img" aria-label="SEARV quote flow">
<path class="wire" d="M110 60 H140"/><path class="wire" d="M250 60 H280"/><path class="wire" d="M390 60 H420"/><path class="wire" d="M530 60 H560"/>
<rect class="box" x="10" y="30" width="100" height="60" rx="12"/><text x="60" y="56" text-anchor="middle">Chat widget</text><text class="sm" x="60" y="74" text-anchor="middle">on the site</text>
<rect class="box" x="140" y="30" width="110" height="60" rx="12"/><text x="195" y="56" text-anchor="middle">5&#8211;10 questions</text><text class="sm" x="195" y="74" text-anchor="middle">niche intake</text>
<rect class="box hi" x="280" y="30" width="110" height="60" rx="12"/><text x="335" y="56" text-anchor="middle">AI pricing</text><text class="sm" x="335" y="74" text-anchor="middle">your price rules</text>
<rect class="box" x="420" y="30" width="110" height="60" rx="12"/><text x="475" y="56" text-anchor="middle">Branded PDF</text><text class="sm" x="475" y="74" text-anchor="middle">emailed</text>
<rect class="box ok" x="560" y="30" width="72" height="60" rx="12"/><text x="596" y="56" text-anchor="middle">&lt; 60s</text><text class="sm" x="596" y="74" text-anchor="middle">total</text>
<text class="sm" x="320" y="130" text-anchor="middle">then 5 follow-up emails over 14 days · stops the moment they reply or book</text>
</svg>"""


# ================================================================ CASE STUDIES
def _checks(items):
    return '<ul class="checks">' + "".join(f"<li>{icon('check-circle')}<span>{i}</span></li>" for i in items) + "</ul>"


def body_kiboko(r):
    return f"""
<h2>The situation</h2>
<p>Kiboko Tours &amp; Travel is a Kenyan safari operator selling private tour packages (enquiry, then quote, then deposit) and, soon, group safaris you can pay for online. They came to me with a simple question: <em>why aren&rsquo;t we getting enquiries like we used to?</em></p>
<p>Nobody had a clear answer, because nobody had looked at the whole path at once. So I pulled everything: 16 months of Search Console, a year of GA4, Clarity recordings, the site code, and their booking database.</p>

<h2>What the data said</h2>
<p>First, the headline. Kiboko hadn&rsquo;t slowly lost interest from customers. It had slowly disappeared from Google.</p>
<div class="fig-grid"><div class="figure">{kiboko_impressions(w=380)}</div><div class="figure">{kiboko_position(w=380)}</div></div>
<p>Digging into why turned up a chain of problems, each one making the next worse:</p>
{_checks(["<strong>Google had indexed the wrong copies of the pages.</strong> Broken canonical tags and empty titles meant Google picked the non-www, trailing-slash versions. <strong>0 of 44</strong> package URLs in the sitemap were known to Google.",
          "<strong>Search Console was under-reporting.</strong> Because Google preferred the non-www copies, their clicks landed in a property nobody had. GA4 showed about 150 organic sessions a month while Search Console showed about 20 clicks.",
          "<strong>The site had been hacked, twice.</strong> Search Console went dark from August to December 2025. Then in April 2026 gambling spam hijacked 3 pages and pulled in 8,125 junk clicks from Indonesian slot-site searches.",
          "<strong>The homepage weighed 5 MB.</strong> 70 files, with single &lsquo;thumbnail&rsquo; images over 500 KB. On a phone on safari-country data, that&rsquo;s a long wait."])}
<div class="figure">{kiboko_weight(w=620)}</div>
<p>And then the finding that mattered most for revenue. The site was actually working for the people who found it: real visitors engaged about half the time, and about 2% of them sent an enquiry. But after the enquiry, nothing was recorded.</p>
<div class="figure">{kiboko_enquiries(w=620)}</div>
<div class="callout"><strong>68 real enquiries in 12 months, and every single one still said &ldquo;new&rdquo;.</strong> No status, no quote amount, no outcome. The business couldn&rsquo;t tell which enquiries became safaris, so it couldn&rsquo;t tell which marketing was worth paying for.</div>

<h2>What I shipped</h2>
<p>The audit took days, not weeks. The first batch of fixes went live the same week, straight into the codebase:</p>
{_checks(["Canonicals, hreflang and social tags fixed site-wide, pointing at the one true www address",
          "Proper titles written for <strong>121 package pages</strong> and every blog post",
          "301 redirects for the path tricks the spam used, plus the index.php duplicates",
          "Sitemap rebuilt around real pages and robots.txt pointed at the right one",
          "SQL-injection holes closed on the pages that took IDs from the URL",
          "GA4 events live for <code>private_enquiry</code>, <code>custom_trip_enquiry</code>, <code>whatsapp_click</code> and <code>form_blocked</code>",
          "Price shown on package pages next to a pre-filled WhatsApp button"])}

<h2>What happens next</h2>
<p>Now every stage from Google to deposit is measured, so the next fixes are decided by numbers, not guesses. The first experiment is already running:</p>
<div class="callout"><strong>Hypothesis:</strong> showing &ldquo;From $X&rdquo; and a pre-filled WhatsApp button next to the quote button lifts private-package enquiries per package viewer from about 30% to 40%+, because international buyers compare on price and prefer to chat.</div>
<div class="callout honest"><strong>Honest status:</strong> Google takes weeks to re-crawl and trust a site again, so the recovery numbers aren&rsquo;t in yet. This page gets updated as they come in. What I can show you today is the diagnosis and the fix, and that&rsquo;s where most agencies never get to.</div>
"""


def body_debluc(r):
    return f"""
<h2>The situation</h2>
<p>Debluc Hair Essentials makes natural hair oils and conditioners in Nairobi. Like a lot of Kenyan brands, their customers browse the website and then order on WhatsApp. The site existed, but it wasn&rsquo;t pulling its weight: thin product pages, two versions of the domain competing with each other, old pages returning 404s, and no tracking that anyone trusted.</p>

<h2>What I did in month one</h2>
{_checks(["Keyword research matched to what Kenyans actually type when they want hair growth products",
          "On-page SEO across all <strong>30 pages</strong>: titles, headings, structure",
          "The whole product catalogue rewritten so each product answers a buyer&rsquo;s questions",
          "Internal linking so Google (and people) can move from guides to products",
          "www and non-www merged into one address",
          "Return policy written and published (trust matters for first-time buyers)",
          "Search Console, GA4 and Clarity installed; products submitted to Google Merchant Center"])}

<h2>The result</h2>
<div class="fig-grid"><div class="figure">{debluc_organic(w=380)}</div><div class="figure">{debluc_engagement(w=380)}</div></div>
<p>Organic search sessions went from <strong>19 to 33 in a month (+74%)</strong>, and held into September. More importantly, the people arriving were the right people: the engagement rate climbed from 47% to 55% to 62%. Average Google position improved from 12.7 to 11.5.</p>
<p>I also cleaned the data. July&rsquo;s &ldquo;direct&rdquo; traffic was inflated by the team&rsquo;s own admin logins. Once those were excluded, direct traffic dropped from 71 to 32. That&rsquo;s not a loss, that&rsquo;s the truth, and every decision after it is better for it.</p>
<div class="figure">{debluc_direct(w=620)}</div>

<h2>What the numbers say to do next</h2>
<p>The pages are now good. The problem is that nobody off-site vouches for them: zero referring domains, no Google Business Profile, no reviews. That&rsquo;s why strong pages sit at positions 12&ndash;19 instead of 3&ndash;5. So the next phase is off-page, not more on-page tinkering.</p>
<table class="data-table"><thead><tr><th>Buying search in striking distance</th><th class="num">Position</th></tr></thead><tbody>
<tr><td>rapid oil</td><td class="num">6</td></tr><tr><td>hair essentials</td><td class="num">8</td></tr>
<tr><td>rosemary and mint shampoo</td><td class="num">9</td></tr><tr><td>kids hair growth oil</td><td class="num">10</td></tr>
<tr><td>best hair growth oil in kenya</td><td class="num">19</td></tr></tbody></table>
<div class="callout"><strong>The money query</strong> is &ldquo;best hair growth oil in kenya.&rdquo; It already has impressions at position 19. Getting it onto page one is worth more than any new blog post.</div>
<div class="callout honest"><strong>Honest status:</strong> WhatsApp orders aren&rsquo;t tracked yet, so I can&rsquo;t show you revenue from this work. That&rsquo;s the next fix: a tracked WhatsApp click event, then chats and orders counted so the whole funnel is visible.</div>
"""


def body_snapshot(r):
    return f"""
<h2>The situation</h2>
<p>Snapshot Team Building Consultants is one of Kenya&rsquo;s established corporate team building companies. They run Google Ads to reach HR and admin teams planning events. The ads were getting clicks. The landing page wasn&rsquo;t turning enough of them into enquiries.</p>
<p>The problem was simple once you looked: the ad made one promise and the page talked about something else. People clicked expecting one thing, didn&rsquo;t see it, and left.</p>

<h2>What I did</h2>
{_checks(["Built a new landing page matched to the Google Ads campaigns, so the ad, the headline and the offer finally said the same thing",
          "Set up Google Tag Manager with full event tracking, so every meaningful action is measured and attributed",
          "Ran an A/B test of the new page against the old one"])}

<h2>The result</h2>
<div class="figure">{snapshot_lift(w=620)}</div>
<p>The new page beat the old one by <strong>47% on conversions</strong>, from the same ad traffic. Same budget, nearly half as many leads again.</p>
<blockquote class="big-quote">&ldquo;Mark is a skilled developer who will do everything possible to deliver the project on time, and I really appreciate that.&rdquo;<cite>Kalala Kamunzyu, Managing Director, Snapshot</cite></blockquote>

<h2>Since then</h2>
<p>That test turned into a relationship that&rsquo;s run since 2022: ongoing Google Ads management, continuous CRO, internal web tools that simplified how their team handles event enquiries, and work for their sister brand, Snapshot Tours and Safaris. Today Snapshot is set up in my RevOps system with a lead-generation funnel tracked from search to booked event.</p>
"""


def body_agent(r):
    return f"""
<h2>The situation</h2>
<p>A Nairobi ecommerce retailer sells mostly through WhatsApp. Customers find a product on the website, tap WhatsApp, and ask the same questions: is it in stock, how much, how fast can you deliver? Answering all of that by hand meant slow replies at busy times and none overnight.</p>

<h2>What I built</h2>
<p>An AI sales agent that answers the store&rsquo;s WhatsApp in natural Kenyan English, from the live catalogue, and hands over to a human when it should.</p>
<div class="figure dark">{AGENT_DIAGRAM}</div>
{_checks(["Replies in seconds in the business&rsquo;s own tone, 24/7",
          "Product catalogue synced both ways with <strong>Odoo</strong> over JSON-RPC: prices, stock, SKUs and images always current",
          "Every customer categorised by sales stage, so the team sees who is browsing and who is ready to pay",
          "Captures orders and alerts admins instantly",
          "Escalates anything it can&rsquo;t answer to a human, with the full conversation",
          "n8n runs scheduled follow-ups and marks abandoned chats for a nudge",
          "Ships with a self-diagnosis health page so problems get caught, not discovered by customers"])}

<h2>The result</h2>
<div class="figure">{agent_speed(w=620)}</div>
<p>First response went from <strong>hours to seconds</strong>, and routine questions (price, stock, delivery) are handled without anyone picking up a phone. The team spends its time on the conversations that need a person.</p>

<h2>Measuring what it sells</h2>
<p>Because every WhatsApp conversation is exportable, this is one of the few funnels where the chat stage is fully measurable. I&rsquo;ve set it up as a tracked funnel: sessions, WhatsApp clicks, agent conversations, qualified, order intent, paid. Each conversation carries its source, so we can see which pages and campaigns produce paying customers, not just chats.</p>
<div class="callout"><strong>Stack:</strong> PHP 8.1 · MySQL · Evolution API · Claude · n8n · Odoo JSON-RPC.</div>
"""


def body_searv(r):
    return f"""
<h2>The problem</h2>
<p>Service businesses lose deals in the gap between &ldquo;how much?&rdquo; and the quote. A cleaner, roofer or coach gets an enquiry, means to price it tonight, and sends it tomorrow or the day after. By then the customer has booked whoever answered first.</p>

<h2>What I built</h2>
<p>SEARV is a Ganiam Tech product: an AI lead-capture and quoting engine. A chat widget on the site asks 5 to 10 questions specific to the business, prices the job using the owner&rsquo;s own rules, and emails a branded PDF quote. In under a minute. Then it follows up.</p>
<div class="figure dark">{SEARV_DIAGRAM}</div>
<div class="figure">{searv_speed(w=620)}</div>
{_checks(["Personalised, branded PDF quote generated and emailed in <strong>under 60 seconds</strong>",
          "A 5-email, 14-day follow-up sequence that stops the moment someone replies or books",
          "Niche templates ready for residential cleaning, roofing, painting and HVAC. A new niche is a settings change, not a rebuild",
          "Multi-client: one hub, a separate instance and database per client, one-click access to each",
          "Full SOP library, install and handover guides, GTM and Google Ads walkthroughs, and a cron heartbeat that checks every instance"])}

<h2>In the wild</h2>
<p>The first live client is <strong>Body &amp; Its Language</strong>, a perimenopause coaching programme. Their new website sends visitors through a 60-second &ldquo;Body Check&rdquo; quiz into a free call, and on to a $495 programme, with SEARV handling the intake and follow-up behind it.</p>
<div class="figure">{browser("bil", "bodyanditslanguage.com", "Body & Its Language website", r)}</div>
"""


def body_bil(r):
    return body_searv(r)


CASES = [
    {"slug": "kiboko", "client": "Kiboko Tours & Travel", "industry": "Safari operator", "where": "Kenya", "year": "2026",
     "services": ["RevOps audit", "Technical SEO", "Tracking", "CRO"], "url": "kibokotoursandtravel.com", "shot": "kiboko",
     "card_title": "The safari company Google forgot",
     "summary": "Visibility had dropped 87% and nobody knew why. One end-to-end audit found the reasons, from broken canonicals to a hacked site to 68 enquiries nobody followed up. The first fixes went live the same week.",
     "metrics": [("-87%", "Google visibility since January (diagnosed)", "down"), ("0/44", "package pages Google knew about", "down"), ("121", "package pages fixed in batch one", "up")],
     "chart": kiboko_impressions,
     "h1": 'Visibility down 87%. Nobody knew why. <span class="serif">Now we do.</span>',
     "lead": "A full-funnel audit of a Kenyan safari operator: 16 months of search data, a year of analytics, the codebase and the booking database. It found why Google stopped showing the site, why enquiries were going nowhere, and what to fix first. Then I fixed it.",
     "stats": [("87%", "drop in Google impressions, Jan to Aug", "down"), ("68", "real enquiries in 12 months, all marked &lsquo;new&rsquo;", ""),
               ("5 MB", "homepage weight on a phone", "down"), ("&lt; 1 wk", "from audit to first fixes live", "up")],
     "body": body_kiboko},
    {"slug": "debluc", "client": "Debluc Hair Essentials", "industry": "Hair care ecommerce", "where": "Nairobi", "year": "2026",
     "services": ["SEO", "Content", "Tracking", "RevOps"], "url": "debluchairessentials.co.ke", "shot": "debluc",
     "card_title": "+74% organic traffic in one month",
     "summary": "A Nairobi hair care brand whose customers order on WhatsApp. I rebuilt all 30 pages for search, rewrote the catalogue, cleaned the data and set up tracking. Organic sessions jumped 74% in a month and the right visitors stayed.",
     "metrics": [("+74%", "organic search sessions, Jul to Aug", "up"), ("62%", "engagement rate, up from 47%", "up"), ("30", "pages rebuilt for search", "")],
     "chart": debluc_organic,
     "h1": 'Organic traffic up <span class="serif">74%</span> in one month.',
     "lead": "Debluc makes natural hair care products in Nairobi and sells mostly through WhatsApp. In month one I rebuilt the site for search, rewrote the catalogue, cleaned up the data and installed proper tracking. Here&rsquo;s what moved, and what the numbers say to do next.",
     "stats": [("+74%", "organic search sessions in one month", "up"), ("47&rarr;62%", "engagement rate, Jul to Sep", "up"),
               ("30", "pages optimised, plus the full catalogue", ""), ("12.7&rarr;11.5", "average Google position", "up")],
     "body": body_debluc},
    {"slug": "snapshot", "client": "Snapshot Team Building", "industry": "Corporate events", "where": "Kenya", "year": "2022&ndash;now",
     "services": ["CRO", "Landing pages", "Google Ads", "GTM tracking"], "url": "snapshotteambuilding.com", "shot": "snapshot",
     "card_title": "+47% conversions from the same ad spend",
     "summary": "Google Ads were getting clicks but the landing page didn&rsquo;t match the ad. A rebuilt, message-matched page, A/B tested against the old one, lifted conversions by 47%. The relationship has run since 2022.",
     "metrics": [("+47%", "conversions vs the old page", "up"), ("A/B", "tested, not guessed", ""), ("4 yrs", "working together", "")],
     "chart": snapshot_lift,
     "h1": '<span class="serif">+47%</span> conversions from the same ad spend.',
     "lead": "Snapshot Team Building runs Google Ads to reach companies planning team events. The ads got clicks, the landing page didn&rsquo;t convert them. A message-matched page, tested against the old one, fixed that.",
     "stats": [("+47%", "conversions from the Google Ads page", "up"), ("Same", "ad budget, no extra spend", ""),
               ("Full", "event tracking in Tag Manager", ""), ("Since 2022", "ongoing CRO, Ads and tools", "")],
     "body": body_snapshot},
    {"slug": "ai-sales-agent", "client": "AI WhatsApp Sales Agent", "industry": "Ecommerce retailer", "where": "Nairobi", "year": "2026",
     "services": ["AI agent", "WhatsApp", "Odoo integration", "n8n"], "url": "", "shot": "",
     "card_title": "An AI salesperson on WhatsApp, synced to the stock system",
     "summary": "A Nairobi retailer that sells through WhatsApp. I built an AI agent that answers from the live Odoo catalogue, tags every customer by sales stage, captures orders and hands over to a human when it should.",
     "metrics": [("Seconds", "first reply, down from hours", "up"), ("24/7", "including nights and weekends", ""), ("Live", "prices and stock from Odoo", "")],
     "chart": agent_speed,
     "h1": 'An AI salesperson that replies in <span class="serif">seconds,</span> from the real stock system.',
     "lead": "A Nairobi ecommerce retailer sells mostly through WhatsApp. I built an AI sales agent that answers customers in natural Kenyan English from the live Odoo catalogue, captures orders, and knows when to call a human.",
     "stats": [("Hours&rarr;secs", "first response time", "up"), ("24/7", "coverage without extra staff", ""),
               ("2-way", "catalogue sync with Odoo", ""), ("6", "funnel stages tracked, click to paid", "")],
     "body": body_agent},
    {"slug": "searv", "client": "SEARV AI Quote Engine", "industry": "Ganiam Tech product", "where": "US / UK / Kenya", "year": "2026",
     "services": ["AI", "Automation", "Lifecycle email", "Product"], "url": "", "shot": "bil",
     "card_title": "From enquiry to branded quote in under 60 seconds",
     "summary": "A productised AI intake and quoting engine for service businesses. It asks the right questions, prices the job, emails a branded PDF quote in under a minute and follows up for 14 days. Live for Body & Its Language.",
     "metrics": [("&lt; 60s", "enquiry to priced quote", "up"), ("14 days", "of automatic follow-up", ""), ("4", "niches ready to deploy", "")],
     "chart": searv_speed,
     "h1": 'From enquiry to branded quote in under <span class="serif">60 seconds.</span>',
     "lead": "SEARV is an AI lead-capture and quoting engine I built for service businesses. It closes the gap where most deals die: the hours or days between &ldquo;how much?&rdquo; and the quote.",
     "stats": [("&lt; 60s", "from enquiry to priced PDF quote", "up"), ("5 emails", "over 14 days, stops on reply", ""),
               ("4", "niches ready: cleaning, roofing, painting, HVAC", ""), ("1 hub", "many clients, one database each", "")],
     "body": body_searv},
]
CASE = {c["slug"]: c for c in CASES}

# Extra proof cards used on service pages that aren't full case studies
EXTRA_PROOF = {
    "bil": {"slug": "searv", "client": "Body & Its Language", "industry": "Health coaching", "where": "Kenya / online", "year": "2026",
            "card_title": "Quiz &rarr; call &rarr; $495 programme funnel",
            "summary": "A new website for a perimenopause coaching programme, built as a funnel: a 60-second Body Check quiz into a free call, then the programme. SEARV runs the intake and follow-up behind it.",
            "visual": lambda r: browser("bil", "bodyanditslanguage.com", "Body & Its Language website", r)},
}


# ================================================================ SYSTEMS
SYSTEMS = [
    ("RevOps Command Centre", "My own product · live", "One app for every growth client: funnels, findings, tasks, reports. Syncs GA4, Search Console and Clarity by API every night, computes each funnel and flags the stage leaking the most money.",
     "<b>GA4 + GSC + Clarity APIs</b> &rarr; nightly sync &rarr; funnel engine &rarr; <b>biggest leak</b> &rarr; task &rarr; report", ["PHP 8", "MySQL", "Google APIs", "n8n"], "6", "clients run on it"),
    ("SEARV AI Quote Engine", "Lead capture &rarr; quote &rarr; follow-up", "Conversational intake, AI pricing and a branded PDF quote in under a minute, then a 14-day follow-up sequence. Multi-client hub with one database per client.",
     "widget &rarr; <b>5&ndash;10 questions</b> &rarr; AI price &rarr; PDF &rarr; email &rarr; <b>14-day sequence</b> <span class=\"ok\">&#10003;</span>", ["AI", "PDF generation", "Email", "Cron"], "&lt; 60s", "enquiry to quote"),
    ("AI WhatsApp Sales Agent", "Conversational commerce", "Answers customers from the live Odoo catalogue, tags every chat by sales stage, captures orders, alerts admins and escalates to a human when it can&rsquo;t help.",
     "WhatsApp &rarr; <b>Evolution API</b> &rarr; webhook &rarr; <b>Claude</b> &rarr; reply / order / escalate", ["Claude API", "Evolution API", "Odoo", "n8n"], "Seconds", "first reply, was hours"),
    ("Client Acquisition CRM", "Outbound RevOps platform", "Full lead-to-close CRM built from scratch: duplicate detection, pipeline stages with history, tasks, templates, suppression list, and an API so n8n can run campaigns from outside.",
     "n8n &rarr; <b>segments/preview</b> &rarr; campaigns/queue &rarr; send &rarr; <b>inbound replies</b> &rarr; stage-apply", ["CRM design", "REST API", "n8n", "Email ops"], "Minutes", "lead response, was hours"),
    ("Outbound Deliverability Engine", "Cold email that lands", "AI-written emails, warm-up ramp, human-like send gaps, per-provider limits, list hygiene at import, bounce suppression and auto-pause. Built for the inbox, not for volume.",
     "import &rarr; <b>MX + hygiene checks</b> &rarr; AI draft &rarr; throttled send &rarr; <b>bounce suppression</b>", ["PHP", "MySQL", "AI", "Deliverability"], "10h &rarr; &lt;1h", "admin per week"),
    ("Multi-model AI QA Pipeline", "Seven chained n8n workflows", "Unzips, converts and hosts documents on S3, then Claude and Gemini review each one against the brief and write a scored report to MySQL. AI failures are held for a human.",
     "archive &rarr; <b>DOCX &rarr; PDF/image</b> &rarr; S3 &rarr; <b>Claude + Gemini</b> &rarr; score &rarr; MySQL", ["n8n", "AWS S3", "Claude", "Gemini"], "~80%", "less review time (est.)"),
    ("Booya Booking Platform", "Bookings, deposits, reminders", "Booking system for beauty and wellness businesses: real availability with staff calendars, deposits via Paystack, self-service reschedule, and WhatsApp + email reminders that cut no-shows.",
     "public link &rarr; <b>availability engine</b> &rarr; Paystack deposit &rarr; <b>24h / 2h reminders</b>", ["Node.js", "Express", "Paystack", "WhatsApp"], "24h + 2h", "automatic reminders"),
    ("Paid Media Dashboard", "Marketing ops reporting", "Google Ads and Meta Ads pulled straight from the APIs across accounts, so spend, conversions and cost per result sit in one view instead of three tabs and a spreadsheet.",
     "<b>Google Ads API + Meta API</b> &rarr; Next.js dashboard &rarr; spend / CPA / ROAS", ["Google Ads API", "Meta API", "Next.js"], "1 view", "instead of 3 platforms"),
]

SITES = [
    ("bil", "Body & Its Language", "bodyanditslanguage.com", "Coaching funnel: quiz &rarr; call &rarr; programme"),
    ("kundi", "Kundi Home", "kundihome.com", "German kitchens, Bradford UK · lead-gen site"),
    ("kiboko", "Kiboko Tours &amp; Travel", "kibokotoursandtravel.com", "Safari packages, quotes and group bookings"),
    ("debluc", "Debluc Hair Essentials", "debluchairessentials.co.ke", "Ecommerce with WhatsApp ordering"),
    ("snapshot", "Snapshot Team Building", "snapshotteambuilding.com", "Corporate events lead generation"),
    ("ganiam", "Ganiam Tech", "ganiamtech.com", "My agency&rsquo;s own site"),
]

CLIENTS = ["Snapshot Team Building", "Kiboko Tours &amp; Travel", "Debluc Hair Essentials", "Kundi Home (UK)",
           "Body &amp; Its Language", "Snapshot Tours &amp; Safaris", "Jacich Safaris", "Sierra Restaurants", "SARL",
           "Wafftech", "JW Law Advocates", "Mommy&amp;Me"]

QUOTES = [
    ("Mark is a skilled developer who will do everything possible to deliver the project on time, and I really appreciate that.", "Kalala Kamunzyu", "Managing Director, Snapshot"),
    ("Loved working with Mark. He&rsquo;s an awesome developer with great attention to detail, and he has a great eye for design.", "Eunice", "Marketing Manager, Jacich Safaris"),
]
