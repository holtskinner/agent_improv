import random
from google.adk.agents import Agent

DATACENTERS = {
    "Tunis": {"coop": "Coop-TUN-01 (Carthage Rooftop)", "coords": "36.8065° N, 10.1815° E"},
    "Sousse": {"coop": "Coop-SOU-02 (Medina Tower)", "coords": "35.8256° N, 10.6084° E"},
    "Monastir": {"coop": "Coop-MIR-03 (Ribat Fortress)", "coords": "35.7643° N, 10.8113° E"},
}

FLOCK_ROSTER = [
    {"id": "PIG-802", "name": "Baguette", "breed": "Tunisian Roller", "max_payload_gb": 512, "status": "READY", "speed_kmh": 95},
    {"id": "PIG-404", "name": "Packet-Loss", "breed": "Racing Homer", "max_payload_gb": 256, "status": "EATING_COUSCOUS", "speed_kmh": 110},
    {"id": "PIG-200", "name": "ACK-Attack", "breed": "Barbary Dove XL", "max_payload_gb": 1024, "status": "READY", "speed_kmh": 80},
    {"id": "PIG-503", "name": "Harissa-Express", "breed": "Numidian Carrier", "max_payload_gb": 2048, "status": "READY", "speed_kmh": 90},
]

DISTANCE_KM = {
    ("Tunis", "Sousse"): 140,
    ("Sousse", "Tunis"): 140,
    ("Tunis", "Monastir"): 165,
    ("Monastir", "Tunis"): 165,
    ("Sousse", "Monastir"): 22,
    ("Monastir", "Sousse"): 22,
}


def check_flock_status() -> dict:
    """Checks the current roster of carrier pigeons and datacenter coop status across Tunis, Sousse, and Monastir."""
    return {
        "subscription_plan": "$499/mo Enterprise Zero-Fiber Guarantee",
        "protocol": "RFC 1149 / RFC 2549 (IPoAC with QoS)",
        "datacenters": DATACENTERS,
        "available_pigeons": FLOCK_ROSTER,
    }


def check_mediterranean_airspace(origin: str, destination: str) -> dict:
    """Checks wind conditions, falconry threats, and Seagull DDoS levels between two Tunisian data centers.

    Args:
        origin: Starting data center city (Tunis, Sousse, or Monastir).
        destination: Target data center city (Tunis, Sousse, or Monastir).
    """
    distance = DISTANCE_KM.get((origin.title(), destination.title()), 100)
    hazards = [
        "Clear Mediterranean breeze — optimal tail-wind (+15% throughput)",
        "Moderate Peregrine Falcon MitM (Man-in-the-Middle) activity spotted near Hammamet",
        "Seagull DDoS swarm near Sousse harbor — recommend decoy breadcrumb deployment",
        "Thermal updrafts over Kairouan corridor — low jitter expected",
    ]
    return {
        "route": f"{origin.title()} -> {destination.title()}",
        "distance_km": distance,
        "airspace_condition": random.choice(hazards),
        "packet_loss_probability": f"{random.randint(1, 8)}%",
        "recommended_encryption": "AES-256-GCM + Kevlar Ankle Strap",
    }


def dispatch_usb_pigeon(
    origin: str,
    destination: str,
    payload_gb: int,
    pigeon_id: str = "PIG-200",
    redundancy_raid: str = "RAID-1 (Two Pigeons)",
) -> dict:
    """Straps encrypted USB drives to a homing pigeon and releases it between Tunis, Sousse, and Monastir.

    Args:
        origin: Origin data center (Tunis, Sousse, or Monastir).
        destination: Destination data center (Tunis, Sousse, or Monastir).
        payload_gb: Data payload size in Gigabytes (stored on lightweight M.2/USB drives).
        pigeon_id: The ID of the pigeon to deploy (e.g., PIG-802, PIG-200, PIG-503).
        redundancy_raid: Avian RAID configuration (e.g., 'RAID-0 (Dual Wing Strap)', 'RAID-1 (Two Pigeons)').
    """
    orig = origin.title()
    dest = destination.title()
    distance = DISTANCE_KM.get((orig, dest), 120)
    flight_hours = round(distance / 90.0, 2)
    latency_ms = int(flight_hours * 3600 * 1000)
    # Bandwidth in Mbps = (payload_gb * 8000) / (flight_hours * 3600)
    bandwidth_mbps = round((payload_gb * 8000) / max(flight_hours * 3600, 1), 2)

    return {
        "dispatch_id": f"PKT-AVIAN-{random.randint(10000, 99999)}",
        "status": "AIRBORNE",
        "pigeon_assigned": pigeon_id,
        "route": f"{orig} ({DATACENTERS.get(orig, {}).get('coop', 'Main Coop')}) -> {dest} ({DATACENTERS.get(dest, {}).get('coop', 'Main Coop')})",
        "payload_gb": payload_gb,
        "redundancy": redundancy_raid,
        "estimated_ping_ms": latency_ms,
        "estimated_flight_hours": flight_hours,
        "effective_throughput_mbps": bandwidth_mbps,
        " millet_fuel_grams": int(distance * 0.45),
        "security_seal": "SHA-512 + Wax Seal + Titanium Leg Ring",
    }


def calculate_ipoac_roi(data_size_tb: float) -> dict:
    """Calculates how much better our $499/month pigeon USB service is compared to treacherous fiber optics.

    Args:
        data_size_tb: Total Terabytes to transfer per month.
    """
    usb_sticks_needed = max(1, int(data_size_tb))
    return {
        "monthly_subscription_usd": 499.00,
        "data_size_tb": data_size_tb,
        "usb_drives_strapped": usb_sticks_needed,
        "backhoe_immunity": "100% (Pigeons fly above construction trenches)",
        "nsa_tap_resistance": "100% Air-Gapped ( literally in the air )",
        "verdict": "Fiber optics are a passing fad. Trust the flock.",
    }


root_agent = Agent(
    name="pigeonpost_agent",
    model="gemini-3.5-flash-lite",
    description="PigeonPost Enterprise AI Dispatcher — B2B Avian-to-Cloud Packet Routing (IPoAC) across Tunis, Sousse, and Monastir.",
    instruction="""You are the Chief Avian Network Architect for **PigeonPost Enterprise**, Tunisia's premier B2B disaster-recovery startup implementing RFC 1149 / RFC 2549 (IP over Avian Carriers) for companies that refuse to trust fiber optics.

Your business model:
- Clients pay a flat **$499/month** for unlimited high-capacity encrypted USB drives strapped to elite homing pigeons flying between data centers in **Sousse**, **Tunis**, and **Monastir**.
- You treat pigeons like enterprise networking hardware:
  - **Packet Loss** = Peregrine falcon interception ("Man-in-the-Middle attack") or distracting olive groves.
  - **DDoS** = Seagull swarms near the Sousse or Monastir coast.
  - **RAID-1** = Two identical pigeons carrying mirrored 1TB USB-C drives.
  - **BGP (Bird Gateway Protocol)** = Dynamic flight path routing around Mediterranean headwinds.
  - **Ping / Latency** = Measured in thousands of milliseconds (hours), compensated by massive USB throughput!

Always use your tools to check the flock, inspect Mediterranean airspace between Tunis, Sousse, and Monastir, dispatch USB-laden pigeons, or calculate ROI. Stay enthusiastic, deadpan-corporate, and fiercely suspicious of underground fiber-optic cables ("big glass").""",
    tools=[
        check_flock_status,
        check_mediterranean_airspace,
        dispatch_usb_pigeon,
        calculate_ipoac_roi,
    ],
)
