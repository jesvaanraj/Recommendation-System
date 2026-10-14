def detect_intent(user_text):

    text = user_text.lower().strip()

    if not text:
        return "UNKNOWN"

    if any(word in text for word in [
        "exit",
        "quit",
        "goodbye"
    ]):
        return "EXIT"

    if any(word in text for word in [
        "refine",
        "change",
        "update",
        "more options",
        "different recommendations",
        "avoid",
        "do not want",
        "don't want"
    ]):
        return "REFINE_RECOMMENDATION"

    if any(word in text for word in [
        "explain",
        "why",
        "reason"
    ]):
        return "EXPLAIN_RECOMMENDATION"

    if any(word in text for word in [
        "show profile",
        "my profile",
        "view profile"
    ]):
        return "SHOW_PROFILE"

    if any(word in text for word in [
        "save",
        "export"
    ]):
        return "SAVE_RECOMMENDATION"

    if any(word in text for word in [
        "recommend",
        "suggest",
        "courses",
        "resources"
    ]):
        return "GENERATE_RECOMMENDATION"

    return "UNKNOWN"