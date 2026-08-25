/* @ds-bundle: {"namespace":"MeasurelyDS","components":[{"name":"ActionButton","sourcePath":"components/general/ActionButton/ActionButton.jsx"},{"name":"Button","sourcePath":"components/general/Button/Button.jsx"},{"name":"ButtonGroup","sourcePath":"components/general/ButtonGroup/ButtonGroup.jsx"},{"name":"RoomSection","sourcePath":"components/general/RoomSection/RoomSection.jsx"},{"name":"Section","sourcePath":"components/general/Section/Section.jsx"},{"name":"Select","sourcePath":"components/general/Select/Select.jsx"},{"name":"Sidebar","sourcePath":"components/general/Sidebar/Sidebar.jsx"},{"name":"Slider","sourcePath":"components/general/Slider/Slider.jsx"},{"name":"SpeakersSection","sourcePath":"components/general/SpeakersSection/SpeakersSection.jsx"},{"name":"Switch","sourcePath":"components/general/Switch/Switch.jsx"}],"sourceHashes":{"components/general/ActionButton/ActionButton.jsx":"73c87932c217","components/general/ActionButton/ActionButton.d.ts":"76ffb46141d8","components/general/ActionButton/ActionButton.prompt.md":"d8d7017eb83e","components/general/Button/Button.jsx":"632a00dff238","components/general/Button/Button.d.ts":"8602b88b419c","components/general/Button/Button.prompt.md":"f43065f996ca","components/general/ButtonGroup/ButtonGroup.jsx":"fde2b63a8961","components/general/ButtonGroup/ButtonGroup.d.ts":"665e20850d2b","components/general/ButtonGroup/ButtonGroup.prompt.md":"1ee1c2983ab4","components/general/RoomSection/RoomSection.jsx":"a42853415f5e","components/general/RoomSection/RoomSection.d.ts":"3d83e46c23c6","components/general/RoomSection/RoomSection.prompt.md":"8f0e3366394f","components/general/Section/Section.jsx":"f80e73eb9061","components/general/Section/Section.d.ts":"5081b95cc9db","components/general/Section/Section.prompt.md":"46d3a3c11107","components/general/Select/Select.jsx":"686c7038e960","components/general/Select/Select.d.ts":"aaf36e9bdddd","components/general/Select/Select.prompt.md":"662e2cc69fae","components/general/Sidebar/Sidebar.jsx":"1bd82f5d5374","components/general/Sidebar/Sidebar.d.ts":"4e7a7736649b","components/general/Sidebar/Sidebar.prompt.md":"7375de61779f","components/general/Slider/Slider.jsx":"0a24c8f5f4a6","components/general/Slider/Slider.d.ts":"43a7e0a64d04","components/general/Slider/Slider.prompt.md":"c84f71636dfa","components/general/SpeakersSection/SpeakersSection.jsx":"ef1b74fb2e34","components/general/SpeakersSection/SpeakersSection.d.ts":"7abaca07729a","components/general/SpeakersSection/SpeakersSection.prompt.md":"cdb8940df850","components/general/Switch/Switch.jsx":"057044604124","components/general/Switch/Switch.d.ts":"5c072ffd17d3","components/general/Switch/Switch.prompt.md":"525d9e6e6b57"},"inlinedExternals":[],"builtBy":"cc-design-sync"} */
"use strict";
var MeasurelyDS = (() => {
  var __create = Object.create;
  var __defProp = Object.defineProperty;
  var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
  var __getOwnPropNames = Object.getOwnPropertyNames;
  var __getProtoOf = Object.getPrototypeOf;
  var __hasOwnProp = Object.prototype.hasOwnProperty;
  var __esm = (fn, res, err) => function __init() {
    if (err) throw err[0];
    try {
      return fn && (res = (0, fn[__getOwnPropNames(fn)[0]])(fn = 0)), res;
    } catch (e) {
      throw err = [e], e;
    }
  };
  var __commonJS = (cb, mod) => function __require() {
    try {
      return mod || (0, cb[__getOwnPropNames(cb)[0]])((mod = { exports: {} }).exports, mod), mod.exports;
    } catch (e) {
      throw mod = 0, e;
    }
  };
  var __export = (target, all) => {
    for (var name in all)
      __defProp(target, name, { get: all[name], enumerable: true });
  };
  var __copyProps = (to, from, except, desc) => {
    if (from && typeof from === "object" || typeof from === "function") {
      for (let key of __getOwnPropNames(from))
        if (!__hasOwnProp.call(to, key) && key !== except)
          __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
    }
    return to;
  };
  var __toESM = (mod, isNodeMode, target) => (target = mod != null ? __create(__getProtoOf(mod)) : {}, __copyProps(
    // If the importer is in node compatibility mode or this is not an ESM
    // file that has been converted to a CommonJS file using a Babel-
    // compatible transform (i.e. "__esModule" has not been set), then set
    // "default" to the CommonJS "module.exports" for node compatibility.
    isNodeMode || !mod || !mod.__esModule ? __defProp(target, "default", { value: mod, enumerable: true }) : target,
    mod
  ));
  var __toCommonJS = (mod) => __copyProps(__defProp({}, "__esModule", { value: true }), mod);

  // <define:import.meta.env>
  var init_define_import_meta_env = __esm({
    "<define:import.meta.env>"() {
    }
  });

  // shim:react-shim
  var require_react_shim = __commonJS({
    "shim:react-shim"(exports, module) {
      init_define_import_meta_env();
      var R = window.React;
      function jsx(t, p, k) {
        return R.createElement(t, k === void 0 ? p : Object.assign({ key: k }, p));
      }
      module.exports = R;
      module.exports.jsx = jsx;
      module.exports.jsxs = jsx;
      module.exports.jsxDEV = jsx;
      module.exports.Fragment = R.Fragment;
    }
  });

  // ../../../measurely-ds-shim/dist/index.js
  var index_exports = {};
  __export(index_exports, {
    ActionButton: () => ActionButton,
    Button: () => Button,
    ButtonGroup: () => ButtonGroup,
    RoomSection: () => RoomSection,
    Section: () => Section,
    Select: () => Select,
    Sidebar: () => Sidebar,
    Slider: () => Slider,
    SpeakersSection: () => SpeakersSection,
    Switch: () => Switch
  });
  init_define_import_meta_env();

  // ../../../measurely-ds-shim/dist/Slider.js
  init_define_import_meta_env();
  var import_jsx_runtime = __toESM(require_react_shim(), 1);
  function Slider({ label, value = 50, min = 0, max = 100, step = 1, unit = "", display, disabled, onChange }) {
    const pct = max > min ? (value - min) / (max - min) * 100 : 50;
    const readout = display ?? (unit ? `${value} ${unit}` : String(value));
    return (0, import_jsx_runtime.jsxs)("div", { className: "demo-field", children: [(0, import_jsx_runtime.jsxs)("div", { className: "demo-field-header", children: [label ? (0, import_jsx_runtime.jsx)("span", { className: "demo-field-label", children: label }) : null, (0, import_jsx_runtime.jsx)("span", { className: "demo-field-value", children: readout })] }), (0, import_jsx_runtime.jsx)("input", { type: "range", className: "measurely-slider", min, max, step, value, disabled, "aria-label": label, style: { "--fill": `${pct.toFixed(1)}%` }, onChange: (e) => onChange?.(parseFloat(e.target.value)) })] });
  }

  // ../../../measurely-ds-shim/dist/Button.js
  init_define_import_meta_env();
  var import_jsx_runtime2 = __toESM(require_react_shim(), 1);
  function Button({ children, variant = "default", active, disabled, title, onClick }) {
    const cls = ["sbox-btn"];
    if (variant === "reset")
      cls.push("sbox-reset");
    if (active)
      cls.push("active");
    return (0, import_jsx_runtime2.jsx)("button", { type: "button", className: cls.join(" "), disabled, title, onClick, children });
  }

  // ../../../measurely-ds-shim/dist/ActionButton.js
  init_define_import_meta_env();
  var import_jsx_runtime3 = __toESM(require_react_shim(), 1);
  function ActionButton({ children, variant = "primary", cta, disabled, onClick }) {
    const cls = ["mly-btn", `mly-btn-${variant}`];
    if (cta && variant === "primary")
      cls.push("is-cta");
    return (0, import_jsx_runtime3.jsx)("button", { type: "button", className: cls.join(" "), disabled, onClick, children });
  }

  // ../../../measurely-ds-shim/dist/ButtonGroup.js
  init_define_import_meta_env();
  var import_jsx_runtime4 = __toESM(require_react_shim(), 1);
  function ButtonGroup({ options, value, onChange }) {
    return (0, import_jsx_runtime4.jsx)("div", { className: "demo-btn-row", children: options.map((o) => (0, import_jsx_runtime4.jsx)(Button, { active: o.key === value, title: o.title, onClick: () => onChange?.(o.key), children: o.label }, o.key)) });
  }

  // ../../../measurely-ds-shim/dist/Switch.js
  init_define_import_meta_env();
  var import_jsx_runtime5 = __toESM(require_react_shim(), 1);
  function Switch({ checked, disabled, label, onChange }) {
    return (0, import_jsx_runtime5.jsxs)("label", { className: "measurely-switch", children: [(0, import_jsx_runtime5.jsx)("input", { type: "checkbox", checked: !!checked, disabled, "aria-label": label, onChange: (e) => onChange?.(e.target.checked) }), (0, import_jsx_runtime5.jsx)("span", { className: "slider" })] });
  }

  // ../../../measurely-ds-shim/dist/Select.js
  init_define_import_meta_env();
  var import_jsx_runtime6 = __toESM(require_react_shim(), 1);
  function Select({ options, value, disabled, label, onChange }) {
    return (0, import_jsx_runtime6.jsx)("select", { className: "measurely-select", value, disabled, "aria-label": label, onChange: (e) => onChange?.(e.target.value), children: options.map((o) => (0, import_jsx_runtime6.jsx)("option", { value: o.value, children: o.label }, o.value)) });
  }

  // ../../../measurely-ds-shim/dist/Section.js
  init_define_import_meta_env();
  var import_jsx_runtime7 = __toESM(require_react_shim(), 1);
  function Section({ label, children }) {
    return (0, import_jsx_runtime7.jsxs)("div", { className: "demo-section", children: [label ? (0, import_jsx_runtime7.jsx)("span", { className: "demo-group-label", children: label }) : null, (0, import_jsx_runtime7.jsx)("div", { style: { display: "flex", flexDirection: "column", gap: 12 }, children })] });
  }

  // ../../../measurely-ds-shim/dist/Sidebar.js
  init_define_import_meta_env();
  var import_jsx_runtime8 = __toESM(require_react_shim(), 1);
  function Sidebar({ header, children, width = 340 }) {
    return (0, import_jsx_runtime8.jsxs)("aside", { className: "demo-panel mly-panel", style: {
      width,
      height: "100%",
      display: "flex",
      flexDirection: "column",
      background: "var(--mly-bg-primary)"
    }, children: [header ? (0, import_jsx_runtime8.jsx)("div", { className: "demo-panel-header", children: header }) : null, (0, import_jsx_runtime8.jsx)("div", { className: "demo-panel-body", children })] });
  }

  // ../../../measurely-ds-shim/dist/RoomSection.js
  init_define_import_meta_env();
  var import_jsx_runtime9 = __toESM(require_react_shim(), 1);
  var React = __toESM(require_react_shim(), 1);
  function RoomSection({ width = 4.2, length = 5.5, height = 2.6, onChange }) {
    const [w, setW] = React.useState(width);
    const [l, setL] = React.useState(length);
    const [h, setH] = React.useState(height);
    const emit = (nw, nl, nh) => onChange?.({ width: nw, length: nl, height: nh });
    return (0, import_jsx_runtime9.jsxs)(Section, { label: "Room Dimensions", children: [(0, import_jsx_runtime9.jsx)(Slider, { label: "Room width", min: 2, max: 8, step: 0.1, value: w, display: `${w.toFixed(1)} m`, onChange: (v) => {
      setW(v);
      emit(v, l, h);
    } }), (0, import_jsx_runtime9.jsx)(Slider, { label: "Room length", min: 2.5, max: 10, step: 0.1, value: l, display: `${l.toFixed(1)} m`, onChange: (v) => {
      setL(v);
      emit(w, v, h);
    } }), (0, import_jsx_runtime9.jsx)(Slider, { label: "Room height", min: 2, max: 4, step: 0.05, value: h, display: `${h.toFixed(1)} m`, onChange: (v) => {
      setH(v);
      emit(w, l, v);
    } })] });
  }

  // ../../../measurely-ds-shim/dist/SpeakersSection.js
  init_define_import_meta_env();
  var import_jsx_runtime10 = __toESM(require_react_shim(), 1);
  var React2 = __toESM(require_react_shim(), 1);
  var ARCHETYPES = [
    { key: "standmount", label: "Standmount" },
    { key: "floorstander", label: "Floorstander" },
    { key: "statement", label: "Statement" },
    { key: "panel", label: "Panel" },
    { key: "monitor", label: "Monitor" }
  ];
  function SpeakersSection({ speakerType = "floorstander", spacing = 2.2, distance = 3.2, toeIn = 10, onChange }) {
    const [type, setType] = React2.useState(speakerType);
    const [sp, setSp] = React2.useState(spacing);
    const [dist, setDist] = React2.useState(distance);
    const [toe, setToe] = React2.useState(toeIn);
    const emit = (next) => onChange?.({ speakerType: type, spacing: sp, distance: dist, toeIn: toe, ...next });
    return (0, import_jsx_runtime10.jsxs)(Section, { label: "Speakers", children: [(0, import_jsx_runtime10.jsx)(ButtonGroup, { options: ARCHETYPES, value: type, onChange: (k) => {
      const t = k;
      setType(t);
      emit({ speakerType: t });
    } }), (0, import_jsx_runtime10.jsx)(Slider, { label: "Speaker spacing", min: 1, max: 4, step: 0.1, value: sp, display: `${sp.toFixed(1)} m`, onChange: (v) => {
      setSp(v);
      emit({ spacing: v });
    } }), (0, import_jsx_runtime10.jsx)(Slider, { label: "Listening distance", min: 1, max: 6, step: 0.1, value: dist, display: `${dist.toFixed(1)} m`, onChange: (v) => {
      setDist(v);
      emit({ distance: v });
    } }), (0, import_jsx_runtime10.jsx)(Slider, { label: "Toe-in", min: 0, max: 30, step: 1, value: toe, unit: "deg", onChange: (v) => {
      setToe(v);
      emit({ toeIn: v });
    } })] });
  }
  return __toCommonJS(index_exports);
})();
window.MeasurelyDS=MeasurelyDS.__dsMainNs?Object.assign({},MeasurelyDS,MeasurelyDS.__dsMainNs,{__dsMainNs:undefined}):MeasurelyDS;
