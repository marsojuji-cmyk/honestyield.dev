# honestyield.dev

**Publishes the honest-yield rule: no admitted before-and-after run pair, no savings number.**

[![CI](https://github.com/marsojuji-cmyk/honestyield.dev/actions/workflows/ci.yml/badge.svg)](https://github.com/marsojuji-cmyk/honestyield.dev/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

**No pair, no number.** Honest yield means **yield you can prove**. Any claim that a system saves tokens, money or time must cite an admitted run pair: a before-and-after measurement on the same workload under stated conditions. Without one, the savings number is null. Negative results are valid ledger entries.

This repo holds the static site for the standard: the Rule, the run-pair ledger, the lab page and an about page.

## What it guarantees

The Rule is a standard for people making claims; it is not enforced by code. What the repo itself enforces in CI:

- **Every internal link resolves**, and **the required files exist**. `scripts/check.py` fails the build otherwise.
- **No placeholder copy ships.** The same check rejects "lorem ipsum".
- **The ledger is append-only by policy.** Corrections arrive as new entries, and pull requests that rewrite an entry don't meet the Rule.

## Quickstart

```bash
git clone https://github.com/marsojuji-cmyk/honestyield.dev && cd honestyield.dev
python3 scripts/check.py      # what CI runs
open index.html               # plain HTML, no build step
```

## How it fails

| Condition | Behaviour |
|---|---|
| A broken internal link or a missing required file | `scripts/check.py` exits non-zero and CI goes red |
| A yield claim without an admitted run pair | Under the Rule, its savings number is null. The ledger shows it as pending, not as a figure |
| A null or negative result | Admitted and published, like a win |

## Evidence

Checked 2026-10-07:

- `python3 scripts/check.py`: "all checks passed". CI runs the same command.
- `ledger/index.html` holds two **format-example** entries and says plainly that "No production run pairs have been admitted yet":
  - An illustrative Permit entry with the delta pending.
  - A prefetch-cache entry with an admitted null result (−0.05%), measured 2026-10-05 and labeled a format example.
- **Deployment:** the `honestyield.dev` domain is on Cloudflare DNS but has no address records yet, so the site is **not live**. Deploy steps are below.

## The Rule (v1.0 draft)

1. A yield claim is a measured claim.
2. A run pair is a before-and-after measurement on the same workload under stated conditions.
3. Without an admitted run pair, the savings number is null. No pair, no number.
4. Negative results are admitted.
5. The ledger is append-only.
6. Authority only narrows.

Read it in full in [`index.html`](index.html).

## Repo layout

| Path | What it is |
|---|---|
| `index.html` | The Rule — canonical, citable, versioned |
| `ledger/` | The published run-pair ledger (wins and nulls) |
| `lab/` | Memory Utility Labs imprint page |
| `about/` | Why the standard exists, contact |
| `styles.css` | The whole design system — one file |
| `scripts/check.py` | CI: link resolution, required files, no-lorem check |

Plain HTML + one stylesheet. No frameworks, no build step. Deploys as-is to Cloudflare Pages.

## Deploy

Drag this folder into Cloudflare Pages (Workers & Pages → Create → Pages → Upload assets), then add the `honestyield.dev` custom domain. No server code, no env vars.

## Contributing a run pair

A run pair enters the ledger only under the Rule: same workload, stated conditions (inputs, model, configuration, date), append-only. Open a PR against `ledger/index.html` following the existing entry format. Corrections arrive as new entries — nothing is rewritten.

## Status

Rule v1.0 is a draft. The ledger has format examples only, and the site is not yet deployed.

## License

MIT. See [LICENSE](LICENSE).
