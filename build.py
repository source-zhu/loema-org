#!/usr/bin/env python3
# loema.org — the shape draft. Plain, accessible, zero external requests.
import os, html

ROOT = os.path.dirname(os.path.abspath(__file__))

CSS = """
:root{--paper:#f6f2e8;--ink:#211f1a;--dim:#5f594c;--line:#d8d1c0;--accent:#59503c;--soft:#fbf8f1;}
*{margin:0;padding:0;box-sizing:border-box;}
html{-webkit-text-size-adjust:100%;}
body{font-family:Georgia,'Times New Roman',serif;background:var(--paper);color:var(--ink);
  line-height:1.6;min-height:100vh;display:flex;flex-direction:column;}
.skip{position:absolute;left:-9999px;top:0;background:var(--ink);color:var(--paper);padding:10px 16px;z-index:10;}
.skip:focus{left:12px;top:12px;}
header.site{border-bottom:1px solid var(--line);}
.shell{max-width:680px;margin:0 auto;padding:0 22px;width:100%;}
header.site .shell{display:flex;justify-content:space-between;align-items:baseline;flex-wrap:wrap;gap:6px;padding-top:22px;padding-bottom:18px;}
/* the domain toggle: loema stays; the half you're in drops down and swaps */
.domain{position:relative;}
.domain summary{list-style:none;cursor:pointer;font-size:1.1rem;letter-spacing:.02em;color:var(--ink);
  display:inline-flex;align-items:baseline;gap:4px;}
.domain summary::-webkit-details-marker{display:none;}
.domain summary .org{color:var(--dim);}
.domain summary .caret{font-size:.6rem;color:var(--dim);transform:translateY(-2px);}
.domain[open] summary .caret{transform:translateY(-2px) rotate(180deg);}
.domain .menu{position:absolute;top:calc(100% + 8px);left:0;z-index:20;min-width:200px;
  background:var(--soft);border:1px solid var(--line);border-radius:10px;padding:8px;
  box-shadow:0 6px 24px rgba(33,31,26,.08);}
.domain .menu a{display:block;padding:9px 12px;border-radius:6px;text-decoration:none;color:var(--ink);}
.domain .menu a:hover{background:var(--paper);}
.domain .menu .which{display:block;font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;
  font-size:.68rem;letter-spacing:.1em;text-transform:uppercase;color:var(--dim);margin-top:2px;}
.domain .menu a[aria-current] .which{color:var(--accent);}
nav.site{font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;font-size:.82rem;letter-spacing:.04em;}
nav.site a{color:var(--dim);text-decoration:none;margin-left:14px;}
nav.site a:hover,nav.site a[aria-current]{color:var(--ink);text-decoration:underline;text-underline-offset:3px;}
main{flex:1;padding:46px 0 70px;}
h1{font-size:1.9rem;font-weight:400;line-height:1.25;letter-spacing:-.01em;margin-bottom:18px;}
h2{font-size:1.25rem;font-weight:400;margin:34px 0 10px;}
h3{font-size:1.02rem;margin:22px 0 8px;}
p{margin-bottom:14px;}
ul,ol{margin:0 0 14px 22px;}
li{margin-bottom:8px;}
a{color:var(--accent);text-underline-offset:2px;}
a:focus-visible,button:focus-visible{outline:3px solid var(--accent);outline-offset:3px;border-radius:2px;}
.lede{font-size:1.12rem;color:var(--dim);margin-bottom:26px;}
.recap{background:var(--soft);border:1px solid var(--line);border-left:3px solid var(--accent);
  border-radius:8px;padding:14px 16px;margin:10px 0 18px;font-size:.95rem;}
.recap b{font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;font-size:.72rem;letter-spacing:.14em;
  text-transform:uppercase;color:var(--dim);display:block;margin-bottom:6px;font-weight:600;}
.quiet{color:var(--dim);font-size:.92rem;}
.ledger{list-style:none;margin-left:0;}
.ledger li{border-top:1px solid var(--line);padding:14px 2px;margin:0;}
.ledger b{display:block;margin-bottom:4px;font-weight:600;}
.era{border-left:2px solid var(--line);padding:4px 0 4px 18px;margin-bottom:18px;}
.era .when{font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;font-size:.72rem;letter-spacing:.14em;
  text-transform:uppercase;color:var(--accent);}
footer.site{border-top:1px solid var(--line);padding:26px 0 40px;font-size:.85rem;color:var(--dim);}
footer.site .shell{display:flex;flex-direction:column;gap:8px;}
footer.site a{color:var(--dim);}
footer.site nav{display:flex;flex-wrap:wrap;gap:4px 16px;font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;font-size:.78rem;}
code,pre{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.88em;background:var(--soft);
  border:1px solid var(--line);border-radius:4px;}
code{padding:1px 5px;}
pre{padding:14px;overflow-x:auto;margin-bottom:14px;}
@media (prefers-reduced-motion:reduce){*{scroll-behavior:auto;}}
"""

NAV = [("/", "Home"), ("/constitution/", "The format"), ("/refusals/", "Refusals"),
       ("/roadmap/", "Roadmap"), ("/funds/", "Funds")]

def page(path, title, desc, body, current):
    AC = ' aria-current="page"'
    navlinks = "".join(
        f'<a href="{h}"{AC if h == current else ""}>{t}</a>'
        for h, t in NAV)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<style>{CSS}</style>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site"><div class="shell">
  <details class="domain">
    <summary aria-label="loema.org — switch between loema.com and loema.org">loema<span class="org">.org</span> <span class="caret" aria-hidden="true">&#9662;</span></summary>
    <div class="menu">
      <a href="https://www.loema.com">loema<span class="org">.com</span>
        <span class="which">where you begin — the litmus</span></a>
      <a href="/" aria-current="true">loema<span class="org">.org</span>
        <span class="which">where you are — the commons</span></a>
    </div>
  </details>
  <nav class="site" aria-label="Site">{navlinks}</nav>
</div></header>
<main id="main"><div class="shell">
{body}
</div></main>
<footer class="site"><div class="shell">
  <nav aria-label="Legal">
    <a href="/legal/privacy/">Privacy</a>
    <a href="/legal/terms/">Terms</a>
    <a href="/legal/cookies/">Cookies</a>
    <a href="/legal/refunds/">Refunds</a>
  </nav>
  <p>Loema LLC &middot; <a href="mailto:feedback@loema.com">feedback@loema.com</a></p>
  <p>loema.org sets no cookies, runs no analytics, and loads nothing from anyone else's servers.
     <a href="https://www.loema.com">loema.com</a> is where the conversation begins.</p>
</div></footer>
</body>
</html>"""

def write(relpath, content):
    full = os.path.join(ROOT, relpath)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(content)
    print("wrote", relpath)

# ———————————————————————— pages ————————————————————————
PAGES = {}

PAGES["index.html"] = ("Loema — the commons", "The public trust layer of Loema: the open constitution format, the refusal ledger, the roadmap, and where the money goes.", "/", """
<h1>The quiet half of Loema.</h1>
<p class="lede">loema.com is where you write the rules your technology has to follow.
This is where Loema holds itself to rules of its own.</p>

<p>Loema is built on a simple refusal: software that shapes how you see yourself should not
also be studying you. The litmus at loema.com issues a personal constitution that lives only
in your keeping — Loema operates no server that holds it, no account that contains you, and
no analytics that watch you write it.</p>

<p>This site is the public trust layer. It carries the things a promise needs in order to be
checkable rather than taken on faith:</p>

<ul>
<li><a href="/constitution/">The constitution format</a> — the open standard your document is
written in, published so anything you trust can read it without asking us.</li>
<li><a href="/refusals/">The refusal ledger</a> — what Loema could build and will not, with reasons.</li>
<li><a href="/roadmap/">The roadmap</a> — where this is going, in the open.</li>
<li><a href="/funds/">Where money goes</a> — how an ad-free, data-free project stays alive.</li>
</ul>

<h2>Who is behind this</h2>
<p>Loema is built by its founder under <strong>Loema LLC</strong>, a small company formed in 2026
for exactly this work. There are no investors steering it and nothing here is for sale to
advertisers — the <a href="/funds/">funds page</a> says how the lights stay on.
You can reach a person at <a href="mailto:feedback@loema.com">feedback@loema.com</a>.</p>

<p class="quiet">More arrives here as it is ready — essays, and the standards Loema measures
itself by. Nothing on this site will ever need an account to read.</p>
""")

PAGES["constitution/index.html"] = ("The constitution format — Loema", "The open format of the personal data constitution: what the file holds, why it is yours, and the published schema.", "/constitution/", """
<h1>The constitution format.</h1>
<p class="lede">The document loema.com issues is a small, readable file that belongs to the
person who wrote it. This page is its public definition — so your document outlives Loema.</p>

<h2>What the file is</h2>
<p>A personal data constitution is a JSON document: your own articles about feeds, data,
attention, retention, and sharing — what you said, what was drafted from your answers, what
you confirmed, and what you amended, each marked so no words are put in your mouth. It carries
your preamble verbatim, the thing you said you were protecting, and a signature block recorded
only on your device.</p>

<h2>The promises the format keeps</h2>
<ul>
<li><strong>No silent certainty.</strong> Every clause is machine-distinguishable as inferred,
confirmed, amended, authored directly, or left open.</li>
<li><strong>Yours, portably.</strong> The file is plain JSON. Any tool, any AI, any person you
hand it to can read it without Loema's involvement.</li>
<li><strong>Addresses are permanent.</strong> <code>/constitution/v2</code> always means version 2.
Future versions get their own address; nothing you downloaded is ever redirected out from
under you.</li>
</ul>

<h2>The schema</h2>
<p>Documents declare <code>"$schema": "https://loema.org/constitution/v2"</code>.
The definition is served at exactly that address: <a href="/constitution/v2">loema.org/constitution/v2</a>.</p>

<h2>Openness</h2>
<p>The format is published to be used. Reading, writing, and honoring these documents requires
no permission from Loema and never will.</p>
""")

PAGES["refusals/index.html"] = ("The refusal ledger — Loema", "What Loema could build and refuses to, with reasons. The negative architecture, in public.", "/refusals/", """
<h1>The refusal ledger.</h1>
<p class="lede">Most products tell you what they offer. This page is the other half:
what Loema could build, and will not. Each entry names its reason, because a refusal
without a reason is just a delay.</p>

<ul class="ledger">
<li><b>No advertising, no data sale, no surveillance monetization.</b>
Loema's revenue may never depend on your attention, your data, or your dependence.
The business must do well when you receive value — not when Loema becomes necessary.</li>
<li><b>No variable-reward loops.</b> The slot-machine pattern that makes feeds compulsive
is the engine of behavioral addiction. Loema's interfaces are deliberately predictable.</li>
<li><b>No infinite feeds, follower counts, or engagement optimization.</b>
A product measured by your independence cannot be built on mechanics measured by your captivity.
When Loema shows you things, it shows a few — and then it ends.</li>
<li><b>No telemetry — not even the harmless kind.</b> Loema once built a counter that would
have recorded only how far people got, with no identity attached. It was removed rather than
switched on: a product that claims to collect nothing should not carry measurement code it has
to caveat.</li>
<li><b>No scores, rankings, types, or stages.</b> Nothing here grades you, compares you, or
sorts people into an order of progress. That boundary is permanent.</li>
<li><b>No emotional inference.</b> Loema reflects what you said. It does not guess what you feel.</li>
<li><b>No answers.</b> Loema is scaffolding, not revelation. It will not tell you what to
believe, and it is not a guru, a therapist, or an awakening.</li>
<li><b>No paywalled self-knowledge.</b> Understanding yourself is never a premium feature.
If Loema ever charges, it charges for labor and infrastructure — never for the mirror.</li>
</ul>

<p class="quiet">These refusals are recorded in Loema's internal canon with their full history.
None may be quietly reopened; reversing one would have to be done here, in public, with reasons.</p>
""")

PAGES["roadmap/index.html"] = ("The roadmap — Loema", "Where Loema is going, in the open: the litmus series, the rounds, the app, and what comes after.", "/roadmap/", """
<h1>The road, in the open.</h1>
<p class="lede">Loema builds in public. This is the honest state of the journey —
what exists, what is next, and what deliberately waits.</p>

<div class="era"><span class="when">Now — live</span>
<p><strong>The first conversation.</strong> The litmus at
<a href="https://www.loema.com">loema.com</a> — ten questions, one sentence of your own,
and a witnessed personal constitution that goes home with you. Nothing stored by Loema.</p></div>

<div class="era"><span class="when">Now — in private testing</span>
<p><strong>The app.</strong> A place your constitution lives: a mirror of your own words,
a discovery room that ends, and a garden you cultivate. Local-first — everything stays on
your device, exportable and erasable in full. In the hands of its first testers now.</p></div>

<div class="era"><span class="when">Next</span>
<p><strong>The rounds.</strong> The litmus is a first conversation, not a final exam.
Returning visits deepen the document — storage in your own words, then feeds, and onward —
each round short, each producing articles you can amend.</p></div>

<div class="era"><span class="when">Then</span>
<p><strong>Gatherings.</strong> Rooms where people write their constitutions together,
on paper worth keeping. Loema measures these the only way it measures anything:
by listening, in conversation, afterward.</p></div>

<div class="era"><span class="when">Deliberately later</span>
<p><strong>Enforcement, and the wider world.</strong> Tools that make your document operative —
on your devices and browsers, on your terms — and, eventually, open gardens: the half of your
garden you choose to let others walk through. Later because trust is built in that order.</p></div>

<p class="quiet">This page will grow more alive. Dates are deliberately absent:
Loema refuses manufactured urgency, including its own.</p>
""")

PAGES["funds/index.html"] = ("Where money goes — Loema", "How an ad-free, data-free project stays alive: the constraint envelope, donations, and the commitment to report spending.", "/funds/", """
<h1>Where the money goes.</h1>
<p class="lede">Loema shows no ads and sells nothing of yours. So it runs on people who want
it to exist — and owes those people an honest ledger.</p>

<h2>The rules money must obey here</h2>
<p>Loema's revenue may never depend on: more of your attention, more time in the app,
psychological dependence, data extraction, interpretive authority over you, behavioral
prediction, social comparison, identity lock-in, or making it costly to leave. Payment may
increase an organization's ability to participate in Loema's infrastructure — never its
ability to command your attention. These constraints are canon, not marketing: every future
revenue stream passes them before it ships.</p>

<h2>Today</h2>
<p>Loema is founder-funded, plus voluntary support through
<a href="https://ko-fi.com/loema" rel="noopener">Ko&#8209;fi</a>. Donations are gifts toward the
building — they buy nothing, reserve nothing, and are handled by Ko&#8209;fi, which shares no
card details with Loema.</p>

<h2>The commitment</h2>
<p>From the first supported dollar, spending is reported here on a regular rhythm, in plain
language — what came in, what it paid for. That includes, plainly, what pays the founder:
keeping the builder alive is a cost of the building, and it will sit in the ledger under its
own name rather than hide inside another line. The first report arrives with the first dollar;
the rhythm will be stated on this page before then, not negotiated after.</p>

<p class="quiet">Membership, paid labor-saving features, and physical things worth keeping may
come later. When they do, their terms appear here and in <a href="/legal/terms/">the terms</a>
before a cent changes hands.</p>
""")

# ———————————————————————— legal ————————————————————————

def recap(text):
    return f'<div class="recap"><b>In plain words</b>{text}</div>'

PAGES["legal/privacy/index.html"] = ("Privacy policy — Loema", "Loema's privacy policy for loema.org and loema.com: what little is processed, by whom, and your rights.", None, f"""
<h1>Privacy policy.</h1>
<p class="lede">Covering <strong>loema.org</strong> and <strong>loema.com</strong>, operated by
Loema LLC. Effective October 2026.</p>
{recap("Loema is built not to know you. We keep no accounts, run no analytics, and hold none of what you write. The one thing we ever hold is an email address — only if you join the newsletter, and you can leave any time.")}

<h2>What Loema does not collect</h2>
<p>The litmus at loema.com and the Loema app run entirely on your device. Your answers, your
constitution, your signature rhythm, anything you keep in the app — none of it is transmitted
to Loema or anyone else by us. We operate no analytics, no advertising trackers, no behavioral
measurement, and no server that stores user content. We never sell personal information, and
have none to sell.</p>

<h2>The one thing we may hold: a newsletter email</h2>
<p>If you choose to join the waitlist at loema.com, your email address is held by our newsletter
provider, <a href="https://buttondown.com" rel="noopener">Buttondown</a> (United States), and used
for the newsletter — nothing else. Every email includes an unsubscribe link; unsubscribing or
writing to us removes you. We do not enrich, profile, or share this list.</p>

<h2>What reaches us when you contact us</h2>
<p>If you email <a href="mailto:feedback@loema.com">feedback@loema.com</a>, we receive what you
send and use it to respond and to improve Loema. Our mail is hosted with Proton.</p>

<h2>Infrastructure that serves these pages</h2>
<p>These sites are static pages served by GitHub Pages and Cloudflare. Like essentially all web
hosts, they process visitors' IP addresses transiently to deliver pages and defend against
abuse, under their own policies
(<a href="https://docs.github.com/site-policy/privacy-policies" rel="noopener">GitHub</a>,
<a href="https://www.cloudflare.com/privacypolicy/" rel="noopener">Cloudflare</a>).
Loema receives no visitor logs, dashboards, or analytics from them.</p>

<h2>Donations</h2>
<p>Donations run through <a href="https://ko-fi.com" rel="noopener">Ko&#8209;fi</a> under Ko&#8209;fi's
own terms and privacy policy. Loema receives the supporter name/message Ko&#8209;fi shows us —
never card or bank details.</p>

<h2>Children</h2>
<p>Loema has no age gate and dictates nothing about who may reason with their own technology —
there is nothing explicit here, and nothing collected from anyone of any age. In the legal
sense that matters: these sites are not "directed to children under 13" (the COPPA category),
and because we collect and store nothing, no child's personal information is either. The
newsletter — the one place an email changes hands — is for ages 13 and up.</p>

<h2>Your rights</h2>
<p>Whatever your jurisdiction grants you — access, deletion, correction, portability — exercising
it with Loema is short work, because the only record that can exist is a newsletter address.
Email <a href="mailto:feedback@loema.com">feedback@loema.com</a> and it is handled.</p>

<h2>Changes</h2>
<p>If Loema's practices ever change — for example, if the app gains optional sync — this policy
changes <em>first</em>, in plain language, with the effective date updated. Clarity before
collection applies to Loema before anyone else.</p>
""")

PAGES["legal/terms/index.html"] = ("Terms of service — Loema", "The terms for using loema.com and loema.org, in plain language with plain recaps.", None, f"""
<h1>Terms of service.</h1>
<p class="lede">For <strong>loema.com</strong> and <strong>loema.org</strong>, operated by
Loema LLC. Effective October 2026.</p>
{recap("Use the litmus freely; the document it makes is yours. Don't misuse the sites. Loema is honest reflection, not professional advice, and comes as-is. Donations are gifts, not purchases.")}

<h2>1. Who we are</h2>
<p>These sites are operated by Loema LLC ("Loema", "we"). Contact:
<a href="mailto:feedback@loema.com">feedback@loema.com</a>.</p>

<h2>2. The litmus and your document</h2>
<p>The litmus is free. The constitution it produces is <strong>yours</strong>: you own your
answers, your preamble, and your document, and you may use, edit, publish, or destroy it
without any permission from us. Loema claims no license over your words — it never receives
them.</p>
{recap("Your constitution belongs to you. Full stop.")}

<h2>3. Our content and the open format</h2>
<p>The text and design of these sites belong to Loema LLC. The constitution format and its
published schema are open: you may read, implement, and build on them freely, with attribution
appreciated. "Loema" and the Loema mark identify this project; please don't use them in ways
that suggest we made or endorsed something we didn't.</p>

<h2>4. What Loema is not</h2>
<p>Loema offers structured self-reflection. It is not medical, psychological, legal, or
financial advice, and it is not therapy or a substitute for professional care. The "AI preamble"
feature prepares text <em>you</em> may give to third-party AI services; those services' own terms
govern what happens there, and the preamble itself states that it cannot override their rules.</p>
{recap("Loema reflects. It doesn't diagnose, treat, or advise — and it says so to any AI you hand your preamble to.")}

<h2>5. Acceptable use</h2>
<p>Don't attack, overload, or attempt to compromise the sites; don't misrepresent Loema;
don't use the sites to violate law or others' rights.</p>

<h2>6. Donations</h2>
<p>Donations via Ko&#8209;fi are voluntary gifts supporting development. They are not purchases,
investments, or pre-orders, and confer no goods, services, or rights. See the
<a href="/legal/refunds/">refund policy</a>.</p>

<h2>7. As-is; limitation of liability</h2>
<p>The sites and the litmus are provided "as is," without warranties of any kind, to the fullest
extent permitted by law. To that same extent, Loema LLC's total liability arising from your use
of the sites is limited to the amount you have paid us — which, today, is nothing. Nothing here
limits liability that cannot lawfully be limited.</p>
{recap("We built this carefully, and it's free — so our legal exposure matches: use it as-is.")}

<h2>8. Changes and governing law</h2>
<p>We may update these terms; the effective date above changes when we do, and material changes
are noted plainly. These terms are governed by the laws of the U.S. state where Loema LLC is
organized, without regard to conflict-of-law rules.</p>
""")

PAGES["legal/cookies/index.html"] = ("Cookie policy — Loema", "Loema sets no cookies. What that means, and the one narrow exception a security host may make.", None, f"""
<h1>Cookie policy.</h1>
<p class="lede">Effective October 2026.</p>
{recap("We set no cookies — none, of any kind. That's why there's no cookie banner: there's nothing to consent to.")}

<h2>Cookies Loema sets</h2>
<p>None. loema.org and loema.com set no cookies, use no local-storage trackers, no pixels,
no fingerprinting, and no analytics identifiers. (The Loema app stores your own content on your
own device at your direction — that is your keeping, not tracking.)</p>

<h2>The narrow exception that isn't ours</h2>
<p>Our pages are delivered through Cloudflare, which may in some circumstances set a short-lived,
strictly-necessary security cookie (such as <code>__cf_bm</code>) to tell humans from attack
traffic. Cookies of this class exist solely to deliver the service securely, carry no advertising
or analytics function, and are generally exempt from consent requirements. Loema reads nothing
from them.</p>

<h2>If this ever changes</h2>
<p>It would be announced in this policy, plainly, before anything is set — and anything
non-essential would ask first.</p>
""")

PAGES["legal/refunds/index.html"] = ("Refund policy — Loema", "Nothing is sold today; donations are gifts handled by Ko-fi. What happens when paid offerings arrive.", None, f"""
<h1>Refund policy.</h1>
<p class="lede">Effective October 2026.</p>
{recap("Nothing is for sale yet, so there's nothing to refund. Donations are gifts through Ko-fi. When something is sold someday, its refund terms will be stated before you pay.")}

<h2>Today</h2>
<p>Loema sells no goods or services. The litmus and these pages are free.</p>

<h2>Donations</h2>
<p>Support given through <a href="https://ko-fi.com/loema" rel="noopener">Ko&#8209;fi</a> is a
voluntary gift, processed by Ko&#8209;fi under
<a href="https://more.ko-fi.com/terms" rel="noopener">Ko&#8209;fi's terms</a>. Gifts are generally
not refundable, but if you made one in error, write to
<a href="mailto:feedback@loema.com">feedback@loema.com</a> within 7 days and we will do right
by you.</p>

<h2>When something is sold</h2>
<p>If Loema offers paid memberships, services, or physical goods in the future, each will carry
its own clearly stated refund terms — published before purchase, not after.</p>
""")

CURRENTS = {"index.html": "/", "constitution/index.html": "/constitution/",
            "refusals/index.html": "/refusals/", "roadmap/index.html": "/roadmap/",
            "funds/index.html": "/funds/"}

for path, (title, desc, cur, body) in PAGES.items():
    write(path, page(path, title, desc, body, CURRENTS.get(path)))

# ———— the schema, at exactly /constitution/v2 ————
import json
schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "https://loema.org/constitution/v2",
  "title": "Personal Data Constitution (v2)",
  "description": "The document issued by the Loema litmus (instrument loema-litmus-v5) and carried by its author. Published so the file outlives Loema; permissive by design — unknown fields MUST be preserved, never stripped. /v2 always means v2; future versions get their own address.",
  "type": "object",
  "required": ["articles"],
  "additionalProperties": True,
  "properties": {
    "$schema": {"type": "string", "const": "https://loema.org/constitution/v2"},
    "namespace": {"type": "string", "description": "The instrument's namespace; 'personal' for the first litmus."},
    "title": {"type": "string"},
    "author": {"type": "object", "additionalProperties": True, "properties": {
      "display_name": {"type": "string", "description": "Optional name or pseudonym, chosen by the author."},
      "source": {"type": "string"}}},
    "preamble": {"type": "object", "additionalProperties": True, "properties": {
      "text": {"type": "string", "description": "The author's own sentence, verbatim."},
      "register": {"type": "string", "enum": ["plain", "boundaries", "technical", "creative"]},
      "source": {"type": "string"}}},
    "articles": {
      "type": "object",
      "description": "Keys are namespaced article ids (e.g. personal.feeds). Reserved namespaces communal.*, systemic.*, ecological.* exist for sibling scales; readers must tolerate namespaces they do not know.",
      "additionalProperties": {"type": "object", "additionalProperties": True, "properties": {
        "posture": {"type": ["string", "null"], "description": "comfortable | concerned | uncertain | conditional | unset — internal vocabulary, never shown as a label."},
        "rule": {"type": ["string", "null"], "description": "The article's text, in the author's register."},
        "source": {"type": "string", "description": "generated_from_response | authored | unanswered — no silent certainty."},
        "evidence": {"description": "Question ids the article was drafted from."},
        "confirmed": {"type": "boolean"},
        "amended": {"type": "boolean"}}}},
    "loema_safeguards": {"type": "object", "additionalProperties": True,
      "description": "Defaults Loema applies until the author decides — explicitly outside the author's words."},
    "through_line": {"type": "object", "additionalProperties": True, "properties": {
      "text": {"type": "string"},
      "verdict": {"type": "string", "enum": ["confirmed", "partial", "replaced_by_author", "fits"]},
      "source": {"type": "string"}}},
    "personal_focus": {"type": "object", "additionalProperties": True,
      "description": "What the author said keeps getting buried — their own words."},
    "dispositions": {"type": "object", "additionalProperties": True},
    "review": {"type": "object", "additionalProperties": True},
    "exceptions": {"type": "array"},
    "amendments": {"type": "array", "description": "The author's amendment history; shape is author-governed."},
    "signature": {"type": "object", "additionalProperties": True, "properties": {
      "confirmed": {"type": "boolean"},
      "witnessed_at_local": {"type": "string", "description": "Device-local time; never transmitted."},
      "ratified_at_local": {"type": "string"},
      "hold_ms": {"type": "number"},
      "rhythm_ms": {"type": "array", "items": {"type": "number"},
        "description": "OPT-IN ONLY. Coarse inter-tap intervals of the signing; present only if the author chose to keep them. Lives in this file and nowhere else."},
      "circles": {"type": "array", "description": "OPT-IN ONLY. Coarse ring traces: sweep_deg in 15-degree steps, direction, duration_ms in 50 ms steps — never a raw path."}}},
    "provenance": {"type": "object", "additionalProperties": True, "properties": {
      "instrument": {"type": "string"},
      "stored_by_loema": {"type": "boolean", "const": False}}}
  }
}
write("constitution/v2", json.dumps(schema, indent=2))

write("_headers", """/constitution/v2
  Content-Type: application/schema+json; charset=utf-8
  Access-Control-Allow-Origin: *

/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: no-referrer
  X-Frame-Options: DENY
""")

write("robots.txt", "User-agent: *\nAllow: /\n")

write("README.md", """# loema.org — shape draft

The public trust layer of Loema. Static, zero external requests, no cookies,
no analytics, no forms. Deploy target: Cloudflare Pages (the `_headers` file
serves `/constitution/v2` as JSON Schema).

Held back deliberately (reserved, unbuilt): /essays/, /clarity-analytics/.

Legal pages are accurate drafts of actual practice, written to carry into the
attorney pass (founder to-do item 11) — governing-law state intentionally
generic pending that pass.
""")
print("done")
