from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
import numpy as numpy
from flask import Flask, request, jsonify, abort, render_template
from utils import thai_text_to_vec

app = Flask(__name__)
model = None
char_to_int = None
int_to_char = None

def load_model():
    global model
    global char_to_int
    global int_to_char
    model = load_model('Im_a_model_you_know_what_I_mean.h5')
    char_to_int = np.load('char_to_int.npy')
    int_to_char = np.load('int_to_char.npy')

def prepare_text(text):
    """
    Accepts a string of Thai text then:
        - Splits around any whitespace
        - Pad each split sentence to 128 characters
    """
    global char_to_int
    sequences = text.split()
    sequences = [thai_text_to_vec(seq, char_to_int) for seq in sequences]
    sequences = pad_sequences(sequences, maxlen=128)
    return sequences
  
def predict(sequences):
    predictions = [model.predict(sequence) for sequence in sequences]
            
@app.route("/", methods=["GET", "POST"])
def index():
    tokenized = None
    if request.method == "POST":
        if request.form and "input" in request.form:
            prepared = prepare_text(request.form['input'])
            predictions = predict(prepared)
            tokenized = predictions

    return render_template("index.html", tokenized=tokenized)

if __name__ == "__main__":
    load_model()
    app.run()