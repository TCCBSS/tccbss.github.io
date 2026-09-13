#!/usr/bin/env python3
"""Generates the static tccbss.com pages. Run: python3 tools/build.py"""
import os, json, datetime, html as H
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE="https://tccbss.com"
EMAIL="info@tccbss.com"
LINKEDIN="https://www.linkedin.com/company/the-consulting-company-tcc"
PORTAL="https://tccbss-learn.azurewebsites.net/teach"
L1="https://nas.io/evgeniyas-business-1/courses/level-1-beginners-certified-contract-management-fo-1"
L2="https://nas.io/evgeniyas-business-1/courses/level-2-advanced-certified-contract-management-oil"
L3="https://nas.io/evgeniyas-business-1/courses/fccm-exam-preparation-course"
FORM_ENDPOINT=os.environ.get("FORM_ENDPOINT","")   # e.g. https://formspree.io/f/xxxxxxx
TODAY=datetime.date.today().isoformat()

ORG={"@type":"ProfessionalService","@id":SITE+"/#organization","name":"TCC Business Support Solution","alternateName":"TCC BSS",
 "legalName":"TCC Business Support Solution W.L.L.","url":SITE+"/","email":EMAIL,"logo":SITE+"/assets/favicon.svg",
 "description":"Doha-based contract management consulting and certified training for oil & gas, EPC and infrastructure. We fix contract leakage: claims, change control, and governance.",
 "address":{"@type":"PostalAddress","addressLocality":"Doha","addressCountry":"QA"},
 "areaServed":["Qatar","Middle East","GCC","North Africa","South Asia","International"],
 "identifier":{"@type":"PropertyValue","propertyID":"Commercial Registration","value":"235393"},
 "sameAs":[LINKEDIN],"knowsAbout":["Contract management","Claims management","Change control","FIDIC contracts","Contract risk management","EPC contracts"]}

MOTIF="""<svg class="motif" viewBox="0 0 460 420" role="img" aria-label="Abstract composition of blocks fitting together, representing contract pieces under control">
<rect x="150" y="40" width="160" height="160" fill="#F7F3EE"/><rect x="60" y="130" width="120" height="120" fill="#F7F3EE" opacity=".78"/>
<rect x="240" y="200" width="140" height="140" fill="#F7F3EE" opacity=".62"/><rect x="120" y="270" width="100" height="100" fill="#F7F3EE" opacity=".9"/>
<rect x="330" y="80" width="70" height="70" fill="#F7F3EE" opacity=".45"/><rect x="200" y="150" width="60" height="60" fill="#4E1329"/>
<rect x="180" y="220" width="40" height="40" fill="#F7F3EE" opacity=".35"/></svg>"""

def esc(s): return H.escape(s,quote=True)

def head(title,desc,path,ld):
    url=SITE+path
    ld=[ORG]+ld
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="TCC Business Support Solution">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{url}">
<meta name="twitter:card" content="summary">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:wght@700&family=Source+Sans+3:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css">
<script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@graph":ld},ensure_ascii=False)}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
  <a class="brand" href="/">TCC BSS<small>Business Support Solution</small></a>
  <button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu <span class="chev"></span></button>
  <ul class="nav" id="nav">
    <li><a href="/"{' aria-current="page"' if path=='/' else ''}>Home</a></li>
    <li class="has-sub"><button aria-expanded="false" aria-haspopup="true">Our Services <span class="chev"></span></button>
      <ul class="sub">
        <li><a href="/consulting-services">Consulting Services</a></li>
        <li><a href="/certified-training">Certified Training</a></li>
        <li><a href="/global-experts">Global Experts</a></li>
        <li><a href="/build-your-own-course">Build Your Own Course</a></li>
      </ul></li>
    <li><a href="/about-us"{' aria-current="page"' if path=='/about-us' else ''}>About Us</a></li>
    <li><a class="cta" href="/#contact">Contact Us</a></li>
  </ul>
</div></header>
<main id="main">
"""

FOOT=f"""</main>
<footer class="site-footer"><div class="wrap">
  <div class="cols">
    <div><a class="brand" href="/">TCC BSS<small>Business Support Solution</small></a>
      <p style="margin-top:1rem;max-width:40ch">Contract management consulting and certified training. Headquartered in Doha, Qatar; serving the Middle East and international projects.</p>
      <p>TCC Business Support Solution W.L.L.<br>Commercial Registration 235393</p></div>
    <div><h4>Services</h4><ul>
      <li><a href="/consulting-services">Consulting Services</a></li><li><a href="/certified-training">Certified Training</a></li>
      <li><a href="/global-experts">Global Experts</a></li><li><a href="/build-your-own-course">Build Your Own Course</a></li></ul></div>
    <div><h4>Contact</h4><ul>
      <li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><a href="{LINKEDIN}" rel="noopener" target="_blank">LinkedIn</a></li>
      <li><a href="/about-us">About Us</a></li><li><a href="/#contact">Send an enquiry</a></li></ul></div>
  </div>
  <div class="legal"><span>Copyright © 2026 TCC Business Support Solution - All Rights Reserved.</span>
    <span><a href="/terms-%26-conditions">Terms &amp; Conditions</a> &nbsp;·&nbsp; <a href="/privacy-policy">Privacy Policy</a></span></div>
</div></footer>
<script src="/assets/site.js" defer></script>
</body>
</html>
"""

def hero(kicker,h1,lead,cta=None,cta2=None,compact=True,motif=False):
    btns=""
    if cta: btns+=f'<a class="btn" href="{cta[1]}">{cta[0]}</a>'
    if cta2: btns+=f'<a class="btn ghost" href="{cta2[1]}">{cta2[0]}</a>'
    return f"""<section class="hero{' compact' if compact else ''}"><div class="wrap"><div>
  {f'<p class="kicker">{kicker}</p>' if kicker else ''}<h1>{h1}</h1><p class="lead">{lead}</p>
  {f'<div class="actions">{btns}</div>' if btns else ''}</div>{MOTIF if motif else ''}</div></section>
"""

def cards(items,tag="h3"):
    return '<div class="grid">'+''.join(f'<article class="card"><{tag}>{t}</{tag}><p>{d}</p></article>' for t,d in items)+'</div>'

def cta_band(h,p,label,href):
    return f'<section class="cta-band"><div class="wrap"><h2>{h}</h2><p>{p}</p><a class="btn" href="{href}">{label}</a></div></section>\n'

TRACK="""<div class="band"><div class="wrap"><ul><li>Headquartered in Doha, Qatar</li><li>Multi-billion-dollar mega-project experience</li><li>Claims and negotiations exceeding USD 140 million</li></ul></div></div>
"""

SERVICES=[("Digital contract templates","Ready-to-use, editable templates (NDA, LOA, Service Agreements, Purchase Orders, Change Orders, notices) with clear instructions and placeholders."),
("Signature-ready documents","Paid customisation to align templates to your transaction, parties, and key terms—clean, ready for signing."),
("Contract administration &amp; change control","Variation/change management process setup, tracking, documentation discipline, and support with approvals and registers."),
("Claims review &amp; negotiation support","Entitlement and substantiation review, claims packaging, negotiation strategy, and position papers to close issues faster."),
("Contract risk management","Risk identification, contract risk registers, governance controls, and reporting to management."),
("Contract management system setup","Requirements definition, workflow/process design, register structures, rollout support, and team training."),
("Build and sell your own course","Publish your professional course on our learning platform — we host it, examine your students and issue verifiable certificates in your name, while you keep 80% of every sale with no subscription.")]

CONTACT=f"""<section id="contact"><div class="wrap"><p class="kicker">Contact Us</p><h2>Send your request and we will get back to you</h2>
<div class="contact">
<form class="f" data-endpoint="{FORM_ENDPOINT}" method="POST" action="{FORM_ENDPOINT or 'mailto:'+EMAIL}" novalidate>
  <div class="row"><div><label for="name">Name</label><input id="name" name="name" type="text" autocomplete="name" required></div>
  <div><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email" required></div></div>
  <div><label for="message">Message</label><textarea id="message" name="message" required></textarea></div>
  <p class="hp" aria-hidden="true"><label>Leave this field empty <input type="text" name="_gotcha" tabindex="-1" autocomplete="off"></label></p>
  <div><button class="btn" type="submit">Send</button></div>
  <p class="status" role="status" aria-live="polite"></p>
  <p class="note">This site is protected by reCAPTCHA-free spam filtering. By sending, you agree to our <a href="/privacy-policy">Privacy Policy</a> and <a href="/terms-%26-conditions">Terms &amp; Conditions</a>.</p>
</form>
<div class="info"><h3>We love our customers, so feel free to contact us at any time</h3>
  <dl><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd><dt>Company</dt><dd>TCC Business Support Solution W.L.L.<br>Doha, State of Qatar</dd>
  <dt>LinkedIn</dt><dd><a href="{LINKEDIN}" rel="noopener" target="_blank">The Consulting Company (TCC)</a></dd></dl></div>
</div></div></section>
"""

pages={}

# ---------- HOME ----------
home=hero("Oil &amp; Gas · EPC · Infrastructure","Contract Management Consulting &amp; Certified Training for Oil &amp; Gas and Infra",
  "We fix contract leakage: claims, change control, and governance",("Talk to us","#contact"),("Explore training","/certified-training"),compact=False,motif=True)
home+=TRACK
home+="""<section><div class="wrap"><p class="kicker">What we do</p><h2>Practical, repeatable contract control</h2>
<p class="intro lead">TCC Business Support Solution helps organisations strengthen contract control and reduce contract leakage through practical, repeatable support. Headquartered in Doha, Qatar, we serve oil &amp; gas, EPC and infrastructure projects across the Middle East and internationally — with experience from multi-billion-dollar mega-projects and claims and negotiations exceeding USD 140 million.</p>
"""+cards(SERVICES)+"""<div class="actions"><a class="btn ghost" href="/consulting-services">See consulting services</a></div></div></section>
"""
home+=f"""<section class="alt"><div class="wrap"><p class="kicker">Certified Training</p><h2>Master Contract Management in Oil &amp; Gas</h2>
<div class="levels">
<div class="level"><div class="tag">Level 1<small>Beginner</small></div><p><strong>Certified Contract Management Foundations (Oil &amp; Gas Infrastructure)</strong> — contract fundamentals, administration basics, change control and records discipline.</p><a class="btn" href="{L1}" rel="noopener" target="_blank">View course</a></div>
<div class="level"><div class="tag">Level 2<small>Advanced</small></div><p><strong>Certified Contract Management (Oil &amp; Gas Infrastructure)</strong> — FIDIC and EPC contracts, claims strategy and dispute resolution from real project cases.</p><a class="btn" href="{L2}" rel="noopener" target="_blank">View course</a></div>
<div class="level"><div class="tag">Level 3<small>Professional</small></div><p><strong>FIDIC Certified Contracts Manager</strong> — advanced FIDIC mechanisms: variations, claims, determinations and dispute boards.</p><a class="btn" href="{L3}" rel="noopener" target="_blank">View course</a></div>
</div><div class="actions"><a class="btn ghost" href="/certified-training">All training details &amp; FAQ</a></div></div></section>
"""
home+=f"""<section><div class="wrap"><p class="kicker">Teach with TCC BSS</p><h2>Publish your own certified course</h2>
<p class="intro lead">Are you a senior contracts, claims or delay professional? Publish your own certified course on the TCC BSS learning platform. You build the course and its final exam — we host it, sell it, examine your students and issue verifiable certificates in your name. You keep 80% of every sale, with no subscription and no fees until you sell. Instructors anywhere in the world are welcome.</p>
<div class="steps">
<article class="card"><div class="num">1</div><h3>You Build the Course</h3><p>Upload your modules as PDF or video, write the final exam (minimum 20 questions), and set your price in QAR.</p></article>
<article class="card"><div class="num">2</div><h3>We Run Everything</h3><p>Hosting, sales, student testing and verifiable TCC BSS certificates issued in your name — reviewed and approved by us before going live.</p></article>
<article class="card"><div class="num">3</div><h3>You Earn Per Sale</h3><p>80% of every sale, whether your course is documents or video. No subscription — you pay nothing until you sell.</p></article>
</div><div class="actions"><a class="btn" href="{PORTAL}" rel="noopener" target="_blank">Open the Instructor Portal</a><a class="btn ghost" href="/build-your-own-course">How it works</a></div></div></section>
"""
home+=CONTACT
pages["index"]=("Contract Management Consulting & Training | TCC Business Support Solution",
 "Doha-based contract management consulting and training for oil & gas, EPC and infrastructure. We fix contract leakage: claims, change control, governance.","/",
 [{"@type":"WebSite","url":SITE+"/","name":"TCC Business Support Solution","publisher":{"@id":SITE+"/#organization"}}],home)

# ---------- ABOUT ----------
about=hero("Doha, Qatar · Middle East · International","About TCC Business Support Solution",
 "TCC Business Support Solution is a contract management consultancy headquartered in Doha, Qatar. We help organisations protect value on complex, high-risk projects by preventing contract leakage across claims, change control and governance.",("Contact Us","/#contact"))
about+="""<section><div class="wrap"><p class="kicker">Track record</p><h2>Experience that protects your position</h2>
<p class="intro lead">Our team's experience comes from inside multi-billion-dollar mega-projects in the Middle East, and from claims and negotiations exceeding USD 140 million — environments where documentation, timely notices and clear approvals directly protect cash flow.</p>
"""+cards([("Consulting","Contract administration, change control, claims support, risk registers and contract management system implementation. <a href=\"/consulting-services\">Consulting services</a>"),
("Certified training","Three levels of certified contract management training, from Foundations to FIDIC Certified Contracts Manager. <a href=\"/certified-training\">Certified training</a>"),
("Global experts","Senior contract, claims and delay experts engaged per assignment, with TCC BSS managing the brief. <a href=\"/global-experts\">Global Experts network</a>")])+"""</div></section>
"""+TRACK+cta_band("Let's talk about your project","Tell us where value is leaking — claims, change control or governance — and we will propose practical, repeatable support.","Contact Us","/#contact")
pages["about-us"]=("About TCC Business Support Solution — Doha, Qatar",
 "Doha-based contract management consultancy with experience on multi-billion-dollar Middle East mega-projects and claims exceeding USD 140 million.","/about-us",
 [{"@type":"AboutPage","url":SITE+"/about-us","name":"About TCC Business Support Solution","about":{"@id":SITE+"/#organization"}}],about)

# ---------- CONSULTING ----------
cons=hero("Oil &amp; Gas · EPC · Infrastructure","Contract Management Consulting",
 "TCC Business Support Solution provides contract management consulting for owners, EPC contractors and subcontractors on oil &amp; gas and infrastructure projects. We install the disciplines that prevent contract leakage: change control, risk registers, governance, and contract management systems your team can run.",("Contact Us","/#contact"))
cons+="<section><div class=\"wrap\"><p class=\"kicker\">What we do</p><h2>Consulting services</h2>"+cards([
("Contract administration &amp; change control","Variation and change management process setup, tracking, documentation discipline, approvals and registers — so every change is captured, priced and approved before it becomes a dispute."),
("Claims review &amp; negotiation support","Independent claim evaluations, entitlement and substantiation review, claims packaging, expert reports, negotiation strategy and position papers. Our team has supported claims and negotiations exceeding USD 140 million."),
("Contract risk management","Risk identification workshops, contract risk registers, governance controls and management reporting that make contract exposure visible before it crystallises."),
("Contract management system setup","Requirements definition, workflow and process design, register structures, rollout support and team training for your contract management system."),
("Commercial management &amp; dispute evidence","Documentation discipline, records strategy and evidence packages that hold up in negotiation, adjudication or arbitration — plus risk, compliance and policy development with mentoring for your team."),
("Digital contract templates &amp; signature-ready documents","Editable NDA, LOA, service agreement, purchase order, change order and notice templates — plus customisation aligned to your transaction, parties and key terms, clean and ready for signing.")])+"</div></section>\n"
cons+=TRACK+cta_band("Need a second set of eyes on a claim or a change?","Consulting services are quoted individually. Send us a short description of the project and the issue, and we will come back with a scope.","Contact Us","/#contact")
pages["consulting-services"]=("Contract Management Consulting for Oil & Gas & EPC | TCC BSS",
 "Contract administration, change control, claims support, risk registers and CMS implementation for oil & gas, EPC and infrastructure projects in Doha, Qatar.","/consulting-services",
 [{"@type":"Service","name":"Contract Management Consulting","serviceType":"Contract management consulting","provider":{"@id":SITE+"/#organization"},"areaServed":["Qatar","Middle East","International"],"url":SITE+"/consulting-services",
   "hasOfferCatalog":{"@type":"OfferCatalog","name":"Consulting services","itemListElement":[{"@type":"Offer","itemOffered":{"@type":"Service","name":n}} for n in ["Contract administration & change control","Claims review & negotiation support","Contract risk management","Contract management system setup","Commercial management & dispute evidence","Digital contract templates & signature-ready documents"]]}}],cons)

# ---------- TRAINING ----------
FAQ=[("What is contract leakage?","Contract leakage is the value an organisation loses between what a contract entitles it to and what it actually realises — through unpriced changes, unclaimed entitlements, missed notices and weak governance. TCC BSS reduces leakage through disciplined change control, claims management and contract governance."),
("Who are the training courses for?","Project and contract professionals in oil & gas, EPC and infrastructure. Level 1 suits engineers and administrators new to contract work; Level 2 suits practising contract administrators and quantity surveyors; Level 3 suits experienced professionals targeting FIDIC contracts manager certification."),
("Where is TCC BSS located?","TCC Business Support Solution is headquartered in Doha, Qatar, and supports clients across the Middle East and internationally. Contact Info@tccbss.com for the current training schedule and delivery format."),
("What is FIDIC and why does it matter?","FIDIC publishes the standard forms of contract most widely used on international construction and infrastructure projects. Employers and contractors on major projects expect contracts managers to know FIDIC mechanisms for variations, claims and dispute resolution — the focus of our Level 2 and Level 3 programmes."),
("Do you provide consulting as well as training?","Yes — both. TCC BSS provides contract administration and change control setup, independent claim evaluations and negotiation support, contract risk management, and contract management system implementation, alongside its certified training programmes.")]
LEVELS=[("Level 1","Beginner","Certified Contract Management Foundations","Beginner level, for engineers, coordinators and team members new to contract administration on oil &amp; gas and infrastructure projects. Covers contract fundamentals, administration basics, change control and records discipline, with practical case work.",L1),
("Level 2","Advanced","Advanced Certified Contract Management","For practising contract administrators, engineers and quantity surveyors. Deepens expertise in FIDIC and EPC contracts, claims strategy and dispute resolution — taught from real project cases.",L2),
("Level 3","Professional","FIDIC Certified Contracts Manager","Professional level, for experienced practitioners. Advanced FIDIC contract mechanisms — variations, claims, determinations and dispute boards — preparing you to manage FIDIC contracts on major international projects.",L3)]
tr=hero("Certified Training","Contract Management Training — Oil &amp; Gas &amp; FIDIC",
 "Three-level certified contract management training for oil &amp; gas and infrastructure teams: Foundations, Advanced, and FIDIC Certified Contracts Manager.",("View the courses","#levels"),("Ask about team programmes","/#contact"))
tr+='<section id="levels"><div class="wrap"><p class="kicker">Three levels</p><h2>Choose your level</h2><div class="levels">'
for tag,sub,name,desc,link in LEVELS:
    tr+=f'<div class="level"><div class="tag">{tag}<small>{sub}</small></div><div><h3 style="margin-bottom:.3rem">{name}</h3><p>{desc}</p></div><a class="btn" href="{link}" rel="noopener" target="_blank">View Course &amp; Enrol</a></div>'
tr+='</div></div></section>\n<section class="alt"><div class="wrap">'+cards([
("Who teaches the courses","All levels are taught by senior practitioners whose experience spans multi-billion-dollar Middle East mega-projects and claims and negotiations exceeding USD 140 million — judgement from real projects, not just theory."),
("Certification","Each level includes practical case work and awards a TCC Business Support Solution certificate of completion — evidence of applied contract management capability for employers in oil &amp; gas, EPC and infrastructure."),
("Schedules, format &amp; enrolment",f"Contact us at <a href=\"mailto:{EMAIL}\">{EMAIL}</a> for the current schedule, delivery format and pricing for each level. We run programmes for individuals and for project teams, from our base in Doha, Qatar.")])+'</div></section>\n'
tr+=f'<section><div class="wrap"><p class="kicker">FAQ</p><h2>Frequently Asked Questions</h2><p class="intro">Answers about our contract management training and consulting. Reach us at <a href="mailto:{EMAIL}">{EMAIL}</a> if you cannot find an answer to your question.</p><div class="faq">'
for q,a in FAQ: tr+=f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>'
tr+='</div></div></section>\n'+cta_band("Training for your project team?","We run all three levels for individuals and for project teams, from our base in Doha, Qatar.","Contact Us","/#contact")
pages["certified-training"]=("Certified Contract Management Training — Oil & Gas & FIDIC | TCC BSS",
 "Three-level certified contract management training for oil & gas and infrastructure teams: Foundations, Advanced, and FIDIC Certified Contracts Manager.","/certified-training",
 [{"@type":"ItemList","name":"Certified contract management training levels","itemListElement":[{"@type":"ListItem","position":i+1,"item":{"@type":"Course","name":f"{t} — {n}","description":H.unescape(d).replace("&amp;","&"),"url":l,"provider":{"@id":SITE+"/#organization"},"educationalLevel":s}} for i,(t,s,n,d,l) in enumerate(LEVELS)]},
  {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ]}],tr)

# ---------- GLOBAL EXPERTS ----------
ge=hero("Senior contract expertise, on demand","Global Experts Network",
 "A curated panel of senior contract administrators, claims specialists, delay analysts, planners, FIDIC practitioners and dispute professionals. Companies engage proven judgement on specific assignments — without hiring — while TCC BSS manages the brief, scope, confidentiality and contractual cover.",("Engage an Expert","/#contact"))
ge+="<section><div class=\"wrap\"><p class=\"kicker\">Assignments</p><h2>What companies engage us for</h2>"+cards([
("Independent claim evaluations","An impartial senior review of a claim's entitlement, substantiation and quantum — before you submit, respond or settle. A trained second set of eyes at the decisive moment."),
("Expert reports","Structured expert reports on claims, delay and quantum, prepared by practitioners with mega-project experience — ready to support negotiation, adjudication or arbitration."),
("Contemporaneous record reviews","An audit of your project records — notices, registers, correspondence, daily reports — to establish how your position would hold up if tested, and what to fix while there is still time."),
("Delay analysis &amp; planning","Senior delay analysts and planners to assess extension-of-time claims, prepare or rebut delay analyses, and align the schedule narrative with the contractual mechanism."),
("Targeted second opinions","A scoped question answered by an expert who has seen it before — a clause interpretation, a negotiation position, a settlement threshold, or a dispute-route decision.")])+"</div></section>\n"
ge+=f"""<section class="alt"><div class="wrap"><p class="kicker">Where we work &amp; how to engage</p><h2>Per assignment, across the region</h2>
<p class="intro lead">Experts are engaged per assignment across the Middle East, GCC, North Africa and South Asia, on oil, gas, LNG, roads and large civil works. Contact <a href="mailto:{EMAIL}">{EMAIL}</a> to scope an assignment — or to join the network as an expert.</p>
<div class="actions"><a class="btn" href="/#contact">Engage an Expert</a><a class="btn ghost" href="mailto:{EMAIL}?subject=Joining%20the%20Global%20Experts%20network">Join as an expert</a></div></div></section>
"""
pages["global-experts"]=("Global Experts — Contract & Claims Specialists On Demand | TCC BSS",
 "Engage senior contract, claims and delay experts on demand: independent claim evaluations, expert reports and second opinions across the Middle East.","/global-experts",
 [{"@type":"Service","name":"Global Experts Network","serviceType":"Contract and claims expert services","provider":{"@id":SITE+"/#organization"},"areaServed":["Middle East","GCC","North Africa","South Asia"],"url":SITE+"/global-experts"}],ge)

# ---------- BUILD YOUR OWN COURSE ----------
by=hero("Instructor Portal","Teach with TCC BSS",
 "Are you a senior contracts, claims or delay professional? Publish your own certified course on the TCC BSS learning platform. You build the course and its final exam — we host it, sell it, examine your students and issue verifiable certificates in your name. You earn 80% of every sale, with no subscription and no fees until you sell. Instructors anywhere in the world are welcome, and you are paid monthly by bank transfer.",("Open the Instructor Portal",PORTAL))
by+="""<section><div class="wrap"><p class="kicker">How it works</p><h2>Three steps from expertise to income</h2><div class="steps">
<article class="card"><div class="num">1</div><h3>You Build the Course</h3><p>Upload your modules as PDF or video, write the final exam (minimum 20 questions), and set your price in QAR.</p></article>
<article class="card"><div class="num">2</div><h3>We Run Everything</h3><p>Hosting, student testing and verifiable TCC BSS certificates issued in your name — reviewed and approved by us before going live.</p></article>
<article class="card"><div class="num">3</div><h3>You Earn Per Sale</h3><p>80% of every sale, whether your course is documents or video. No subscription — you pay nothing until you sell.</p></article>
</div></div></section>
"""+cta_band("Ready to publish?","Create your instructor account, upload your first course and set your price. We review every course before it goes live.","Open the Instructor Portal",PORTAL)
pages["build-your-own-course"]=("Build Your Own Course — Teach with TCC BSS",
 "Discover the Instructor Portal by TCC BSS for teaching opportunities, certified course publishing, and exceptional contract management training.","/build-your-own-course",
 [{"@type":"WebPage","url":SITE+"/build-your-own-course","name":"Teach with TCC BSS","about":{"@id":SITE+"/#organization"}}],by)

# ---------- LEGAL ----------
def legal(h1,sections):
    out=f'<section><div class="wrap"><div class="article"><h1>{h1}</h1>'
    for h,p in sections: out+=f'<h2>{h}</h2><p>{p}</p>'
    return out+'</div></div></section>\n'
M=f'<a href="mailto:{EMAIL}">{EMAIL}</a>'; W='<a href="https://www.tccbss.com">www.tccbss.com</a>'
pp=legal("Privacy Policy",[
("1. Who controls your data",f"TCC Business Support Solution W.L.L. (Commercial Registration 235393), Doha, State of Qatar, is responsible for the personal data collected through {W} and our learning platform at courses.tccbss.com. For any question about your data, contact {M}."),
("2. What we collect and why","We collect your name and email address when you buy a course or contact us, so that we can give you access, issue your certificate and answer your enquiry. We record your progress and test results so that we can award and verify certificates. Instructors also give us their country and bank details so that we can pay them. We collect basic website statistics to understand how the site is used."),
("3. Payment details","We do not collect or store your card details. Card payments are handled directly by a licensed payment provider, which processes your card data under its own security standards. We receive only confirmation that a payment succeeded, together with the amount and a reference."),
("4. Who we share it with","We do not sell your personal data. We share it only where necessary: with our payment provider to take payment, with our hosting and email providers so the platform and notifications work, and with the authorities where the law requires it. Where a course was created by an independent instructor, we tell them that a sale has been made, but we do not give them your contact details."),
("5. How long we keep it, and cookies","We keep your account and course records for as long as your certificate needs to remain verifiable, and we keep payment and payout records for as long as Qatari law requires. Our website uses cookies to keep the site working and to measure visits. You can refuse non-essential cookies in the banner shown on your first visit, or block cookies in your browser."),
("6. Your rights",f"You may ask us for a copy of the personal data we hold about you, ask us to correct it, or ask us to delete it. Write to {M} and we will respond. Please note that deleting your account also removes any certificate issued to you, which will then no longer verify. If we change this policy we will update this page.")])
pages["privacy-policy"]=("Privacy Policy | TCC Business Support Solution - Data Privacy & Cookies",
 "Explore TCC Business Support Solution's privacy policy, detailing user data protection, data privacy practices, and cookies policy for all visitors.","/privacy-policy",[],pp)
tc=legal("Terms &amp; Conditions",[
("1. Who we are",f"TCC Business Support Solution W.L.L. (Commercial Registration 235393), registered in Doha, State of Qatar. Contact: {M}. These terms govern your purchase and use of our services through {W} and our learning platform at courses.tccbss.com. By placing an order you accept these terms."),
("2. What we sell and our prices","We provide contract management consulting services, and online certified training courses delivered through our learning platform. The price of each course is shown on its page on this website and is confirmed to you before you pay. We may change our prices and our range of courses and services at any time; the price shown at the time of your purchase is the price that applies to that purchase. Consulting services are quoted individually."),
("3. Payment","Course fees are payable in full at the time of purchase. We accept Visa and Mastercard, and payments are processed by a licensed payment provider. We do not see or store your card details. Your order is confirmed once payment is authorised."),
("4. How your course is delivered","Courses are delivered online. After payment you receive an access code by email, usually within minutes, which you use at courses.tccbss.com to open your course. Each code admits one person. Course materials are available to study at your own pace. On passing the final test you receive a certificate of completion which can be verified on our website."),
("5. Refunds and cancellations",f"Because course access is issued immediately after payment, we do not offer refunds once your access code has been issued and used. If your access code is not delivered, or the course cannot be accessed because of a fault on our side, we will either resolve the problem or refund you in full. If you have paid but not yet used your access code, contact {M} within 14 days and we will consider a refund. Refunds are made to the original payment card."),
("6. Courses by other instructors, and governing law",f"Some courses on our platform are created by independent instructors. TCC BSS reviews and approves every course before it is offered for sale, hosts it, handles the sale and issues the certificate. The instructor owns their course content. Instructors are bound by our Instructor Agreement. You must not share, copy, resell or publish course materials. We may suspend access where materials are misused. These terms are governed by the laws of the State of Qatar, and the Qatari courts have jurisdiction. Questions: {M}.")])
pages["terms-&-conditions"]=("TCC BSS Terms and Conditions for Consulting and Training",
 "Explore our Terms and Conditions at TCC BSS. We offer contract management consulting and online certified training. Understand our refund policy and more!","/terms-%26-conditions",[],tc)

# ---------- 404 ----------
nf='<section><div class="wrap"><div class="article"><p class="kicker">Error 404</p><h1>Page not found</h1><p class="lead">The page you are looking for does not exist or has moved.</p><div class="actions"><a class="btn" href="/">Go to the homepage</a><a class="btn ghost" href="/#contact">Contact us</a></div></div></div></section>\n'
pages["404"]=("Page not found | TCC Business Support Solution","Page not found.","/404",[],nf)

# ---------- WRITE ----------
urls=[]
for slug,(title,desc,path,ld,body) in pages.items():
    doc=head(title,desc,path,ld)+body+FOOT
    if slug=="404": doc=doc.replace('<link rel="canonical" href="https://tccbss.com/404">','<meta name="robots" content="noindex">')
    with open(os.path.join(ROOT,slug+".html"),"w",encoding="utf-8") as f: f.write(doc)
    if slug!="404": urls.append(path)
with open(os.path.join(ROOT,"sitemap.xml"),"w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for u in urls: f.write(f'  <url><loc>{SITE}{u}</loc><lastmod>{TODAY}</lastmod></url>\n')
    f.write('</urlset>\n')
print("built:",", ".join(s+".html" for s in pages),"+ sitemap.xml")
