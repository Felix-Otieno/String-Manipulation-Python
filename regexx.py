import re

phrase = ' Do   or do    not   there    is  no try   '

phrase_no_space = re.sub(r'\s+', '', phrase)

print(phrase)
# Do   or do    not   there    is  no try   

print(phrase_no_space)
#Doordonotthereisnotry