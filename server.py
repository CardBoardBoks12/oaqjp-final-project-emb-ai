""" This file serves the server API """
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """ Function to handle emotionDetector route """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        emotion_response = "Invalid input! Try again."
    else:
        emotion_response = (
            "For the given statement, the system response is" +
            " 'anger': " + str(anger_score) +
            ", 'disgust': " + str(disgust_score) +
            ", 'fear': " + str(fear_score) +
            ", 'joy': " + str(joy_score) +
            ", and 'sadness': " + str(sadness_score) +
            ". The dominant emotion is " + str(dominant_emotion)
        )

    return emotion_response

@app.route("/")
def render_index_page():
    """ Function to render index page """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
