from keras.models import load_model
import numpy as np
from flask import Flask, request, abort, render_template, jsonify, make_response
from utils import predictions_to_text, prepare_text

app = Flask(__name__)
model = load_model('data/Im_a_model_you_know_what_I_mean.h5')
model._make_predict_function()
char_to_int = np.load('data/char_to_int.npy').item()
int_to_char = np.load('data/int_to_char.npy').item()
  
def predict(original_text):
    split_text = original_text.split()
    prepared = prepare_text(split_text, char_to_int)
    predictions = model.predict(prepared)
    predictions[predictions > 0.3] = 1
    predictions[predictions <= 0.3] = 0
    tokenized = predictions_to_text(split_text, predictions)
    return tokenized

# codepen first sends and HTTP Options request to ensure
# cors is enabled before sending a post request
@app.route("/predict", methods=["OPTIONS"])
def allow_cors():
    res = make_response()
    res.headers['Access-Control-Allow-Origin'] = 'https://s.codepen.io'
    res.headers['Access-Control-Allow-Headers'] = 'content-type'
    res.headers['Access-Control-Allow-Method'] = 'POST'
    return res

@app.route("/predict", methods=["POST"])
def api_predict():
    data = request.get_json()
    if data and 'text' in data:
        tokenized = predict(data['text'])
        res = make_response(jsonify({'tokenized': tokenized}))
    else:
        res = make_response(jsonify({'error':400, 'message': 'Bad Request'}))
    
    # allow cors for use on codepen
    res.headers['Access-Control-Allow-Origin'] = 'https://s.codepen.io'
    res.headers['Access-Control-Allow-Headers'] = 'content-type'
    res.headers['Access-Control-Allow-Method'] = 'POST'
    return res

# handles post if javascript is disabled
# otherwise, /predict is called using ajax
@app.route("/", methods=["GET", "POST"])
def index():
    tokenized = None
    if request.method == "POST":
        if request.form and "text" in request.form:
            tokenized = predict(request.form["text"])
        else:
            abort(400)

    return render_template("index.html", tokenized=tokenized)

if __name__ == "__main__":
    app.run()