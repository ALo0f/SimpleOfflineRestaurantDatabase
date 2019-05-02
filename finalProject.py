#  Offline restaurant database
#restaurant.py
#WU TIANYI
#Michael
#twu116

#import libraries for use

from graphics import *

import random

import time

import math


#This class method stores restaurants as lists 
#,it can also search restaurant, add new restaurant to database and randomly recommend a restaurant in database

class restaurantList:

    #setting up environment
    def __init__(self):
        self.name=[]
        self.flavor=[]
        self.contact=[]
        self.price=[]
        self.address=[]

    #parameter is name, flabor, contact, price,address
    #it append each parameter into lists set in the init
    def add(self,name,flavor,contact,price,address):
        self.name.append(name)
        self.flavor.append(flavor)
        self.contact.append(contact)
        self.price.append(price)
        self.address.append(address)

    #parameter is text, text is what user typed in the searching box(after clicking the submit button), which is in line 176
    #it does have multiple if statement to play against bad inputs
    def search(self,text):
        result = []
        if text !="":
            text = text.lower()
            for i in range(len(self.name)):
                if self.name[i].lower().find(text) >= 0:
                    result.append(i)
    
        return result

    #parameter is a,b,c,d,e, which corresponds to line 435-441 and line 452
    def addrest(self,a,b,c,d,e):
        aList=[a,b,c,d,e]
        result = " ".join(aList)
        self.add(a,b,int(c),int(d),e)
        file = open("restaurant.txt", "a")
        print(result, file=file)
        file.close()
    #it will randomly pick an int from length of name lists,then return a random picked number
    #it is used in line 520
    def randomRest(self):
        index = random.randint(0, len(self.name)-1)
        return index
            

rList = restaurantList()


#Setting up the graph window 
#Window name is offline restaurant database
# Size is 600*600,background is White for a clear view,coordinates setting from -10 to 10, center point is (0,0)
def setUpWindow():
    win=GraphWin("offline restaurant database",600,600)

    win.setBackground("white")

    win.setCoords(-10,-10,10,10)

    return win

#Lable 2 titles for menu
def titleLable(win):
    titleLable=Text(Point(0,9.5),"Welcome To Offline Restaurant Database")
    titleLable.setSize(20)
    titleLable.draw(win)
    
    titleLable1=Text(Point(0,8),"Please Click The Button To Move On")
    titleLable1.setSize(8)
    titleLable1.draw(win)

    

#making button for 4 choices in menu
#search button,add button,any recommend button and quit button
def fourChoices(win):
    searchButton=Rectangle(Point(-8,6.5),Point(-2,0))
    searchButtonLable=Text(Point(-5,3.25),"SEARCH")
    searchButton.draw(win)
    searchButtonLable.draw(win)

    addButton=Rectangle(Point(2,6.5),Point(8,0))
    addButtonLable=Text(Point(5,3.25),"ADD")
    addButton.draw(win)
    addButtonLable.draw(win)

    
    
    randomButton=Rectangle(Point(-3,-2),Point(3,-8))
    randomButtonLable=Text(Point(0,-5.25),"ANY RECOMMEND?")
    randomButton.draw(win)
    randomButtonLable.draw(win)

    quitButton=Rectangle(Point(6.5,-8),Point(9,-10))
    quitButtonLable=Text(Point(7.7,-9),"QUIT")
    quitButton.draw(win)
    quitButtonLable.draw(win)



#It checks whether the user's clicked point is in one specific area
#it first get x&y coordinates of user's click and determine whether it is in one specific area or not
def checkButtonClick(clickedPoint,leftUpper,rightLower):
    if clickedPoint == None:
        return 0
    if clickedPoint.getX()>=leftUpper.getX() and clickedPoint.getX()<=rightLower.getX() and clickedPoint.getY()<=leftUpper.getY() and clickedPoint.getY()>=rightLower.getY():
        return 1

    else:
        return 0




#This function will show the graph and choices only when user clicked serach button in menu
def searchClicked():

    #draw the window

    win=setUpWindow()

    #draw entry box,top lable,submit button and quitButton
    enterName=Entry(Point(0,2),50)
    enterName.draw(win)

    titleLable2=Text(Point(0,9.5),"Please type in restaurant you want to search")
    titleLable2.setSize(20)
    titleLable2.draw(win)

    titleLable3=Text(Point(0,3.5),"Please type in restaurant you want to search")
    titleLable3.setSize(15)
    titleLable3.draw(win)

    submitButton=Rectangle(Point(-3,-3),Point(3,-6))
    submitButtonLable=Text(Point(0,-4.5),"SUBMIT")
    submitButton.draw(win)
    submitButtonLable.draw(win)

    quitButton=Rectangle(Point(6.5,-8),Point(9,-10))
    quitButtonLable=Text(Point(7.7,-9),"QUIT")
    quitButton.draw(win)
    quitButtonLable.draw(win)

    menuButton=Rectangle(Point(-6.5,-8),Point(-9,-10))
    menuButtonLable=Text(Point(-7.7,-9),"Menu")
    menuButton.draw(win)
    menuButtonLable.draw(win)

    clickedPoint=win.getMouse()

    #using while loop to recognize whether user clicked specific button or not
    #if not, while loop will keep collecting users' click
    #if it is true, then it will first close the window and then execute other functions and finally break
    while True:


        if checkButtonClick(clickedPoint,Point(-3,-3),Point(3,-6)) == 1:
            win.close()
            text=enterName.getText()
            x=rList.search(text)
            pageEntered(x)
            break
    

        if checkButtonClick(clickedPoint,Point(6.5,-8),Point(9,-10)) == 1:
            win.close()
            break

        if checkButtonClick(clickedPoint,Point(-9,-8),Point(-6.5,-10)) == 1:
            win.close()
            
            main()
            break

    

        clickedPoint=win.checkMouse()
        
    

    

#this function will show graph and choices only when user clicked "submit" after the above function
#x is a parameter for this function, x is derived from line 172, which represents the position of a searched restaurant in rList()
def pageEntered(x):
    #draw window
    win=setUpWindow()

    #draw 4 boxes and 4 lables

    yesButton=Rectangle(Point(-8,-3),Point(-2,-6))
    yesButtonLable=Text(Point(-5,-4.5),"YES")
    yesButton.draw(win)
    yesButtonLable.draw(win)


    noButton=Rectangle(Point(2,-3),Point(8,-6))
    noButtonLable=Text(Point(5,-4.5),"NO")
    noButton.draw(win)
    noButtonLable.draw(win)

    askingLable=Text(Point(0,2),"Do you find what you want to search? ")
    askingLable.setSize(20)
    askingLable.draw(win)

    enteredBox=Rectangle(Point(-8,7),Point(8,3))

    #setting an empty string for use
    string = ""
    
    #use for loop to get i number of information it needs in rList
    for i in x:
        string += "Name: " + rList.name[i]
        string += " Flavor: " + rList.flavor[i]
        string += " Contact: " + str(rList.contact[i])
        string += "\nPrice:" + str(rList.price[i])
        string += " Address: "
        string += "Local" if rList.address[i] == "True" else "Not Local"
        string += "\n"

    #setting up an if statement to test if there is no matching result
    if x == [] :
        string = "Resturant not found in Database"

    #draw information collected from the above,as i used string to store restaurant information
    enteredBoxLable=Text(Point(0,5),string)
    
    enteredBox.draw(win)

    enteredBoxLable.draw(win)
    
    #setting up quit button and menu button
    quitButton=Rectangle(Point(6.5,-8),Point(9,-10))
    quitButtonLable=Text(Point(7.7,-9),"QUIT")
    quitButton.draw(win)
    quitButtonLable.draw(win)

    menuButton=Rectangle(Point(-6.5,-8),Point(-9,-10))
    menuButtonLable=Text(Point(-7.7,-9),"Menu")
    menuButton.draw(win)
    menuButtonLable.draw(win)

    #using while loop to collect user clicks, it will call specific functions if user clicks in a specific area
    #if not, it will keep collecting user clicks
    clickedPoint=win.getMouse()
    while True:

        if checkButtonClick(clickedPoint,Point(-8,-3),Point(-2,-6)) == 1:
            win.close()
            yesPage()
            break


        if checkButtonClick(clickedPoint,Point(2,-3),Point(8,-6)) == 1:
            win.close()
            noPage()
            break

        if checkButtonClick(clickedPoint,Point(6.5,-8),Point(9,-10)) == 1:
            win.close()
            break

        if checkButtonClick(clickedPoint,Point(-9,-8),Point(-6.5,-10)) == 1:
            win.close()
            main()
            break

        

        clickedPoint=win.checkMouse()

#it will draw graph and give lables only when user click "YES" button in the PageEntered()
def yesPage():
    #draw window
    win=setUpWindow()

    #draw Lable
    firstLable=Text(Point(0,1),"Thanks for using offline")
    firstLable.setSize(20)
    secondLable=Text(Point(0,0),"Restaurant Database")
    secondLable.setSize(20)
    firstLable.draw(win)
    secondLable.draw(win)

    #when user clicked the mouse, the window closed
    win.getMouse()
    win.close()
    

#it will draw graph and give choices to user only when user click "NO" button in the PageEntered()     
def noPage():
    #draw window
    win=setUpWindow()

    #draw Lable

    againButton=Rectangle(Point(-8,2),Point(-2,-1))
    againButtonLable=Text(Point(-5,0.5),"search again")
    againButton.draw(win)
    againButtonLable.draw(win)


    addRButton=Rectangle(Point(2,2),Point(8,-1))
    addRButtonLable=Text(Point(5,0.5),"add rest")
    addRButton.draw(win)
    addRButtonLable.draw(win)

    quitButton=Rectangle(Point(6.5,-8),Point(9,-10))
    quitButtonLable=Text(Point(7.7,-9),"QUIT")
    quitButton.draw(win)
    quitButtonLable.draw(win)

    menuButton=Rectangle(Point(-6.5,-8),Point(-9,-10))
    menuButtonLable=Text(Point(-7.7,-9),"Menu")
    menuButton.draw(win)
    menuButtonLable.draw(win)

    

    clickedPoint=win.getMouse()
    #using while loop to recognize if user clicks a specific button
    #if yes, excute specific function
    #if not, keep collecting user clicks' position and recognize it
    while True:

        if checkButtonClick(clickedPoint,Point(-8,2),Point(-2,-1)) == 1:
            win.close()
            searchClicked()
            break


        if checkButtonClick(clickedPoint,Point(2,2),Point(8,-1)) == 1:
            win.close()
            addRest()
            break

        if checkButtonClick(clickedPoint,Point(6.5,-8),Point(9,-10)) == 1:
            win.close()
            break

        if checkButtonClick(clickedPoint,Point(-9,-8),Point(-6.5,-10)) == 1:
            win.close()
            main()
            break

        

        clickedPoint=win.checkMouse()


#it will draw graph and functioning for user to add Restaurant
#it will execute only when being called in noPage() or being called in the main()[which is in the menu]
def addRest():

    #draw window
    win=setUpWindow()

    #draw lable

    titleLable=Text(Point(0,9),"Please enter details for your new restaurant")
    titleLable.setSize(20)
    titleLable.draw(win)

    quitButton=Rectangle(Point(6.5,-8),Point(9,-10))
    quitButtonLable=Text(Point(7.7,-9),"QUIT")
    quitButton.draw(win)
    quitButtonLable.draw(win)

    menuButton=Rectangle(Point(-6.5,-8),Point(-9,-10))
    menuButtonLable=Text(Point(-7.7,-9),"Menu")
    menuButton.draw(win)
    menuButtonLable.draw(win)

    
    #setting i equals to 0 for calculation in for loop
    #setting myBoxes as empty list for user input
    i=0
    myBoxes = []

    #this for loop draws 5 entry boxes and append user input in myBoxes
    for i in range(5):
        detailBox=Entry(Point(-3,-6+(i+1)),9)
        detailBox.setSize(20)
        detailBox.draw(win)
        myBoxes.append(detailBox)

    

    #draw lables for each entry box and a submit button  
    lable5=Text(Point(-8,-1),"Price:")
    lable4=Text(Point(-8,-2),"Contact:")
    lable3=Text(Point(-8,-3),"Address:")
    lable2=Text(Point(-8,-4),"Flavor:")
    lable1=Text(Point(-8,-5),"Name:")

    lable1.draw(win)
    lable2.draw(win)
    lable3.draw(win)
    lable4.draw(win)
    lable5.draw(win)
        
        
    
    subButton=Rectangle(Point(3,-0.5),Point(8,-5.5))
    subButtonLable=Text(Point(5.5,-3),"submit")
    subButton.draw(win)
    subButtonLable.draw(win)
    

    #using while loop to recognize it user's click is in specific area or not
    #if True, it will closed the window first and then execute the specific function
    #if not, it will keep collecting user clicks and recognize its position(coordinates)
    clickedPoint=win.getMouse()
    while True:
        if checkButtonClick(clickedPoint,Point(3,-0.5),Point(8,-5.5)) == 1:
            d=myBoxes[4].getText()
            c=myBoxes[3].getText()
            #for e, i set restaurant location only for local and not local
            #so if user input "local" for location, the restaurant will be "local"
            e= "True" if myBoxes[2].getText().lower() == "local" else "False"
            b=myBoxes[1].getText()
            a=myBoxes[0].getText()

            #2 if statement is placed here in case of some bad input for contact and price(those should be both int)
            if not c.isdigit():
                badInput()
                clickedPoint=win.checkMouse()
                continue
            if not d.isdigit():
                badInput()
                clickedPoint=win.checkMouse()
                continue
            rList.addrest(a,b,c,d,e)
            break

        if checkButtonClick(clickedPoint,Point(6.5,-8),Point(9,-10)) == 1:
            win.close()
            break

        if checkButtonClick(clickedPoint,Point(-9,-8),Point(-6.5,-10)) == 1:
            win.close()
            main()
            break

        clickedPoint=win.checkMouse()
    win.close()
    #main()
    

#this function will pop up a window for bad input, which is used in line 446 and line 450
#it give user hints of what good input should be, the window will close after user click
def badInput():

    win=GraphWin("ERROR",300,200)

    win.setBackground("white")

    win.setCoords(-10,-10,10,10)

    askingLable=Text(Point(0,0),"Error Input\nPlease type Numbers")
    askingLable.setSize(20)
    askingLable.draw(win)

    win.getMouse()
    win.close()





#it will randomly pick a restaurant for user after clicking "any recommed"
#and it will display different lable for user according to different system time
def recommendClicked():
    #draw window
    win=setUpWindow()

    #Get system time
    timeList=time.localtime(time.time())

    #Get hours in a day and use if statement to recognize which lable should display to user
    if timeList[3] >= 11 and timeList[3] <= 15:
        titleLable=Text(Point(0,9),"Here is the recommendation for your Lunch\n Have a good day !")
        titleLable.setSize(20)
        titleLable.draw(win)

    elif timeList[3] >=17 and timeList[3] <= 21:
        titleLable=Text(Point(0,9),"Here is the recommendation for your Dinner\n Have a good night !")
        titleLable.setSize(20)
        titleLable.draw(win)

    else:
        titleLable=Text(Point(0,9),"Here is the recommend restaurant for you !")
        titleLable.setSize(20)
        titleLable.draw(win)
        
        
    

    
    #give and draw information from randomly picked database and with formating, it will close window after user clicks
    #i is an index derived randomly from line 62-64
    #as an index, it will give position for each lists(for example:name,flavor,contact,price)
    i = rList.randomRest()
    string = ""
    string += "Name: " + rList.name[i]
    string += " Flavor: " + rList.flavor[i]
    string += " Contact: " + str(rList.contact[i])
    string += "\nPrice:" + str(rList.price[i])
    string += " Address: "
    string += "Local" if rList.address[i] == "True" else "Not Local"
    string += "\n"

    lable=Text(Point(0,0),"")

    lable.setText(string)

    lable.draw(win)

    win.getMouse()

    win.close()

    
def main():

    #open file
    file=open("restaurant.txt","r")
    infile=file.readlines()
    for line in infile:
        newline = line.rstrip().split()
        rList.add(newline[0], newline[1], int(newline[2]), int(newline[3]), newline[4])
    file.close()
    #create a graphics window
    win=setUpWindow()

    #Draw two lines of words and three choices boxes
    titleLable(win)
    #Draw three choices boxes with words
    fourChoices(win)

    
    
    #using while loop to determine whether user clicks on specific area
    #if yes,then fist close present window and call specific function
    #if no, then keep collecting user clicks
    clickedPoint=win.getMouse()
    while True:

        if checkButtonClick(clickedPoint,Point(-8,6.5),Point(-2,0)) == 1:
            win.close()
            searchClicked()
            break
            

        if checkButtonClick(clickedPoint,Point(2,6.5),Point(8,0)) == 1:
            win.close()
            addRest()
            break

        if checkButtonClick(clickedPoint,Point(-3,-2),Point(3,-8)) == 1:
            win.close()
            recommendClicked()
            break

        if checkButtonClick(clickedPoint,Point(6.5,-8),Point(9,-10)) == 1:
            win.close()
            break

        clickedPoint=win.checkMouse()
    

        


main()
    

    

    
    


    





