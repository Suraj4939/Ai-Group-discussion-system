async function startDiscussion() {

    const topic =
        document.getElementById('topic').value;

    const message =
        document.getElementById('message').value;

    const response = await fetch('/discuss', {

        method: 'POST',

        headers: {
            'Content-Type': 'application/json'
        },

        body: JSON.stringify({
            topic: topic,
            message: message
        })
    });

    const data = await response.json();

    if (data.status === 'success') {

        document.getElementById('supportive')
        .innerText = data.supportive;

        document.getElementById('opponent')
        .innerText = data.opponent;

        document.getElementById('moderator')
        .innerText = data.moderator;

        document.getElementById('prediction')
        .innerText =
        "ML Prediction: " + data.prediction;

        document.getElementById('sentiment')
        .innerText =
        "Sentiment: " + data.feedback.sentiment;

        document.getElementById('confidence')
        .innerText =
        "Confidence Score: "
        + data.feedback.confidence + "%";

        document.getElementById('grammar')
        .innerText =
        "Grammar: "
        + data.feedback.grammar;
    }
}