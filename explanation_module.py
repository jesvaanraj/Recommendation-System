def add_explanations(recommendations):

    for item in recommendations:

        if not item.get("reason"):

            item["reason"] = (
                "Recommended based on the user's "
                "interests, skill level and learning goal."
            )

    return recommendations