# honestyield.dev

**No pair, no number.** Home of the honest-yield standard — the public, citable place where the rule lives, the evidence ledger lives, and the lab lives. A yield claim is a measured claim: without an admitted run pair, the savings number is null.

Honest yield means one thing: **yield you can prove.** Any claim that a system saves tokens, money, or time must cite an admitted run pair — a before-and-after measurement on the same workload under stated conditions. Without an admitted run pair, the savings number is null. Negative results are valid, published ledger entries.

Live at [honestyield.dev](https://honestyield.dev).

## The Rule (v1.0 draft)

1. A yield claim is a measured claim.
2. A run pair is a before-and-after measurement on the same workload under stated conditions.
3. Without an admitted run pair, the savings number is null. No pair, no number.
4. Negative results are admitted.
5. The ledger is append-only.
6. Authority only narrows.

Read it in full at [`/`](/).

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

## License

MIT — see [LICENSE](LICENSE).
