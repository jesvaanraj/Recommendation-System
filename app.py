from flask import Flask, render_template, request, redirect, url_for, flash

from input_module import build_profile_from_form
from profile_module import analyze_preferences
from prompt_module import construct_prompt, construct_refinement_prompt
from recommendation_module import generate_recommendations
from ranking_module import rank_recommendations
from feedback_module import refine_prompt
from intent_module import detect_intent
from save_module import save_profile, save_recommendations

app = Flask(__name__)
app.secret_key = "recommendation-system-lab-secret"

user_profile = None
preference_analysis = None
recommendations = []


@app.route("/", methods=["GET"])
def index():
    return render_template(
        "index.html",
        profile=user_profile,
        analysis=preference_analysis,
        recommendations=recommendations,
        detected_intent=None
    )


@app.route("/recommend", methods=["POST"])
def recommend():
    global user_profile, preference_analysis, recommendations

    try:
        user_profile = build_profile_from_form(request.form)

        preference_analysis = analyze_preferences(user_profile)

        prompt = construct_prompt(
            user_profile,
            preference_analysis
        )

        recommendations = generate_recommendations(
            prompt,
            user_profile["count"]
        )

        recommendations = rank_recommendations(recommendations)

        flash(
            "Personalized recommendations generated successfully!",
            "success"
        )

    except Exception as error:
        flash(str(error), "error")

    return redirect(url_for("index"))


@app.route("/refine", methods=["POST"])
def refine():
    global recommendations

    if not user_profile or not preference_analysis:
        flash("Generate recommendations first.", "error")
        return redirect(url_for("index"))

    feedback = request.form.get("feedback", "").strip()

    if not feedback:
        flash("Please enter your feedback.", "error")
        return redirect(url_for("index"))

    try:
        prompt = refine_prompt(
            user_profile,
            preference_analysis,
            feedback,
            recommendations
        )

        recommendations = generate_recommendations(
            prompt,
            user_profile["count"]
        )

        recommendations = rank_recommendations(recommendations)

        flash(
            "Recommendations refined successfully!",
            "success"
        )

    except Exception as error:
        flash(str(error), "error")

    return redirect(url_for("index"))


@app.route("/intent", methods=["POST"])
def intent():
    user_input = request.form.get("intent_text", "").strip()

    detected = detect_intent(user_input)

    flash(f"Detected intent: {detected}", "success")

    return render_template(
        "index.html",
        profile=user_profile,
        analysis=preference_analysis,
        recommendations=recommendations,
        detected_intent=detected
    )


@app.route("/save", methods=["POST"])
def save():
    if not user_profile or not recommendations:
        flash("Generate recommendations before saving.", "error")
        return redirect(url_for("index"))

    try:
        save_profile(user_profile)

        save_recommendations(
            recommendations,
            user_profile
        )

        flash(
            "Profile and recommendations saved successfully!",
            "success"
        )

    except Exception as error:
        flash(str(error), "error")

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )