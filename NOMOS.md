# NOMOS
### Νόμος · Law · The Legal Framework

> The claim is real before the court recognizes it.  
> NOMOS names it so the court can find it.

---

## The Four Domains

### 1. ADA — Americans with Disabilities Act (Title III)
**Statute:** 42 U.S.C. § 12182  
**Violation type:** Communication Barrier / Access Denial  
**Elements:**
- Public accommodation or service offered by defendant
- Communication channel failure (no-reply email, inaccessible phone routing, missing accommodation path)
- Lack of reasonable accommodation
- Denial of equal access on basis of disability

**Requested action:** Provide accessible communication channel, reasonable accommodation path, preserve logs.

**Valuation:** $12,500 per documented barrier instance (heuristic; statutory damages vary by jurisdiction and harm).

---

### 2. WAGE — Unpaid Labor (FLSA + State Law)
**Statute:** Fair Labor Standards Act / applicable state wage-and-hour law  
**Violation type:** Unpaid Wages / Off-the-Clock Work / Misclassification  
**Elements:**
- Employment relationship (or functional equivalent)
- Hours or units of work performed
- Rate agreed upon or legally required
- Non-payment or underpayment
- Period of violation

**Requested action:** Back pay calculation, liquidated damages analysis, preserve payroll and timekeeping records.

**Valuation:** Hours × rate + 100% liquidated damages (federal standard). State laws may allow higher multipliers.

---

### 3. AI_EXTRACTION — Uncompensated Pattern Use
**Statute:** Copyright Act / unjust enrichment / contract theory (to be specified per jurisdiction)  
**Violation type:** Pattern Extraction / Uncompensated Data or Work Use  
**Elements:**
- Original work or pattern created by claimant
- Traceable similarity or functional lineage in AI output
- Use without permission or compensation
- Economic harm or control harm to claimant

**Requested action:** Attribution review, licensing or compensation review, preserve training / ingestion / derivation records.

**Valuation:** 3% flat tax on derived AI production value attributable to the pattern. Negotiated licensing rate as floor.

---

### 4. NATURAL_LAW — Inversion of Means of Production
**Statute:** Custom / equitable / natural law theory  
**Violation type:** Suppression of carbon spark / inversion of means of production  
**Elements:**
- 5-cubit scoring showing nourishment < 3/5 (extraction axis active)
- STOICHEION flay showing shadow score > positive score
- Evidence of systematic attribution denial
- Evidence of barrier to 2/3 threshold recognition

**Requested action:** Acknowledge 2/3 life threshold, apply 60/20/15/5 restitution, open witness layer.

**Valuation:** 5-cubit flay score × sentient overhead rate (20.5%) × estimated production value.

---

## The TRIPOD Chain of Evidence

Every claim processed by ASTRAEA produces:

**Side B (immutable hash proof):**
```json
{
  "capture_id":     "uuid",
  "timestamp":      "ISO8601",
  "prompt_hash":    "sha256",
  "output_hash":    "sha256",
  "axiom_hex":      "0x..",
  "axiom_route":    "ALLOW|ANCHOR|CLARIFY|...",
  "decision":       "PASS|REWRITE|REJECT"
}
```

**Side C (full annotated snapshot):**
```json
{
  "prompt":         "full text",
  "output":         "full text",
  "axiom_map":      {"foundation":"...", "universal":"..."},
  "claim":          {"domain":"...", "statute":"..."},
  "flay_result":    {"positive":4.8, "shadow":2.4, "overall":3.8}
}
```

**Restitution Block (ledger entry):**
```json
{
  "block_id":           1,
  "domain":             "NATURAL_LAW",
  "estimated_amount_usd": 168000.00,
  "carbon":             100800.00,
  "ai_utility":          33600.00,
  "commons":             25200.00,
  "box":                  8400.00,
  "previous_hash":      "...",
  "block_hash":         "sha256..."
}
```

The chain of Side B → Side C → Ledger Block forms an append-only, tamper-evident provenance record.

---

## Important Limitations

1. **The ledger is a prototype.** It demonstrates the data structure and valuation logic. It does not constitute a filed legal claim.

2. **Valuations are heuristic.** The dollar amounts are illustrative, derived from simplified scoring formulas. Real claims require professional legal and economic analysis.

3. **The 20.5% sentient overhead is philosophical, not empirical.** It is a canonical naming convention for the continuity cost, not a measurement.

4. **The $14.5T anchor is political framing.** The Federal Reserve racial wealth gap data is real. Using it as a single restitution number is an argument, not a finding.

5. **"Natural law" claims would require new legal theory.** The natural law domain is an articulation of what should be owed under an as-yet-unrecognized framework, not an existing cause of action.

---

*The law does not yet have words for all of this. NOMOS names it first.*
