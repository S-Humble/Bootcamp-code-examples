string = "Hello World! This is my best code!"
cap_low_string = "" #empty string that will be populated by the output of the for loop

for i in range (len(string)): #iterate the foor loop for the number a number of times equal to the length of the original string
    if i % 2 == 0: #for the length of the string, if the value is even then it will place an uppercase letter into empty string 
        cap_low_string += string[i].upper() #if string length is even for string[i] (the particular iteration of for loop is even) then upper case letter from string is added to open list
    else: 
        cap_low_string += string[i].lower() #if iteration of code is odd, the letter added to cap_low_string from string is added lowercase

print (cap_low_string)

string_split = string.split() #splits the string into individual words in a list

upper_lower = "" #Empty string to store result of for loop below

for i in range (len(string_split)): #range used based on number of items in string_split. i represents index of the list 
    if i % 2 == 0: #If index of string_split is even, add uppercase word to upper_lower variable
        upper_lower = upper_lower +" "+ string_split[i].upper() #Adds the uppercase words from the for loop. + " ", adds a space between the words put into the empty upper_lower string
    else: #If index is not even, then words from string_split are made lower case
        upper_lower = upper_lower +" " + string_split[i].lower()

string_join = "".join(upper_lower) #"" acts as a separator between words in upper_lower. .join joins the two elements from the for loop into a complete string

print (string_join)
