text = ' '
print(text.isspace())
#output: True

text = ' \f\n\r\t\v'
print(text.isspace())
#output: True

text = '                        '
print(text.isspace())
#output: True

text = '' # notice this is an empty string, there is no white space here
print(text.isspace())
#output: False

text = 'This is a regular text'
print(text.isspace())
#output: False