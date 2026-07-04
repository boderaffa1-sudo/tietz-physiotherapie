#!/usr/bin/env python3
"""Generate individual service detail pages from a shared template."""

TEMPLATE = """<!doctype html>
<html lang="de">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title} — Praxis Tietz</title>
<meta name="description" content="{meta_desc}" />
<link rel="icon" href="../img/favicon.svg" type="image/svg+xml" />
<link rel="preconnect" href="https://api.fontshare.com" />
<link href="https://api.fontshare.com/v2/css?f[]=switzer@400,500,600,700&display=swap" rel="stylesheet" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400..600;1,9..144,400..600&family=Work+Sans:wght@400;500;600;700&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="../css/tokens.css" />
<link rel="stylesheet" href="../css/base.css" />
<link rel="stylesheet" href="../css/style.css" />
</head>
<body>

<svg width="0" height="0" style="position:absolute">
  <symbol id="logo-mark" viewBox="0 0 48 48">
    <path d="M24 4C15 10 7 14 7 24c0 9.4 7.6 17 17 17s17-7.6 17-17c0-10-8-14-17-20Z" fill="none" stroke="currentColor" stroke-width="1.6"/>
    <path d="M14 25c2-4 4-4 6 0s4 4 6 0 4-4 6 0 4 4 6 0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
  </symbol>
</svg>

<header class="site-header" id="siteHeader">
  <div class="container header-inner">
    <a href="../index.html" class="logo">
      <svg aria-hidden="true"><use href="#logo-mark"/></svg>
      <span class="logo-text">Praxis Tietz<small>Physiotherapie &amp; Osteopathie</small></span>
    </a>
    <nav class="main-nav" aria-label="Hauptnavigation">
      <ul>
        <li><a href="../leistungen.html">Leistungen</a></li>
        <li><a href="../ueber-uns.html">Über uns</a></li>
        <li><a href="../index.html#ablauf">Ablauf</a></li>
        <li><a href="../kontakt.html">Kontakt</a></li>
      </ul>
    </nav>
    <div class="header-actions">
      <button class="theme-toggle" data-theme-toggle aria-label="Dunkelmodus umschalten">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
      </button>
      <a href="tel:+4930892902 7" class="btn btn-ghost">030 892 90 27</a>
      <a href="../kontakt.html#termin" class="btn btn-primary">Termin anfragen</a>
    </div>
    <button class="nav-toggle" id="navToggle" aria-label="Menü öffnen">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
    </button>
  </div>
</header>

<div class="mobile-nav" id="mobileNav">
  <div class="mobile-nav-header">
    <a href="../index.html" class="logo"><svg aria-hidden="true"><use href="#logo-mark"/></svg><span class="logo-text">Praxis Tietz</span></a>
    <button id="navClose" aria-label="Menü schließen" style="width:40px;height:40px;color:var(--color-text)">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
    </button>
  </div>
  <ul>
    <li><a href="../leistungen.html">Leistungen</a></li>
    <li><a href="../ueber-uns.html">Über uns</a></li>
    <li><a href="../index.html#ablauf">Ablauf</a></li>
    <li><a href="../kontakt.html">Kontakt</a></li>
  </ul>
  <div class="mobile-nav-ctas">
    <a href="tel:+4930892902 7" class="btn btn-ghost btn-lg">030 892 90 27 anrufen</a>
    <a href="../kontakt.html#termin" class="btn btn-primary btn-lg">Termin anfragen</a>
  </div>
</div>

<main>
  <section class="page-hero">
    <div class="container">
      <p class="breadcrumb"><a href="../leistungen.html">Leistungen</a> <span>/</span> <span>{title}</span></p>
      <p class="eyebrow">{tag}</p>
      <h1>{title}</h1>
      <p>{intro}</p>
    </div>
  </section>

  <section class="container">
    <div class="detail-grid{reverse_class}">
      <div class="detail-visual" data-reveal>
        <img src="../img/{image}" alt="{image_alt}" />
      </div>
      <div class="detail-content" data-reveal>
        <h2>Was Sie erwarten können</h2>
        {paragraphs}
        <ul>
          {bullets}
        </ul>
      </div>
    </div>
  </section>

  <section class="container">
    <div class="booking" style="text-align:center; padding: clamp(var(--space-12), 6vw, var(--space-16)) var(--space-8)">
      <h2 class="section-title" style="margin-inline:auto">Interesse an {title_lower}?</h2>
      <p class="section-lead" style="margin-inline:auto; margin-bottom:var(--space-6)">Rufen Sie uns an oder schreiben Sie uns — wir beraten Sie gern, ob diese Behandlung zu Ihrem Anliegen passt.</p>
      <a href="../kontakt.html#termin" class="btn btn-primary btn-lg">Termin anfragen</a>
    </div>
  </section>
</main>

<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="../index.html" class="logo"><svg aria-hidden="true"><use href="#logo-mark"/></svg><span class="logo-text">Praxis Tietz</span></a>
        <p>Physiotherapie &amp; Osteopathie in Berlin-Halensee. Ganzheitlich, persönlich, mit Zeit für Sie.</p>
      </div>
      <div class="footer-col">
        <h4>Praxis</h4>
        <ul>
          <li><a href="../leistungen.html">Leistungen</a></li>
          <li><a href="../ueber-uns.html">Über uns</a></li>
          <li><a href="../index.html#ablauf">Ablauf</a></li>
          <li><a href="../index.html#faq">Häufige Fragen</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Kontakt</h4>
        <ul>
          <li><a href="tel:+4930892902 7">030 892 90 27</a></li>
          <li><a href="mailto:TeamTietz@mailbox.org">TeamTietz@mailbox.org</a></li>
          <li><span>Lützenstraße 13, 10711 Berlin</span></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Öffnungszeiten</h4>
        <ul>
          <li><span>Mo–Do: 8–19 Uhr</span></li>
          <li><span>Fr: 9–17 Uhr</span></li>
          <li><span>sowie nach Vereinbarung</span></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 Praxis Tietz — Josch Tietz, Physiotherapeut &amp; Heilpraktiker</span>
      <ul>
        <li><a href="../impressum.html">Impressum</a></li>
        <li><a href="../datenschutz.html">Datenschutz</a></li>
      </ul>
    </div>
  </div>
</footer>

<script src="../js/main.js"></script>
</body>
</html>
"""

CHECK_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 12l2 2 4-4"/><circle cx="12" cy="12" r="10"/></svg>'

pages = [
    {
        "slug": "osteopathie",
        "title": "Osteopathie",
        "tag": "Selbstzahlerleistung",
        "meta_desc": "Osteopathie in der Praxis Tietz Berlin-Halensee: ganzheitliche, manuelle Behandlung für mehr Beweglichkeit und Gleichgewicht im Körper.",
        "intro": "Ein ganzheitliches, medizinisches Verfahren, das auf genauer Kenntnis von Anatomie und Physiologie beruht: Bewegung ist Leben — der Körper ist dann gesund, wenn sich alle Strukturen frei bewegen können.",
        "image": "balance-stones.png",
        "image_alt": "Balancierte Steine als Sinnbild für osteopathisches Gleichgewicht",
        "reverse": False,
        "paragraphs": [
            "In der Osteopathie lösen wir Festigkeiten und Bewegungseinschränkungen im Gewebe, damit Ihr Körper wieder in ein stimmiges Gleichgewicht findet — und die eigenen Selbstheilungskräfte wirken können.",
            "Wir arbeiten mit sehr sanften bis festeren Techniken, je nachdem, was Ihr Körper und Ihre Situation gerade brauchen. Die Behandlung berücksichtigt drei Ebenen: cranio-sakral (Nerven, Schädel, Wirbelsäule), viszeral (Organe und ihre Verbindungen) und parietal (Knochen, Gelenke, Muskeln).",
        ],
        "bullets": [
            "Ganzheitlicher Blick auf Körper und Beschwerden",
            "Sanfte bis feste Techniken, individuell angepasst",
            "Als Selbstzahlerleistung buchbar, unabhängig vom Rezept",
        ],
    },
    {
        "slug": "krankengymnastik",
        "title": "Krankengymnastik",
        "tag": "Kassenleistung",
        "meta_desc": "Krankengymnastik / Physiotherapie in Berlin-Halensee: ärztlich verordnete Bewegungstherapie bei orthopädischen, neurologischen und inneren Beschwerden.",
        "intro": "Physiotherapie ist ärztlich verordnete Bewegungstherapie — eine der ältesten Heilmethoden überhaupt, heute wissenschaftlich fundiert und individuell auf Ihre Beschwerden abgestimmt.",
        "image": "hero-treatment.png",
        "image_alt": "Sanfte Bewegungstherapie in ruhiger Praxisatmosphäre",
        "reverse": True,
        "paragraphs": [
            "Krankengymnastik orientiert sich an Ihrer Diagnose und Ihrem Körper. Wir setzen spezielle Behandlungstechniken zur Therapie, Rehabilitation und Vorbeugung ein — informieren und schulen Sie dabei, damit Sie auch selbst aktiv zu Ihrer Gesundheit beitragen können.",
            "Anwendungsbereiche reichen von rheumatischen und orthopädischen Erkrankungen über Erkrankungen innerer Organe bis zu neurologischen Beschwerden wie nach einem Schlaganfall.",
        ],
        "bullets": [
            "Auf ärztliche Verordnung von der Krankenkasse übernommen",
            "Individuelle Übungsauswahl je nach Diagnose",
            "Begleitend zu Reha, Prävention oder akuten Beschwerden",
        ],
    },
    {
        "slug": "manuelle-therapie",
        "title": "Manuelle Therapie",
        "tag": "Kassenleistung",
        "meta_desc": "Manuelle Therapie in Berlin-Halensee: gezielte Handgriffe bei Funktionsstörungen an Gelenken, Muskeln und Nerven.",
        "intro": "Wörtlich „Heilbehandlung mit den Händen“ — ein offizieller Bestandteil der klassischen Physiotherapie zur gezielten Behandlung von Funktionsstörungen des Bewegungssystems.",
        "image": "hands-care.png",
        "image_alt": "Zwei Hände in behutsamer Berührung",
        "reverse": False,
        "paragraphs": [
            "Manuelle Therapie kombiniert präzise Untersuchung mit gezielten Behandlungstechniken: Schmerzlinderung durch Mobilisierung und Beeinflussung der Gewebebeschaffenheit, ergänzt durch Beratung und Instruktion.",
            "Wir betrachten dabei nicht nur das betroffene Gelenk, sondern Ihre gesamte Lebenssituation — für eine wirklich ganzheitliche Sicht auf Ihre Beschwerden am Bewegungsapparat.",
        ],
        "bullets": [
            "Nur nach zertifizierter Zusatzausbildung durchgeführt",
            "Bei allen reversiblen Dysfunktionen am Bewegungsapparat",
            "Von gesetzlichen Krankenkassen übernommen",
        ],
    },
    {
        "slug": "craniosakrale-therapie",
        "title": "Cranio-Sakrale Therapie",
        "tag": "Selbstzahlerleistung",
        "meta_desc": "Cranio-Sakrale Therapie in Berlin-Halensee: sehr sanfte manuelle Behandlung über den craniosakralen Rhythmus, auch als Ausgleich bei Erschöpfung.",
        "intro": "Eine sanfte und zugleich wirksame manuelle Behandlungsform, die über den feinen Rhythmus zwischen Schädel und Kreuzbein arbeitet — manche nennen ihn den „dritten Puls“, neben Atem und Herzschlag.",
        "image": "wellness-still.png",
        "image_alt": "Ruhiges Stillleben als Sinnbild für die sanfte Cranio-Sakrale Therapie",
        "reverse": True,
        "paragraphs": [
            "Durch die behutsame Harmonisierung des craniosakralen Rhythmus können Spannungen abgebaut, Schmerzen gelindert und Blockaden gelöst werden. Ein Heilungsprozess wird so eingeleitet oder wirkungsvoll unterstützt.",
            "Da die Behandlung am zentralen Nervensystem ansetzt, eignet sie sich besonders auch als Ausgleich bei Erschöpfung, Anspannung oder Schlafstörungen — gut kombinierbar mit anderen Verfahren.",
        ],
        "bullets": [
            "Sehr sanfte, kaum spürbare Technik",
            "Unterstützend bei Erschöpfung und Schlafstörungen",
            "Gut kombinierbar mit Osteopathie oder Manueller Therapie",
        ],
    },
    {
        "slug": "tre",
        "title": "TRE — Trauma-Lösungsübungen",
        "tag": "Selbstzahlerleistung",
        "meta_desc": "TRE (Tension Releasing Exercises) in Berlin-Halensee: Übungen nach David Berceli zur sanften Lösung von Stress- und Spannungsmustern.",
        "intro": "„Die Weisheit Ihres Körpers nutzen.“ TRE steht für Tension &amp; Trauma Releasing Exercises — Übungen, die helfen, alte Verspannungen zu lösen und aktuellen Stress schneller zu regulieren.",
        "image": "practice-room.png",
        "image_alt": "Ruhiger Raum für achtsame Körperarbeit",
        "reverse": False,
        "paragraphs": [
            "Ein Trauma ist ein starker Stressor, der körperlich oder seelisch nicht vollständig verarbeitet werden konnte — Spannungen nisten sich im Körper ein. In einer TRE-Sitzung regen wir zunächst die Stressmuskulatur sanft an und ermüden sie leicht.",
            "Anschließend aktivieren wir den körpereigenen Schüttel- und Korrekturmechanismus, der die Stressspannungen löst. Die Intensität der Arbeit bestimmen Sie dabei immer selbst.",
            "Neben Einzelsitzungen bieten wir Einführungs-Tagesworkshops und fortlaufende Gruppen an — aktuelle Termine finden Sie über core-evolving.com.",
        ],
        "bullets": [
            "Sanfte, körpereigene Regulation von Stress und Anspannung",
            "Die Intensität bestimmen Sie jederzeit selbst",
            "Einzeln oder in begleiteten Gruppen/Workshops möglich",
        ],
    },
    {
        "slug": "physiosoul",
        "title": "PhysioSoul-Körperarbeit",
        "tag": "Selbstzahlerleistung",
        "meta_desc": "PhysioSoul-Körperarbeit in Berlin-Halensee: verbindet körperliche, geistige und seelische Anteile im Gespräch und in der Körperarbeit.",
        "intro": "Eine Methode, die körperliche, geistige und seelische Anteile des Menschen miteinander verbindet — für mehr Bewusstheit über gestörte Zusammenhänge und mehr Lebensqualität.",
        "image": "consultation.png",
        "image_alt": "Ruhiges, persönliches Gespräch in warmer Atmosphäre",
        "reverse": True,
        "paragraphs": [
            "Wir befinden uns oft in einer künstlichen Trennung von Körper, Geist und Seele, die ein erfülltes Lebensgefühl erschwert. Grundlage der PhysioSoul-Arbeit können körperliche Beschwerden ebenso sein wie seelische oder auch spirituelle Themen.",
            "Im Gespräch ermitteln wir gemeinsam Ihr Anliegen und betrachten Ihre Körperhaltung als Ausdruck individueller Bewegungs- und Haltungsmuster. So kann das im Gespräch gefundene Thema in der Körperarbeit tiefer erlebt und verankert werden.",
        ],
        "bullets": [
            "Verbindet Gespräch und körperorientierte Arbeit",
            "Individuell auf Ihr Anliegen zugeschnitten",
            "Für körperliche, seelische und persönliche Entwicklungsthemen",
        ],
    },
]

import os

out_dir = os.path.join(os.path.dirname(__file__), "leistungen")
os.makedirs(out_dir, exist_ok=True)

for p in pages:
    paragraphs_html = "\n        ".join(f"<p>{t}</p>" for t in p["paragraphs"])
    bullets_html = "\n          ".join(f'<li>{CHECK_SVG}<span>{b}</span></li>' for b in p["bullets"])
    html = TEMPLATE.format(
        title=p["title"],
        title_lower=p["title"].lower(),
        tag=p["tag"],
        meta_desc=p["meta_desc"],
        intro=p["intro"],
        image=p["image"],
        image_alt=p["image_alt"],
        reverse_class=" reverse" if p["reverse"] else "",
        paragraphs=paragraphs_html,
        bullets=bullets_html,
    )
    path = os.path.join(out_dir, f"{p['slug']}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Wrote {path}")
