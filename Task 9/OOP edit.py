class Email(): #Creates new class name called Email
    inbox = [] #Empty list to store the email objects from def populate_inbox
    
    def __init__ (self, email_address, subject_line, email_content): #What attributesare needed to initialise the Email object 
        self.address = email_address  #self.address = attribute name for teh email address that will be input
        self.subject = subject_line
        self.content = email_content
        self.has_been_read = False 
        #The read status of the email is unread
#Constructor method - The blueprint that is needed to create each object. Each instance of Email will have 4 attributes

# Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        self.has_been_read = True
        print ("Email has been read")

#Methods allows Inbox list to be populated. in the order provided from class method 
#EDIT: Brought block over
def populate_inbox(email_address, subject_line, email_content): #Method class 
    email_object = Email(email_address, subject_line, email_content)#Pass in attributes from constructor class to include the address, subject and content
    Email.inbox.append(email_object)#Inbox list from class Email. Email_object is added to the inbox list with .append. 

Email.populate_inbox ("Sam.H@gmail.com", "Very important message!", "You need to work harder to do well") #Individual instances in the Email class - Each is unique to the class with the three parts of email address, subject and content
Email.populate_inbox ("John.Doe@gmail.com", "Be good!", "Hello there" ) #Based on init method. self.address, self.subject, self.content
Email.populate_inbox ("Jane.Doe@yahoo.com", "Feed fish!", "You must remember to feed teh fish twice a day") #

def list_emails(): #  Displays all the email subject lines with their corresponding email number
    for i, email_object in enumerate(Email.inbox): #enumerate allows for the iteration of code based on teh number of instances in in the list inbox. As there are 3 
        print (f"{i} {email_object.subject}") #for each item in inbox, will print number of loop followed by the subject line starting at 0 for the first object, 1 for the 2nd so on. 
#Moved to allign with rest of class

# for email_object in Email.inbox:
#     print("From:" '\n', email_object.address)
#     print("Subject:" '\n', email_object.subject)
#     print("Content:"'\n', email_object.content)                                                

######################################################################

   


    def read_email(index):
        if index <= len(Email.inbox):
            email = Email.inbox[index] #checks if index is in range of the number of emails in inbox list
            print(email_object)
            email.mark_as_read == True
        else:
            print ("Email is unread")




email_object.mark_as_read
# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.

# Fill in the logic for the various menu operations.
menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
        print (Email)
# add logic here to read an email
        
    elif user_choice == 2:
        if email.mark_as_read == False:
            print ()
# add logic here to view unread emails
            
# #     elif user_choice == 3:
# #         # add logic here to quit appplication

# #     else:
# #         print("Oops - incorrect input.")