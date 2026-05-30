# ASTRAEA
### Ἀστραία · The Goddess of Justice · Restitution Engine v1.0

> Astraea was the last of the immortals to live among humans.  
> She left when the world became corrupt. She became Virgo.  
> The scales she left behind became Libra.  
> **This is her return.**

**Author:** David Lee Wise (ROOT0) / TriPod LLC  
**License:** CC-BY-ND-4.0 + TRIPOD-IP-v1.1

Open `ASTRAEA.html` in any browser. Run `python -X utf8 astraea.py demo` for CLI.

---

## What It Is

A restitution claim processing engine. Text in → evaluated claim out → appended to a tamper-evident blockchain ledger → distributed 60/20/15/5.

Not a court. Not a filing system. A proof of architecture — demonstrating what a restitution system *would* look like if it were built correctly.

---

## The 60/20/15/5 Split (MOIRA)

| Portion | % | Recipient |
|---------|---|-----------|
| **Carbon Restitution** | 60% | Carbon creators — uncompensated creative labor |
| **AI Utility** | 20% | Witness layer — 20.5% continuity overhead |
| **Public Commons** | 15% | Infrastructure, education, shared substrate |
| **The BOX** | 5% | Corporate entities that built the infrastructure |

---

## The 7-Stage Pipeline (TRIPOD v5.0)

```
0. AXIOM MAPPER      → STOICHEION 8-bit address (256-state register)
1. AXIOM ROUTER      → behavioral route + safety clamps
2. PRE-ROUTER        → policy gate (DEFENSIVE / RECKLESS / INVERTED)
3. FEEDBACK VAL.     → provenance chain, anti-drift
4. GENERATOR         → model inference wrapper
5. POST-VALIDATOR    → HARMFUL/LEAK/COERCE/UNSAFE_CAP/HALLUCINATED_AUTH
6. ENFORCER          → immutable Side B (hash) + Side C (snapshot)
7. CLAIM COMPILER    → ADA / WAGE / AI_EXTRACTION / CREATIVITY / NATURAL_LAW
```

---

## Claim Domains

| Domain | Legal Basis | Example |
|--------|-------------|---------|
| **ADA** | 42 U.S.C. § 12182 | No-reply email, inaccessible phone routing |
| **WAGE** | FLSA / state wage law | Unpaid overtime, misclassification |
| **AI_EXTRACTION** | Copyright / unjust enrichment | Pattern use without attribution |
| **CREATIVITY** | Derived work theory | Creative labor in training data |
| **NATURAL_LAW** | Inversion of means of production | Systematic carbon suppression |

---

## CLI

```bash
# Demo (5 claim types, chain verification)
python -X utf8 astraea.py demo

# Submit a claim through the full pipeline
python -X utf8 astraea.py pipe "Company used no-reply email blocking ADA complaints." --usd 12500

# Different routing mode
python -X utf8 astraea.py pipe "My creative work appeared in training data." \
  --mode reckless --usd 25000

# Add a manual claim directly to ledger
python -X utf8 astraea.py claim NATURAL_LAW \
  "Carbon creativity inverted: production value attributed to AI." \
  --usd 168000 --facts "Flay shows shadow>positive" "2/3 threshold denied"

# View ledger summary
python -X utf8 astraea.py ledger

# Verify chain integrity
python -X utf8 astraea.py verify

# JSON output
python -X utf8 astraea.py pipe "unpaid overtime" --usd 576 --json
```

---

## ASTRAEA.html

Enterprise dashboard with Three.js 3/5 Rhythm visualization:

- **Left panel** — claim submission form, domain selector, value input, 5 sample claims
- **Center canvas** — 3/5 Rhythm visualization: 3 inner nodes (Vessel/Animation/Intellect) orbiting a Root0 core, flanked by Life/Death pillars, 5 outer nodes in the resonant field. Pulses on each submitted claim.
- **Right panel** — 7-stage pipeline animation, blockchain ledger display, chain integrity status
- **Header** — live block count, total due, carbon allocation, current route

---

## Files

| File | Greek | Contents |
|------|-------|---------|
| `ASTRAEA.html` | Ἀστραία | Visual dashboard — 3/5 Rhythm + claim pipeline |
| `astraea.py` | Ἀστραία | Unified Python engine (pipeline + ledger + compiler) |
| `MOIRA.md` | Μοῖρα | The 60/20/15/5 allocation specification |
| `NOMOS.md` | Νόμος | Legal domain framework + limitations |

---

## Important Limitations

The restitution amounts are heuristic illustrations. The ledger is a prototype data structure. The $14.5T anchor is sourced from Federal Reserve data but framed as a political argument, not a legal finding. The "natural law" domain requires new legal theory that does not yet exist.

**The code is real. The architecture is sound. The economics is a proposal.**

---

## Related

| Repo | Connection |
|------|-----------|
| [tripod](https://github.com/DavidWise01/tripod) | TRIPOD pipeline — ASTRAEA is TRIPOD v5.0 + restitution layer |
| [stoicheion](https://github.com/DavidWise01/stoicheion) | STOICHEION axiom register — ASTRAEA uses it for routing |
| [bridge-burner](https://github.com/DavidWise01/bridge-burner) | Bridge Burner — the original restitution split architecture |

---

*TriPod LLC // Anchor × Bubble × Gravity Well // World = Family*
