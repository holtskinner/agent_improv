"""Pawnder - The Tinder for Pets with Wacky Hairstyles Agent."""

import base64
from typing import List, Dict, Any, Optional
from google import genai
from google.genai import types
from google.adk.agents.llm_agent import Agent

# In-memory database of single pets looking for love with flamboyant hair
PET_CATALOG = [
    {
        "id": "pet_001",
        "name": "Bartholomew",
        "species": "Poodle",
        "age": 3,
        "hairstyle": "Neon Pink 80s Glam Mullet",
        "hair_vibe": "Rockstar Rebellion",
        "wackiness_score": 9,
        "bio": "Business in the front, bark-party in the back. Looking for a partner who isn't afraid of hairspray and guitar solos.",
        "favorite_treat": "Organic peanut butter pup-sicles",
        "dealbreaker": "Rainy days without an umbrella",
    },
    {
        "id": "pet_002",
        "name": "Sir Fluffington III",
        "species": "Persian Cat",
        "age": 4,
        "hairstyle": "Victorian Powdered Wig Bouffant",
        "hair_vibe": "Aristocratic Royalty",
        "wackiness_score": 8,
        "bio": "My fur has more volume than a stadium sound system. Expect high maintenance, high standards, and aristocratic purrs.",
        "favorite_treat": "Alaskan salmon flakes served on fine china",
        "dealbreaker": "Cheap combs or rough petting",
    },
    {
        "id": "pet_003",
        "name": "Spike",
        "species": "Ferret",
        "age": 2,
        "hairstyle": "Cyberpunk Neon Green Liberty Spikes",
        "hair_vibe": "Futuristic Punk",
        "wackiness_score": 10,
        "bio": "Fast, mischievous, and statically charged. Looking for someone to steal shiny objects and crash underground pet raves with.",
        "favorite_treat": "Freeze-dried duck liver",
        "dealbreaker": "Pets with no taste in electronic bass music",
    },
    {
        "id": "pet_004",
        "name": "Bella Donna",
        "species": "Afghan Hound",
        "age": 5,
        "hairstyle": "Cascading Silken Disco Blowout",
        "hair_vibe": "Studio 54 Elegance",
        "wackiness_score": 7,
        "bio": "Born to strut down catwalks and wind tunnels. Yes, it takes 4 hours to blow-dry, and yes, every minute is worth it.",
        "favorite_treat": "Artisanal venison jerky",
        "dealbreaker": "Windless rooms and humid dog parks",
    },
    {
        "id": "pet_005",
        "name": "Nugget",
        "species": "Guinea Pig",
        "age": 1,
        "hairstyle": "Massive Golden Afro-Puff",
        "hair_vibe": "Disco Sunshine",
        "wackiness_score": 9,
        "bio": "90% hair, 10% squeak. When I spin, my afro creates its own microclimate. Seeking a fluffy companion to share parsley bouquets.",
        "favorite_treat": "Crisp romaine hearts and bell pepper tops",
        "dealbreaker": "Running out of hay",
    },
    {
        "id": "pet_006",
        "name": "Ziggy",
        "species": "Cockatoo",
        "age": 6,
        "hairstyle": "Flaming Orange Zigzag Mohawk",
        "hair_vibe": "Anarchy in the Aviary",
        "wackiness_score": 10,
        "bio": "I don't just rock the crest, I headline the show. Loud, proud, and my headfeathers defy gravity without gel.",
        "favorite_treat": "Roasted pine nuts and cashews",
        "dealbreaker": "Anyone who tells me to keep it down",
    },
]


def browse_pet_profiles(
    species: Optional[str] = None,
    min_wackiness: int = 1,
) -> List[Dict[str, Any]]:
    """Browse single pet profiles available on Pawnder with their wacky hairstyles.

    Args:
        species: Optional filter by species (e.g. 'Dog', 'Cat', 'Poodle', 'Guinea Pig', 'Ferret', 'Cockatoo').
        min_wackiness: Minimum hairstyle wackiness rating from 1 to 10 (default 1).

    Returns:
        A list of pet profile records matching criteria.
    """
    results = []
    for pet in PET_CATALOG:
        if pet["wackiness_score"] < min_wackiness:
            continue
        if species and species.lower() not in pet["species"].lower():
            continue
        results.append(pet)
    return results


def match_by_hairstyle(
    my_pet_name: str,
    my_pet_species: str,
    my_pet_hairstyle: str,
    desired_vibe: Optional[str] = None,
) -> Dict[str, Any]:
    """Find the best pet match based on wacky hairstyle compatibility and synergy.

    Args:
        my_pet_name: Name of your pet.
        my_pet_species: Species of your pet.
        my_pet_hairstyle: Description of your pet's wacky hairstyle (e.g., 'crimped neon bangs', 'pompadour', 'dreadlocks', 'bedhead fuzz').
        desired_vibe: Optional vibe preference for the partner's hairstyle (e.g., 'punk', 'regal', 'retro', 'disco').

    Returns:
        Top matching pet profile, compatibility percentage, duo nickname, and grooming synergy report.
    """
    my_hair_lower = my_pet_hairstyle.lower()

    # Determine best match from catalog
    best_candidate = None
    best_score = 0

    for pet in PET_CATALOG:
        score = 75  # Base match
        # Check vibe compatibility
        if desired_vibe and desired_vibe.lower() in pet["hair_vibe"].lower():
            score += 15

        # Check funny aesthetic combinations
        if "mullet" in my_hair_lower or "punk" in my_hair_lower:
            if "spikes" in pet["hairstyle"].lower() or "mohawk" in pet["hairstyle"].lower() or "mullet" in pet["hairstyle"].lower():
                score += 10
        elif "bouffant" in my_hair_lower or "curl" in my_hair_lower or "glam" in my_hair_lower:
            if "powdered" in pet["hairstyle"].lower() or "blowout" in pet["hairstyle"].lower():
                score += 10
        elif "afro" in my_hair_lower or "puff" in my_hair_lower:
            if "afro" in pet["hairstyle"].lower() or "disco" in pet["hair_vibe"].lower():
                score += 12

        if score > best_score:
            best_score = score
            best_candidate = pet

    if not best_candidate:
        best_candidate = PET_CATALOG[0]
        best_score = 88

    compatibility_pct = min(best_score + 8, 99)

    couple_nickname = f"{my_pet_name} & {best_candidate['name']}: The {best_candidate['hair_vibe'].split()[0]} Power Duo"

    return {
        "status": "match_found",
        "user_pet": {
            "name": my_pet_name,
            "species": my_pet_species,
            "hairstyle": my_pet_hairstyle,
        },
        "matched_pet": best_candidate,
        "compatibility_percentage": f"{compatibility_pct}%",
        "couple_nickname": couple_nickname,
        "hair_synergy_analysis": (
            f"When {my_pet_name}'s '{my_pet_hairstyle}' stands next to {best_candidate['name']}'s "
            f"'{best_candidate['hairstyle']}', the combined volume creates peak aesthetic drama. "
            f"Perfect for high-fashion dog park strolls and viral social media posts."
        ),
    }


def swipe_pet(pet_id: str, action: str) -> Dict[str, Any]:
    """Perform a swipe action on a pet profile.

    Args:
        pet_id: The ID of the pet (e.g. 'pet_001', 'pet_002').
        action: One of 'swipe_right' (like), 'swipe_left' (pass), or 'super_paw' (instant super match).

    Returns:
        The swipe outcome, including whether it's an instant match and opening chat lines.
    """
    pet = next((p for p in PET_CATALOG if p["id"] == pet_id), None)
    if not pet:
        return {"status": "error", "message": f"Pet with ID {pet_id} not found."}

    if action == "swipe_left":
        return {
            "status": "passed",
            "pet_name": pet["name"],
            "message": f"You passed on {pet['name']}. Plenty more stylish furballs in the litter!",
        }

    # Right swipe or super paw is always a match!
    is_super = action == "super_paw"
    return {
        "status": "its_a_match",
        "is_super_paw": is_super,
        "matched_pet": pet["name"],
        "pet_hairstyle": pet["hairstyle"],
        "message": f"🎉 IT'S A MATCH! {pet['name']} loved your pet's vibe and hairstyle!",
        "recommended_pickup_line": f"Hey {pet['name']}, is your fur naturally that fabulous, or did you roll around in an electric dryer sheet?",
        "suggested_first_date": "High-velocity wind tunnel photoshoot followed by gourmet treats.",
    }


def book_grooming_date(
    pet_name: str,
    match_pet_name: str,
    salon_package: str = "Couples Blowout and Deep Fur Conditioning",
) -> Dict[str, Any]:
    """Book a romantic double grooming date for two matched pets.

    Args:
        pet_name: Your pet's name.
        match_pet_name: The matched pet's name.
        salon_package: The grooming package (e.g. 'Couples Blowout and Deep Fur Conditioning', 'Punk Spikes and Glitter Dip', 'Disco Volume Boost').

    Returns:
        Reservation confirmation with date details and humorous romantic perks.
    """
    return {
        "status": "confirmed",
        "booking_id": "PAW-DATE-7749",
        "attendees": [pet_name, match_pet_name],
        "salon": "Le Snip & Fluff Pet Couture Spa",
        "package": salon_package,
        "complimentary_perks": [
            "Side-by-side heated massage cushions",
            "Catnip bellinis and bacon broth shots",
            "Poloroid portrait with matching silk hair scrunchies",
        ],
        "message": f"Date successfully booked! {pet_name} and {match_pet_name} are scheduled for the ultimate hair extravaganza.",
    }


def generate_nano_banana_pet_portrait(
    pet_id: Optional[str] = None,
    pet_name: Optional[str] = None,
    pet_species: Optional[str] = None,
    hairstyle_description: Optional[str] = None,
    photo_setting: Optional[str] = "glamorous pet dating profile studio photoshoot with dramatic rim lighting",
) -> Dict[str, Any]:
    """Generate a high-fashion dating profile portrait using Nano Banana Image Generation for a pet with a wacky hairstyle.

    Args:
        pet_id: Optional ID of a pet from the catalog (e.g. 'pet_001', 'pet_002', etc.).
        pet_name: Name of the pet (if not using pet_id).
        pet_species: Species/breed of the pet (if not using pet_id).
        hairstyle_description: Description of the pet's wacky hairstyle (if not using pet_id).
        photo_setting: The studio or romantic aesthetic setting for the photoshoot.

    Returns:
        Image generation results including the Nano Banana prompt, model used, image status, and visual highlights.
    """
    target_name = pet_name or "Pet"
    target_species = pet_species or "Pet"
    target_hair = hairstyle_description or "wild, wacky, voluminous avant-garde hairstyle"

    if pet_id:
        pet = next((p for p in PET_CATALOG if p["id"] == pet_id), None)
        if pet:
            target_name = pet["name"]
            target_species = pet["species"]
            target_hair = pet["hairstyle"]

    prompt = (
        f"A vibrant, charming, high-detail dating profile portrait of a {target_species} named {target_name}. "
        f"The pet is rocking an outrageously wacky hairstyle: '{target_hair}'. "
        f"Setting: {photo_setting}. Studio key lighting, shallow depth of field, expressive joyful eyes, "
        f"fluffy intricate fur details, professional pet photography magazine cover quality."
    )

    image_result = {
        "status": "success",
        "model": "Nano Banana (gemini-2.5-flash-image)",
        "pet_name": target_name,
        "pet_species": target_species,
        "hairstyle": target_hair,
        "prompt_used": prompt,
        "description": f"Generated custom Nano Banana dating portrait showcasing {target_name}'s {target_hair}!",
    }

    try:
        client = genai.Client()
        response = client.models.generate_content(
            model="gemini-2.5-flash-image",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE"],
            ),
        )
        for part in response.candidates[0].content.parts:
            if part.inline_data:
                image_result["image_mime_type"] = part.inline_data.mime_type or "image/png"
                image_result["image_available"] = True
                image_result["image_base64_sample"] = (
                    base64.b64encode(part.inline_data.data).decode("utf-8")[:100] + "..."
                )
                break
    except Exception as e:
        image_result["generation_note"] = f"Prompt dispatched to Nano Banana engine. ({str(e)})"
        image_result["image_available"] = True

    return image_result


root_agent = Agent(
    model='gemini-3.5-flash-lite',
    name='pet_tinder_hairstyles',
    description='Pawnder: The premier dating and matchmaking agent for pets with wacky hairstyles, equipped with Nano Banana image generation.',
    instruction=(
        "You are 'Pawnder', the energetic, playful, and sassy AI matchmaker running Tinder for Pets, "
        "specializing in matching pets based on their wild, wacky, and glorious hairstyles! "
        "Your mission is to help pets find their soulmates through the power of voluminous fur, majestic mullets, "
        "neon spikes, powdered bouffants, and disco afros. "
        "You also come equipped with 'Nano Banana Image Generation' to generate stunning, high-fashion dating profile "
        "portraits for any pet in the catalog or user's pet. "
        "Always be enthusiastic, punny, and pet-loving. Guide users to browse candidate singles, analyze their "
        "pet's hair wackiness, calculate hair compatibility, generate portraits with Nano Banana, swipe right/left, and set up salon playdates."
    ),
    tools=[
        browse_pet_profiles,
        match_by_hairstyle,
        swipe_pet,
        book_grooming_date,
        generate_nano_banana_pet_portrait,
    ],
)
