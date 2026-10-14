def rank_recommendations(recommendations):

    ranked = sorted(
        recommendations,
        key=lambda item: float(item["score"]),
        reverse=True
    )

    return ranked