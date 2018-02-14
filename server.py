from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
import numpy as np
from flask import Flask, request, jsonify, abort, render_template
from utils import thai_text_to_vec

app = Flask(__name__)
model = load_model('Im_a_model_you_know_what_I_mean.h5')
model._make_predict_function()
char_to_int = np.load('char_to_int.npy').item()
int_to_char = np.load('int_to_char.npy').item()

def prepare(text):
    """
    Accepts a string of Thai text then:
        - Splits around any whitespace
        - Pad each split sentence to 128 characters
    """
    global char_to_int
    sequences = [thai_text_to_vec(seq, char_to_int) for seq in text]
    sequences = pad_sequences(sequences, maxlen=128, padding='post', truncating='post')
    return sequences

def predictions_to_text(samples, predictions):
    text_with_spaces = []
    for i, text in enumerate(samples):
      for j, char in enumerate(text):
        temp = char if predictions[i,j] == 0 else " " + char
        text_with_spaces.append(temp)

    return "".join(text_with_spaces).lstrip()
  
def predict(original_text):
    split_text = original_text.split()
    prepared = prepare(split_text)
    predictions = model.predict(prepared)
    predictions[predictions > 0.7] = 1
    predictions[predictions <= 0.7] = 0
    tokenized = predictions_to_text(split_text, predictions)
    return tokenized
            
@app.route("/", methods=["GET", "POST"])
def index():
    tokenized = None
    if request.method == "POST":
        if request.form and "input" in request.form:
            tokenized = predict(request.form["input"])

    return render_template("index.html", tokenized=tokenized)

if __name__ == "__main__":
    app.run(debug=True)