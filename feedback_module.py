from prompt_module import construct_refinement_prompt


def refine_prompt(
    profile,
    analysis,
    feedback,
    previous_recommendations
):

    return construct_refinement_prompt(
        profile,
        analysis,
        feedback,
        previous_recommendations
    )