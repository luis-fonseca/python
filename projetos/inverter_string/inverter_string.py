def reverse(text):
    
    index = len(text) - 1
    output = ""

    while index >= 0:
        output += text[index]
        index -= 1
