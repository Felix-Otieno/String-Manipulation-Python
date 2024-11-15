regular_text = "AbC#This is a regular text.$@G#"

clean_text = regular_text.strip("AbC#$@G")

print(regular_text)
#AbC#This is a regular text.$@G#

print(clean_text)
#This is a regular text.