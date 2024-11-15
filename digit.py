word = '32'
print(word.isdigit())
#output: True

print("\u2083".isdigit()) #unicode for subscript 3
#output: True

word = 'beach'
print(word.isdigit())
#output: False

word = 'number32'
print(word.isdigit())
#output: False

word = '1 2 3' #notice the space between chars
print(word.isdigit())
#output: False

word = '@32$' #notice the special chars '@' and '$'
print(word.isdigit())
#output: False