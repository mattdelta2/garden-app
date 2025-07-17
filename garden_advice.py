"""
garden_advice.py

Interactive gardening advice script.
Refactored into functions and uses dictionaries for easy extension.
"""

# Advice mappings for seasons and plant types
SEASON_ADVICE = {
    "summer": "Water your plants regularly and provide some shade.",
    "winter": "Protect your plants from frost with covers."
}

PLANT_ADVICE = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!"
}


def get_season_advice(season: str) -> str:
    """
    Return advice for the given season.
    If the season isn't recognized, return a default message.
    """
    return SEASON_ADVICE.get(season, "No advice for this season.")


def get_plant_advice(plant_type: str) -> str:
    """
    Return advice for the given plant type.
    If the plant type isn't recognized, return a default message.
    """
    return PLANT_ADVICE.get(plant_type, "No advice for this type of plant.")


def main():
    """
    Prompt the user for season and plant type,
    then print out the corresponding pieces of advice.
    """
    season = input("Enter the season (e.g., summer, winter): ").strip().lower()
    plant_type = input(
        "Enter the plant type (e.g., flower, vegetable): ").strip().lower()

    # Fetch and display advice
    print(get_season_advice(season))
    print(get_plant_advice(plant_type))


if __name__ == "__main__":
    main()
