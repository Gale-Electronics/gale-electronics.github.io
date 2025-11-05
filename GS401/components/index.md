---
title: Components
layout: bare
---

<style>
  :root{
    --paper:#f7f5ee; --card:#fff; --border:#e0dacb; --ink:#111; --muted:#6b6b6b;
    --radius:14px; --shadow:0 6px 24px rgba(0,0,0,.06);
  }
  body{background:var(--paper);color:var(--ink)}
  h2{margin:1rem 0 .6rem}

  .block{
    background:var(--card);border:1px solid var(--border);border-radius:var(--radius);
    padding:14px;margin:0 0 1rem;box-shadow:var(--shadow)
  }
  /* Desktop/tablet: show embedded PDF */
  .pdf-embed{
    display:block;width:100%;
    height:72vh;            /* responsive height, no giant grey gap */
    border:0;border-radius:10px;
  }
  /* Mobile: hide embed, show a tidy card with buttons */
  .pdf-mobile{display:none}

  @media (max-width:720px){
    .pdf-embed{display:none;}     /* hide iframe/object on phones */
    .pdf-mobile{display:block;}   /* show mobile card instead */
  }

  .meta{color:var(--muted);font-size:.95rem;margin:.5rem 0 0}
  .btns a{display:inline-block;margin:.4rem .6rem .2rem 0;text-decoration:none}
</style>

## Speaker Wiring (PDF)
<div class="block">
  <iframe class="pdf-embed" src="/GS401/components/speaker-wiring.pdf#toolbar=0&navpanes=0"></iframe>
  <div class="pdf-mobile">
    <p class="meta">View the PDF full-screen on mobile for best readability.</p>
    <p class="btns">
      <a href="/GS401/components/speaker-wiring.pdf">Open PDF →</a>
      <a href="/GS401/components/speaker-wiring.pdf" download>⤓ Download</a>
    </p>
  </div>
</div>

## Crossover (PDF)
<div class="block">
  <iframe class="pdf-embed" src="/GS401/components/crossover.pdf#toolbar=0&navpanes=0"></iframe>
  <div class="pdf-mobile">
    <p class="meta">Open full-screen on mobile.</p>
    <p class="btns">
      <a href="/GS401/components/crossover.pdf">Open PDF →</a>
      <a href="/GS401/components/crossover.pdf" download>⤓ Download</a>
    </p>
  </div>
</div>

## Capacitor — Shopping List (PDF)
<div class="block">
  <iframe class="pdf-embed" src="/GS401/components/crossover-shopping-list.pdf#toolbar=0&navpanes=0"></iframe>
  <div class="pdf-mobile">
    <p class="meta">Open full-screen on mobile.</p>
    <p class="btns">
      <a href="/GS401/components/crossover-shopping-list.pdf">Open PDF →</a>
      <a href="/GS401/components/crossover-shopping-list.pdf" download>⤓ Download</a>
    </p>
  </div>
</div>

## Stands (PDF)
<div class="block">
  <iframe class="pdf-embed" src="/GS401/components/401-stands.pdf#toolbar=0&navpanes=0"></iframe>
  <div class="pdf-mobile">
    <p class="meta">Open full-screen on mobile.</p>
    <p class="btns">
      <a href="/GS401/components/401-stands.pdf">Open PDF →</a>
      <a href="/GS401/components/401-stands.pdf" download>⤓ Download</a>
    </p>
  </div>
</div>
