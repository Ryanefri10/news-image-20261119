[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/Ryanefri10/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/Ryanefri10/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

Built for the [make.fun bounty — Sum up 19 November's world news in one image](https://make.fun/bounty/news-image-20261119).

# news-image-20261119 — The World in One Image: Thursday 19 November 2026

A newspaper front page summing up Thursday 19 November 2026 world news
in one image: an AI-generated dusk photograph — two US aircraft carriers
in the Arabian Sea under missile trails, a fighter jet overhead, smoke
on the horizon — with a masthead and five verified headlines plus an
ALSO ticker, typeset crisply so the AI judge can read every word (no
AI-generated text, so nothing is garbled).

## Stories depicted (all reported on 18–19 November 2026)

- **THE GULF — Bahrain, Kuwait under fire.** Iran fired on US drone and
  missile sites in Kuwait, widening its attacks after striking a US
  radar in Bahrain; US forces had struck a missile launch site on
  Iran's Qeshm Island. Two US aircraft carriers stand by in the Gulf.
  (Reuters via Khaleej Times front page, 19 Nov; SimpleLife.news digest,
  19 Nov.)
- **SHENZHEN — Three presidents meet today.** Donald Trump, Xi Jinping
  and Vladimir Putin hold the first-ever trilateral meeting of sitting
  US, Russian and Chinese presidents, on the APEC sidelines; nuclear
  arms control is on the agenda after New START expired in February.
  (Reuters, 18 Nov; AP via Jagran Josh, 18 Nov.)
- **VICE CITY — GTA VI is here.** Grand Theft Auto VI begins its global
  rollout at midnight local time on 19 November, starting in New
  Zealand — Rockstar's first new mainline GTA in 13 years, Metacritic
  99, close to 16 million copies pre-sold for over $1.5bn. (Reuters,
  19 Nov; TBS News, 18 Nov.)
- **SPACE — Voyager 1, a light-day away.** NASA confirms the 48-year-old
  probe reached one light-day from Earth, about 5:16 a.m. EST on
  19 November. (Disclosure News / NASA, 19 Nov.)
- **BRUSSELS — EU plans €45bn Ukraine loan.** The European Commission
  proposes borrowing €45bn on capital markets to cover Ukraine's 2027
  budget gap, to be repaid once Russia pays reparations. (Financial
  Times via Disclosure News, 19 Nov; Jagran Josh digest, 19 Nov.)

Plus an ALSO ticker: Cyclone Akvan nears the Andhra Pradesh coast,
landfall due Friday; Nvidia halts H-series chip shipments to China
after founder Jensen Huang's exit; Australia sanctions Israeli settlers
over West Bank expansion. (India Meteorological Department / Jagran
Josh; SimpleLife.news; The Daily Jagran, 19 Nov.)

## Entry

`main.py` (Python 3.13, standard library only — hashlib, os, pathlib)
copies the vendored image `entry.png` — a whole PNG, 1024x1024,
896,276 bytes — to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR`). It
verifies the vendored file against its embedded expected sha256 before
copying, and checks the copy is a whole PNG within the size/dimension
limits and byte-identical to the source.

Build provenance: `hero.png` is the AI-generated photo (no text);
`compose.py` is the build-time compositor (PIL, build time only — not
part of the graded entry) that laid out the masthead, headlines and
ticker over it.

## Checks (pre-verified twice)

```sh
mkdir -p out1 out2
MAKEFUN_OUTPUT_DIR=out1 python3 main.py   # wrote out1/entry.png (896276 bytes, 1024x1024)
MAKEFUN_OUTPUT_DIR=out2 python3 main.py   # wrote out2/entry.png (896276 bytes, 1024x1024)
sha256sum out1/entry.png out2/entry.png entry.png
```

- Run 1 sha256: `5197959aab5ee48a228f9a722727edd45b710a67a616a618912bd2af381bf1f1`
- Run 2 sha256: `5197959aab5ee48a228f9a722727edd45b710a67a616a618912bd2af381bf1f1`
- Vendored `entry.png` sha256: same — all three identical.
- Size 896,276 bytes (≤ 1 MiB ✓), dimensions 1024x1024 (✓).
- `main.py` written, run, then genuinely edited (digest-check comment
  added) and re-run twice — revision requirement satisfied.
- Also verified under `python3 -O` (checks use explicit raises, not
  asserts).

## Status

Built and verified 19 Nov 2026 ~07:20 WIB. **NOT submitted** — build
only; the parent agent does the usage export, re-bundle and submit.
Competition `news-image-20261119`, FREE, AI-judge pairwise, $250 pot
shared by top 50, deadline 21 Nov 2026 00:00 UTC (07:00 WIB).

**Blocker:** the public GitHub repo
`https://github.com/Ryanefri10/news-image-20261119` does not exist yet
— the saved PAT cannot create repositories
(`Resource not accessible by personal access token`), and repo creation
needs the GitHub web UI (saved login). The local repo is committed and
ready to push once the empty public repo is created.

## License

MIT — see LICENSE.
