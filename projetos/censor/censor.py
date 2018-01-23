def censor(text, word):

  new_text = text.replace(word, "*" * len(word))

  return new_text

  
text = "this hack is wack hack"
word = "hack"

print(censor(text, word))
