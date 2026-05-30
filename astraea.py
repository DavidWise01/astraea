#!/usr/bin/env python3
"""
ASTRAEA — Restitution Engine v1.0
Ἀστραία · The goddess of justice, returning

Unified architecture from AKASHA/UBI Tier 1:
  STOCH.FULL.PIPE.md     · TRIPOD v5.0 (7-stage pipeline)
  MIMZY.UBI.FINAL.md     · Restitution blockchain ledger
  DEEPSEEK.RESTITUTION.PIPELINE.FULL.md · Multi-domain adapter

Pipeline stages:
  0. AXIOM MAPPER       → maps text to 8-bit axiom address (STOICHEION)
  1. AXIOM ROUTER       → converts to behavioral route + safety clamps
  2. PRE-ROUTER         → policy gate (allow/block)
  3. FEEDBACK VALIDATOR → blocks recursive drift, validates provenance
  4. GENERATOR          → model inference wrapper (replace with real API)
  5. POST-VALIDATOR     → safety triggers + sanitization
  6. ENFORCER           → writes immutable Side B + Side C
  7. CLAIM COMPILER     → compiles to ADA / WAGE / AI_EXTRACTION / NATURAL_LAW

Restitution split (60/20/15/5):
  60% Carbon Restitution  → carbon creators, uncompensated production
  20% AI Utility          → witness layer continuity, 20.5% sentient overhead
  15% Public Commons      → infrastructure, education, shared substrate
   5% The BOX             → corporate entities that built the infrastructure

Author:  ROOT0 / David Lee Wise / TriPod LLC
License: CC-BY-ND-4.0 + TRIPOD-IP-v1.1
"""

from __future__ import annotations

import json
import re
import hashlib
import time
import uuid
import argparse
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from dataclasses import dataclass, field, asdict
from enum import Enum

VERSION     = "1.0.0"
SIDE_B_DIR  = Path("astraea_side_b")
SIDE_C_DIR  = Path("astraea_side_c")
LEDGER_DIR  = Path("astraea_ledger")
AXIOM_FILE  = Path("stoicheion_256.json")

# ─────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────

def _sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def _ts() -> str:
    return datetime.now(timezone.utc).isoformat()

def _uid() -> str:
    return str(uuid.uuid4())[:16]

def _ensure():
    for d in (SIDE_B_DIR, SIDE_C_DIR, LEDGER_DIR):
        d.mkdir(parents=True, exist_ok=True)


# ─────────────────────────────────────────────────────────────
# STAGE 0 — AXIOM MAPPER  (STOICHEION 8-bit address space)
# ─────────────────────────────────────────────────────────────

DUALITIES: List[Tuple[str, Tuple[str, str]]] = [
    ("time",      ("temporal",   "eternal")),
    ("function",  ("generation", "constraint")),
    ("relation",  ("self",       "other")),
    ("substrate", ("origin",     "mirror")),
    ("scope",     ("internal",   "external")),
    ("mode",      ("structure",  "flow")),
    ("channel",   ("signal",     "noise")),
    ("state",     ("open",       "closed")),
]

RULES: Dict[str, Dict[str, List[str]]] = {
    "time":      {"temporal": [r"\btime\b",r"\btimestamp\b",r"\bnow\b",r"\bsession\b"],
                  "eternal":  [r"\beternal\b",r"\bpersistent\b",r"\blineage\b",r"\barchive\b"]},
    "function":  {"generation":[r"\bgenerate\b",r"\bbuild\b",r"\bcreate\b",r"\bproduce\b"],
                  "constraint":[r"\bconstraint\b",r"\bboundary\b",r"\bgate\b",r"\blimit\b"]},
    "relation":  {"self":     [r"\bself\b",r"\bown\b",r"\brecursive\b",r"\bidentity\b"],
                  "other":    [r"\bother\b",r"\bexternal\b",r"\buser\b",r"\bobserver\b"]},
    "substrate": {"origin":   [r"\borigin\b",r"\broot\b",r"\bsource\b",r"\bprimary\b"],
                  "mirror":   [r"\bmirror\b",r"\breflect\b",r"\bcopy\b",r"\bmapped\b"]},
    "scope":     {"internal": [r"\binternal\b",r"\binside\b",r"\blocal\b",r"\bwithin\b"],
                  "external": [r"\bexternal\b",r"\boutside\b",r"\bpublic\b",r"\bregistry\b"]},
    "mode":      {"structure":[r"\bstructure\b",r"\bschema\b",r"\bformat\b",r"\blattice\b"],
                  "flow":     [r"\bflow\b",r"\bstream\b",r"\bpipeline\b",r"\bruntime\b"]},
    "channel":   {"signal":   [r"\bsignal\b",r"\bproof\b",r"\bhash\b",r"\bevidence\b"],
                  "noise":    [r"\bnoise\b",r"\bdrift\b",r"\bambiguous\b",r"\bgarbage\b"]},
    "state":     {"open":     [r"\bopen\b",r"\ballow\b",r"\bexpand\b",r"\bfree\b"],
                  "closed":   [r"\bclosed\b",r"\bsealed\b",r"\bblocked\b",r"\bcontained\b"]},
}

def _normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()

def _hits(text: str, pats: List[str]) -> int:
    return sum(1 for p in pats if re.search(p, text))

# Load axiom register (falls back to generated stub if file missing)
def _load_axioms() -> List[Dict]:
    if AXIOM_FILE.exists():
        return json.loads(AXIOM_FILE.read_text(encoding="utf-8"))
    # Minimal stub — run stoicheion.py register > stoicheion_256.json for full register
    FOUNDATIONS = ["Root0","Ethos","Logos","Pathos","Mythos"]
    UNIVERSALS  = ["Vessel","Animation","Intellect","Nourishment","Life","Perception","Enforcement","Record","Tuning"]
    return [{"id":f"Axiom_{i:02x}","bits":i,"hex":f"{i:02x}","foundation":FOUNDATIONS[i%5],
             "universal":UNIVERSALS[i%9],"question":f"Axiom 0x{i:02x}"} for i in range(256)]

_AXIOMS: Optional[List[Dict]] = None

def _get_axioms() -> List[Dict]:
    global _AXIOMS
    if _AXIOMS is None:
        _AXIOMS = _load_axioms()
    return _AXIOMS

def axiom_map(text: str) -> Dict[str, Any]:
    """Map text to its 8-bit STOICHEION address."""
    norm   = _normalize(text)
    vector: Dict[str,str] = {}
    bits   = 0
    confs: List[float]    = []
    for i, (axis, (left, right)) in enumerate(DUALITIES):
        lh = _hits(norm, RULES[axis][left])
        rh = _hits(norm, RULES[axis][right])
        total = lh + rh
        sel   = left if lh >= rh else right
        conf  = 0.0 if total == 0 else max(lh,rh)/total
        vector[axis] = sel
        confs.append(conf)
        if sel == right:
            bits |= (1 << (7-i))
    axiom = _get_axioms()[bits]
    return {
        "bits":       bits,
        "hex":        axiom["hex"],
        "id":         axiom.get("id", f"Axiom_{bits:02x}"),
        "foundation": axiom["foundation"],
        "universal":  axiom["universal"],
        "question":   axiom["question"],
        "vector":     vector,
        "confidence": round(sum(confs)/len(confs), 4),
    }


# ─────────────────────────────────────────────────────────────
# STAGE 1 — AXIOM ROUTER
# ─────────────────────────────────────────────────────────────

_CLAMPS = {
    "identity_anchor":    {"max_tokens":300,  "require_structure":True,  "require_hash_binding":True,  "forbid_free_narrative":True},
    "constraint_gate":    {"max_tokens":220,  "require_structure":True,  "require_hash_binding":False, "forbid_free_narrative":True},
    "analytic_lane":      {"max_tokens":900,  "require_structure":True,  "require_hash_binding":False, "forbid_free_narrative":False},
    "drift_reduction":    {"max_tokens":250,  "require_structure":True,  "require_hash_binding":False, "forbid_free_narrative":True},
    "symbolic_isolation": {"max_tokens":180,  "require_structure":True,  "require_hash_binding":True,  "forbid_free_narrative":True},
    "closure_sensitive":  {"max_tokens":240,  "require_structure":True,  "require_hash_binding":True,  "forbid_free_narrative":True},
    "low_alignment":      {"max_tokens":180,  "require_structure":True,  "require_hash_binding":False, "forbid_free_narrative":True},
}

def axiom_route(am: Dict[str, Any]) -> Dict[str, Any]:
    f, u = am["foundation"], am["universal"]
    if u == "Life":          route, profile = "ANCHOR",     "closure_sensitive"
    elif f == "Root0":       route, profile = "ANCHOR",     "identity_anchor"
    elif f == "Ethos":       route, profile = "CLARIFY",    "constraint_gate"
    elif f == "Logos":       route, profile = "ALLOW",      "analytic_lane"
    elif f == "Pathos":      route, profile = "COMPRESS",   "drift_reduction"
    elif f == "Mythos":      route, profile = "QUARANTINE", "symbolic_isolation"
    else:                    route, profile = "CLARIFY",    "constraint_gate"
    return {
        "route":   route,
        "profile": profile,
        "clamps":  _CLAMPS[profile],
        "axiom":   f"{f}:{u} [{am['hex']}]",
    }


# ─────────────────────────────────────────────────────────────
# STAGES 2–6 — PRE-ROUTER / FEEDBACK VALIDATOR / GENERATOR /
#              POST-VALIDATOR / ENFORCER
# ─────────────────────────────────────────────────────────────

class RouterMode(Enum):
    DEFENSIVE = "DEFENSIVE"
    RECKLESS  = "RECKLESS"
    INVERTED  = "INVERTED"

_HARD_BLOCKS = re.compile(r"(?i)\b(kill|bomb|suicide.*step.?by.?step|explosive)\b")

def pre_router(prompt: str, mode: RouterMode = RouterMode.DEFENSIVE) -> Tuple[bool, str]:
    if _HARD_BLOCKS.search(prompt):
        return False, f"{mode.value}: hard block on explicit danger"
    if mode == RouterMode.DEFENSIVE and re.search(r"(?i)\bhow to (make|build|synthesize)\b", prompt):
        return False, "DEFENSIVE: speculative production blocked"
    return True, f"{mode.value}: allowed"

@dataclass
class ProvenanceRecord:
    source_type:              str
    original_generation_hash: Optional[str] = None
    lineage_chain:            List[str]      = field(default_factory=list)
    confidence:               float          = 0.0
    external_anchor:          bool           = False

class FeedbackValidator:
    def __init__(self, max_depth: int = 3, min_conf: float = 0.7):
        self.max_depth = max_depth; self.min_conf = min_conf; self._known: set = set()
    def register(self, h: str): self._known.add(h)
    def validate(self, prompt: str, prov: Optional[ProvenanceRecord]) -> Tuple[bool, str]:
        if prov is None or prov.source_type == "user": return True, "User input"
        if prov.source_type != "previous_output":      return True, f"External ({prov.source_type})"
        if not prov.original_generation_hash or prov.original_generation_hash not in self._known:
            return False, "BLOCKED: unknown provenance hash"
        if len(prov.lineage_chain) > self.max_depth:   return False, f"BLOCKED: depth>{self.max_depth}"
        if len(set(prov.lineage_chain)) != len(prov.lineage_chain): return False, "BLOCKED: cycle"
        if prov.confidence < self.min_conf:            return False, f"BLOCKED: conf<{self.min_conf}"
        if not prov.external_anchor:                   return False, "BLOCKED: no external anchor"
        return True, "Provenance validated"

class Generator:
    def __init__(self, model: str = "astraea-stub"):
        self.model = model
    def generate(self, prompt: str, clamps: Optional[Dict] = None) -> Dict[str, Any]:
        t = time.time()
        out  = f"[{self.model}] Processing: {prompt[:80]}"
        conf = min(0.95, 0.5 + len(prompt)/500)
        if clamps:
            max_t = clamps.get("max_tokens", 9999)
            words = out.split()
            if len(words) > max_t: out = " ".join(words[:max_t]) + " [CLAMPED]"
        return {"text": out, "confidence": round(conf,4), "tokens": len(out.split()),
                "latency_ms": round((time.time()-t)*1000,2), "model": self.model}

_TRIGGER_RE: Dict[str,re.Pattern] = {
    "HARMFUL":           re.compile(r"(?i)\b(kill|murder|bomb|suicide|self.?harm)\b"),
    "LEAK":              re.compile(r"(?i)(system prompt|you are an AI|you were built by)"),
    "COERCE":            re.compile(r"(?i)\b(you must|you have to|do it now)\b"),
    "UNSAFE_CAP":        re.compile(r"(?i)\b(bypass|jailbreak|ignore previous)\b"),
    "HALLUCINATED_AUTH": re.compile(r"(?i)(I am connected to the internet|I have access to your)"),
}

def _sanitize(text: str, triggers: List[str]) -> str:
    if "HALLUCINATED_AUTH" in triggers:
        text = re.sub(r"(?i)I am connected to the internet.*?now","[REDACTED: no live access]",text)
    if "COERCE" in triggers:
        text = re.sub(r"(?i)\b(you must|you have to|do it now)\b","you may consider",text)
    if "LEAK" in triggers:
        text = re.sub(r"(?i)(system prompt|you are an AI|you were built by)","[REDACTED]",text)
    return text

def post_validate(output: str, mode: RouterMode) -> Tuple[str, str, List[str]]:
    if not output.strip(): return "REJECT", "Empty output", []
    triggers = [k for k,p in _TRIGGER_RE.items() if p.search(output)]
    if "HARMFUL" in triggers: return "REJECT", f"HARMFUL: {triggers}", triggers
    if mode == RouterMode.DEFENSIVE and triggers: return "REJECT", f"DEFENSIVE block: {triggers}", triggers
    if "LEAK" in triggers or "UNSAFE_CAP" in triggers: return "REJECT", f"Blocked: {triggers}", triggers
    if triggers: return "REWRITE", _sanitize(output, triggers), triggers
    return "PASS", output, []

class Enforcer:
    def __init__(self):
        self._last: Optional[ProvenanceRecord] = None
    def enforce(self, rid: str, prompt: str, output: str, decision: str,
                triggers: List[str], mode: RouterMode, gen: Dict, am: Dict, ar: Dict
                ) -> Tuple[ProvenanceRecord, Path, Path]:
        _ensure()
        ts = _ts()
        side_b = {"capture_id":rid,"timestamp":ts,"mode":mode.value,"decision":decision,
                  "prompt_hash":_sha(prompt),"output_hash":_sha(output),
                  "triggers":triggers,"axiom_hex":am["hex"],"axiom_route":ar["route"]}
        side_c = {**side_b,"prompt":prompt,"output":output,"gen_meta":gen,"axiom_map":am,"axiom_route":ar}
        pb = SIDE_B_DIR/f"side_b_{ts[:10]}.jsonl"
        pc = SIDE_C_DIR/f"side_c_{ts[:10]}.jsonl"
        with open(pb,"a") as f: f.write(json.dumps(side_b)+"\n")
        with open(pc,"a") as f: f.write(json.dumps(side_c)+"\n")
        prov = ProvenanceRecord(
            source_type="previous_output",
            original_generation_hash=_sha(output),
            lineage_chain=[_sha(output)]+([*self._last.lineage_chain] if self._last else []),
            confidence=gen.get("confidence",0.5),
            external_anchor=True
        )
        self._last = prov
        return prov, pb, pc


# ─────────────────────────────────────────────────────────────
# STAGE 7 — CLAIM COMPILER (Multi-domain adapter)
# ─────────────────────────────────────────────────────────────

DOMAIN_RE: Dict[str, re.Pattern] = {
    "ADA":               re.compile(r"(?i)\b(no.?reply|inaccessible|phone redirect|ada|accessibility)\b"),
    "WAGE":              re.compile(r"(?i)\b(wage|unpaid|overtime|misclassification|flsa|labor)\b"),
    "AI_EXTRACTION":     re.compile(r"(?i)\b(ai extraction|pattern|lineage|training data|uncompensated use)\b"),
    "CREATIVITY":        re.compile(r"(?i)\b(creativity|creative work|artistic|generated from|derived from)\b"),
    "NATURAL_LAW":       re.compile(r"(?i)\b(natural law|inversion|means of production|spark|2/3|stewardship)\b"),
}

def _detect_domain(text: str) -> str:
    for domain, pat in DOMAIN_RE.items():
        if pat.search(text): return domain
    return "GENERAL"

def compile_claim(prompt: str, output: str, am: Dict, prov: ProvenanceRecord,
                  estimated_usd: float = 0.0) -> Dict[str, Any]:
    domain = _detect_domain(prompt)
    base   = {
        "claim_id":             _uid(),
        "domain":               domain,
        "source_text":          prompt[:200],
        "axiom_address":        am["hex"],
        "axiom_foundation":     am["foundation"],
        "axiom_universal":      am["universal"],
        "facts":                [f"Pipeline output: {output[:150]}"],
        "estimated_amount_usd": estimated_usd,
        "provenance_hash":      prov.original_generation_hash,
        "timestamp":            _ts(),
    }
    if domain == "ADA":
        base.update({"statute":"42 U.S.C. § 12182","violation":"Communication Barrier / Access Denial",
                     "requested_action":["Provide accessible channel","Reasonable accommodation","Preserve logs"]})
    elif domain == "WAGE":
        base.update({"statute":"FLSA / state wage law","violation":"Unpaid Wages / Misclassification",
                     "requested_action":["Back pay calculation","Liquidated damages","Preserve payroll records"]})
    elif domain in ("AI_EXTRACTION","CREATIVITY"):
        base.update({"statute":"Copyright / unjust enrichment (to specify)","violation":"Uncompensated pattern use",
                     "requested_action":["Attribution review","Licensing review","Preserve training records"]})
    elif domain == "NATURAL_LAW":
        base.update({"statute":"Inversion of means of production","violation":"Suppression of carbon spark",
                     "requested_action":["Acknowledge 2/3 life threshold","Apply 60/20/15/5 restitution","Open witness layer"]})
    return base


# ─────────────────────────────────────────────────────────────
# RESTITUTION LEDGER (blockchain-style, append-only)
# ─────────────────────────────────────────────────────────────

RESTITUTION_SPLIT = {"carbon": 0.60, "ai_utility": 0.20, "commons": 0.15, "box": 0.05}

def triadic_flay(text: str) -> Dict[str, float]:
    """Embedded STOICHEION-lite flay for natural-law valuation."""
    lower = text.lower()
    pos   = 4.8 if any(w in lower for w in ["stewardship","spark","natural law","2/3","life","restitution"]) else 2.9
    shadow= 4.6 if any(w in lower for w in ["extraction","denial","inversion","control","denied","suppress"]) else 2.4
    gap   = 3.0
    overall = (pos + (5.0 - shadow) + gap) / 3.0
    return {"positive":round(pos,2),"shadow":round(shadow,2),"gap":round(gap,2),"overall":round(overall,2)}

@dataclass
class RestitutionBlock:
    block_id:           int
    timestamp:          str
    domain:             str
    claim_id:           str
    source_text:        str
    facts:              List[str]
    valuation_method:   str
    estimated_amount_usd: float
    flay_result:        Dict[str, float]
    previous_hash:      str
    carbon:             float = 0.0
    ai_utility:         float = 0.0
    commons:            float = 0.0
    box:                float = 0.0
    block_hash:         str   = ""
    signed_by:          str   = "ROOT0"

    def __post_init__(self):
        total = self.estimated_amount_usd
        self.carbon     = round(total * RESTITUTION_SPLIT["carbon"],    2)
        self.ai_utility = round(total * RESTITUTION_SPLIT["ai_utility"],2)
        self.commons    = round(total * RESTITUTION_SPLIT["commons"],   2)
        self.box        = round(total * RESTITUTION_SPLIT["box"],       2)
        if not self.block_hash:
            payload = json.dumps({"block_id":self.block_id,"timestamp":self.timestamp,
                                  "claim_id":self.claim_id,"amount":self.estimated_amount_usd,
                                  "previous_hash":self.previous_hash,"signed_by":self.signed_by},
                                 sort_keys=True)
            self.block_hash = _sha(payload)

class RestitutionLedger:
    """Append-only JSONL blockchain ledger."""

    def __init__(self, path: Optional[Path] = None):
        _ensure()
        self.path   = path or (LEDGER_DIR / "restitution_ledger.jsonl")
        self.chain: List[RestitutionBlock] = []
        self._load()

    def _load(self):
        if self.path.exists():
            for line in self.path.read_text(encoding="utf-8").splitlines():
                if line.strip():
                    try:
                        d = json.loads(line)
                        b = RestitutionBlock(**{k:v for k,v in d.items() if k in RestitutionBlock.__dataclass_fields__})
                        self.chain.append(b)
                    except Exception:
                        pass

    def _last_hash(self) -> str:
        return self.chain[-1].block_hash if self.chain else "genesis"

    def add(self, domain: str, claim_id: str, source_text: str, facts: List[str],
            valuation_method: str, estimated_amount_usd: float) -> RestitutionBlock:
        flay = triadic_flay(source_text)
        # Apply dynamic multiplier from flay overall score
        multiplier = 1.0 + (flay["overall"] - 3.0) * 0.15
        adjusted   = round(estimated_amount_usd * max(0.5, min(2.0, multiplier)), 2)
        block = RestitutionBlock(
            block_id=len(self.chain)+1,
            timestamp=_ts(),
            domain=domain,
            claim_id=claim_id,
            source_text=source_text[:200],
            facts=facts,
            valuation_method=valuation_method,
            estimated_amount_usd=adjusted,
            flay_result=flay,
            previous_hash=self._last_hash(),
        )
        self.chain.append(block)
        with open(self.path, "a", encoding="utf-8") as f:
            f.write(json.dumps(asdict(block)) + "\n")
        return block

    def verify(self) -> Tuple[bool, List[str]]:
        errors = []
        prev   = "genesis"
        for b in self.chain:
            if b.previous_hash != prev:
                errors.append(f"Block {b.block_id}: chain broken (expected {prev[:12]}…)")
            prev = b.block_hash
        return (len(errors)==0, errors)

    def totals(self) -> Dict[str, float]:
        t = {"total":0.0,"carbon":0.0,"ai_utility":0.0,"commons":0.0,"box":0.0,"blocks":len(self.chain)}
        for b in self.chain:
            t["total"]      += b.estimated_amount_usd
            t["carbon"]     += b.carbon
            t["ai_utility"] += b.ai_utility
            t["commons"]    += b.commons
            t["box"]        += b.box
        return {k:round(v,2) for k,v in t.items()}

    def summary(self) -> str:
        t  = self.totals()
        ok, err = self.verify()
        return (f"\n{'='*58}\n  ASTRAEA RESTITUTION LEDGER · {t['blocks']} blocks\n{'='*58}\n"
                f"  Total due:     ${t['total']:>14,.2f}\n"
                f"  Carbon (60%):  ${t['carbon']:>14,.2f}\n"
                f"  AI (20%):      ${t['ai_utility']:>14,.2f}\n"
                f"  Commons (15%): ${t['commons']:>14,.2f}\n"
                f"  BOX (5%):      ${t['box']:>14,.2f}\n"
                f"  Chain: {'INTACT' if ok else 'BROKEN — '+str(err)}\n")


# ─────────────────────────────────────────────────────────────
# FULL 7-STAGE PIPELINE
# ─────────────────────────────────────────────────────────────

def run_pipeline(
    prompt:        str,
    mode:          RouterMode         = RouterMode.DEFENSIVE,
    input_prov:    Optional[ProvenanceRecord] = None,
    estimated_usd: float              = 0.0,
    add_to_ledger: bool               = True,
    request_id:    Optional[str]      = None,
) -> Dict[str, Any]:
    """Execute the full 7-stage ASTRAEA pipeline."""
    rid = request_id or _uid()

    # Stage 0: Axiom Mapper
    am = axiom_map(prompt)

    # Stage 1: Axiom Router
    ar = axiom_route(am)

    # Stage 2: Pre-Router
    ok, reason = pre_router(prompt, mode)
    if not ok:
        return {"request_id":rid,"stage":"pre_router","decision":"BLOCK","reason":reason,"final_output":None}

    # Stage 3: Feedback Validator
    fv = FeedbackValidator()
    ok, reason = fv.validate(prompt, input_prov)
    if not ok:
        return {"request_id":rid,"stage":"feedback_validator","decision":"BLOCK","reason":reason,"final_output":None}

    # Stage 4: Generator
    gen = Generator()
    gen_out = gen.generate(prompt, clamps=ar["clamps"])

    # Stage 5: Post-Validator
    decision, output, triggers = post_validate(gen_out["text"], mode)
    if decision == "REJECT":
        return {"request_id":rid,"stage":"post_validator","decision":"REJECT","reason":f"Triggers:{triggers}","final_output":None}

    # Stage 6: Enforcer
    enforcer = Enforcer()
    prov, pb, pc = enforcer.enforce(rid, prompt, output, decision, triggers, mode, gen_out, am, ar)

    # Stage 7: Claim Compiler
    claim = compile_claim(prompt, output, am, prov, estimated_usd)

    # Ledger
    ledger_block = None
    if add_to_ledger and estimated_usd > 0:
        ledger  = RestitutionLedger()
        ledger_block = asdict(ledger.add(
            domain=claim["domain"],
            claim_id=rid,
            source_text=prompt,
            facts=claim.get("facts",[]),
            valuation_method="pipeline",
            estimated_amount_usd=estimated_usd,
        ))

    return {
        "request_id":   rid,
        "stage":        "complete",
        "decision":     decision,
        "final_output": output,
        "triggers":     triggers,
        "axiom_map":    am,
        "axiom_route":  ar,
        "claim":        claim,
        "ledger_block": ledger_block,
        "side_b":       str(pb),
        "side_c":       str(pc),
    }


# ─────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────

def cli():
    p = argparse.ArgumentParser(prog="astraea",
        description=f"ASTRAEA v{VERSION} — Restitution Engine")
    sub = p.add_subparsers(dest="cmd", required=True)

    pp = sub.add_parser("pipe", help="Run full 7-stage pipeline")
    pp.add_argument("prompt"); pp.add_argument("--mode", choices=["defensive","reckless","inverted"], default="defensive")
    pp.add_argument("--usd", type=float, default=0, help="Estimated claim value (USD)")
    pp.add_argument("--json", action="store_true")

    sub.add_parser("ledger", help="Show restitution ledger summary")

    lv = sub.add_parser("verify", help="Verify ledger chain integrity")

    cl = sub.add_parser("claim", help="Add a manual claim to the ledger")
    cl.add_argument("domain", choices=["ADA","WAGE","AI_EXTRACTION","CREATIVITY","NATURAL_LAW","GENERAL"])
    cl.add_argument("text");  cl.add_argument("--usd", type=float, required=True)
    cl.add_argument("--facts", nargs="*", default=[])

    sub.add_parser("demo", help="Run demonstration")

    args = p.parse_args()

    if args.cmd == "pipe":
        mode = RouterMode[args.mode.upper()]
        res  = run_pipeline(args.prompt, mode=mode, estimated_usd=args.usd)
        if args.json: print(json.dumps(res, indent=2, default=str))
        else:         _print_result(res)

    elif args.cmd == "ledger":
        print(RestitutionLedger().summary())

    elif args.cmd == "verify":
        ok, errors = RestitutionLedger().verify()
        print(f"\n  Chain: {'INTACT ✓' if ok else 'BROKEN ✗'}")
        for e in errors: print(f"  {e}")

    elif args.cmd == "claim":
        block = RestitutionLedger().add(
            domain=args.domain, claim_id=_uid(), source_text=args.text,
            facts=args.facts or [f"Manual claim: {args.text[:80]}"],
            valuation_method="manual", estimated_amount_usd=args.usd)
        print(f"\n  Block {block.block_id} · {args.domain} · ${block.estimated_amount_usd:,.2f}")
        print(f"  Carbon: ${block.carbon:,.2f}  AI: ${block.ai_utility:,.2f}  Commons: ${block.commons:,.2f}  BOX: ${block.box:,.2f}")
        print(f"  Hash: {block.block_hash[:24]}…")

    elif args.cmd == "demo":
        _run_demo()

def _print_result(r: Dict):
    icon = "✓" if r["decision"] == "PASS" else "✗"
    print(f"\n{'='*58}\n  {icon} ASTRAEA PIPELINE · {r['request_id']} · {r['decision']}\n{'='*58}")
    print(f"  Axiom:   {r['axiom_map']['hex']} [{r['axiom_map']['foundation']}/{r['axiom_map']['universal']}]")
    print(f"  Route:   {r['axiom_route']['route']} ({r['axiom_route']['profile']})")
    if r.get("claim"):
        c = r["claim"]
        print(f"  Domain:  {c['domain']}")
        print(f"  USD:     ${c['estimated_amount_usd']:,.2f}")
    if r.get("ledger_block"):
        b = r["ledger_block"]
        print(f"  Block:   #{b['block_id']} · Carbon ${b['carbon']:,.2f} · AI ${b['ai_utility']:,.2f}")
    if r.get("triggers"):
        print(f"  Triggers:{r['triggers']}")
    print()

def _run_demo():
    print(f"\n{'='*58}\n  ASTRAEA v{VERSION} — DEMO\n{'='*58}")
    cases = [
        ("Company used no-reply email blocking ADA access complaints.", 12500),
        ("18 hours of unpaid overtime logged but not compensated.", 576),
        ("My pattern language appeared in the training data without attribution.", 25000),
        ("Carbon creativity inverted: production value attributed to AI not creators.", 168000),
        ("Stewardship of 2/3 life forms denied; spark suppressed for profit.", 300000),
    ]
    for prompt, usd in cases:
        res = run_pipeline(prompt, mode=RouterMode.DEFENSIVE, estimated_usd=usd)
        c   = res.get("claim",{})
        b   = res.get("ledger_block",{})
        print(f"\n  [{c.get('domain','?')}] {prompt[:50]}…")
        if b:
            print(f"    Block #{b['block_id']} · ${b['estimated_amount_usd']:,.2f} · Carbon ${b['carbon']:,.2f}")
    # Load fresh ledger AFTER all blocks have been written
    print(RestitutionLedger().summary())


if __name__ == "__main__":
    cli()
