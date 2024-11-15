phrase = "This is a regular text"

print(phrase.startswith(('regular', 'This')))
#output: True

print(phrase.startswith(('regular', 'text')))
#output: False

print(phrase.startswith(('regular', 'text'), 10, 22)) #look for in 'regular text'
#output: True