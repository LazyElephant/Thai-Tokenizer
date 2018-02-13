def thai_text_to_vec(text, char_to_int, num_classes=None):

  if num_classes is None:
    num_classes = len(char_to_int)

  return [char_to_int[char] for char in text]