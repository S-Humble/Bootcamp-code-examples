string = "Hello World!"
cap_low_string = "" #empty string that will be populated by the output of the for loop

for i in range (len(string)): #iterate the foor loop for the number a number of times equal to the length of the original string
    if i % 2 == 0: #for the length of the string, if the value is even then it will place an uppercase letter into empty string 
        cap_low_string += string[i].upper() #if string length is even for string[i] (the particular iteration of for loop is even) then upper case letter from string is added to open list
    else: 
        cap_low_string += string[i].lower() #if iteration of code is odd, the letter added to cap_low_string from string is added lowercase

print (cap_low_string)