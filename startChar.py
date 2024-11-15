phrase = "This is a regular text"

print(phrase.startswith('regular', 10)) #the word regular starts at position 10 of the phrase
#output: True

print(phrase.startswith('regular', 10, 22)) #look for in 'regular text'
#output: True

print(phrase.startswith('regular', 10, 15)) ##look for in 'regul'
#output: False