def anti_vowel(text):
  vowel = ["a", "e", "i", "o", "u"]
  output = ""
  
  for c in text:
    if not c.lower() in vowel:
      output += c

  return output


print(anti_vowel("Hello"))
    
