
#this section imports all the libaries needed for the pogram to work
import tkinter as tk #importing the tkniter module as tk
from tkinter import messagebox #importingmessagebox from the module tkinter
import random #importing the random module
import math #importing the math module
import csv #importing the csv module
import matplotlib.pyplot as plt #importing the matplotlib module as plt
import hashlib #importing the hashlib module



#The class Login_Page is GUI that the user can use to login to the program
#the login page will contain two labels, three buttons and two entry boxes
class Login_Page:#defines the class as Login_Page

    #makes the funtion __init__ that atomatically initilizes when the class is called
    def __init__(self, root, password_username):#pulls the variables self, root and passwrod_username into the funtion


        #creates the format of the GUI for the Login page with all the buttons, labels and entry boxes required
        
        #creates the label that says "Username" and places it at a given location on the GUI
        self.username_label = tk.Label(root, text="Username").place(x = 0, y = 0)
        #creates the label that says "Password" and places it at a given location on the GUI
        self.username_label = tk.Label(root, text="Password").place(x = 0, y = 20)
        #creates the entry box that the user types their username into
        self.username_entry = tk.Entry(root)
        #places the entry box at a given locationon the GUI
        self.username_entry.place(x = 70, y = 0)
        #creates the entry box that the user types their username into, it also converts the input into * so that the password is hidden when typed
        self.password_entry = tk.Entry(root, show = "*")
        #places the entry box at a given locationon the GUI
        self.password_entry.place(x = 70, y = 20)
        #creates the Login button that calls forward the function Login that is inside the class
        self.login_button = tk.Button(root, text="Login", command = lambda:self.Login(root, password_username))
        #places the login button entry box at a given locationon the GUI
        self.login_button.place(x = 0, y = 45)
        #creates the Quit button that calls forward the function Quit that is inside the class
        self.quit_button = tk.Button(root, text="Quit", command = lambda:self.Quit(root))
        #places the quit button entry box at a given locationon the GUI
        self.quit_button.place(x = 45, y = 45)
        #creates the new user button that calls forward the function new_user that is inside the class
        self.new_user_button = tk.Button(root, text = "Create New User", command = lambda:self.new_user(root))
        #places the new user button entry box at a given locationon the GUI
        self.new_user_button.place(x = 90, y = 45)


        #this section produces any error messages neeeded when the login page is loaded, for example it creates the error message "wrong password"
        #when the usesr inputs a correct username but the password is incorrect

        #Checks to see is the variable password_username is the string 1
        if password_username == "1":
            #if the password_username is the string 1, then a label that says "wrong password" is created and places at a given location in the GUI
            tk.Label(root, text = "Wrong Password").place(x = 0, y = 75)
        #checks to see is the variable password_username is the string 2
        elif password_username == "2":
            #if the password_username is the string 2, then a label that says "wrong username and password" is created and places at a given location in the GUI
            tk.Label(root, text = "Wrong Username and Password").place(x = 0, y = 75)


     
    def Login(self, root, password_username):#creates the function Login and pulls in the variables self, root and password_username, this funtion is called when the login button is pressed
        
        global user_row #tells the program that the variable user_row is a globalvariable and not a local variable
        user_row = 0
        Username = self.username_entry.get() #sets the variable Username to the string inside of the username entry box
        Password = self.password_entry.get() #sets the variables Password to the string inside of the password entry box
        hashed_password = hashlib.md5(Password.encode())#hashes the password using the md5 algorithm and saves as variable hashed_password
        Password = (hashed_password.hexdigest())#says the hexidecimal form of the hashed password as the variable Password
        with open("score.csv") as csvfile: #opens the csv file called"score.csv")
            database = csv.DictReader(csvfile)#reads the file and saves it as the variable databse
            Username = str.lower(Username) #reassigns the varibale Username to the lower case version of the variable Username
            correct = "0" #sets the variable correct to the string 0
            while correct != "1":#loops if the variable correct matches the string 1
                for row in database: #loops for the a set amount of times, the set amount of time is how many rows the variables database has
                    user_row = user_row+1 #incraeses the user_row by 1
                    Username_File = row["username"] #sets the variable Username_File to the string value in the database in the location, row and the username column
                    Password_File = row["password"]#sets the variable Password_File to the string value in the database in the location, row and the password column
                    if Username_File == Username and Password_File == Password: #checks if the variable Usernme_File matches the variable Username and the variable Password_File matches the variable Password
                        correct = "1" #sets the variable correct to the string value 1 
                        root.destroy() #destroys the GUI
                        create_main_page() #calls forward the create_main_page class
                    elif Username_File == Username and Password_File != Password: #checks if the variable Usernme_File matches the variable Username but the variable Password_File doesn't matches the variable Password
                        password_username = "1" #sets the variable password_username to the string value 1
                        correct = "2" #sets the variable correct to the string value 2
                    elif Username_File != Username and Password_File != Password: #checks if the variable Usernme_File doesn't matches the variable Username but the variable Password_File doesn't matches the variable Password
                        if correct != "2":#checks to see if the variable correct doesn't match the string 2
                            correct = "3"#sets the variable correct to equal the string value 1
                            password_username = "2"#sets the variable password_username to the string value 2
                break
                            
            if correct == "2":#checks to see if the variable correct matches the string 2
                root.destroy()#destroys the GUI
                create_login_page(password_username)#calls forward the create_login_page class with variable password_username
            else:#if correct doesn't equal 2
                root.destroy()#detroys the GUI
                create_login_page(password_username)#calls forward the create_login_page class with variable password_username
                
    def Quit(self, root):#creates the funtion quit with the parameters self and root, this funtion is called when the quit button is pressed
        
        root.destroy()#destroys the GUI

    def new_user(self, root):#creates the funtion new_user with the parameters self and root, this funtion is called when the quit button is pressed

        root.destroy()#destroys the GUI
        root = tk.Tk()#creatses the root GUI window
        root.geometry("300x160")#sets the size of window to 300 pixels wide and 160pixels tall
        root.title("")#sets the title of the window to ""


        app = new_user_page(root, password_username) # calls forward the new_user_page class with the variables root and password_username

            
#creates class new_user_page that is called forward when the new user button is pressed on the login page
#this window contains 4 labels, 4 entry boxes and two buttons
class new_user_page:

    #makes the funtion __init__ that atomatically initilizes when the class is called
    def __init__(self,root, password_username):# pulls the variables self, root and password_username into the function 
        
        #creates the first name label thats says "first name" and places it at a given location in the GUI
        self.firt_name_label = tk.Label(root, text = "First Name:").place(x = 0, y = 0)
        #creates the last name label thats says "surname" and places it at a given location in the GUI
        self.last_name_label = tk.Label(root, text = "Surname:").place(x = 0, y = 20)
        #creates the username label thats says "username"and places it at a given location in the GUI
        self.username_label = tk.Label(root, text = "Username:").place(x = 0, y = 40)
        #creates the password label thats says "password"and places it at a given location in the GUI
        self.password_label = tk.Label(root, text = "Password:").place(x = 0, y = 60)
        #creates the confirm password label thats says "confirm password" and places it at a given location in the GUI
        self.confirm_password = tk.Label(root, text = "Confirm Password:").place(x = 0, y = 80)

        #creates the first name entry box
        self.first_name_entry = tk.Entry(root)
        #places the first name entry box at a given location in the GUI
        self.first_name_entry.place(x = 110, y = 0)

        #creates the last name entry box
        self.last_name_entry = tk.Entry(root)
        #places the last name entry box at a given location in the GUI
        self.last_name_entry.place(x = 110, y = 20)

        #creates the username entry box
        self.username_entry = tk.Entry(root)
        #places the username entry box at a given location in the GUI
        self.username_entry.place(x = 110, y = 40)

        #creates the password entry box, it also converts the input into * so that the password is hidden when typed
        self.password_entry = tk.Entry(root, show = "*")
        #places the password entry box at a given location in the GUI
        self.password_entry.place(x = 110, y = 60)

        #creates the confirm password entry box, it also converts the input into * so that the password is hidden when typed
        self.confirm_password_entry = tk.Entry(root, show = "*")
        #places the confirm password entry box at a given location in the GUI
        self.confirm_password_entry.place(x = 110, y = 80)

        #creates the new account button the says "create new account" and places it at a given location in the GUI, this button calls forward the create_new_user funtion when clicked
        self.new_account_button = tk.Button(root, text = "Create New Account", command = lambda:self.create_new_user(root, password_username)).place(x = 0, y = 110)
        #creates the return button the says "returnt" and places the new account button the says "create new account" and places it at a given location in the GUI, this button calls forward the back funtion when clicked
        self.return_button = tk.Button(root, text = "Return", command = lambda:self.back(root, password_username)).place(x = 150, y = 110)

    def create_new_user(self,root, password_username):#creates the function create_new_user and pulls in the variables self, root and password entry, this function is called when the create new account button is pressed
        all_usernames = []#sets the variable all_usernames to an empty list
        unique = "0"#sets the variable unique to the string value 0
        first_name = self.first_name_entry.get()#sets the variable first_name to the string value in the firstname entry box
        surname = self.last_name_entry.get()#sets the variable surname to the string value in the last name entry box
        username = self.username_entry.get()#sets the varible username to the string value in the uername entry box
        password = self.password_entry.get()#sets the variable password to the string value in the password entry box
        confirm_password = self.confirm_password_entry.get()#sets the variable confirm_password to the string value in the confirm password entry box
        if password != confirm_password:#checks to see if the variable password doesn't match the variable confirm password
            tk.messagebox.showerror("Error", "Passwords do not match")#creates a message box with the message "passwords do not match"
        else:#if the variable password does match the variable confirm password
            with open("score.csv") as csvfile:#opens the file score.csv as the varible csvfile
                database = csv.DictReader(csvfile)#reads the file and saves it as the variable databse
                for row in database:#loops for the a set amount of times, the set amount of time is how many rows the variables database has
                    Username_File = row['username']#sets the variable Username_File to the string value in the database in the location, row and the username column
                    all_usernames.append(Username_File)#add thes variable Username_File to the end of the list all_usernames
                    num_users = len(all_usernames)#saves the length of the list all_usernames as the varible num_users
                    for i in range (0,num_users):#loops a set amount of times, loops as any times as the variable num_users
                        current_username = all_usernames[i]#sets the variable current_username to the string value of the value in the loction i in the list all_usernames
                        if username == current_username:#checks to see if the variable username matches the variable current_username
                            unique = "1"#sets the variable unique to the string value 1
                        else:#if variable username doesn't match the variable current_usernames 
                            if unique != "1":#checks to see if the variable unique doesn't matches the string value 1
                                unique = "3"#sets the variable unique to the string value 3
                if unique == "3":#checks to see if the variable unique matches the string value 3
                    with open("score.csv", "a",newline="") as data_storage:#opens the file scores.csv in append mode as the variable data_storage
                        tk.messagebox.showinfo("","Your account has been successfully created")#creates a pop up message box saying "Your account has been successfully created"
                        #sets the list variable fieldnames to the column headings of the csvfile
                        fieldnames = ["first name","last name","username","password","al 1","al 2","al 3","seq 1","seq 2","seq 3","tri 1","tri 2","tri 3","ar 1","ar 2","ar 3","gr 1","gr 2","gr 3"]
                        writer = csv.DictWriter(data_storage, fieldnames = fieldnames)#sets up the score.csv file in a format so that it can be written to
                        hashed_password = hashlib.md5(password.encode())#hashes the password using the md5 algorithm and saves as variable hashed_password
                        hashed_password = (hashed_password.hexdigest())#says the hexidecimal form of the hashed password as the variable hashed_password
                        #writes a new row in the file "score.csv" that contains all the users initial details
                        writer.writerow({"first name":first_name,"last name":surname,"username":username,"password":hashed_password,"al 1":"0","al 2":"0","al 3":"0","seq 1":"0","seq 2":"0","seq 3":"0","tri 1":"0","tri 2":"0","tri 3":"0","ar 1":"0","ar 2":"0","ar 3":"0","gr 1":"0","gr 2":"0","gr 3":"0"})
                        root.destroy()#closes the window
                        create_login_page(password_username)#calls foward the create_login_page function
                elif unique == "1":#checks to see if the variable unique matches the string value 1
                    tk.messagebox.showinfo("","That username is already taken, please try another")#creates a pop up message box saying "That username is already taken, please try another"
 
        

    def back(self, root, password_username):#creates the function create_new_user and pulls in the variables self, root and password entry, this function is called forward when the return button is pressed
        root.destroy()#destroys the GUI
        create_login_page(password_username)#calls forward the create_login_page function with the variable password_username
        
            


        
#creates class main_page that is called forward when the user succesfully logs in
#this class creates a window with 6 buttons and 20 labels
class main_page:

    #makes the funtion __init__ that atomatically initilizes when the class is called
    def __init__(self, root, question, score):#the vaiables self, root, question and score are pulled into the function

        global container, user_score #tells the program that the variables user_score and container is a globalvariable and not a local variable

        level = "0"#sets the variable level to the string value 0
        
        frame1 = tk.Frame(container)#creates a frames inside the container frame
        frame1.grid(row = 0, column = 0)#places the frame in  a set location in the GUI
        frame1.config( width=600, height = 600 )#sets the size of the frame to 600 pixels wide and 600 pixels tall

        #creates the lesson label that says "lesson" and places at a set location in the GUI
        self.lessonLabel = tk.Label(frame1, text= "Lesson" ).place(x = 0, y = 0)
        #creates the score label that says "scores:" and places at a set location in the GUI
        self.scoreLabel = tk.Label(frame1, text="  Scores:  ").place(x = 65, y = 0)
        #creates the level 1 label that says "level 1" and places at a set location in the GUI
        self.level1Label = tk.Label(frame1, text="  Level 1  ").place(x = 120, y = 0)
        #creates the level 2 label that says "level 2" and places at a set location in the GUI
        self.level2Label = tk.Label(frame1, text="  Level 2  ").place(x = 180, y = 0)
        #creates the level 3 label that says "level 3" and places at a set location in the GUI
        self.level3Label = tk.Label(frame1, text="  Level 3  ").place(x = 240, y = 0)

        #creates the algebra button that says "algebra" thats calls forward the class algebra when called
        self.algebraButton = tk.Button(frame1, text ="Algebra", command = lambda:algebra(level, question, score, root))
        #places the button at a set location
        self.algebraButton.place(x = 0, y = 20)
        #sets the size of the button
        self.algebraButton.config(width = 8)

        #creates the triangle button that says "triangles" thats calls forward the class triangles when called
        self.triangleButton = tk.Button(frame1, text ="Triangles", command = lambda:triangles(level, question, score, root))
        #places the button at a set location
        self.triangleButton.place(x = 0, y = 50)
        #sets the size of the button
        self.triangleButton.config(width = 8)

        #creates the sequence button that says "sequence" thats calls forward the class sequence when called
        self.sequenceButton = tk.Button(frame1, text ="Sequences", command = lambda:sequences(level, question, score, root))
        #places the button at a set location
        self.sequenceButton.place(x = 0, y = 80)
        #sets the size of the button
        self.sequenceButton.config(width = 8)

        #creates the area button that says "area" thats calls forward the class area when called
        self.areaButton = tk.Button(frame1, text ="Area", command = lambda:area(level, question, score, root))
        #places the button at a set location
        self.areaButton.place(x = 0, y = 110)
        #sets the size of the button
        self.areaButton.config(width = 8)

        #creates the graph button that says "graph" thats calls forward the class graph when called
        self.areaButton = tk.Button(frame1, text ="Graphs", command = lambda:graph(level, question, score, root))
        #places the button at a set location
        self.areaButton.place(x = 0, y = 140)
        #sets the size of the button
        self.areaButton.config(width = 8)

        #creates the refresh button that says "refresh" thats calls forward the function refresh when called
        self.refreshButton = tk.Button(frame1, text="Refresh", command = lambda:self.refresh(root))
        #places the button at a set location
        self.refreshButton.place(x = 0, y = 190)
        #sets the size of the button
        self.refreshButton.config(width = 8)

        #creates the refresh button that says "Log out" thats calls forward the function log_out when called
        self.logoutButton = tk.Button(frame1, text="Log Out", command = lambda:self.log_out(root))
        #places the button at a set location
        self.logoutButton.place(x = 0, y = 220)    
        #sets the size of the button
        self.logoutButton.config(width = 8)
        
        database=open("score.csv")#saves the file "score.csv" as the varible database
        scores=[]#sets the variable scores to a empty list
        userScores = csv.reader(database)

        for item in userScores:#lopps for a set amount of times, the set amount of times is how many columns in the userScores 
            scores.append(item)#adds the item from userScores to the list scores
        for i in range(4,19):#loops from 2 to 19
            user_score.append(scores[user_row][i])#adds the item from scores to the list user_scores

        #takes the value from the lsit user_score and uses the value as the text on a lable that is placed at a set location in the GUI
        #this happens for the next 15 lines but the value used moves one along in the list each time
        self.al_l1 = tk.Label(frame1, text = user_score[0]).place(x = 140, y = 20)
        self.al_l2 = tk.Label(frame1, text = user_score[1]).place(x = 200, y = 20)
        self.al_l3 = tk.Label(frame1, text = user_score[2]).place(x = 260, y = 20)
        self.tri_l1 = tk.Label(frame1, text = user_score[3]).place(x = 140, y = 50)
        self.tri_l2 = tk.Label(frame1, text = user_score[4]).place(x = 200, y = 50)
        self.tri_l3 = tk.Label(frame1, text = user_score[5]).place(x = 260, y = 50)
        self.seq_l1 = tk.Label(frame1, text = user_score[6]).place(x = 140, y = 80)
        self.seq_l2 = tk.Label(frame1, text = user_score[7]).place(x = 200, y = 80)
        self.seq_l3 = tk.Label(frame1, text = user_score[8]).place(x = 260, y = 80)
        self.ar_l1 = tk.Label(frame1, text = user_score[9]).place(x = 140, y = 110)
        self.ar_l2 = tk.Label(frame1, text = user_score[10]).place(x = 200, y = 110)
        self.ar_l3 = tk.Label(frame1, text = user_score[11]).place(x = 260, y = 110)
        self.gr_l1 = tk.Label(frame1, text = user_score[12]).place(x = 140, y = 140)
        self.gr_l2 = tk.Label(frame1, text = user_score[13]).place(x = 200, y = 140)
        self.gr_l3 = tk.Label(frame1, text = user_score[14]).place(x = 260, y = 140)

    def refresh(self,root):#creates the function back and pulls in the variables self and root, this function is called forward when the refresh button is pressed
        root.destroy()#destroys the GUI
        create_main_page() #calls forward the create_main_page variable

    def log_out(self,root):
        root.destroy()
        password_username = "0"
        create_login_page(password_username)

#creates the algebra class which is called when the algebra button is pressed
#the algebra class creates four buttons, one entry box per question
# the class also randomly generates questions on three different levels
class algebra:

    #makes the funtion __init__ that atomatically initilizes when the class is called
    def __init__(self, level, question, score, root):#the variables self, level, question and score are pulled into the function

        root.title("Algebra")

        lesson = "algebra"#sets the variable lesson to the string value algebra
        
        frame2 = tk.Frame()#creates a frames inside the container frame
        frame2.config( width=600, height = 600 )#sets the size of the frame to 600 pixels wide and 600 pixels tall
        frame2.grid(row = 0,column = 0)#places the frame in  a set location in the GUI
            
        frame2.tkraise()#raises the frame so that its viewable

        question = question + 1#increase the variable question by one
        question_number = tk.Label(frame2, text = str(question)+"/5").place(x = 200, y = 0)#places label that shows the user what questin out of 5 they are on

        if level == "0":#checks to see if the variable level is the string value 0

            #creates the levelpick label thats says "pick a level" and places it at a set loctaion on the GUI
            self.levelpick = tk.Label(frame2, text="Pick a level").place(x =90, y = 0)

            #creates the level1 button that says "level 1" that when pressed calls forward the level1 function inside this class
            self.level1button = tk.Button(frame2, text = "Level 1", command = lambda:self.level1(frame2, lesson, question, score))
            #places the button at a set location in the GUI
            self.level1button.place(x = 0, y = 30)

            #creates the level2 button that says "level 2" that when pressed calls forward the level2 function inside this class
            self.level2button = tk.Button(frame2, text = "Level 2",command = lambda:self.level2(frame2, lesson, question, score))
            #places the button at a set location in the GUI
            self.level2button.place(x = 100, y = 30)

            #creates the level3 button that says "level 3" that when pressed calls forward the level3 function inside this class
            self.level3button = tk.Button(frame2, text = "Level 3", command = lambda:self.level3(frame2, lesson, question, score))
            #places the button at a set location in the GUI
            self.level3button.place(x = 200, y = 30)

        if level == "1":#checks if the variable level matches the string value 1
            self.level1(frame2, lesson, question, score)#calls forward the level1 function with the variables frame2, lesson, question and score
        elif level == "2":#checks if the variable level matches the string value 2
            self.level2(frame2, lesson, question, score)#calls forward the level2 function with the variables frame2, lesson, question and score
        elif level == "3":#checks if the variable level matches the string value 3
            self.level3(frame2, lesson, question, score)#calls forward the level3 function with the variables frame2, lesson, question and score

    


    #creates the funtion level1 with the variables self, frame2, lesson, question and score
    def level1(self, frame2, lesson, question, score):
        level = "1"#sets the variables level to the string value 1
        Xvalue = random.randint(3,10)#sets the variable Xvalue to a random interger from 3-10
        answer = random.randint(3,8)#sets the variable answer to a random interger from 3-8
        rhs = Xvalue*answer#sets the variable rhs to the interger value of Xvalue times answer
        #creates the question line 1 label that says the question and places it at a set location on the GUI
        self.QLine1 = tk.Label(frame2, text = str(Xvalue)+"x = "+str(rhs)).place(x = 0, y = 60)
        #creates the question line 2 label that says "what does x equal" and places it at a set location on the GUI
        self.QLine2 = tk.Label(frame2, text = "What does x equal?").place(x=0 , y = 90)
        #creates the answer label that says "answer" and places it at a set location on the GUI                       
        self.answerLabel = tk.Label(frame2, text = "Answer:").place(x = 0, y = 120)
        #creates the answer entry box
        self.user_answer_entry = tk.Entry(frame2)
        #places the answer entry box at a set location on the GUI
        self.user_answer_entry.place(x = 75, y = 120)
        #creates the enter button that says "submit" and places it at a set location on the GUI, when clicked the button calls forward the get_user_answer funtion that is inside the class
        self.enter = tk.Button(frame2, text = "Submit", command = lambda:self.get_user_answer(frame2, answer, level, lesson, question, score)).place(x = 200, y = 120)

            
    #creates the funtion level1 with the variables self, frame2, lesson, question and score
    def level2(self, frame2, lesson, question, score):
        level = "2"#sets the variables level to the string value 2
        Xvalue = random.randint(3,10)#sets the variable Xvalue to a random interger from 3-10
        answer = random.randint(3,8)#sets the variable answer to a random interger from 3-8
        rhs_unit = Xvalue*answer#sets the variable rhs to the interger value of Xvalue times answer
        lhs_unit = random.randint(5,rhs_unit-3)#sets the variable lhs_unit to a random interger from 5 to rhs_unit minus 3
        negORpos = random.choice([True,False])#sets the negORpos value to a random boolean value true or false
        if negORpos == True:#checks to see if negORpos matches the boolean value true
            rhs_unit = rhs_unit - lhs_unit#sets the variable rhs_unit to the interger value of rhs_unit minus lhs_unit 
            questionLine1 = str(str(Xvalue)+"x -"+str(lhs_unit)+"="+str(rhs_unit))#creates the variable questionLine1 and sets it to the level 2 question            
        else:#if the negORpos variable matches the boolean value false
            rhs_unit = rhs_unit + lhs_unit#sets the variable rhs_unit to the interger value of rhs_unit plus lhs_unit
            questionLine1 = str(str(Xvalue)+"x +"+str(lhs_unit)+"="+str(rhs_unit))#creates the variable questionLine1 and sets it to the level 2 question

        #creates the question line 1 label that text says the string value stored in variable questionline1 and places it at set loation on the GUI
        self.QLine1 = tk.Label(frame2, text = questionLine1).place(x = 0, y = 60)
        #creates the question line 2 label that says "what does x equal" and places it at a set location on the GUI
        self.QLine2 = tk.Label(frame2, text = "What does x equal?").place(x=0 , y = 90)
                    
        #creates the answer label that says "answer" and places it at a set location on the GUI                       
        self.answerLabel = tk.Label(frame2, text = "Answer:").place(x = 0, y = 120)
        #creates the answer entry box
        self.user_answer_entry = tk.Entry(frame2)
        #places the answer entry box at a set location on the GUI
        self.user_answer_entry.place(x = 75, y = 120)
        #creates the enter button that says "submit" and places it at a set location on the GUI, when clicked the button calls forward the get_user_answer funtion that is inside the class
        self.enter = tk.Button(frame2, text = "Submit", command = lambda:self.get_user_answer(frame2, answer, level, lesson, question, score)).place(x = 200, y = 120)   

    #creates the funtion level1 with the variables self, frame2, lesson, question and score
    def level3(self, frame2, lesson, question, score):
        level = "3"#sets the variables level to the string value 3
        Xvalue = random.randint(5,14)#sets the variable Xvalue to a random interger from 5-14
        answer = random.randint(3,8)#sets the variable answer to a random interger from 3-8
        rhs_unit = Xvalue*answer#sets the variable rhs to the interger value of Xvalue times answer
        lhs_unit = random.randint(5,rhs_unit-5)#sets the variable lhs_unit to a random interger from 5 to rhs_unit minus 5
        rhs_xValue = random.randint(2,Xvalue-2)#sets the variable rhs_xValue to a random interger from 2 to xValue minus 2
        negORpos = random.choice([True,False])#sets the negORpos value to a random boolean value true or false
        negORpos2 = random.choice([True,False])#sets the negORpos2 value to a random boolean value true or false
        if negORpos == True:#checks to see if the varible negORpos is True
            rhs_unit = rhs_unit - lhs_unit#sets the variable lhs_unit to the interger value of the variable rhs_unit minus the variable lhs_unit
            if negORpos2 == True:#checks to see if the varible negORpos2 is True
                lhs_xValue = Xvalue - rhs_xValue#sets the variable lhs_xValue to the interger value of the variable xValue minus the variable rhs_xValue
                questionLine1 = str(str(lhs_xValue)+ "x -"+str(lhs_unit)+"="+str(rhs_unit)+"-"+str(rhs_xValue)+"x")#creates the variable questionLine1 and sets it to the level 3 question
            else:#if the negORpos2 variable matches the boolean value false
                lhs_xValue = Xvalue + rhs_xValue
                questionLine1 = str(str(lhs_xValue)+ "x -"+str(lhs_unit)+"="+str(rhs_unit)+"+"+str(rhs_xValue)+"x")#creates the variable questionLine1 and sets it to the level 3 question
        else:#if the negORpos variable matches the boolean value false
            rhs_unit = rhs_unit + lhs_unit#sets the variable rhs_unit to the interger value of the variable rhs_unit plus the variable lhs_unit
            if negORpos2 == True:#checks to see if the varible negORpos2 is True
                lhs_xValue = Xvalue - rhs_xValue#sets the variable lhs_xValue to the interger value of the variabe Xvalue minus the variable rhs_xValue
                questionLine1 = str(str(lhs_xValue)+ "x +" +str(lhs_unit)+"="+str(rhs_unit)+"-"+str(rhs_xValue)+"x")#creates the variable questionLine1 and sets it to the level 3 question
            else:#if the negORpos2 variable matches the boolean value false
                lhs_xValue = Xvalue + rhs_xValue#sets the variable hs_xValue to the interger value of the variable Xvalue plus the variable rhs_xValue
                questionLine1 = str(str(lhs_xValue)+ "x +"+str(lhs_unit)+"="+str(rhs_unit)+"+"+str(rhs_xValue)+"x")#creates the variable questionLine1 and sets it to the level 3 question

        #creates the question line 1 label that text says the string value stored in variable questionline1 and places it at set loation on the GUI
        self.QLine1 = tk.Label(frame2, text = questionLine1).place(x = 0, y = 60)
        #creates the question line 2 label that says "what does x equal" and places it at a set location on the GUI
        self.Qline2 = tk.Label(frame2, text = "What does x equal?").place(x=0 , y = 90)
                               
        #creates the answer label that says "answer" and places it at a set location on the GUI                       
        self.answerLabel = tk.Label(frame2, text = "Answer:").place(x = 0, y = 120)
        #creates the answer entry box
        self.user_answer_entry = tk.Entry(frame2)
        #places the answer entry box at a set location on the GUI
        self.user_answer_entry.place(x = 75, y = 120)
        #creates the enter button that says "submit" and places it at a set location on the GUI, when clicked the button calls forward the get_user_answer funtion that is inside the class
        self.enter = tk.Button(frame2, text = "Submit", command = lambda:self.get_user_answer(frame2, answer, level, lesson, question, score)).place(x = 200, y = 120) 

    #creates the function get_user_answer with the variables self, frame2, answer, level, lesson, question and score
    def get_user_answer(self, frame2, answer, level, lesson, question, score):
        user_answer = self.user_answer_entry.get()#sets the variable user_answer to the string value in the user answer entry box
        frame = frame2#sets the variable frame to the variable frame2
        #calls forward the check_answer function with the variables frame, answer, user_answer, level, lesson, question and score
        check_answer(frame, answer, user_answer, level, lesson, question, score)


#creates the triagle class which is called when the triangle button is pressed
#the triangle class creates four buttons, one entry box per question
# the class also randomly generates questions on three different levels
class triangles():

    #makes the funtion __init__ that atomatically initilizes when the class is called
    def __init__(self, level, question, score):#the variables self, level, question and score are pulled into the function

        root.title("Triangles")

        lesson = "triangles"#sets the variable lesson to the string value triangles 
        
        frame3 = tk.Frame()#creates a frames inside the container frame
        frame3.config( width=600, height = 600 )#sets the size of the frame to 600 pixels wide and 600 pixels tall
        frame3.grid(row = 0,column = 0)#places the frame in  a set location in the GUI
            
        frame3.tkraise()#raises the frame so that its viewable

        question = question + 1#increase the variable question by one
        question_number = tk.Label(frame3, text = str(question)+"/5").place(x = 200, y = 0)#places label that shows the user what questin out of 5 they are on

        if level == "0":#checks to see if the variable level is the string value 0

            #creates the levelpick label thats says "pick a level" and places it at a set loctaion on the GUI
            self.levelpick = tk.Label(frame3, text="Pick a level").place(x =90, y = 0)

            #creates the level1 button that says "level 1" that when pressed calls forward the level1 function inside this class
            self.level1button = tk.Button(frame3, text = "Level 1", command = lambda:self.level1(frame3, lesson, question, score))
            #places the button at a set location in the GUI
            self.level1button.place(x = 0, y = 30)

            #creates the level2 button that says "level 2" that when pressed calls forward the level2 function inside this class
            self.level2button = tk.Button(frame3, text = "Level 2",command = lambda:self.level2(frame3, lesson, question, score))
            #places the button at a set location in the GUI
            self.level2button.place(x = 100, y = 30)

            #creates the level3 button that says "level 3" that when pressed calls forward the level3 function inside this class
            self.level3button = tk.Button(frame3, text = "Level 3", command = lambda:self.level3(frame3, lesson, question, score))
            #places the button at a set location in the GUI
            self.level3button.place(x = 200, y = 30)
        

        if level == "1":#checks if the variable level matches the string value 1
            self.level1(frame3, lesson, question, score)#calls forward the level1 function with the variables frame2, lesson, question and score
        elif level == "2":#checks if the variable level matches the string value 2
            self.level2(frame3, lesson, question, score)#calls forward the level2 function with the variables frame2, lesson, question and score
        elif level == "3":#checks if the variable level matches the string value 3
            self.level3(frame3, lesson, question, score)#calls forward the level3 function with the variables frame2, lesson, question and score


    #creates the funtion level1 with the variables self, frame3, lesson, question and score
    def level1(self, frame3, lesson, question, score):
        level = "1"#sets the level variable to the string value 1
        combinedAngles = int(180)#sets the variable combinedAngles to the interger value 180
        while combinedAngles > 170:#loops while the variable combinedAngles is greater then the interger value 170
            angleA = random.randint(10,120)#sets the variable angleA to a random interger from 10-120
            angleB = random.randint(10,120)#sets the variable angleB to a random interger from 10-120
            combinedAngles = angleA + angleB#sets the variable combinedAngles to the inter value of the variable angleA plus the variable angleB
        answer = (180 - angleA)-angleB#sets the variable answer to the interger value of 180 minus the variable angleA minus the variable angleB

        photo = tk.PhotoImage(file = "triangleslevel1.png")#sets the variable photo to the photo stored in the file triagleslevel1.png
        self.pic_label = tk.Label(frame3, image=photo)#creates the picture label with the photo variable as the image
        self.pic_label.image = photo#sets the label as a photo
        self.pic_label.place(x = 135, y = 70)#places the label at a set location on the GUI
        
        #creates the question line 1 label with the text "angle A = (the variable angleA) degrees" and places it at a set loction on the GUI
        self.QLine1 = tk.Label(frame3, text = "Angle A = "+str(angleA)+" degrees").place(x = 0, y = 120)
        #creates the question line 2 label with the text "angle B = (the variable angleB) degrees" and places it at a set loction on the GUI
        self.QLine2 = tk.Label(frame3, text = "Angle B = "+str(angleB)+" degrees").place(x = 0, y = 150)
        #creates the question line 3 label with the text "what is the size of angle c" and places it at a set location on the GUI
        self.QLine3 = tk.Label(frame3, text = "What is the size of angle C?").place(x = 0, y = 180)

        #creates the answer label that says "answer" and places it at a set location on the GUI                       
        self.answerLabel = tk.Label(frame3, text = "Answer:").place(x = 0, y = 210)
        #creates the answer entry box
        self.user_answer_entry = tk.Entry(frame3)
        #places the answer entry box at a set location on the GUI
        self.user_answer_entry.place(x = 75, y = 210)
        #creates the enter button that says "submit" and places it at a set location on the GUI, when clicked the button calls forward the get_user_answer funtion that is inside the class
        self.enter = tk.Button(frame3, text = "Submit", command = lambda:self.get_user_answer(frame3, answer, level, lesson, question, score)).place(x = 200, y = 210)

    #creates the funtion level2 with the variables self, frame3, lesson, question and score
    def level2(self, frame3, lesson, question, score):
        level = "2"#sets the vriable level to the string value 2
        abORbc = random.choice([True,False])#sets the negORpos value to a random boolean value true or false
        if abORbc == True:#checks to see if the variable abORbc equals the boolean value true
            sideA = random.randint(2,12)#sets the variable sideA to a random interger from 2-12
            sideB = random.randint(2,12)#sets the variable sideB to a random interger from 2-12
            answer = float((sideA**2 + sideB**2)**0.5)#sets the variable answer to the square root of the combined squares of the variables sideA and sideB
            answer = round(answer,1)#sets the answer to answer rounded to one decimal place
            questionLine1 = str("Side A = "+str(sideA)+"cm")#sets the variable questionline1 to the string value of the question 
            questionLine2 = str("Side B = "+str(sideB)+"cm")#sets the variable questionline2 to the string value of the question
            #creates the question line 3 label that says "What is the length of side C (to one decimal place):" and places the label at a set location
            QLine3 = tk.Label(frame3, text = "What is the length of side C (to one decimal place): ").place(x = 0, y = 180)
                  
        elif abORbc == False:#checks to see if the variable abORbc equals the boolean value false
            sideC = random.randint(6,20)#sets the variable sideC to a random interger from 6-20
            sideB = random.randint(2,sideC-2)#sets the variable sideB to a random interger from 2  to the variable sideC minus 2
            answer = float((sideC**2 - sideB**2)**0.5)#sets the variable answer to the square roots of the squares of  sideC minus sideB
            answer = round(answer, 1)#rounds the variable answer to one decimal place
            questionLine1 = str("Side B = "+ str(sideB)+"cm")#sets the variable questionline1 to the string value of the question
            questionLine2 = str("Side C = "+str(sideC)+"cm")#sets the variable questionline2 to the string value of the question
            #creates the question line 3 label that says "What is the length of side A (to one decimal place):" and places the label at a set location
            QLine3 = tk.Label(frame3, text = "What is the length of side A (to one decimal place): ").place(x = 0, y = 180)

        photo = tk.PhotoImage(file = "triangleslevel2.png")#sets the variable photo to the photo stored in the file triagleslevel12.png
        self.pic_label = tk.Label(frame3, image=photo)#creates the picture label with the photo variable as the image
        self.pic_label.image = photo#sets the label as a photo
        self.pic_label.place(x = 120, y = 65)#places the label at a set location on the GUI

        #creates the question line 1 label that says the string variable questionLine1 and places it at a set location on the GUI
        self.QLine1 = tk.Label(frame3, text = questionLine1).place(x = 0, y = 120)
        #creates the question line 2 label that says the string variable questionLine2 and places it at a set location on the GUI
        self.QLine2 = tk.Label(frame3, text = questionLine2).place(x = 0, y = 150)
        #creates the answer label that says "answer" and places it at a set location on the GUI
        tk.Label(frame3, text = "Answer:").place(x = 0, y = 210)
        #creates the answer entry box
        self.user_answer_entry = tk.Entry(frame3)
        #places the answer entry box at a set location on the GUI
        self.user_answer_entry.place(x = 75, y = 210)
        #creates the enter button that says "submit" and places it at a set location on the GUI, when clicked the button calls forward the get_user_answer funtion that is inside the class        
        self.enter = tk.Button(frame3, text = "Submit", command = lambda:self.get_user_answer(frame3, answer, level, lesson, question, score)).place(x = 200, y = 210)


    #creates the funtion level3 with the variables self, frame3, lesson, question and score
    def level3(self, frame3, lesson, question, score):
        level = "3"#sets the variable level to the string value 3

        combinedAngles = int(180)#sets the variable combinedAngles to the interger value 180
        while combinedAngles > 170:#loops while the variable combinedAngles is greater then the interger value 170
            angleA = random.randint(10,120)#sets the variable angleA to a random interger from 10-120
            angleB = random.randint(10,120)#sets the variable angleB to a random interger from 10-120
            angleC = int((180 - angleB)-angleA)#sets the variable angleC to the interger value of 180 minus the variables angleA and angleB
            combinedAngles = angleA + angleB#sets the variable combinedAngles to the inter value of the variable angleA plus the variable angleB

        photo = tk.PhotoImage(file = "triangleslevel3.png")#sets the variable photo to the photo stored in the file triagleslevel13.png
        self.pic_label = tk.Label(frame3, image=photo)#creates the picture label with the photo variable as the image
        self.pic_label.image = photo#sets the label as a photo
        self.pic_label.place(x = 100, y = 65)#places the label at a set location on the GUI

        #creates the question line 1 label that says the first line of the generated question and places it at a set location on the GUI
        self.QLine1 = tk.Label(frame3, text = str("Angle A = "+ str(angleA))).place(x = 0, y = 60)
        #creates the question line 2 label that says the second line of the generated question and places it at a set location on the GUI
        self.QLine2 = tk.Label(frame3, text = str("Angle B = "+ str(angleB))).place(x = 0, y = 90)
        angleA = math.radians(angleA)#coverts the variable angleA from degrees to radians
        angleC = math.radians(angleC)#coverts the variable angleA from degrees to radians
        sideA = random.randint(2,12)#sets the variable sideA to a random interger from 2-12
        sideB = random.randint(2,12)#sets the variable sideB to a random interger from 2-12
        #creates the question line 3 label that says the third line of the generated question and places it at a set location on the GUI
        self.QLine3 = tk.Label(frame3, text = str("Side A = "+ str(sideA))).place(x = 0, y = 120)
        #creates the question line 4 label that says the fourth line of the generated question and places it at a set location on the GUI
        self.QLine4 = tk.Label(frame3, text = str("Side B = "+ str(sideB))).place(x = 0, y = 150)
        sinA = math.sin(angleA)#finds the sin value of the variable angleA and sets it as the variable sinA
        sinC = math.sin(angleC)#finds the sin value of the variable angleC and sets it as the variable sinC
        answer = float((sideA/sinA)*sinC)#works out the length of side C and sets it as the real variable answer 
        answer = round(answer,1)#rounds the variable answer to one decimal place
        #creates the question line 5 label that says "What is the length of side C (to one deciaml place)?" the  and places it at a set location on the GUI  
        self.QLine5 = tk.Label(frame3, text = "What is the length of side C (to one deciaml place)?").place(x = 0, y = 180)

        #creates the answer label that says "answer" and places it at a set location on the GUI
        tk.Label(frame3, text = "Answer:").place(x = 0, y = 210)
        #creates the answer entry box
        self.user_answer_entry = tk.Entry(frame3)
        #places the answer entry box at a set location on the GUI
        self.user_answer_entry.place(x = 75, y = 210)
        #creates the enter button that says "submit" and places it at a set location on the GUI, when clicked the button calls forward the get_user_answer funtion that is inside the class
        self.enter = tk.Button(frame3, text = "Submit", command = lambda:self.get_user_answer(frame3, answer, level, lesson, question, score)).place(x = 200, y = 210)

    #creates the function get_user_answer with the variables self, frame3, answer, level, lesson, question and score
    def get_user_answer(self, frame3, answer, level, lesson, question, score):
        user_answer = self.user_answer_entry.get()#sets the variable user_answer to the string value in the user answer entry box
        frame = frame3 #sets the variable frame to the variable frame3
        #calls forward the check_answer function with the variables frame, answer, user_answer, level, lesson, question and score
        check_answer(frame, answer, user_answer, level, lesson, question, score)

#creates the sequences class which is called when the sequences button is pressed on the main page
#the sequences class creates four buttons, one entry box per question
# the class also randomly generates questions on three different levels
class sequences():

    #makes the funtion __init__ that atomatically initilizes when the class is called
    def __init__(self, level, question, score):#the variables self, level, question and score are pulled into the function

        root.title("Sequences")

        lesson = "sequences"#sets the variable lesson to the string value sequences 
        
        frame4 = tk.Frame()#creates a frames inside the container frame
        frame4.config( width=600, height = 600 )#sets the size of the frame to 600 pixels wide and 600 pixels tall
        frame4.grid(row = 0,column = 0)#places the frame in  a set location in the GUI
            
        frame4.tkraise()#raises the frame so that its viewable

        question = question + 1#increase the variable question by one
        question_number = tk.Label(frame4, text = str(question)+"/5").place(x = 200, y = 0)#places label that shows the user what questin out of 5 they are on

        if level == "0":#checks to see if the variable level is the string value 0

            #creates the levelpick label thats says "pick a level" and places it at a set loctaion on the GUI
            self.levelpick = tk.Label(frame4, text="Pick a level").place(x =90, y = 0)

            #creates the level1 button that says "level 1" that when pressed calls forward the level1 function inside this class
            self.level1button = tk.Button(frame4, text = "Level 1", command = lambda:self.level1(frame4, lesson, question, score))
            #places the button at a set location in the GUI
            self.level1button.place(x = 0, y = 30)

            #creates the level2 button that says "level 2" that when pressed calls forward the level2 function inside this class
            self.level2button = tk.Button(frame4, text = "Level 2",command = lambda:self.level2(frame4, lesson, question, score))
            #places the button at a set location in the GUI
            self.level2button.place(x = 100, y = 30)

            #creates the level3 button that says "level 3" that when pressed calls forward the level3 function inside this class
            self.level3button = tk.Button(frame4, text = "Level 3", command = lambda:self.level3(frame4, lesson, question, score))
            #places the button at a set location in the GUI
            self.level3button.place(x = 200, y = 30)
        

        if level == "1":#checks if the variable level matches the string value 1
            self.level1(frame4, lesson, question, score)#calls forward the level1 function with the variables frame4, lesson, question and score
        elif level == "2":#checks if the variable level matches the string value 2
            self.level2(frame4, lesson, question, score)#calls forward the level2 function with the variables frame4, lesson, question and score
        elif level == "3":#checks if the variable level matches the string value 3
            self.level3(frame4, lesson, question, score)#calls forward the level3 function with the variables frame4, lesson, question and score

    #creates the funtion level1 with the variables self, frame4, lesson, question and score
    def level1(self, frame4, lesson, question, score):
        level = "1"#sets the variable level to the string value 1
        xTerm = random.randint(3,10)#sets the variable xTerm to a random interger from 3-10
        numTerm = random.randint(3,15)#sets the variable numTerm to a random interger from 3-15
        negORpos = random.choice([True,False])#sets the variable negORpos to a random boolean value true or false
        nTerm = random.randint(4,10)#sets the variable nTerm to a random interger from 4-10

        if negORpos == True:#checks to see if the variable negORpos is true
            questionLine1 = str("The nth term is:   "+str(xTerm)+"X +"+str(numTerm))#sets the variable questionline1to the string value of the first line of the question        
        else:#if the variable negORpos is false
            questionLine1 = str("The nth term is:    "+str(xTerm)+"X - "+str(numTerm))#sets the variable questionline1to the string value of the first line of the question
            numTerm = numTerm * -1#coverts the varible numTerm to the negative version of numTerm
                
        answer = ((xTerm*nTerm)+numTerm)#sets variable answer to the interger value of variables xTerm and nTerm multiplied and the variable numTerm added on
        #creates the question line 2 label with the second line of the question as the text
        self.QLine2 = tk.Label(frame4, text = str("Work out the "+str(nTerm)+"th term")).place(x = 0, y = 60)
        #creates the question line 1 label with the questionLine1 variable as the text
        self.Qline1 = tk.Label(frame4, text = questionLine1).place(x = 0, y = 90)

        #creates the answer label that says "answer" and places it at a set location on the GUI
        tk.Label(frame4, text = "Answer:").place(x = 0, y = 120)
        #creates the answer entry box
        self.user_answer_entry = tk.Entry(frame4)
        #places the answer entry box at a set location on the GUI
        self.user_answer_entry.place(x = 75, y = 120)
        #creates the enter button that says "submit" and places it at a set location on the GUI, when clicked the button calls forward the get_user_answer funtion that is inside the class
        self.enter = tk.Button(frame4, text = "Submit", command = lambda:self.get_user_answer(frame4, answer, level, lesson, question, score)).place(x = 200, y = 120)


    #creates the function level2 with the variables self, frame4, lesson, question and score
    def level2(self, frame4, lesson, question, score):
        level = "2"#sets the variable level to the string value 2
        xTerm = random.randint(2,6)#sets the variable xTerm to a random interger from 2-6
        numTerm = random.randint(3,15)#sets the variable numTerm to a random interger 3-15
        negORpos = random.choice([True,False])#sets the variable negORpos to a random boolean value of true or false
        nTerm = random.randint(4,10)#sets the variable nTerm to a random interger 4-10

        if negORpos == True:#checks to see if the variable negORpos is true
            questionLine1 = str("The nth term is:   "+str(xTerm)+"X^2 +"+str(numTerm))#sets the variable questionline 1 to the string value of the generated question        
        else:#if the variable negORpos is false
            questionLine1 = str("The nth term is:    "+str(xTerm)+"X^2 - "+str(numTerm))#sets the variable questionline 1 to the string value of the generated question
            numTerm = numTerm * -1#coverts the varible numTerm to the negative version of numTerm

        answer = (((nTerm**2)*xTerm)+numTerm)#sets the interger variable answer to the varible nTerm squared multiplied by the variable xTerm and the variable numTerm added
        #creates the QLine2 label that says the seconded line of the generated question and places it at a set location
        self.QLine2 = tk.Label(frame4, text = str("Work out the "+str(nTerm)+"th term")).place(x = 0, y = 60)
        #creates the QLine1 label that says the string value stored in the variable questionLine1 and places it at a set location on the GUI
        self.QLine1 = tk.Label(frame4, text = questionLine1).place(x = 0, y = 90)

        #creates the answer label that says "answer" and places it at a set location on the GUI
        tk.Label(frame4, text = "Answer:").place(x = 0, y = 120)
        #creates the answer entry box
        self.user_answer_entry = tk.Entry(frame4)
        #places the answer entry box at a set location on the GUI
        self.user_answer_entry.place(x = 75, y = 120)
        #creates the enter button that says "submit" and places it at a set location on the GUI, when clicked the button calls forward the get_user_answer funtion that is inside the class
        self.enter = tk.Button(frame4, text = "Submit", command = lambda:self.get_user_answer(frame4, answer, level, lesson, question, score)).place(x = 200, y = 120)
            

    #creates the level3 function with the variables self, frame4, lesson, question and score    
    def level3(self, frame4, lesson, question, score):
        level = "3"#sets the variable level to the string value 3
        xTerm = random.randint(2,5)#sets the variable xTerm to a random interger from 2-5
        numTerm = random.randint(1,5)#sets the variable numTerm to a random interger from 1-5
        negORpos = random.choice([True,False])#sets the variable negORpos to a random boolean value true or false
        termList = []#sets the variable termList to an empty list
        if negORpos == True:#checks if the variable negORpos is true
            numTerm = numTerm * -1#turns the varibale numTerm negative
        for i in range (1,6):#loops for a set amount of times
            term = ((xTerm*i)+numTerm)#the variable term is set as the value of the variable term multiplied by i and the variable numTerm added on
            termList.append(term)#the value term is added to the end of the list variable termList

        #creates the QLine1 label that says "The first five terms of the sequence are:" and places it at a set location on the GUI
        self.QLine1 = tk.Label(frame4, text = "The first five terms of the sequence are:").place(x = 0, y = 60)
        #creates the QLine2 label that says the second line of the question and places it at a set location on the GUI
        self.QLine2 = tk.Label(frame4, text = str(termList)).place(x = 0, y = 90)
        #creates the QLine3 label that says the third line of the question and places it at a set location on the GUI
        self.QLine3 = tk.Label(frame4, text = "What is the nth term (in terms of x)").place(x = 0, y = 120)
        xTerm = str(xTerm)#converts the interger variable xTerm to a string variable
        numTerm = str(numTerm)#converts the interger variable numTerm to a string variable
        if negORpos == True:#checks to see if the variable negORpos is true
            answer = (xTerm+"x"+numTerm)#generates the answer
        else:#if the variable negORpos is false
            answer = (xTerm+"x+"+numTerm)#generates the answer

        #creates the answer label that says "answer" and places it at a set location on the GUI
        tk.Label(frame4, text = "Answer:").place(x = 0, y = 150)
        #creates the answer entry box
        self.user_answer_entry = tk.Entry(frame4)
        #places the answer entry box at a set location on the GUI
        self.user_answer_entry.place(x = 75, y = 150)
        #creates the enter button that says "submit" and places it at a set location on the GUI, when clicked the button calls forward the get_user_answer funtion that is inside the class
        self.enter = tk.Button(frame4, text = "Submit", command = lambda:self.get_user_answer(frame4, answer, level, lesson, question, score)).place(x = 200, y = 150)

    #creates the function get_user_answer with the variables self, frame4, answer, level, lesson, question and score
    def get_user_answer(self, frame4, answer, level, lesson, question, score):
        user_answer = self.user_answer_entry.get()#sets the variable user_answer to the string value in the user answer entry box
        frame = frame4#sets the variable frame to the variable frame4
        #calls forward the check_answer function with the variables frame, answer, user_answer, level, lesson, question and score
        check_answer(frame, answer, user_answer, level, lesson, question, score)


#creates the area class which is called when the area button is pressed on the main page
#the area class creates four buttons, one entry box per question
# the class also randomly generates questions on three different levels
class area():

    #makes the funtion __init__ that atomatically initilizes when the class is called
    def __init__(self, level, question, score):#the variables self, level, question and score are pulled into the function

        root.title("Area")

        lesson = "area"#sets the variable lesson to the string value area 
        
        frame5 = tk.Frame()#creates a frames inside the container frame
        frame5.config( width=600, height = 600 )#sets the size of the frame to 600 pixels wide and 600 pixels tall
        frame5.grid(row = 0,column = 0)#places the frame in  a set location in the GUI
            
        frame5.tkraise()#raises the frame so that its viewable

        question = question + 1#increase the variable question by one
        question_number = tk.Label(frame5, text = str(question)+"/5").place(x = 200, y = 0)#places label that shows the user what questin out of 5 they are on

        if level == "0":#checks to see if the variable level is the string value 0

            #creates the levelpick label thats says "pick a level" and places it at a set loctaion on the GUI
            self.levelpick = tk.Label(frame5, text="Pick a level").place(x =90, y = 0)

            #creates the level1 button that says "level 1" that when pressed calls forward the level1 function inside this class
            self.level1button = tk.Button(frame5, text = "Level 1", command = lambda:self.level1(frame5, lesson, question, score))
            #places the button at a set location in the GUI
            self.level1button.place(x = 0, y = 30)

            #creates the level2 button that says "level 2" that when pressed calls forward the level2 function inside this class
            self.level2button = tk.Button(frame5, text = "Level 2",command = lambda:self.level2(frame5, lesson, question, score))
            #places the button at a set location in the GUI
            self.level2button.place(x = 100, y = 30)

            #creates the level3 button that says "level 3" that when pressed calls forward the level3 function inside this class
            self.level3button = tk.Button(frame5, text = "Level 3", command = lambda:self.level3(frame5, lesson, question, score))
            #places the button at a set location in the GUI
            self.level3button.place(x = 200, y = 30)
        

        if level == "1":#checks if the variable level matches the string value 1
            self.level1(frame5, lesson, question, score)#calls forward the level1 function with the variables frame5, lesson, question and score
        elif level == "2":#checks if the variable level matches the string value 2
            self.level2(frame5, lesson, question, score)#calls forward the level2 function with the variables frame5, lesson, question and score
        elif level == "3":#checks if the variable level matches the string value 3
            self.level3(frame5, lesson, question, score)#calls forward the level3 function with the variables frame5, lesson, question and score


    #creates the function level1 with the variables sefl, frame5, lesson, question and score   
    def level1(self, frame5, lesson, question, score):
        level = "1"#sets the variable level to the string value 1
        sideA = random.randint(3,12)#sets the variable sideA to a random interger from 3-12
        sideB = random.randint(3,12)#sets the variable sideB to a random interger from 3-12
        strSideA = str(sideA)#sets the variable strtSideA to the string value of the variable sideA
        strSideB = str(sideB)#sets the variable strtSideB to the string value of the variable sideB
        questionLine1= str("Side A = " +strSideA)#sets the variable questionLine1 to the string value of the first line of the generate question
        questionLine2 = str("Side B = "+strSideB)#sets the variable questionLine2 to the string value of the second line of the generate question
        answer = sideA*sideB#generates the answern and sets it as the variable answer

        photo = tk.PhotoImage(file = "arealevel1.png")#sets the variable photo to the photo stored in the file arealevel1.png
        self.pic_label = tk.Label(frame5, image=photo)#creates the picture label with the photo variable as the image
        self.pic_label.image = photo#sets the label as a photo
        self.pic_label.place(x = 100, y = 65)#places the label at a set location on the GUI

        #creates the label QLine1 that says the string value stored in the variable questionLine1 and places it at a set location on the GUI
        self.QLine1 = tk.Label(frame5, text = questionLine1).place(x = 0, y = 120)
        #creates the label QLine2 that says the string value stored in the variable questionLine2 and places it at a set location on the GUI
        self.QLine2 = tk.Label(frame5, text = questionLine2).place(x = 0, y = 150)
        #creates the label QLine3 that says "What is the area of the rectangle?" and places it at a set location on the GUI
        self.QLine3 = tk.Label(frame5, text = "What is the area of the rectangle?").place(x = 0, y = 180)

        #creates the answer label that says "answer" and places it at a set location on the GUI
        tk.Label(frame5, text = "Answer:").place(x = 0, y = 210)
        #creates the answer entry box
        self.user_answer_entry = tk.Entry(frame5)
        #places the answer entry box at a set location on the GUI
        self.user_answer_entry.place(x = 75, y = 210)
        #creates the enter button that says "submit" and places it at a set location on the GUI, when clicked the button calls forward the get_user_answer funtion that is inside the class
        self.enter = tk.Button(frame5, text = "Submit", command = lambda:self.get_user_answer(frame5, answer, level, lesson, question, score)).place(x = 200, y = 210)


    #creatse the function level2 with the variables self, frame5, lesson, question and score   
    def level2(self, frame5, lesson, question, score):
        level = "2"#set the varible level as the string value 2
        radius = random.randint(3,15)#set the variable radius as a random interger from 3-15
        strRadius = str(radius)#sets the variable strRadius as the string value of the variable radius
        questionLine1 = str("The radius of the circle is "+str(radius)+"cm")#sets the variable questionLine1 as the string value of the generated question
        #creates the label QLine1 that says the string value stored in the variable questionLine1 and places it at a set location on the GUI
        self.QLine1 = tk.Label(frame5, text = questionLine1).place(x = 0, y = 150)
        #creates the label QLine2 that says "What is the area of the circle (to one deciaml place):" and places it at a set location on the GUI
        self.QLine2 = tk.Label(frame5, text = "What is the area of the circle (to one deciaml place):").place(x = 0, y = 180)
        pi = math.pi#sets the variable pi to equal the value pi from themath libary
        answer = ((radius**2)*pi)#generates the answer and sets it as the real variable answer
        answer = round(answer,1)#rounds the variable answer to one decimal place

        photo = tk.PhotoImage(file = "arealevel2.png")#sets the variable photo to the photo stored in the file arealevel12.png
        self.pic_label = tk.Label(frame5, image=photo)#creates the picture label with the photo variable as the image
        self.pic_label.image = photo#sets the label as a photo
        self.pic_label.place(x = 180, y = 65)#places the label at a set location on the GUI

        #creates the answer label that says "answer" and places it at a set location on the GUI
        tk.Label(frame5, text = "Answer:").place(x = 0, y = 210)
        #creates the answer entry box
        self.user_answer_entry = tk.Entry(frame5)
        #places the answer entry box at a set location on the GUI
        self.user_answer_entry.place(x = 75, y = 210)
        #creates the enter button that says "submit" and places it at a set location on the GUI, when clicked the button calls forward the get_user_answer funtion that is inside the class
        self.enter = tk.Button(frame5, text = "Submit", command = lambda:self.get_user_answer(frame5, answer, level, lesson, question, score)).place(x = 200, y = 210)

    #creates the function level3 with the variables self, frame5, lesson, question and score
    def level3(self, frame5, lesson, question, score):
        level = "3"#sets the variable level as the string value 3
        sideA = random.randint(2,14)#sets the variable sideA as a random interger from 2-14
        sideB = random.randint(2,14)#sets the variable sideB as a random interger from 2-14
        height = random.randint(2,8)#sets the variable height as a random interger from 2-8
        strSideA = str(sideA)#sets the variable strSideA as the string value of the variable sideA
        strSideB = str(sideB)#sets the variable strSideB as the string value of the variable sideB
        strHeight = str(height)#sets the variable strHeight as the string value of the variable height
        questionLine1 = str("Side A = "+strSideA)#sets the variable questionLine1 as the string of the first line of the generated question
        questionLine2 = str("Side B = "+strSideB)#sets the variable questionLine2 as the string of the second line of the generated question
        questionLine3 = str("Height = "+strHeight)#sets the variable questionLine3 as the string of the third line of the generated question

        photo = tk.PhotoImage(file = "arealevel3.png")#sets the variable photo to the photo stored in the file arealevel13.png
        self.pic_label = tk.Label(frame5, image=photo)#creates the picture label with the photo variable as the image
        self.pic_label.image = photo#sets the label as a photo
        self.pic_label.place(x = 100, y = 65)#places the label at a set location on the GUI

        #creates the label QLine1 that says the string value stored in the variable questionLine1 and places it at a set location on the GUI
        self.QLine1 = tk.Label(frame5, text = questionLine1).place(x = 0, y = 90)
        #creates the label QLine2 that says the string value stored in the variable questionLine2 and places it at a set location on the GUI
        self.QLine2 = tk.Label(frame5, text = questionLine2).place(x = 0, y = 120)
        #creates the label QLine3 that says the string value stored in the variable questionLine3 and places it at a set location on the GUI
        self.QLine3 = tk.Label(frame5, text = questionLine3).place(x = 0, y = 150)
        #creates the label QLine4 that says "What is the area of the trapezoid (to one decimal place):" and places it at a set location on the GUI
        self.QLine4 = tk.Label(frame5, text = "What is the area of the trapezoid (to one decimal place):").place(x=0, y = 180)

        #creates the answer label that says "answer" and places it at a set location on the GUI
        tk.Label(frame5, text = "Answer:").place(x = 0, y = 210)
        #creates the answer entry box
        self.user_answer_entry = tk.Entry(frame5)
        #places the answer entry box at a set location on the GUI
        self.user_answer_entry.place(x = 75, y = 210)
        answer = float((0.5*(sideA+sideB))*height)
        #creates the enter button that says "submit" and places it at a set location on the GUI, when clicked the button calls forward the get_user_answer funtion that is inside the class
        self.enter = tk.Button(frame5, text = "Submit", command = lambda:self.get_user_answer(frame5, answer, level, lesson, question, score)).place(x = 200, y = 210)

    #creates the function get_user_answer with the variables self, frame5, answer, level, lesson, question and score
    def get_user_answer(self, frame5, answer, level, lesson, question, score):
        user_answer = self.user_answer_entry.get()#sets the variable user_answer to the string value in the user answer entry box
        frame = frame5#sets the variable frame to the variable frame5
        #calls forward the check_answer function with the variables frame, answer, user_answer, level, lesson, question and score
        check_answer(frame, answer, user_answer, level, lesson, question, score)


#creates the graph class which is called when the graph button is pressed on the main page
#the graph class creates four buttons, one entry box per question
# the class also randomly generates questions on three different levels
#the class also generates one graph per question
class graph:

    #makes the funtion __init__ that atomatically initilizes when the class is called
    def __init__(self, level, question, score):#the variables self, level, question and score are pulled into the function

        root.title("Graph")

        lesson = "graph"#sets the variable lesson to the string value graph 
        
        frame6 = tk.Frame()#creates a frames inside the container frame
        frame6.config( width=600, height = 600 )#sets the size of the frame to 600 pixels wide and 600 pixels tall
        frame6.grid(row = 0,column = 0)#places the frame in  a set location in the GUI
            
        frame6.tkraise()#raises the frame so that its viewable

        question = question + 1#increase the variable question by one
        question_number = tk.Label(frame6, text = str(question)+"/5").place(x = 200, y = 0)#places label that shows the user what questin out of 5 they are on

        if level == "0":#checks to see if the variable level is the string value 0

            #creates the levelpick label thats says "pick a level" and places it at a set loctaion on the GUI
            self.levelpick = tk.Label(frame6, text="Pick a level").place(x =90, y = 0)

            #creates the level1 button that says "level 1" that when pressed calls forward the level1 function inside this class
            self.level1button = tk.Button(frame6, text = "Level 1", command = lambda:self.level1(frame6, lesson, question, score))
            #places the button at a set location in the GUI
            self.level1button.place(x = 0, y = 30)

            #creates the level2 button that says "level 2" that when pressed calls forward the level2 function inside this class
            self.level2button = tk.Button(frame6, text = "Level 2",command = lambda:self.level2(frame6, lesson, question, score))
            #places the button at a set location in the GUI
            self.level2button.place(x = 100, y = 30)

            #creates the level3 button that says "level 3" that when pressed calls forward the level3 function inside this class
            self.level3button = tk.Button(frame6, text = "Level 3", command = lambda:self.level3(frame6, lesson, question, score))
            #places the button at a set location in the GUI
            self.level3button.place(x = 200, y = 30)
        

        if level == "1":#checks if the variable level matches the string value 1
            self.level1(frame6, lesson, question, score)#calls forward the level1 function with the variables frame6, lesson, question and score
        elif level == "2":#checks if the variable level matches the string value 2
            self.level2(frame6, lesson, question, score)#calls forward the level2 function with the variables frame6, lesson, question and score
        elif level == "3":#checks if the variable level matches the string value 3
            self.level3(frame6, lesson, question, score)#calls forward the level3 function with the variables frame6, lesson, question and score


    
    #creates the function level1 with the variables self, frame6, lesson, question and score
    def level1(self, frame6, lesson, question, score):
        
        level = "1"#sets the variable level to the string value 1
        xFactor = random.randint(2,5)#sets the variable xFactor to a random interger from 2-5
        unit = random.randint(1,5)#sets the variable unit to a random interger from 1-5
        yValues = []#sets the variable yValues to an empty list
        xValue = random.randint(1,5)#sets the variable xValue to a random interger from 1-5
        answer = (xValue*xFactor)+unit#sets the variable answer to the interger value of the variable xValue multiplied by the variable xFactor plus the variable unit

        #creates the label QLine1 that says first line of the question and places it at a set location on the GUI
        self.QLine1 = tk.Label(frame6, text = "What is the value of Y when X is "+str(xValue)+":").place(x = 0, y = 90)

        #creates the answer label that says "answer" and places it at a set location on the GUI
        tk.Label(frame6, text = "Answer:").place(x = 0, y = 120)
        #creates the answer entry box
        self.user_answer_entry = tk.Entry(frame6)
        #places the answer entry box at a set location on the GUI
        self.user_answer_entry.place(x = 75, y = 120)
        #creates the enter button that says "submit" and places it at a set location on the GUI, when clicked the button calls forward the get_user_answer funtion that is inside the class
        self.enter = tk.Button(frame6, text = "Submit", command = lambda:self.get_user_answer(frame6, answer, level, lesson, question, score)).place(x = 200, y = 120)

        for i in range(1,6):#loops through 5 times
            y = (i*xFactor)+unit#sets the interger variable y to the varible i multiplied by the variable xFactor and the variable unit added
            yValues.append(y)#adds the variable y to the end of the yValues list
                               
        plt.plot([1,2,3,4,5],yValues)#plots graph with the values inside the first square brackets as the x co-ordinates and the values in the yValues list as the y co-ordinates
        plt.show()#makes the graph visable     



            
    #creates the function level2 with the variables self, frame6, lesson, question and score
    def level2(self, frame6, lesson, question, score):
        level = "2"#sets the variable level to the string value 2
        xFactor = random.randint(2,5)#sets the variable xFactor to a random interger from 2-5
        unit = random.randint(1,5)#sets the variable unit to a random interger 1-5
        yValues = []#sets the variable yValues to an empty list

        #creates the answer label that says "answer" and places it at a set location on the GUI
        tk.Label(frame6, text = "Answer:").place(x = 0, y = 120)
        #creates the answer entry box
        self.user_answer_entry = tk.Entry(frame6)
        #places the answer entry box at a set location on the GUI
        self.user_answer_entry.place(x = 75, y = 120)
        #creates the enter button that says "submit" and places it at a set location on the GUI, when clicked the button calls forward the get_user_answer funtion that is inside the class
        self.enter = tk.Button(frame6, text = "Submit",command = lambda:self.get_user_answer(frame6, answer, level, lesson, question, score)).place(x = 200, y = 120)   
        Qline2 = tk.Label(frame6, text = "True or False:").place(x=0,y=90)
        
        TrueOrFalse = random.choice([True,False])#sets the variable TrueOrFalse to a random boolean value true or false
        if TrueOrFalse == True:#checks to see if the TrueOrFalse variable is true
            answer = "true"#sets the variable answer to the string value true
            #creates the label QLine1 that says first line of the question and places it at a set location on the GUI
            QLine1 = tk.Label(frame6, text = "Is this graph "+str(xFactor)+"x +"+str(unit)).place(x=0, y=60)
        else:#if the variable TrueOrFlase is false
            answer = "false"#set the variable answer to the string value false
            falsexFactor = random.randint(2,5)#sets the variable falsexFactor to a random interger value 2-5
            while falsexFactor == xFactor:#checks if the variable falsexFactor matches the variable xFactor
                falsexFactor = random.randint(2,5)#sets the variable falsexFactor to a random interger value 2-5
            falseUnit = random.randint(1,5)#sets the variable falseUnit to a random interger value 1-5
            #creates the label QLine1 that says first line of the question and places it at a set location on the GUI
            QLine1 = tk.Label(frame6, text = "Is this graph "+str(falsexFactor)+"x +"+str(falseUnit)).place(x=0, y=60)

        for i in range(1,6):#loops through 5 times, with i starting at 1 and ending at 5
            y = (i*xFactor)+unit#sets the interger variable y to the varible i multiplied by the variable xFactor and the variable unit added
            yValues.append(y)#adds the variable y to the end of the yValues list
                               
        plt.plot([1,2,3,4,5],yValues)#plots graph with the values inside the first square brackets as the x co-ordinates and the values in the yValues list as the y co-ordinates
        plt.show()#makes the graph visable 

    #creates the function level3 with the variables self, frame6, lesson, question and score                          
    def level3(self, frame6, lesson, question, score):
        level = "3"#sets the variable level to the string value 3
        typeOfGraph = random.randint(1,3)#sets the variable tyoeOfGraph to a random interger 1-3
        xValue = random.randint(2,5)#sets the variable xValue to a random interger 2-5
        unit = random.randint(1,5)#sets the variable unit to a random interger 1-5
        yValues = []#sets the variable yValues to an empty list
        #creates the label QLine1 that says f"Is the graph cubic, quadratic or linear:" and places it at a set location on the GUI
        self.QLine1 = tk.Label(frame6, text = "Is the graph cubic, quadratic or linear:").place(x = 0, y = 90)

        #creates the answer label that says "answer" and places it at a set location on the GUI                       
        tk.Label(frame6, text = "Answer:").place(x = 0, y = 120)
        #creates the answer entry box
        self.user_answer_entry = tk.Entry(frame6)
        #places the answer entry box at a set location on the GUI
        self.user_answer_entry.place(x = 75, y = 120)
        self.enter = tk.Button(frame6, text = "Submit",command = lambda:self.get_user_answer(frame6, answer, level, lesson, question, score)).place(x = 200, y = 120)
                               
        if typeOfGraph == 1:#checks if the variable typeOfGraph matches the interger value 1
            for i in range(-5,6):#loops through 10 times, with i starting at -5 and ending at 5
                y = (i**3)+(i**2)+(i*xValue)+unit#makes the variable y set to a cubic equation with i as the variable
                yValues.append(y)#adds the variable y to the end of the yValues list
            answer = "cubic"#set the variable answer to the string value cubic
        elif typeOfGraph == 2:#checks if the variable typeOfGraph matches the interger value 2
            for i in range(-5,6):#loops through 10 times, with i starting at -5 and ending at 5
                y = (i**2)+(i*xValue)+unit#makes the variable y set to a quadratic equation with i as the variable
                yValues.append(y)#adds the variable y to the end of the yValues list
            answer = "quadratic"#set the variable answer to the string value quadratic
        elif typeOfGraph == 3:#checks if the variable typeOfGraph matches the interger value 3
            for i in range(-5,6):#loops through 10 times, with i starting at -5 and ending at 5
                y = (i*xValue)+unit#makes the variable y set to a linear equation with i as the variable
                yValues.append(y)#adds the variable y to the end of the yValues list
            answer = "linear"#set the variable answer to the string value linear
        plt.plot([-5,-4,-3,-2,-1,0,1,2,3,4,5],yValues)#plots graph with the values inside the first square brackets as the x co-ordinates and the values in the yValues list as the y co-ordinates
        plt.show()#makes the graph visable 

    #creates the function get_user_answer with the variables self, frame6, answer, level, lesson, question and score
    def get_user_answer(self, frame6, answer, level, lesson, question, score):
        plt.close()#closes the graph window
        user_answer = self.user_answer_entry.get()#sets the variable user_answer to the string value in the user answer entry box
        user_answer = user_answer.lower()#converts the variable user_answer to lower case
        frame = frame6#sets the variable frame to the variable frame6
        #calls forward the check_answer function with the variables frame, answer, user_answer, level, lesson, question and score
        check_answer(frame, answer, user_answer, level, lesson, question, score)

#creates check_answer function with the variables frame, answer, usesr_answer, level, lesson, question and score
def check_answer(frame, answer, user_answer, level, lesson, question, score):
    global user_score, user_row#defines the variables user_score and user_row as global variables
    frame.destroy()#destroys the current question frame
    answer = str(answer)#coverts the variable answer into a string value
    if answer == user_answer:#checks to see if the user got the correct answer
        score = score + 1#increase the variable score by one
        tk.messagebox.showinfo("","Correct")#creates a message box that says "correct"
    else:#if the user got the question wrong
        tk.messagebox.showinfo("","Incorrect")#creates a message box that says "incorrect"
    if question == 5:#checks if the variable question matches the interger value 5
        database = csv.reader(open('score.csv'))#opens the file 'score.csv' as the variable database
        lines = [l for l in database]
        question = 0#sets the variable question to the interger value 0
        if lesson == "algebra":#checks if the variable lesson matches the string value algebra
            if level == "1":#checks if the variable level matches the string value 1
                user_score[0] = score#sets the correct position in the user_score list to the new score
                lines[user_row][2] = str(score)#changes the score in the score.csv file to the new score
            elif level == "2":#checks if the variable level matches the string value 2
                user_score[1] = score#sets the correct position in the user_score list to the new score
                lines[user_row][3] = str(score)#changes the score in the score.csv file to the new score
            else:#if the variable level is the string value 3
                user_score[2] = score#sets the correct position in the user_score list to the new score
                lines[user_row][4] = str(score)#changes the score in the score.csv file to the new score
        elif lesson == "triangles":#checks if the variable lesson matches the string value algebra
            if level == "1":#checks if the variable level matches the string value 1
                user_score[3] = score#sets the correct position in the user_score list to the new score
                lines[user_row][5] = str(score)#changes the score in the score.csv file to the new score
            elif level == "2":#checks if the variable level matches the string value 2
                user_score[4] = score#sets the correct position in the user_score list to the new score
                lines[user_row][6] = str(score)#changes the score in the score.csv file to the new score
            else:#if the variable level is the string value 3
                user_score[5] = score#sets the correct position in the user_score list to the new score
                lines[user_row][7] = str(score)#changes the score in the score.csv file to the new score
        elif lesson == "sequences":#checks if the variable lesson matches the string value algebra
            if level == "1":#checks if the variable level matches the string value 1
                user_score[6] = score#sets the correct position in the user_score list to the new score
                lines[user_row][8] = str(score)#changes the score in the score.csv file to the new score
            elif level == "2":#checks if the variable level matches the string value 2
                user_score[7] = score#sets the correct position in the user_score list to the new score
                lines[user_row][9] = str(score)#changes the score in the score.csv file to the new score
            else:#if the variable level is the string value 3
                user_score[8] = score#sets the correct position in the user_score list to the new score
                lines[user_row][10] = str(score)#changes the score in the score.csv file to the new score
        elif lesson == "area":#checks if the variable lesson matches the string value algebra
            if level == "1":#checks if the variable level matches the string value 1
                user_score[9] = score#sets the correct position in the user_score list to the new score
                lines[user_row][11] = str(score)#changes the score in the score.csv file to the new score
            elif level == "2":#checks if the variable level matches the string value 2
                user_score[10] = score#sets the correct position in the user_score list to the new score
                lines[user_row][12] = str(score)#changes the score in the score.csv file to the new score
            else:#if the variable level is the string value 3
                user_score[11] = score#sets the correct position in the user_score list to the new score
                lines[user_row][13] = str(score)#changes the score in the score.csv file to the new score
        elif lesson == "graph":#checks if the variable lesson matches the string value algebra
            if level == "1":#checks if the variable level matches the string value 1
                user_score[12] = score#sets the correct position in the user_score list to the new score
                lines[user_row][14] = str(score)#changes the score in the score.csv file to the new score
            elif level == "2":#checks if the variable level matches the string value 2
                user_score[13] = score#sets the correct position in the user_score list to the new score
                lines[user_row][15] = str(score)#changes the score in the score.csv file to the new score
            else:#if the variable level is the string value 3
                user_score[14] = score#sets the correct position in the user_score list to the new score
                lines[user_row][16] = str(score)#changes the score in the score.csv file to the new score

        writer = csv.writer(open('score.csv', 'w', newline=''))#opens the file score.csv in write mode
        writer.writerows(lines)#adds the new scores into the file score.csv
        score = 0#sets the variable score to the interger value 0
        
    else:#if the variable question is not the interger value 5
        if lesson == "algebra":#checks if the variable lesson matches the string value algebra
           algebra(level, question, score)#calls forward the class algebra with the variables level, question and score
        elif lesson == "triangles":#checks if the variable lesson matches the string value traiangles
            triangles(level, question, score)#calls forward the class triangles with the variables level, question and score
        elif lesson == "sequences":#checks if the variable lesson matches the string value sequences
            sequences(level, question, score)#calls forward the class sequences with the variables level, question and score
        elif lesson == "area":#checks if the variable lesson matches the string value area
            area(level, question, score)#calls forward the class area with the variables level, question and score
        elif lesson == "graph":#checks if the variable lesson matches the string value graph
            graph(level, question, score)#calls forward the class graph with the variables level, question and score


#creates the fuction create_main_page
def create_main_page():

    global container #defines the variable container as a global variable

    score = int(0)#sets the variable score as the interger value 0
    question = int(0)#sets the variable question as the interger value 0
    root = tk.Tk()#sets the variable root as a tkinter window
    root.geometry("350x250")#sets the size of the window 
    root.title("Main Page")#sets the title of the window to main page
    container = tk.Frame(root)#creates the frae container in the window
    container.grid(column = 0, row = 0)#places the container frame in a set location

    app = main_page(root, question, score)#calls forward the main_page class

#creates the function create_login_page with the variable password_username
def create_login_page(password_username):
  
    root = tk.Tk()#sets the variable root as a tkinter window
    root.geometry("190x95")#sets the size of the window
    root.title("Login Page")#sets the title of the window to main page

    app = Login_Page(root, password_username)#calls forward the Login_page class



container = ""#sets the variable container as a empty string value
user_row = 0#sets the variable user_row variable as the interger value 0
user_score = []#sets the variable user_score as an empty list
password_username = "0"#sets the variable password_username as the string variable 0
create_login_page(password_username)#calls forward the create_login_page class

