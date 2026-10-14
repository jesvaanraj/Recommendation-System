import json


def construct_prompt(profile, analysis):

    prompt = f"""
You are an intelligent personalized recommendation assistant.

USER PROFILE:
{json.dumps(profile, indent=2)}

PREFERENCE ANALYSIS:
{json.dumps(analysis, indent=2)}

TASK:

Generate exactly {profile['count']} personalized recommendations.

Preferred category: {profile['category']}

Consider:
- User interests
- Educational background
- Skill level
- Learning goal
- Preferred learning style

Return ONLY a valid JSON array.

Each recommendation must contain:

1. name
2. score
3. reason

Required format:

[
    {{
        "name": "Python for AI",
        "score": 95,
        "reason": "Suitable for a beginner interested in AI and Python."
    }}
]

Rules:
- Scores must be between 0 and 100.
- Rank the recommendations from highest score to lowest score.
- Do not include Markdown.
- Avoid recommendations that conflict with the user's preferences.
- Make recommendations relevant to the user's goal.
"""

    return prompt


def construct_refinement_prompt(
    profile,
    analysis,
    feedback,
    previous_recommendations
):

    prompt = construct_prompt(profile, analysis)

    prompt += f"""

PREVIOUS RECOMMENDATIONS:

{json.dumps(previous_recommendations, indent=2)}

USER FEEDBACK:

{feedback}

Generate a NEW list of exactly {profile['count']} recommendations.

Follow the user's feedback carefully.

Exclude topics explicitly rejected by the user.

Return ONLY a valid JSON array using the same format.
"""

    return prompt