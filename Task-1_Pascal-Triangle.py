#Asssignment-2
#Name: Md Asif Iqbal
#Student ID: 29789109
#Task-1 : Pascal Triangle

alist = []                #alist is an empty List
def printPascal(alist,n):
    """
    printPascal prints the Pascal triangle.
    This is a recursive function.
    The base case is n = 0
    """
    #aList is a list and n is an an non-negative integer input
    if len(alist) < 1:
        #This puts the element in the aList
        alist.append(1)        
    else:
        #bList is a list that always contains the number 1 because I need 1 at start.
        blist = [1]           
        if len(alist) > 1:
            #This puts element in the middle of the row.
            for line in range(len(alist) - 1):
                #This adds the values of the previous lines.
                j = alist[line] + alist[line + 1]
                #This puts the element in the bList
                blist.append(j)              
        #I need  1 at the end so I am putting 1 at the end.
        blist.append(1)      
        alist = blist
    print(" ".join(str(x) for x in alist))

    n = n - 1
    if n > 0:
        printPascal(alist, n)   #The base case is n = 0

    else:
        return 1            #Return 1 because of recursion.



def inputCheck():
    """
    inputCheck is the function that checks if it is a
    valid input or not
    """
    #To make sure that the user is inputting integers only.
    while True:
        try:
            return int(input('Enter a integer: '))
        except:
            print("That's not a valid input!")

def input_valid_n():
    """
    input_valid_n takes input from the user and also checks whether it is
    a non-negative integer or not
    """
    n = inputCheck()
    # n is a non-negative integer
    #This asks user to input again if the input is wrong
    while n < 0:
        print("Enter a number >= 0")
        n = inputCheck()
    return n

#This calls the function input_valid_n
n = input_valid_n()
#This calls the function printPascal
printPascal(alist, n+1)
