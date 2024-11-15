word = 'beach'
print(word.isalnum())
#output: True

word = '32'
print(word.isalnum())
#output: True

word = 'number32' #notice there is no space
print(word.isalnum())
#output: True

word = 'Favorite number is 32' #notice the space between words
print(word.isalnum())
#output: False

word = '@number32$' #notice the special chars '@' and '$'
print(word.isalnum())
#output: False