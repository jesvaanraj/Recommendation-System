import json
from pathlib import Path
from datetime import datetime


OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"


def save_profile(profile):

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    output_file = OUTPUT_DIR / "user_profile.json"

    with output_file.open(
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            profile,
            file,
            indent=4,
            ensure_ascii=False
        )

    return str(output_file)


def save_recommendations(recommendations, profile=None):

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    output_file = OUTPUT_DIR / "recommendations.txt"

    with output_file.open(
        "w",
        encoding="utf-8"
    ) as file:

        file.write("PERSONALIZED RECOMMENDATIONS\n")
        file.write("=" * 40 + "\n\n")

        if profile:

            file.write(f"Name: {profile['name']}\n")
            file.write(f"Interests: {profile['interests']}\n")
            file.write(f"Goal: {profile['goal']}\n")

        file.write(
            f"Saved at: {datetime.now().isoformat()}\n\n"
        )

        for rank, item in enumerate(
            recommendations,
            start=1
        ):

            file.write(f"Rank: {rank}\n")
            file.write(f"Name: {item['name']}\n")
            file.write(f"Score: {item['score']}%\n")
            file.write(f"Reason: {item['reason']}\n")
            file.write("-" * 40 + "\n")

    return str(output_file)