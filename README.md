# Personalized Recommendation System

An AI-powered Personalized Recommendation System built using Python, Flask, and Ollama. The application analyzes user profiles, interests, skill levels, and goals to generate personalized recommendations with suitability scores and explanations.

## Features

- **User Profile Collection:** Collects user details, interests, preferences, and learning goals.
- **Preference Analysis:** Identifies primary interests, skill levels, and learning requirements.
- **AI-Powered Recommendations:** Generates personalized recommendations using Ollama.
- **Recommendation Ranking:** Ranks recommendations according to suitability scores.
- **Recommendation Explanations:** Explains why each recommendation matches the user's profile.
- **Feedback-Based Refinement:** Updates recommendations based on user feedback.
- **Intent Detection:** Identifies user intentions from natural-language commands.
- **Save Results:** Saves user profiles and recommendations locally.
- **Web Interface:** Provides an interactive interface using Flask, HTML, and CSS.

## Technologies Used

- Python
- Flask
- Ollama
- Llama 3.2
- HTML5
- CSS3
- Pandas
- Sentence Transformers

## Project Structure

```text
Recommendation-System/
│
├── app.py
├── input_module.py
├── profile_module.py
├── prompt_module.py
├── recommendation_module.py
├── ranking_module.py
├── explanation_module.py
├── feedback_module.py
├── intent_module.py
├── save_module.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── outputs/
├── requirements.txt
└── README.md
