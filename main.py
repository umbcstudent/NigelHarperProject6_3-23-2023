# Create an empty dictionary to store the students and their grades
students = {}

# Shows the user what options they have
def displayMenu():

  # This option will involve you adding a student and a collection for their grades to a dictionary!
  print("1. Add a Student")

  # This option will involve you removing a pair from a dictionary!
  print("2. Remove a Student")

   # You'll also need to use a pre-written function that ensures the user is entering a valid grade (a decimal number)
  print("3. Add Quiz Grade for Student")

  # This option will require you to use a loop to list all of the grades for an INDIVIDUAL student!
  print("4. List a Student's Quiz Grades")

  # This option will have you write a function that takes in a student's grade as a number and return the letter grade equivalent!
  print("5. Get Student's Letter Grade")
#Stop the program 
  print("6. Quit")
  
#Function to get a float number for the student
def getNumberGradeFromUser():

  val = None

  while(val == None):
    try:
      test = float(input("Enter a Grade: "))
      val = test
    except:
      val = None
  
  return val

# Function to add a student to the dictionary
def add_student():
    name = input("Enter student name: ")
    students[name] = []

# Function to remove a student from the dictionary
def remove_student():
    name = input("Enter student name: ")
    if name in students:
        del students[name]
        print("Student removed.")
    else:
        print(f"{name} not in the dictionary")

# Function to add a quiz grade for a student
def add_quiz_grade():
    name = input("Enter student name: ")
    if name in students:
        grade = getNumberGradeFromUser()
        students[name].append(grade)
    else:
        print("Student not found")

# Function to list a student's quiz grades
def list_quiz_grades():
    name = input("Enter student name: ")
    if name in students:
        grades = students[name]
        print(f"{name}'s Quiz Grades: {grades}")
    else:
        print("Student not found")

# Function to get a student's letter grade
def get_letter_grade():
    name = input("Enter student name: ")
    if name in students:
        grades = students[name]
        average = sum(grades) / len(grades)
        letter_grade = calculate_letter_grade(average)
        print(f"{name}'s current grade is a {letter_grade}")
    else:
        print("Student not found")

# Function to calculate letter grade
def calculate_letter_grade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"

# Application Loop
while(True):

  # Prompt the user to select an option
  print()
  displayMenu()
  selection = input("Enter selection: ")

  # Add a Student
  if selection == "1":
    add_student()
    print("Student added.")

  # Remove a Student
  elif selection == "2":
    remove_student()
    
  
  # Add Quiz Grade for Student
  elif selection == "3":
    add_quiz_grade()
    print("Quiz grade added.")
  
  # List a Student's Grades
  elif selection == "4":
    list_quiz_grades()
  
  #List a Student's Letter Grades
  elif selection == "5":
    get_letter_grade()
  
  #Quit the program 
  elif selection == "6":
    break
    
  
    

    
    
      
   

    
   
    
    



