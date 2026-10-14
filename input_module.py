def build_profile_from_form(form):

    name = form.get("name", "").strip()
    age_text = form.get("age", "").strip()
    background = form.get("background", "").strip()
    interests = form.get("interests", "").strip()
    skill_level = form.get("skill_level", "Beginner").strip()
    category = form.get("category", "Courses").strip()
    preference = form.get("preference", "").strip()
    goal = form.get("goal", "").strip()
    count_text = form.get("count", "5").strip()

    if not all([
        name,
        age_text,
        background,
        interests,
        preference,
        goal
    ]):
        raise ValueError(
            "Please complete all required fields."
        )

    try:
        age = int(age_text)
        count = int(count_text)

    except ValueError:
        raise ValueError(
            "Age and recommendation count must be numbers."
        )

    if age < 1 or age > 120:
        raise ValueError("Please enter a valid age.")

    if count < 1 or count > 10:
        raise ValueError(
            "Choose between 1 and 10 recommendations."
        )

    return {
        "name": name,
        "age": age,
        "background": background,
        "interests": interests,
        "skill_level": skill_level,
        "category": category,
        "preference": preference,
        "goal": goal,
        "count": count
    }