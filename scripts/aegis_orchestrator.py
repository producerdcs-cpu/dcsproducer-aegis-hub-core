#!/usr/bin/env python3
"""
DcsProducer AEGIS OS - Orchestrator
Version: 1.0.0 | Meta Global AI Developer Hackathon 2026
Command: python scripts/aegis_orchestrator.py --init
"""
from __future__ import annotations

import argparse
import json
import os
import time
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Optional

AEGIS_VERSION = "1.0.0"
META_API_BASE = os.getenv("META_API_BASE", "https://api.llama-api.com")
META_API_KEY = os.getenv("META_API_KEY", "YOUR_META_API_KEY_HERE")
CORE_HUB = os.getenv("CORE_HUB_URL", "https://core-hub-aegis.vercel.app/")
METARAG_HUB = os.getenv("METARAG_HUB_URL", "https://dcsproducer-hub-pqj9.vercel.app/")


class Pilar(Enum):
    DEVOPS = "01 DevOps"
    MICROSERVICOS = "02 Microsservicos"
    SERVERLESS = "03 Serverless"
    CONTAINERS = "04 Containers"
    ARQUITETURA_LIMPA = "05 Arquitetura Limpa"
    DDD = "06 DDD"
    OBSERVABILITY = "07 Observability"
    DEVSECOPS = "08 DevSecOps"
    EVENT_DRIVEN = "09 Event-Driven"


class SixPillarsEngineer:
    """Prompt optimizer — injects engineering vocabulary (token discipline)."""

    @staticmethod
    def optimize_prompt(raw_prompt: str) -> Dict:
        optimized = (
            "[AEGIS-OPT] pillars=6 | fail-closed | evidence-first | "
            f"{raw_prompt[:400]}"
        )
        approx = lambda t: max(1, int(len(t.split()) * 1.3))
        return {
            "original_tokens": approx(raw_prompt),
            "optimized_tokens": approx(optimized),
            "optimized_prompt": optimized,
            "checklist": [
                "Technical vocabulary injected?",
                "Explicit contract / output schema?",
                "AEGIS gate path?",
                "Traceability (request-id)?",
            ],
        }


@dataclass
class AegisRequest:
    request_id: str
    source: str
    intent: str
    pilar: Optional[str] = None


class AegisLayer:
    def gate_check(self, request: AegisRequest) -> bool:
        print(f"\n[AEGIS L1] Gate Check — {request.request_id}")
        print(f"  intent: {request.intent[:100]}")
        # Hackathon: wire Llama Guard here (fail-closed)
        if not request.intent.strip():
            print("[AEGIS L1] BLOCKED — empty intent (fail-closed)")
            return False
        print("[AEGIS L1] PASSED — fail-closed OK")
        return True

    def call_meta_api(self, prompt: str) -> str:
        if META_API_KEY in ("", "YOUR_META_API_KEY_HERE"):
            return (
                "[MOCK META API] Set META_API_KEY in .env for live Llama / Guard. "
                f"Prompt head: {prompt[:120]}"
            )
        # Wire Meta Model API + Guard in hackathon window
        return f"[META API placeholder] {prompt[:120]}"


class AegisOrchestrator:
    def init(self) -> None:
        print(
            """
╔══════════════════════════════════════════════════╗
║  DcsProducer AEGIS Hub Core — MetaRAG            ║
║  AEGIS ORCHESTRATOR INIT                         ║
║  Governance · Protection · Intelligence          ║
╚══════════════════════════════════════════════════╝
"""
        )
        print(f"[INIT] {AEGIS_VERSION} — Circular Hub + L0–L5")
        print("[L0] Cloud | On-prem | Containers")
        print("[L1] AEGIS kernel — Gate / Security / Observability")
        print(f"[L2] MetaRAG Hub — {METARAG_HUB}")
        print(f"[L5] Core Hub — {CORE_HUB}")
        print("\n✓ AEGIS ORCHESTRATOR READY")
        print("  python scripts/aegis_orchestrator.py --init")
        print('  python scripts/aegis_orchestrator.py --intent "..." --pilar "08 DevSecOps"')

    def handle(self, raw_intent: str, pilar_name: str = "07 Observability") -> dict:
        req_id = f"aegis-{int(time.time())}"
        opt = SixPillarsEngineer.optimize_prompt(raw_intent)
        print(
            f"\n[SIX-PILLARS] ~{opt['original_tokens']:.0f} → ~{opt['optimized_tokens']:.0f} tokens (approx)"
        )
        for item in opt["checklist"]:
            print(f"  [ ] {item}")
        req = AegisRequest(req_id, "cli", opt["optimized_prompt"], pilar_name)
        if not AegisLayer().gate_check(req):
            return {"status": "blocked", "request_id": req_id}
        meta_resp = AegisLayer().call_meta_api(opt["optimized_prompt"])
        result = {
            "status": "ok",
            "request_id": req_id,
            "pilar": pilar_name,
            "meta_response": meta_resp,
            "trace": f"{CORE_HUB.rstrip('/')}/trace/{req_id}",
            "hub": METARAG_HUB,
        }
        print(f"\n[RESULT]\n{json.dumps(result, indent=2, ensure_ascii=False)}")
        return result


def main() -> None:
    parser = argparse.ArgumentParser(description="DcsProducer AEGIS Orchestrator")
    parser.add_argument("--init", action="store_true")
    parser.add_argument("--intent", type=str)
    parser.add_argument("--pilar", type=str, default="07 Observability")
    args = parser.parse_args()
    orch = AegisOrchestrator()
    if args.init:
        orch.init()
    elif args.intent:
        orch.handle(args.intent, args.pilar)
    else:
        print("Examples:")
        print("  python scripts/aegis_orchestrator.py --init")
        print(
            '  python scripts/aegis_orchestrator.py --intent "Analyze SST PDF and draft NR-35 checklist" --pilar "08 DevSecOps"'
        )


if __name__ == "__main__":
    main()
