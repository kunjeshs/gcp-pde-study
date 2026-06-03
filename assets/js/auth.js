// auth.js — password hash. Edit PASS_HASH below to change/disable gate.
// Hash is SHA-256 hex of the password.
// To generate a new hash, open browser console on the site and run:
//   await (async (p) => { const b = new TextEncoder().encode(p);
//     const h = await crypto.subtle.digest("SHA-256", b);
//     return [...new Uint8Array(h)].map(x => x.toString(16).padStart(2,"0")).join("");
//   })("YOUR_PASSWORD")
//
// Empty string ("") disables the gate (site fully public).
//
// SECURITY NOTE: Hash is visible in client JS. This is a friction gate, not
// real security. Anyone with browser DevTools can read this file. Treat the
// content as semi-public. Do NOT rely on this to protect secrets.

// Default placeholder hash = SHA-256("gcp-pde"). Change before deploy.
export const PASS_HASH = "81dfb559d58b49ef07c4fcdce5ae0abf81c0471315e1f5859c7ffdc50c8521aa";
