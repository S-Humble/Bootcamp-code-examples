number_students = int(input("How many students are entering?"))

with open ('reg_form.txt', 'w') as file: 

    for i in range (number_students):
        student_id_num= int(input("Enter student ID number: "))
        file.write("Student ID:"+  str(student_id_num) + "\n")


       # student_id = ("Student ID:", student_id_num, "\n")
        #file.write("Student ID:" + '\n')
        #file.write(str(student_id_num))#+ "\n")

#write the student ID into a documenft called reg_form.txt
#Include a dotted line after each student ID to act as a line to sign on 
          
