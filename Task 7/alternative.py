string = "Hello World!"
cap_low_string = ""

for i in range (len(string)):
    if i % 2 == 0:
        cap_low_string += string[i].upper()
    else:
        cap_low_string += string[i].lower()

print (cap_low_string)