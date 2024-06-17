import cv2 as cv
import numpy as np

img =cv.imread('C:\\C++ MUDIT\\TASKS\\tc2-1.png',0)
img=img[30:770,30:570]
flipped=False

def flippedCheck(row_number):
# In this function I have passsed a row to chek postion of diamond(for number) if it is on right side(i.e >300 coloumns) then image is flipped
    global flipped
    for column in range(img.shape[1]):
        if img[row_number][column]!=255 and column>300:
            flipped=True

   
def rowCheck(row_number):
# THIS FUNCTION BASICALLY RETURN WHETHER A COMPLETE ROW IS WHITE OR NOT  
# IT RETURN FALSE AS SOON AS 1 NON-WHITE PIXEL IS FOUND SO HELPS TO DETECT CORNERS 

    for each_coloumn in range(img.shape[1]):
        if img[row_number][each_coloumn]!=255:
            return False
    return True


def coloumnCheck(coloumn_number):
# THIS FUNCTION BASICALLY RETURN WHETHER A COMPLETE COLUMN IS WHITE OR NOT  
# IT RETURN FALSE AS SOON AS 1 NON-WHITE PIXEL IS FOUND SO HELPS TO DETECT CORNERS 

    for each_row in range(img.shape[0]):
        if img[each_row][coloumn_number]!=255:
            return False
    return True
   

def findNumber(img):
    row=[]
# This for loop helps to get the 2 vertical corners of each diamond i.e. A ROW
    for row_number in range(1,img.shape[0]):
        if rowCheck(row_number-1)==True and rowCheck(row_number)!=True:
            row.append(row_number)
        elif rowCheck(row_number)==True and rowCheck(row_number-1)!=True:
            row.append(row_number-1)
    temp=0
    row1=[]
    i=1
    final=0
# then in this while loop i check for largest diagonal (vertical) and store THE ONE position(1st,2nd etc) in a new list
    while i>0 and i<12:
        x=row[i]-row[i-1]
        if x>temp:
            temp=x
            row1.clear()
            row1.append(i)
            final=row[i]
        i=i+2
    number=int((row1[0]+1)/2)

    flippedCheck(final)
    if flipped:
        number=7-number

    return number


def findGroup(img):
    column=[]
# This function helps to get the 2 horizontal corners of each diamond i.e. A COLUMN
    for i in range(1,img.shape[1]):
        if coloumnCheck(i-1)==True and coloumnCheck(i)!=True:
            column.append(i)
        elif coloumnCheck(i)==True and coloumnCheck(i-1)!=True:
            column.append(i-1)
    temp=0
    column1=[]
    i=1
# then in this while loop i check for largest diagonal (HORIZONTAL) and store THE ONE position(1st,2nd etc) in a new list
    while i>0 and i<10:
        x=column[i]-column[i-1]
        if x>temp:
            temp=x
            column1.clear()
            column1.append(i)
        i=i+2
    diamond_position=int((column1[0]+1)/2)-1

    if flipped:
        diamond_position=4-diamond_position

    return diamond_position



# THIS IS THE DICTIONARY FOR NUMBER
number_dict={
    1:'Ace',
    2:'2',
    3:'3',
    4:'4',
    5:'5',
    6:'6',
}

# THIS IS THE DICTIONARY FOR GROUP
group_dict={
    1:' of Hearts',
    2:' of Clubs',
    3:' of Spades',
    4:' of diamonds',
}

print(number_dict[findNumber(img)]+group_dict[findGroup(img)])

# cv.imshow('img',img)
# cv.waitKey(0)
# cv.destroyAllWindows()