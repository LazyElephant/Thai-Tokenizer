from keras.preprocessing.sequence import pad_sequences

def thai_text_to_vec(text, char_to_int, num_classes=None):

  if num_classes is None:
    num_classes = len(char_to_int)

  return [char_to_int[char] for char in text]

def predictions_to_text(samples, predictions):
    text_with_spaces = []
    for i, text in enumerate(samples):
      for j, char in enumerate(text):
        temp = char if predictions[i,j] == 0 else " " + char
        text_with_spaces.append(temp)

    return "".join(text_with_spaces).lstrip()

def prepare_text(text, char_to_int):
    """
    Accepts a list of Thai text strings then:
        - Converts each string to an integer array
        - Pad each array to 128 characters
    """
    sequences = [thai_text_to_vec(seq, char_to_int) for seq in text]
    sequences = pad_sequences(sequences, maxlen=128, padding='post', truncating='post')
    return sequences