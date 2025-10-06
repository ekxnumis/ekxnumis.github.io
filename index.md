---
title: Ekxnumis
subtitle: Exploring the World of British Coins
layout: default
show_sidebar: False
---

<main id="main-content" class="container is-max-widescreen">

    <section class="hero is-medium main-hero py-6 mb-6">
        <div class="hero-body has-text-centered">
            <p class="title is-1 hero-title mb-4">
                Ekxnumis: The Collector's Compass 🧭
            </p>
            <p class="subtitle is-4 hero-subtitle">
                Your definitive reference for British coin grading, varieties, and numismatic research.
            </p>
            <div class="buttons is-centered mt-5">
                <a href="/grading/" class="button is-primary is-large is-outlined">
                    <span class="icon"><i class="fas fa-search-dollar"></i></span>
                    <span>Start Grading</span>
                </a>
                <a href="/blog/" class="button is-link is-large is-outlined">
                    <span class="icon"><i class="fas fa-scroll"></i></span>
                    <span>Explore Varieties</span>
                </a>
            </div>
        </div>
    </section>

<div class="columns is-multiline is-variable is-6">

<div class="column is-half-desktop is-full-tablet">
            <div class="box feature-box p-5" style="height: 100%; border-left: 5px solid #00d1b2;">
                <h2 class="title is-3 box-title mb-4">
                    Coin Grading Standards 🔍
                </h2>
                <p class="mb-4 is-size-5 box-text">
                    Master the **Sheldon Scale** and descriptive grading systems. Use our guides to accurately assess wear, luster, and strike quality across all grades, from **Poor (P-1) to Mint State (MS-70)**.
                </p>
                <ul class="mb-4" style="list-style: none; margin-left: 0;">
                    <li><span class="icon has-text-primary"><i class="fas fa-check"></i></span> Learn the MS-70 criteria.</li>
                    <li><span class="icon has-text-primary"><i class="fas fa-check"></i></span> Compare CGS/UK and US standards.</li>
                </ul>
                <a href="/grading/" class="button is-primary is-fullwidth is-outlined">
                    <strong>View Grading Guides</strong>
                </a>
            </div>
        </div>
<div class="column is-half-desktop is-full-tablet">
            <div class="box feature-box p-5" style="height: 100%; border-left: 5px solid #2596be;">
                <h2 class="title is-3 box-title mb-4">
                    Variety & Numismatic Blogs 📜
                </h2>
                <p class="mb-4 is-size-5 box-text">
                    Dive into specific coin **varieties**, die states, mint marks, and historical anomalies. Our in-depth articles provide the research needed to identify the rarest and most unique pieces.
                </p>
                <ul class="mb-4" style="list-style: none; margin-left: 0;">
                    <li><span class="icon has-text-link"><i class="fas fa-check"></i></span> Explore articles by Monarch.</li>
                    <li><span class="icon has-text-link"><i class="fas fa-check"></i></span> Discover unique coin errors.</li>
                </ul>
                <a href="/blog/" class="button is-link is-fullwidth is-outlined">
                    <strong>Read Variety Articles</strong>
                </a>
            </div>
        </div>

<div class="column is-full">
            <hr class="divider-hr">
        </div>

    </div>

    <section class="mb-6 py-5">
    <h3 class="title is-3 section-title has-text-centered mb-5">
        Collector's Reference - Explore Coin Varieties by Monarch 👑
    </h3>

    <div class="columns is-multiline is-variable is-3 is-mobile">

        {% assign monarch_links = 
            "George III:/monarchs/GeorgeIII.html,
             George IV:/monarchs/GeorgeIV.html,
             William IV:/monarchs/WilliamIV.html,
             Victoria:/monarchs/Vitoria.html,
             Edward VII:/monarchs/EdwardVII.html,
             George V:/monarchs/GeorgeV.html,
             George VI:/monarchs/GeorgeVI.html,
             Elizabeth II:/monarchs/ElizabethII.html" 
            | split: "," %}

        {% for item in monarch_links %}
          {% assign parts = item | split: ":" %}
          {% assign monarch = parts[0] %}
          {% assign link = parts[1] %}

          <div class="column is-half-mobile is-one-quarter-tablet is-one-fifth-desktop">
             <a href="{{ link | strip }}" 
                  class="box monarch-card p-4 has-text-centered is-clickable-card"
                  style="height: 100%; transition: transform 0.2s, box-shadow 0.2s; border-top: 3px solid #2596be;">
                  
                  <p class="title is-5 monarch-title mb-1">
                      {{ monarch }}
                  </p>
                  <p class="subtitle is-7 box-text">
                      View Catalogue
                  </p>
              </a>
          </div>
        {% endfor %}

    </div>
</section>

<style>
:root {
    /* --- DARK MODE (DEFAULT) --- */
    --main-bg: #1c1c1c;
    --hero-bg: #2a2a2a;
    --box-bg: #242424;
    --main-text: #ffffff;
    --sub-text: #b5b5b5;
    --title-accent: #07f3f3ff; /* Light warning color */
    --divider-color: #4a4a4a;
    --box-title-primary: #85d9ee; /* Light primary/link color */
}

@media (prefers-color-scheme: light) {
    :root {
        /* --- LIGHT MODE OVERRIDES (HIGH CONTRAST) --- */
        --main-bg: #f5f5f5;
        --hero-bg: #e0e0e0;
        --box-bg: #ffffff;
        --main-text: #363636;
        --sub-text: #4a4a4a;
        --title-accent: #000000; /* Use black for max contrast on Monarch cards */
        --divider-color: #dbdbdb;
        --box-title-primary: #00d1b2; /* Bulma primary */
    }
    
    /* Add subtle shadow to boxes in light mode for definition */
    .feature-box, .monarch-card, .conversion-box {
        box-shadow: 0 2px 3px rgba(10, 10, 10, 0.1), 0 0 0 1px rgba(10, 10, 10, 0.1);
    }
    /* Remove shadow from the hero section which is usually flat */
    .main-hero {
        box-shadow: none !important;
    }
}

/* ----------------------------------------------------------------
   APPLYING THE CSS VARIABLES TO THE PAGE ELEMENTS 
   ---------------------------------------------------------------- */

/* Body/Main Content Background */
body {
    background-color: var(--main-bg);
}

/* Hero Section */
.main-hero {
    background-color: var(--hero-bg) !important;
}
.hero-title {
    color: var(--main-text) !important;
}
.hero-subtitle {
    color: var(--sub-text) !important;
}

/* Feature Boxes & Conversion Box */
.feature-box, .monarch-card, .conversion-box {
    background-color: var(--box-bg) !important;
    color: var(--sub-text) !important;
    /* Ensure no text-light/dark classes conflict */
    padding: 20px; /* Reset Bulma padding */
}

.box-title {
    /* Uses the accent color for Grading/Variety titles, but falls back to dark text in light mode for the Monarch/Conversion titles */
    color: var(--box-title-primary) !important;
}
.box-text {
    color: var(--sub-text) !important;
}


/* Monarch Card Titles (Need High Contrast) */
.monarch-card .monarch-title {
    /* This title needs to be high contrast in light mode (black) 
       and light in dark mode, so we use the title-accent variable. */
    color: var(--title-accent) !important;
}

/* General Section Titles */
.section-title {
    color: var(--main-text) !important;
}

/* Dividers */
.divider-hr {
    border: 1px solid var(--divider-color) !important; 
    margin: 0.5rem 0 2rem 0 !important;
}

/* Hover effect from original code */
.is-clickable-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.4);
}
.is-clickable-card {
    text-decoration: none !important;
}
</style>

<div class="column is-full">
            <hr class="divider-hr">
        </div>

 <section class="mb-6">
        <div class="box conversion-box p-5 has-text-centered">
            <h3 class="title is-4 section-title">
                Need to Convert a Grade?
            </h3>
            <p class="subtitle is-6 box-text mb-4">
                Instantly compare numerical (Sheldon) grades to descriptive (UK/CGS) grades using our comprehensive comparison chart.
            </p>
            <a href="/grading/system-comparison.html" class="button is-warning is-medium is-outlined">
                <span class="icon"><i class="fas fa-exchange-alt"></i></span>
                <span>See Comparison Chart</span>
            </a>
        </div>
    </section>

</main>