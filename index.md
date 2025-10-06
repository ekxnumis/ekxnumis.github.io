---
title: Ekxnumis
subtitle: Exploring the World of British Coins
layout: default
show_sidebar: False
---

<main id="main-content" class="container is-max-widescreen">

    <section class="hero is-medium has-background-dark py-6 mb-6">
        <div class="hero-body has-text-centered">
            <p class="title is-1 has-text-white mb-4">
                Ekxnumis: The Collector's Compass 🧭
            </p>
            <p class="subtitle is-4 has-text-grey-light">
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

<!-- Feature Columns -->
    <div class="columns is-multiline is-variable is-6">

<!-- Grading Standards -->
        <div class="column is-half-desktop is-full-tablet">
            <div class="box has-background-darker p-5 has-text-light" style="height: 100%; border-left: 5px solid #00d1b2;">
                <h2 class="title is-3 has-text-primary-light mb-4">
                    Coin Grading Standards 🔍
                </h2>
                <p class="mb-4 is-size-5 has-text-grey-light">
                    Master the **Sheldon Scale** and descriptive grading systems. Use our guides to accurately assess wear, luster, and strike quality across all grades, from **Poor (P-1) to Mint State (MS-70)**.
                </p>
                <ul class="mb-4" style="list-style: none; margin-left: 0;">
                    <li><span class="icon has-text-primary"><i class="fas fa-check"></i></span> Learn the MS-70 criteria.</li>
                    <li><span class="icon has-text-primary"><i class="fas fa-check"></i></span> Compare CGS/UK and US standards.</li>
                </ul>
                <a href="/grading/" class="button is-primary is-fullwidth is-outlined">
                    View Grading Guides
                </a>
            </div>
        </div>
<!-- Variety & Blog -->
        <div class="column is-half-desktop is-full-tablet">
            <div class="box has-background-darker p-5 has-text-light" style="height: 100%; border-left: 5px solid #2596be;">
                <h2 class="title is-3 has-text-link-light mb-4">
                    Variety & Numismatic Blogs 📜
                </h2>
                <p class="mb-4 is-size-5 has-text-grey-light">
                    Dive into specific coin **varieties**, die states, mint marks, and historical anomalies. Our in-depth articles provide the research needed to identify the rarest and most unique pieces.
                </p>
                <ul class="mb-4" style="list-style: none; margin-left: 0;">
                    <li><span class="icon has-text-link"><i class="fas fa-check"></i></span> Explore articles by Monarch.</li>
                    <li><span class="icon has-text-link"><i class="fas fa-check"></i></span> Discover unique coin errors.</li>
                </ul>
                <a href="/blog/" class="button is-link is-fullwidth is-outlined">
                    Read Variety Articles
                </a>
            </div>
        </div>

<!-- Divider -->
        <div class="column is-full">
            <hr style="border: 1px solid #4a4a4a; margin: 0.5rem 0 2rem 0;">
        </div>

    </div>

    <section class="mb-6 py-5">
    <h3 class="title is-3 has-text-white has-text-centered mb-5">
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
                 class="box has-background-darker p-4 has-text-centered is-clickable-card"
                 style="height: 100%; transition: transform 0.2s, box-shadow 0.2s; border-top: 3px solid #2596be;">
                  
                  <p class="title is-5 has-text-warning-light mb-1">
                      {{ monarch }}
                  </p>
                  <p class="subtitle is-7 has-text-grey-light">
                      View Catalogue
                  </p>
              </a>
          </div>
        {% endfor %}

    </div>
</section>

<style>
/* Makes the entire card lift slightly on hover */
.is-clickable-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.4);
}
.is-clickable-card {
    text-decoration: none !important;
}
</style>

<!-- Divider -->
        <div class="column is-full">
            <hr style="border: 1px solid #4a4a4a; margin: 0.5rem 0 2rem 0;">
        </div>

 <!-- Conversion Tool -->
    <section class="mb-6">
        <div class="box has-background-darker p-5 has-text-light has-text-centered">
            <h3 class="title is-4 has-text-warning-light">
                Need to Convert a Grade?
            </h3>
            <p class="subtitle is-6 has-text-grey-light mb-4">
                Instantly compare numerical (Sheldon) grades to descriptive (UK/CGS) grades using our comprehensive comparison chart.
            </p>
            <a href="/grading/system-comparison.html" class="button is-warning is-medium is-outlined">
                <span class="icon"><i class="fas fa-exchange-alt"></i></span>
                <span>See Comparison Chart</span>
            </a>
        </div>
    </section>

</main>