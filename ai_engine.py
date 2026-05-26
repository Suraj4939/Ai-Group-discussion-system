import random

supportive_responses = [
    "AI improves productivity and saves time.",
    "Artificial intelligence helps students learn faster.",
    "Technology creates innovation and growth.",
    "AI can automate repetitive tasks effectively."
]

opponent_responses = [
    "AI may reduce employment opportunities.",
    "Technology dependency can become dangerous.",
    "Human creativity cannot be fully replaced.",
    "Artificial intelligence may create privacy concerns."
]

moderator_responses = [
    "Both viewpoints are important in this discussion.",
    "Let us consider advantages and disadvantages equally.",
    "This topic requires balanced thinking.",
    "The discussion is becoming very informative."
]

def generate_ai_discussion(topic, user_input):

    return {
        "supportive": random.choice(supportive_responses),
        "opponent": random.choice(opponent_responses),
        "moderator": random.choice(moderator_responses)
    }