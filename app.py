from flask import Flask, render_template, request, jsonify
import joblib

from ai_engine import generate_ai_discussion
from feedback import generate_feedback

app = Flask(__name__)

model = joblib.load('models/sentiment_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/discuss', methods=['POST'])
def discuss():

    try:
        data = request.get_json()

        topic = data['topic']
        user_input = data['message']

        prediction = model.predict([user_input])[0]

        if prediction == 1:
            sentiment_result = "Positive Opinion"
        else:
            sentiment_result = "Negative Opinion"

        ai_replies = generate_ai_discussion(topic, user_input)

        feedback = generate_feedback(user_input)

        return jsonify({
            'status': 'success',
            'prediction': sentiment_result,
            'supportive': ai_replies['supportive'],
            'opponent': ai_replies['opponent'],
            'moderator': ai_replies['moderator'],
            'feedback': feedback
        })

    except Exception as e:

        return jsonify({
            'status': 'error',
            'message': str(e)
        })

if __name__ == '__main__':
    app.run(debug=True)