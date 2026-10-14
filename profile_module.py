def analyze_preferences(profile):

    interests = [
        item.strip()
        for item in profile["interests"].split(",")
        if item.strip()
    ]

    primary_interest = (
        interests[0] if interests else "General Learning"
    )

    secondary_interest = (
        interests[1] if len(interests) > 1 else "None"
    )

    other_interests = interests[2:]

    analysis = {
        "primary_interest": primary_interest,
        "secondary_interest": secondary_interest,
        "other_interests": other_interests,
        "skill_level": profile["skill_level"],
        "goal": profile["goal"],
        "category": profile["category"],
        "preference": profile["preference"],
        "constraints": [
            f"Skill level: {profile['skill_level']}",
            f"Category: {profile['category']}",
            f"Preference: {profile['preference']}"
        ]
    }

    return analysis