regular_text = "$@G#This is a regular text."

clean_begin_text = regular_text.lstrip("#$@G")

print(regular_text)
#$@G#This is a regular text.

print(clean_begin_text)
#This is a regular text.