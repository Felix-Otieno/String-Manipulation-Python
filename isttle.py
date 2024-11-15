text = 'This is a regular text'
print(text.istitle())
#output: False

text = 'This Is A Regular Text'
print(text.istitle())
#output: True

text = 'This $ Is @ A Regular 3 Text!'
print(text.istitle())
#output: True