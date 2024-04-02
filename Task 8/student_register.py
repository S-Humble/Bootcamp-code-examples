number_students = int(input("How many students are registering?")) #initial input requesting number of students to be registered
to_sign = "...................." #Used to input a space to sign after the students ID number

with open ('reg_form.txt', 'a+') as file: #opens (creates if doesn't already exist) a file to input the data. 'a' appends new data and doesn't overwrite existing file if it already exists
    file.seek (0) #looks back to first character of document when opened
    if len(file.read()) == 0:#if the file has nothing inside i.e newly created, then will allow first file.write to add headings below. If not, will just input student ID
        file.write("Student ID number:             Sign below" + "\n") # adds headings to identify what is being displayed on document and the purpose of the dots at the end before starting a new line
    
    for i in range (number_students):#Creates loop for input of student ID based on number of students entering 
        student_id = int(input("Enter student ID number: ")) #allows input of studentID
        file.write("Student ID:"+  str(student_id) +  "  " + to_sign + "\n")
            

#write the student ID into a documenft called reg_form.txt
#Include a dotted line after each student ID to act as a line to sign on 
          
