text = '' # notice this is an empty string, there is no white space here
print(text.isprintable())
#output: True

text = 'This is a regular text'
print(text.isprintable())
#output: True

text = ' ' #one space
print(text.isprintable())
#output: True

text = '                        '  #many spaces
print(text.isprintable())
#output: True

text = '\f\n\r\t\v'
print(text.isprintable())
#output: False