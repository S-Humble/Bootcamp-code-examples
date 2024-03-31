name = []  #Empty list to add names to
bithdate = [] #empty list to add birthdate to
names_dob = [] #empty list to store the two tuple name and date list append

with open ('DOB.txt', 'r+') as file: 
   for line in file: #opens the DOB.txt file and reads through each line in the document
       
    txt_split = line.split() #splits the string line in file into separate items, with each separate block of text as an individual item
    name = ' '.join(txt_split[0:2]) #joins the first 2 items from the split string i.e. first and last name ' ' creates a space between the two names
    birthdate = ' '.join(txt_split[2:]) #joins the rest of the split string from index 2 to the end of the line for each name to give birthdate, index 2, 3 and 4
    names_dob.append((name, birthdate)) #Joins the two variables name and birthdate as a tuple pair. Matching the name with the corresponding birthdate for each line in the original text  
#'firstnamelastname','DayDateYear')
    
names_only = [item[0] for item in names_dob] #puts the names into a new list list from names_dob. 0 index first tuple  
dob_only = [item[1] for item in names_dob] ##puts the dates of birth into a new list list from names_dob. 1 index second tuple  
    
print ("Names:") #Names: prints before the list of names from names_only
for name in names_only: #initiates a loop that ccyles through all of the names and prints the name in each iteration 
    print (name) #prints the name

print  ("\n" "Birthdates:") #\n gives a space before printing the birthdates
for birthdate in dob_only: #initiates a loop that ccyles through all of the birthdates and prints the date in each iteration 
    print (birthdate)