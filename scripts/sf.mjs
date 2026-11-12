// sf.mjs — wrapper Node pour single-file-cli.
// Polyfill les globals Web API manquants sous Node.js, puis délègue à
// single-file-node.js (mêmes arguments en ligne de commande).

if (typeof globalThis.CloseEvent === "undefined") {
  globalThis.CloseEvent = class CloseEvent extends Event {
    constructor(type, init = {}) {
      super(type, init);
      this.code = init.code ?? 1000;
      this.reason = init.reason ?? "";
      this.wasClean = init.wasClean ?? true;
    }
  };
}
if (typeof globalThis.ErrorEvent === "undefined") {
  globalThis.ErrorEvent = class ErrorEvent extends Event {
    constructor(type, init = {}) {
      super(type, init);
      this.error = init.error;
      this.message = init.message ?? "";
    }
  };
}

await import("../node_modules/single-file-cli/single-file-node.js");
