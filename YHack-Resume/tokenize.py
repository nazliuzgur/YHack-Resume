# Given input text, return next word




# Given input text, return list with tokens
def input_file(input_text, tokens):
  if(input_text == ""):
    return tokens
  word = next_word(input_text)
  tokens.append(word)
  input_text = input_text[len(word)-1:] # take out the word from text
  if(input_text == ""): # if that was the last word
    return tokens
  else:
    input_text = input_text[1:] # get rid of the whitespace
  input_file(input_text,tokens)