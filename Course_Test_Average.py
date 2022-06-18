def toFixed(value, digits):
    return "%.*f" % (digits, value)

testAverage = 0.0
count = 0
totalScore = 0.0

# Main Column Heading
print("===================================================================")
print("CLASS TEST SCORE INFORMATION")
print("===================================================================")
print("STUDENT NAME    TEST SCORE")
print("===================================================================")

# Initialize lcv "answer"
print("Do you wish to enter a student's name and test score? [type 'y' or 'Y' otherwise enter 'no']")
answer = input()

# Display a blank line
print(" ")
while answer == "y" or answer == "Y":
    
    # Input Operations
    print("Enter the Student's name")
    studentName = input()
    print("What is the student's test score?")
    testScore = float(input())
    
    # keep a running total of grades for each student
    totalScore = totalScore + testScore
    
    # count or tally the number of students / grades
    count = count + 1
    
    # output each student name and their grade as a column
    print(studentName + " " + str(testScore))
    
    # update lcv answer
    print("Do you wish to enter a student's name and test score? [type 'y' or 'Y' otherwise enter 'no']")
    answer = input()
    print(" ")
    
    # end while loop
# calculate the total grades for the class
testAverage = totalScore / count

# Output operations
print("===================================================================")

# Displays the total grade for the class
print("TOTAL TEST SCORES =" + toFixed(totalScore,2))
print("===================================================================")

# Displays the average grade for the class
print("THE CLASS AVERAGE = " + toFixed(testAverage,2) + "%")
print("===================================================================")

# IF statement to determine overall status of class grade
if testAverage >= 90 and testAverage <= 100:
    print("EXCELLENT CLASS AVERAGE")
else:
    if testAverage >= 80 and testAverage <= 89.99:
        print("GOOD CLASS AVERAGE")
    else:
        if testAverage >= 70 and testAverage <= 79.99:
            print("SATISFACTORY CLASS AVERAGE")
        else:
            if testAverage <= 60:
                print("UNSATISFACTORY CLASS AVERAGE")
print("===================================================================")
print("THIS PROGRAM IS COMPLETE - EDITED BY JESSICA RYAN")
print("===================================================================")

# END PROGRAM
