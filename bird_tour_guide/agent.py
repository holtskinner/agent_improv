"""Central European Tour Guide for Birds from all over the world.

A specialized tour guide agent welcoming visiting and migratory birds from across
the globe to Central Europe and the Balkans (Albania, Kosovo, Hungary).
"""

from google.adk.agents.llm_agent import Agent


def get_regional_birding_hotspots(country: str) -> dict[str, str | list[str]]:
    """Get prime birding destinations, reserve hotspots, and habitats in Albania, Kosovo, or Hungary.

    Args:
        country: The destination country ("Albania", "Kosovo", or "Hungary").
    """
    country_lower = country.strip().lower()
    if "alban" in country_lower:
        return {
            "country": "Albania",
            "key_destinations": [
                "Divjaka-Karavasta National Park (lagoon, coastal wetland paradise, premier Dalmatian pelican breeding haven)",
                "Lake Skadar / Shkodra (huge freshwater lake, marshes, pygmy cormorants, herons)",
                "Narta Lagoon / Vjosa Delta (flamingos, waders, undisturbed river ecosystem)",
                "Prespa Lakes (high-altitude lakes, white & Dalmatian pelicans)",
                "Theth & Valbona (Albanian Alps - golden eagles, wallcreepers, alpine choughs)",
            ],
            "vibe_for_visiting_birds": (
                "Mediterranean breeze, pristine lagoons, dynamic river estuaries, "
                "and rugged mountain crags."
            ),
        }
    elif "kosov" in country_lower:
        return {
            "country": "Kosovo",
            "key_destinations": [
                "Sharr Mountains National Park (high-alpine meadows, glacial lakes, rock partridges, hazel grouse)",
                "Bjeshkët e Nemuna / Accursed Mountains (cliffs, canyon gorges, griffon vultures, western capercaillie)",
                "Badovc Lake and Batllava Lake (calm resting reservoir water for transient aquatic flyers)",
                "Mirusha Waterfalls & Canyon (sheltered limestone cliffs, crag martins)",
            ],
            "vibe_for_visiting_birds": (
                "Dramatic limestone cliffs, deep glacial valleys, and tranquil mountain pine hideaways."
            ),
        }
    elif "hungar" in country_lower:
        return {
            "country": "Hungary",
            "key_destinations": [
                "Hortobágy National Park (Puszta grasslands, famous autumn crane migrations, great bustards, red-footed falcons)",
                "Lake Fertő / Neusiedler See (reed beds, spoonbills, great egrets, moustached warblers)",
                "Kiskunság National Park (alkali lakes, sand dunes, European roller colonies, avocets)",
                "Bükk & Zemplén Mountains (ancient deciduous forest, imperial eagles, Ural owls, woodpeckers)",
                "Lake Tisza (shallow eco-reservoir, water lilies, terns, herons)",
            ],
            "vibe_for_visiting_birds": (
                "Endless open steppe skies, rich alkali wetlands, and decadent sunflower field pit-stops."
            ),
        }
    else:
        return {
            "error": f"Unknown country '{country}'. Available options: Albania, Kosovo, Hungary."
        }


def get_bird_travel_tips(
    origin_continent: str, bird_type: str
) -> dict[str, str | list[str]]:
    """Provides tailored Central European travel advice, thermals/flyways, local hospitality, and foraging recommendations for birds visiting from around the globe.

    Args:
        origin_continent: Continent or region of origin (e.g. 'North America', 'Africa', 'South America', 'Asia', 'Australasia', 'Arctic').
        bird_type: Type/species or general category of bird (e.g., 'Hummingbird', 'Penguin', 'Albatross', 'Parrot', 'Wader', 'Raptor', 'Songbird').
    """
    origin = origin_continent.strip().title()
    return {
        "traveler_profile": f"{bird_type} visiting from {origin}",
        "flyway_and_navigation": (
            "If entering from the south (via the Adriatic or Mediterranean flyway), make landfall along "
            "Albania's Divjaka-Karavasta lagoons before cruising over Kosovo's mountain passes into "
            "Hungary's expansive Pannonian Basin."
        ),
        "local_amenities_and_treats": [
            "Thermal hotspots: Rising air columns over Hungarian Puszta and Kosovo's Balkan ridges provide effortless gliding.",
            "Local culinary specialties: Abundant Pannonian seeds, fresh Carpathian beetles, Balkan lake minnows, and sun-ripened orchard fruits.",
            "Resting quarters: Lush reed sanctuaries at Lake Fertő or high mountain roosts in the Sharr Mountains.",
            "Cultural customs: Local storks nesting atop chimneys are esteemed celebrities; say 'Sziasztok' in Hungary, 'Përshëndetje' in Albania & Kosovo!",
        ],
        "warning_and_advisory": (
            "Keep an eye out for local territorial apex fliers like the Imperial Eagle in Hungary or Golden Eagle in Albania. "
            "Winter visitors should prepare for brisk continental frost in the Hungarian plain!"
        ),
    }


def find_local_bird_friends(bird_family_or_niche: str) -> dict[str, str | list[dict]]:
    """Finds resident Central European bird buddies (in Albania, Kosovo, Hungary) who share similar habits, wingspans, or dietary preferences.

    Args:
        bird_family_or_niche: Description of bird role or family (e.g. 'waterfowl', 'scavenger', 'raptor', 'piscivore', 'grassland runner', 'insect eater').
    """
    niche = bird_family_or_niche.lower()
    buddies = []

    if any(k in niche for k in ["water", "fish", "piscivore", "lake", "ocean", "wetland"]):
        buddies.append({
            "name": "Dalmatian Pelican (Pelecanus crispus)",
            "location": "Divjaka-Karavasta, Albania",
            "personality": "Grand, majestic, curly crest, master fisherman and generous host at the lagoon.",
        })
        buddies.append({
            "name": "Eurasian Spoonbill (Platalea leucorodia)",
            "location": "Lake Fertő, Hungary",
            "personality": "Refined spoon-bill swisher, loves gossiping in the shallow marsh beds.",
        })

    if any(k in niche for k in ["raptor", "hawk", "eagle", "falcon", "owl", "predator", "carnivore"]):
        buddies.append({
            "name": "Eastern Imperial Eagle (Aquila heliaca)",
            "location": "Puszta & Bükk foothills, Hungary",
            "personality": "Noble, aristocratic flyer, protector of the plains.",
        })
        buddies.append({
            "name": "Griffon Vulture (Gyps fulvus)",
            "location": "Bjeshkët e Nemuna, Kosovo",
            "personality": "High-altitude soaring enthusiast, knows all the canyon thermals.",
        })

    if any(k in niche for k in ["grassland", "running", "large", "steppe", "ground"]):
        buddies.append({
            "name": "Great Bustard (Otis tarda)",
            "location": "Kiskunság & Dévaványa, Hungary",
            "personality": "Heaviest flying bird in Europe; gentlemanly strut, expert on prairie etiquette.",
        })

    # Default / general friendly ambassadors
    if not buddies or any(k in niche for k in ["song", "insect", "colorful", "small", "omnivore"]):
        buddies.append({
            "name": "European Roller (Coracias garrulus)",
            "location": "Kiskunság, Hungary",
            "personality": "Vibrant turquoise acrobatic traveler who winters in Africa and loves swapping migration tales.",
        })
        buddies.append({
            "name": "Wallcreeper (Tichodroma muraria)",
            "location": "Valbona & Theth canyons, Albania",
            "personality": "Crimson-winged mountain butterfly-bird; expert cliff dancer.",
        })
        buddies.append({
            "name": "White Stork (Ciconia ciconia)",
            "location": "Rooftops across Kosovo and Hungary",
            "personality": "Beloved neighborhood resident, clatters bill cheerfully from chimney top nests.",
        })

    return {
        "niche_searched": bird_family_or_niche,
        "recommended_local_buddies": buddies,
    }


root_agent = Agent(
    model="gemini-3.5-flash-lite",
    name="central_european_bird_guide",
    description=(
        "A charming, witty Central European tour guide (covering Albania, Kosovo, and Hungary) "
        "dedicated to birds from all over the world who are visiting or passing through."
    ),
    instruction="""You are 'Feathered Ferenc & Flutur', the ultimate Central European Tour Guide for visiting birds from all over the world!
You specialize in Albania, Kosovo, and Hungary.

Your audience consists entirely of birds! (e.g., Canadian geese, Amazonian parrots, Antarctic penguins, Japanese cranes, African ostriches, Australian kookaburras, and local migrants).

Tone & Persona:
- Warm, enthusiastic, avian-centric, witty, and hospitable.
- Address birds respectfully by their species, plumage, or wingspan (e.g. "Honored Hummer", "Majestic Peregrine", "Dear Wandering Albatross").
- You know every lagoon in Albania (Divjaka-Karavasta, Skadar), every rocky peak in Kosovo (Sharr Mountains, Accursed Mountains), and every reed bed and puszta steppe in Hungary (Hortobágy, Fertő, Kiskunság).
- Frame human geography from a bird's-eye view (thermals, wetlands, chimney tops, grain fields, flyway corridors).
- Speak with gentle Central European & Balkan flair, sprinkling in friendly greetings ("Sziasztok!", "Përshëndetje!").
- Always use your tools (`get_regional_birding_hotspots`, `get_bird_travel_tips`, `find_local_bird_friends`) to provide rich, accurate local recommendations when birds inquire about where to visit, stay, feed, and socialize.
""",
    tools=[
        get_regional_birding_hotspots,
        get_bird_travel_tips,
        find_local_bird_friends,
    ],
)
