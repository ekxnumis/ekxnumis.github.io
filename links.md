---
layout: default
title: Links 
permalink: /links/
---

<main id="main-content" class="container">
    <h1 class="title is-2 page-title" style="margin-bottom: 2rem;">
        <span class="icon is-medium"><i class="fas fa-link"></i></span>
        Numismatic Links & Resources
    </h1>
    <p class="subtitle is-6 page-subtitle">
        Curated articles and videos on coin collecting and numismatics.
    </p>

<hr class="divider-hr" style="margin: 2rem 0;">
    
  <!-- Accordion Section -->
  <div class="links-toc" style="max-width: 800px; margin-top: 2rem;">

    <!-- Important Reference Articles -->
    <details class="mb-4 box accordion-box" open style="padding: 0;">
        <summary class="p-4 is-size-5 accordion-summary has-text-weight-bold" style="cursor: pointer; list-style-type: none;">
            <div class="is-flex is-justify-content-space-between is-align-items-center">
            <span class="is-flex is-align-items-center">
                <span class="icon is-small mr-2 has-text-warning"><i class="fas fa-book"></i></span>
                Important Reference Articles
                </span>
            <span class="icon is-small chevron-indicator"><i class="fas fa-chevron-right"></i></span>
            </div>
        </summary>
            
        <div class="content p-4 pt-0">
            <ul class="accordion-content" style="list-style-type: square; margin-left: 1.5rem;">
                <li><a href="https://britnumsoc.blog/2022/11/04/an-unrecorded-george-ii-shilling-overdate-1747-6-gary-oddie/" 
                    class="accordion-link has-text-weight-medium">An Unrecorded George II Shilling Overdate – 1747/6 – Gary Oddie</a></li>
                <li><a href="/blog/" 
                    class="accordion-link has-text-weight-medium">My Blogs Section</a></li>
            </ul>
        </div>
        </details>

    <!-- My YouTube Videos -->
    <details class="mb-4 box accordion-box" style="padding: 0;">
        <summary class="p-4 is-size-5 accordion-summary has-text-weight-bold" style="cursor: pointer; list-style-type: none;">
            <div class="is-flex is-justify-content-space-between is-align-items-center">
                <span class="is-flex is-align-items-center">
                    <span class="icon is-small mr-2 has-text-warning"><i class="fab fa-youtube"></i></span>
                    My YouTube Videos
                </span>
                <span class="icon is-small chevron-indicator"><i class="fas fa-chevron-right"></i></span>
            </div>
        </summary>
            
            <div class="content p-4 pt-0">
                <ul class="accordion-content" style="list-style-type: square; margin-left: 1.5rem;">
                    <li><a href="https://www.youtube.com/watch?v=OOs9GW4E-wk" 
                        class="accordion-link has-text-weight-medium">1787 Shilling study</a></li>
                    <li><a href="https://www.youtube.com/watch?v=example2" 
                        class="accordion-link has-text-weight-medium">Rare Coins Explained</a></li>
                </ul>
            </div>
        </details>

    </div>

</main>

<style>
:root {
    --main-bg: #1c1c1c;
    --box-bg: #242424;
    --main-text: #ffffff;
    --sub-text: #b5b5b5;
    --section-title-color: #85d9ee;
    --accordion-summary-text: #00d1b2;
    --link-text: #85d9ee;
    --divider-color: #2596be;
    --box-border-color: #444;
}

@media (prefers-color-scheme: light) {
    :root {
        --main-bg: #f5f5f5;
        --box-bg: #ffffff;
        --main-text: #363636;
        --sub-text: #4a4a4a;
        --section-title-color: #00d1b2;
        --accordion-summary-text: #000000;
        --link-text: #00d1b2;
        --divider-color: #dbdbdb;
        --box-border-color: #dbdbdb;
    }
    .accordion-box {
        box-shadow: 0 2px 3px rgba(10, 10, 10, 0.1), 0 0 0 1px rgba(10, 10, 10, 0.1) !important;
    }
}

body { background-color: var(--main-bg); }
.page-title { color: var(--main-text) !important; }
.page-subtitle { color: var(--sub-text) !important; }
.section-title { color: var(--section-title-color) !important; }
.divider-hr { border: 1.5px solid var(--divider-color) !important; }
.accordion-box { background-color: var(--box-bg) !important; border: 1px solid var(--box-border-color) !important; }
.accordion-summary { color: var(--accordion-summary-text) !important; }
.accordion-link { color: var(--link-text) !important; }
.blog-toc a:hover { text-decoration: underline !important; }
.blog-toc summary { list-style: none; }
.chevron-indicator { transition: transform 0.2s ease-in-out; }
.accordion-box[open] .chevron-indicator { transform: rotate(90deg); }
.blog-toc details[open] summary { border-bottom: 1px solid var(--box-border-color); }
</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
  const accordions = document.querySelectorAll('.accordion-box');

  accordions.forEach((accordion) => {
    const summary = accordion.querySelector('summary');

    summary.addEventListener('click', () => {
      // Close all other accordions
      accordions.forEach((other) => {
        if (other !== accordion) other.removeAttribute('open');
      });
    });
  });
});
</script>