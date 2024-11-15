my_csv = "mary;32;australia;mary@email.com"
my_data = my_csv.split(";")

for data in my_data:
    print(data)

#output:
#mary
#32
#australia
#mary@email.com

print(my_data[3])
#output:
# mary@email.com