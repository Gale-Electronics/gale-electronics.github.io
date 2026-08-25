# Measurely Design System

Measurely is an acoustic-intelligence platform for hi-fi audiophiles and the retailers
who serve them. Brand line: **"The room is the product."** The visual language is
**monochrome plus a single soft teal accent** (`#3A9D93`), **DM Sans** throughout, on
light surfaces. Never introduce other accent colours: teal appears only on
active/selected states and the one primary call-to-action per view.

## Setup — no provider needed

Components are self-contained and need **no context provider or theme wrapper**. The
design system's `styles.css` is enough — it defines every `--mly-*` token on `:root` and
loads DM Sans. Render the library components directly; they already carry the styling.

## Compose components and set props — don't hand-write classes

Style by composing the library components and setting their props. The design language is
carried by the props, not by CSS classes you write yourself:

- **`Button`** — the in-sidebar control button. `active` for the selected state,
  `variant="reset"` for the muted "reset to defaults" treatment.
- **`ActionButton`** — page-level CTA family. `variant="primary" | "secondary" |
  "utility" | "danger"`; add `cta` for the single highest-intent action. One primary per view.
- **`Slider`** — `label`, `value`, `min`/`max`/`step`, and either `unit` or a preformatted
  `display` string for the readout.
- **`ButtonGroup`** — single-select row. `options={[{ key, label }]}` + `value`.
- **`Switch`** — binary `checked`. Renders only the control; pair with a label in a flex row.
- **`Select`** — `options={[{ value, label }]}` + `value`, for longer lists.
- **`Section`** — a labelled control group; `label` is the uppercase heading.
- **`Sidebar`** — the scrolling control panel; fill it with `Section`s.
- **`RoomSection`** / **`SpeakersSection`** — ready-made composed panel sections.

## Your own layout glue → use the tokens

For wrappers and spacing you write yourself, use the CSS variables — never hard-coded
colours or fonts:

- `var(--mly-bg-primary)` `#FFFFFF`, `var(--mly-bg-recessed)` `#F7F7F7`
- `var(--mly-text-primary)` `#1A1A1A`, `var(--mly-text-secondary)` `#666666`
- `var(--mly-border)` `#E8E8E8`, `var(--mly-teal)` `#3A9D93`
- `var(--mly-font-family)` (DM Sans), radii `var(--mly-radius-sm | -md | -lg)`

## Where the truth lives

Read `styles.css` (and its `@import`s) for the full token + component CSS, and each
component's `<Name>.prompt.md` / `<Name>.d.ts` for its exact API.

## Idiomatic example

```tsx
<Sidebar header={<strong style={{ fontFamily: 'var(--mly-font-family)' }}>Room setup</strong>}>
  <RoomSection />
  <Section label="Speakers">
    <ButtonGroup
      value="floorstander"
      options={[
        { key: 'standmount', label: 'Standmount' },
        { key: 'floorstander', label: 'Floorstander' },
        { key: 'monitor', label: 'Monitor' },
      ]}
    />
    <Slider label="Toe-in" min={0} max={30} value={10} unit="deg" />
  </Section>
</Sidebar>
```

# MeasurelyDS (@measurely/design@0.0.0)

This design system is the published @measurely/design React library, bundled as a single
browser global. All 10 components are the real upstream code.

## Where things are

- `_ds_bundle.js` — the whole-DS bundle at the project root; loads every component to `window.MeasurelyDS`. First line is a `/* @ds-bundle: … */` metadata header.
- `styles.css` — the single stylesheet entry: it `@import`s the tokens, fonts, and component styles (`_ds_bundle.css`). Link this one file.
- `components/<group>/<Name>/<Name>.prompt.md` (example JSX + variants), `<Name>.d.ts` (types), `<Name>.html` (variant grid).
- `tokens/*.css` — CSS custom properties, names verbatim from upstream.
- `fonts/` — `@font-face` files + `fonts.css` (when the package ships fonts).

For a specific component, `read_file("components/<group>/<Name>/<Name>.prompt.md")`.

## Loading

Add these two lines to your page once (React must be on the page first):

```html
<link rel="stylesheet" href="styles.css">
<script src="_ds_bundle.js"></script>
```

Components are then available at `window.MeasurelyDS.*`. Mount into a dedicated child node (e.g. `<div id="ds-root">`), not the host page's own React root, so the two trees don't collide:

```jsx
const { ActionButton } = window.MeasurelyDS;
ReactDOM.createRoot(document.getElementById('ds-root')).render(<ActionButton />);
```

## Tokens

54 CSS custom properties from @measurely/design. Names are
preserved verbatim from upstream. They are declared inside `_ds_bundle.css` (this DS ships one compiled stylesheet rather than separate token files).

- **color** (14): `--mly-viewport-text-muted`, `--mly-viewport-text-subtle`, `--mly-viewport-surface`, …
- **typography** (1): `--mly-font-family`
- **radius** (4): `--mly-radius-sm`, `--mly-radius-md`, `--mly-radius-lg`, …
- **shadow** (2): `--mly-shadow-tab`, `--mly-shadow-modal`
- **other** (33): `--mly-viewport-bg`, `--mly-viewport-text`, `--mly-viewport-border`, …

## Components

### general
- `ActionButton` — Page-level action button (.mly-btn).
- `Button` — Sidebar control button (.sbox-btn).
- `ButtonGroup` — Single-select button row (.demo-btn-row of .sbox-btn).
- `RoomSection` — Room Dimensions panel section.
- `Section` — Labelled control group (.demo-section + .demo-group-label).
- `Select` — Dropdown select (select.measurely-select).
- `Sidebar` — Control-panel sidebar (.demo-panel / .mly-panel).
- `Slider` — Measurely control-panel slider (.measurely-slider inside a .demo-field).
- `SpeakersSection` — Speakers panel section.
- `Switch` — Toggle switch (.measurely-switch).
