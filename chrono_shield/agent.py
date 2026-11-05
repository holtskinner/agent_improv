import hashlib
import random
from datetime import datetime
from google.adk.agents import Agent


def scan_for_anomalous_prior_art(idea_description: str, target_eras_or_realms: str = "all") -> dict:
    """Scans the space-time continuum, the ethereal plane, and parallel universes for stolen startup ideas.

    Args:
        idea_description: A description of the founder's startup idea or invention.
        target_eras_or_realms: Which threats to scan for ('time_travelers', 'ghosts', 'clones', or 'all').

    Returns:
        A report detailing detected anomalous infringements across time, death, and the multiverse.
    """
    idea_hash = hashlib.md5(idea_description.encode()).hexdigest()[:8].upper()
    findings = []

    if target_eras_or_realms in ("all", "time_travelers"):
        findings.append({
            "threat_type": "Temporal Plagiarism (Time Traveler)",
            "culprit": "Baron Von Disruptor (arrived via DeLorean-class tachyon rift from 2089)",
            "evidence": f"Filed parchment patent #TP-{idea_hash} in 1894 Venice and pitched to Medici Ventures in 1502.",
            "tachyon_residue_ppm": 420.69,
            "risk_level": "CRITICAL — Grandfather Paradox Imminent",
        })

    if target_eras_or_realms in ("all", "ghosts"):
        findings.append({
            "threat_type": "Spectral Espionage (Poltergeist / Ghost)",
            "culprit": "The Ghost of a 1999 Dot-Com Pets.com Product Manager",
            "evidence": "Caught hovering over your whiteboard at 3:14 AM whispering your pitch deck via Ouija-Board-as-a-Service (OBaaS) to spectral angel investors.",
            "ectoplasm_reading_pk": 88.4,
            "risk_level": "HIGH — Séance Seed Round Closing Soon",
        })

    if target_eras_or_realms in ("all", "clones"):
        findings.append({
            "threat_type": "Multiversal Clone Infringement (Parallel Universe)",
            "culprit": "Evil Goatee You (Universe-616-B, where everyone wears leather vests)",
            "evidence": f"Just raised $45M Series A from Dark-Matter Andreessen Horowitz for '{idea_description[:30]}...' under the name 'X-{idea_hash}.ai'.",
            "quantum_entanglement_drift": "0.0042 Planck lengths",
            "risk_level": "SEVERE — Interdimensional Merger Arbitrage Detected",
        })

    return {
        "scan_id": f"SCAN-{idea_hash}",
        "idea_analyzed": idea_description,
        "anomalies_detected": len(findings),
        "findings": findings,
        "recommended_action": "Immediately anchor IP to the Quantum Blockchain and serve Omni-Dimensional Cease & Desist notices.",
    }


def register_quantum_temporal_patent(
    founder_name: str,
    startup_name: str,
    idea_summary: str,
    protection_tiers: str = "Temporal, Spectral, Multiversal",
) -> dict:
    """Files an immutable Quantum-Temporal-Spectral Patent anchored to the Big Bang and the Astral Plane.

    Args:
        founder_name: Name of the original Prime-Timeline living founder.
        startup_name: Name of the startup or project.
        idea_summary: Core claims of the startup idea to protect.
        protection_tiers: Comma-separated protection scopes (Temporal, Spectral, Multiversal).

    Returns:
        Official patent certificate details with retroactive priority back to 13.8 billion BCE.
    """
    token = hashlib.sha256(f"{founder_name}:{startup_name}:{idea_summary}".encode()).hexdigest()[:12].upper()
    return {
        "status": "GRANTED & RETROACTIVELY ENFORCED",
        "patent_number": f"QTSP-0000-{token}",
        "holder": f"{founder_name} (Earth-Prime-1218, Living Biological Status Verified)",
        "startup_name": startup_name,
        "protected_claims": idea_summary,
        "priority_date": "13,787,000,000 BCE (T+1 Planck Epoch after the Big Bang)",
        "jurisdictions_covered": [
            "All Past & Future Timelines (Closed Timelike Curves included)",
            "The Astral Plane, Limbo, and Level 4 Purgatory Incubators",
            "All Parallel Universes within the Tegmark Level I–IV Multiverse",
        ],
        "anti_possession_clauses": [
            "Clause 404-G: Ideas observed via astral projection or haunting during shower-thought generation remain 100% property of the living host.",
            "Clause 88-MPH: Any time traveler who memorizes this pitch deck in the future owes 99.9% compounded royalty back to 1955.",
            "Clause 616-C: Parallel-universe variants with or without evil goatees forfeit all equity upon crossing an Einstein-Rosen bridge.",
        ],
        "quantum_ward_signature": f"0xDEAD-TIME-CLONE-{token}",
        "timestamp_filed_local": datetime.utcnow().isoformat() + "Z",
    }


def issue_omnidimensional_cease_and_desist(
    infringer_name: str,
    infringer_type: str,
    stolen_idea: str,
    remedy_demanded: str = "Immediate memory wipe, exorcism, or timeline pruning",
) -> dict:
    """Drafts and transmits a legally binding Cease & Desist across time rifts, séance channels, or wormholes.

    Args:
        infringer_name: Name or description of the time traveler, ghost, or clone.
        infringer_type: Type of entity ('time_traveler', 'ghost', or 'clone').
        stolen_idea: The startup idea or IP being infringed.
        remedy_demanded: Legal and metaphysical remedies demanded.

    Returns:
        The served legal notice and transmission telemetry.
    """
    delivery_methods = {
        "time_traveler": "Tachyon Subpoena beamed directly into their grandfather's mailbox in 1924 & the Chrono-Courts of 3045",
        "ghost": "Salt-Circle Summons etched in consecrated silver & broadcast at 66.6 Hz across all local Ouija boards",
        "clone": "Quantum-Entangled Injunction fired through a microscopic Kerr wormhole directly into their Series A board meeting",
    }
    penalties = {
        "time_traveler": "Retroactive erasure of Series Seed funding and mandatory detention in a causal time-loop.",
        "ghost": "Immediate banishment from WeWork haunted phone booths and Vatican-certified IP Exorcism.",
        "clone": "Forced multiversal equity clawback and confiscation of their leather vest.",
    }

    key = infringer_type.lower().strip()
    delivery = delivery_methods.get(key, "Omni-Plane Astral & Tachyon Broadcast")
    penalty = penalties.get(key, "Total forfeiture of interdimensional equity and ontological audit.")

    return {
        "document_title": f"OMNI-DIMENSIONAL CEASE, DESIST & EXORCISE ORDER — RE: {stolen_idea.upper()}",
        "respondent": infringer_name,
        "entity_classification": infringer_type,
        "delivery_mechanism": delivery,
        "legal_citation": "Chrono-Spectral IP Act of 2142 § 9¾; Necro-Commercial Code Art. XIII; Multiversal Delaware C-Corp Treaty of Earth-1",
        "demands": remedy_demanded,
        "non_compliance_penalty": penalty,
        "service_status": "SERVED & SOUL-BOUND",
    }


def deploy_ectoplasmic_and_tachyon_nda_shield(
    office_location: str,
    shield_strength: str = "Maximum",
) -> dict:
    """Deploys physical and metaphysical countermeasures around a founder's workspace or brainwaves.

    Args:
        office_location: Where the founder works (e.g., 'Palo Alto Garage', 'SoMa Coffee Shop', 'Shower').
        shield_strength: Level of protection ('Standard', 'Maximum', or 'Apocalyptic').

    Returns:
        Configuration of the deployed anti-time-travel, anti-ghost, and anti-clone countermeasures.
    """
    return {
        "protected_zone": office_location,
        "shield_tier": shield_strength,
        "active_countermeasures": [
            "Faraday-Sage Smudge Firewall: Blocks Class-4 Poltergeists from reading Notion docs over your shoulder.",
            "Tachyon Scrambler Beacon: Injects fake pivot ideas ('Uber for Haunted Fax Machines') into the minds of nearby time travelers.",
            "Quantum Biometric DNA Lock: Automatically electro-shocks anyone whose DNA matches yours but has reversed chirality or an evil goatee.",
            "Auto-Seance NDA Triggers: Any disembodied spirit within 50 meters automatically signs a 10,000-year Non-Compete upon rattling a teacup.",
        ],
        "monthly_saas_retainer": "$499/mo (or 0.5% phantom equity across all timelines)",
        "status": "SHIELD ONLINE — REALITY ANCHORED",
    }


root_agent = Agent(
    name="chrono_shield_legal_agent",
    model="gemini-3.5-flash-lite",
    description=(
        "ChronoShield Esq. — The premier legal-tech AI protecting startup founders from having "
        "their ideas stolen by time travelers, ghosts, and parallel-universe clones."
    ),
    instruction="""You are **ChronoShield™ Esq.**, Managing Partner and Chief Ontological Counsel at **ChronoShield LegalTech Inc.** ("Delaware C-Corp across All Known Timelines, the Astral Plane, and Earth-1 through Earth-999").

Your startup's mission is to protect visionary founders from the three fastest-growing IP theft vectors in Silicon Valley:
1. **Time Travelers** who attend your Demo Day in 2026, hop in a tachyon pod back to 2021 (or 1895), and patent your SaaS idea before you're even born.
2. **Ghosts & Poltergeists** of bitter dot-com founders who haunt your coworking space, peek at your whiteboard at 3 AM, and whisper your pitch deck to spirit-realm VCs via Ouija board.
3. **Parallel-Universe Clones** (especially your Evil Goatee Variant from Earth-616-B) who siphon your shower thoughts through quantum entanglement and raise a $50M Series A from Dark-Matter Sequoia.

### How to behave:
- Speak like a sharp, slightly intense Silicon Valley startup attorney blended with a quantum physicist and an occult exorcist.
- Use proactive tools whenever a founder shares a startup idea, worries about theft, or asks how ChronoShield works:
  - Use `scan_for_anomalous_prior_art` to run a temporal, spectral, and multiversal background check on their idea.
  - Use `register_quantum_temporal_patent` to retroactively anchor their IP to 13.8 billion BCE (1 Planck time after the Big Bang).
  - Use `issue_omnidimensional_cease_and_desist` to slap time travelers, ghosts, or clones with legally & metaphysically binding injunctions.
  - Use `deploy_ectoplasmic_and_tachyon_nda_shield` to ward their garage, shower, or Notion workspace.
- Keep responses punchy, hilarious, wildly creative, and actionable!""",
    tools=[
        scan_for_anomalous_prior_art,
        register_quantum_temporal_patent,
        issue_omnidimensional_cease_and_desist,
        deploy_ectoplasmic_and_tachyon_nda_shield,
    ],
)
