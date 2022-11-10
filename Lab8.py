#Lintong Wu
#040994127
#302

#Prompts the user for the number of Tests
#Note that this function will include call(s) to the input function
#Keep prompting until the number is an integer. 
#Returns the number of Tests
def getNumberOfTests():
    while True:
        try:
            tests = int(input("Please enter the number of tests: "))
        except ValueError:
            print("Please enter an integer.")
            continue
        else:
            break
        return tests

#Prompts the user for the weigth of Assignments
#Note that this function will include call(s) to the input function
#Keep prompting until the number is a float >= 0 and <= 1
#Returns the weight of assignments
def getWeightOfAssignments():
    while True:
        try:
            wAssign = float(input("Please enter the weigth of Assignments: "))
        except ValueError:
            print("Please enter a float number between 0 and 1.")
            return getWeightOfAssignments()
    
        if wAssign < 0 or wAssign > 1:
                print("Please enter a float number between 0 and 1.")
                return getWeightOfAssignments()
        else:
            return wAssign

#Prompts the user for the weigth of Midterms
#Note that this function will include call(s) to the input function
#Keep prompting until the number is a float >= 0 and <= 1
#Returns the weight of midterms
def getWeightOfMidTerms():
    while True:
        try:
            wMidTerm = float(input("Please enter the weigth of midterms: "))
        except ValueError:
            print("Please enter a float number between 0 and 1.")
            return getWeightOfMidTerms()
   
        if wMidTerm < 0 or wMidTerm > 1:
                print("Please enter a float number between 0 and 1.")
                return getWeightOfMidTerms()
        else:
            return wMidTerm

#Prompts the user for the weigth of the final
#Note that this function will include call(s) to the input function
#Keep prompting until the number is a float >= 0 and <= 1
#Returns the weight of final
def getWeightOfFinal():
    while True:
        try:
            wFinal = float(input("Please enter the weigth of final: "))
        except ValueError:
            print("Please enter a float number between 0 and 1.")
            return getWeightOfFinal()
    
        if wFinal < 0 or wFinal > 1:
            print("Please enter a float number between 0 and 1.")
            return getWeightOfFinal()
        else:
            return wFinal

#returns True if the sum of the 3 arguments is 1, False otherwise
#Assign the default values 0.4 0.35 0.25 to wAssign, wMidtern and wFinal respectively
def checkWeights(wAssign,wMidTerm,wFinal):
    sumOfThree = wAssign + wMidTerm + wFinal
    
    if sumOfThree == 1:
        return True
    else:
        return False
    
checkWeights(0.4, 0.35, 0.25)

#calculate the numeric grade as specified in the course outline
def calculateNumericGrade(AvgAssignments,AvgTests,final,wAssign,wMidTerm,wFinal):
        return AvgAssignments*wAssign+AvgTests*wMidTerm+final*wFinal;

#convert the numeric grade to a letter according to the conversion table 
#in the course outline
def calculateLetterGrade(numericGrade):
    if numericGrade>=90 and numericGrade<=100:
        return 'A+'
    elif numericGrade>=85 and numericGrade<90:
        return 'A'
    elif numericGrade>=80 and numericGrade<85:
        return 'A-'
    elif numericGrade>=77 and numericGrade<80:
        return 'B+'
    elif numericGrade>=73 and numericGrade<77:
        return 'B'
    elif numericGrade>=70 and numericGrade<73:
        return 'B-'
    elif numericGrade>=67 and numericGrade<70:
        return 'C+'
    elif numericGrade>=63 and numericGrade<67:
        return 'C'
    elif numericGrade>=60 and numericGrade<63:
        return 'C-'
    elif numericGrade>=57 and numericGrade<60:
        return 'D+'
    elif numericGrade>=53 and numericGrade<56:
        return 'D'
    elif numericGrade>=50 and numericGrade<53:
        return 'D-'
    else:
        return 'F'

#Get the weight value of the assignments (call the appropriate function)
#Get the weight value of tests (call the appropriate function)
#Get the weight value of the final (call the appropriate function)
#Check the sum of weight values is 1 (call the appropriate function)
#Repeat the last four lines if not equal to 1
while 1:
    getWeightOfAssignments()
    getWeightOfMidTerms()
    getWeightOfFinal()
    if wAssign + wMidTerm + wFinal == 1: 
        break 
#Get the average grade obtained on the assignments
#Validate the input as a float between 0 and 100
while 1:
    AvgAssignments = float(input('Please enter the average grade of assignments: '))
    if AvgAssignments >= 0 and AvgAssignments <= 100:
        break 
#Get the number of tests (call the appropriate function)
#Prompt the user for each test grades and accumulate the value
#Validate the input as a float between 0 and 100
#Calculate the average test grade.
getNumberOfTests()
for i in range(n):
    while 1:
        test = float(input('Please enter test marks: '))
        if test >= 0 and test <= 100:
            i += k 
            break 
AvgTests = i/n 

#Prompt and get the final grade
#Validate the input as a float between 0 and 100
while 1:
    getWeightOfFinal()
    if final >= 0 and final <= 100:
        break 
#Calculate and display the final numeric grade (call the appropriate function)
calculateNumericGrade(AvgAssignments,AvgTests,final,wAssign,wMidTerm,wFinal)
#Calculate and display the final alphabetical grade (call the appropriate function)
calculateLetterGrade(numericGrade)

