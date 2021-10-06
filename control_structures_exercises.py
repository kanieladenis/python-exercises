# 1 Conditional Basics

# 1A prompt the user for a day of the week, print out whether the day is Monday or not

day_of_the_week = input('Enter the day of the week:')

if day_of_the_week.lower() == 'monday':
    print('Monday')
else:
    print('Not Monday')


# 1B prompt the user for a day of the week, print out whether the day is a weekday or a weekend

day_of_the_week = input('Enter the day of the week:')

if day_of_the_week.lower() in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']:
    print('Weekday')
else:
    print('Not Weekend')
    

# 1C create variables and make up values for:
    # 1) the number of hours worked in one week
    # 2) the hourly rate
    # 3) how much the week's paycheck will be 
    # 4) write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours
    
weekly_hours_worked = int(input('Enter hours worked this week: '))
hourly_rate = int(input('Enter hourly pay rate: '))

if weekly_hours_worked > 40:
     weekly_paycheck_overtime = (weekly_hours_worked - 40) * (hourly_rate * 1.5)
     week_pay = weekly_paycheck_overtime + (hourly_rate * 40)
     print("Week's Pay: ", week_pay)
else:
    week_pay = weekly_hours_worked * hourly_rate
    print("Week's Pay: ", week_pay)


    
    
# 2 Loop Basics

# 2A While

# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.
# Your output should look like this:


i = 5
while i in range(16):
    print(i)
    i += 1
    

# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

i = 0
while i <= 100:
    print(i)
    i += 2
    
    
# Alter your loop to count backwards by 5's from 100 to -10.

i = 100
while i >+ -11:
    print(i)
    i -= 1
    
    
# Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:

i = 2
while i < 1000000:
    print(i)
    i = i ** 2
    
    
# Write a loop that uses print to create the output shown below.

i = 100
while i <= 100 and i >= 5:
    print(i)
    i -= 5
    
    
# 2B For Loops

# B1) Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

user_number = int(input('Enter Number: '))
for num in range(1,11):
    print(f' {user_number} x {num} = {num * user_number}')


# B2) Create a for loop that uses print to create the output shown below.

for num in range(1,10):
    print(str(num)*num)
    
    
# 2C break and continue

# Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.

user_number = input('Enter a number between 1 and 50: ') 

while not user_number.isdigit() or int(user_number) < 1 or int(user_number) > 50:
    user_number = input('Enter a number between 1 and 50: ')

print(f'Number to skip is: {user_number}\n\n')
for number in range(1, int(user_number) + 1):
    if number % 2 != 0:
        if number == int(user_number):
            print('Yikes! Skip this number')
            continue
        print(f'Here is an odd number: {number}')
        

# 2D) The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)

user_number = input('Enter Positive Number: ')
count = []

while user_number.isdigit() == False or int(user_number) < 1:
    user_number = input('Enter Positive Number: ')
    
for number in range(1,int(user_number) + 1):
    print(number)
    count.append(number)
print(f'this is the count: {sum(count)}') 


# 2E) Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.

user_number = input('Enter Positive Number: ')

while user_number.isdigit() == False or int(user_number) < 1:
    user_number = input('Enter Positive Number: ')
    
for number in range(int(user_number), 0, -1):
    print(number)
    
    
    
# 3 Fizzbuzz

# One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print(f'FizzBuzz')
    elif number % 3 == 0:
        print(f'Fizz')
    elif number % 5 == 0:
        print(f'Buzz')
    else:
        print(number)

    
# 4 Display a table of powers.

# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.


from tabulate import tabulate

user_number = input('Enter Integer: ')

while user_number.isdigit() == False or int(user_number) < 1:
    user_number = input('Enter Integer: ')
 
number_list = [] 
for number in range(1, int(user_number) + 1):
    num_sq = number ** 2
    num_cube = number ** 3
    num_list = [number, num_sq, num_cube]
    number_list.append(num_list)
print(tabulate(number_list, headers=['number', 'squared', 'cubed']))

# OR

user_number = input('Enter Integer: ')

while user_number.isdigit() == False or int(user_number) < 1:
    user_number = input('Enter Integer: ')
 
number_list = [] 
for number in range(1, int(user_number) + 1):
    num_sq = number ** 2
    num_cube = number ** 3
    num_list = [number, num_sq, num_cube]
    number_list.append(num_list)

print("{:<10} {:<10} {:<10}".format('number', 'squared', 'cubed'))
print("{:<10} {:<10} {:<10}".format('------', '-------', '-----'))

for element in number_list:
    number, squared, cubed = element
    print ("{:<10} {:<10} {:<10}".format(number, squared, cubed))
    
    
# 6 Convert given number grades into letter grades.

# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:
    # A : 100 - 88
    # B : 87 - 80
    # C : 79 - 67
    # D : 66 - 60
    # F : 59 - 0
# Bonus (Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).
    
next_grade = input('Would you like to enter a grade? Yes / No: ')
user_number = input('Enter numerical grade from 0 - 100: ')

while user_number.isdigit() == False or int(user_number) < 0 or int(user_number) > 100:
        user_number = input('Enter numberical grade from  - 100: ')
    

while next_grade.lower() == 'yes':
    if int(user_number) in range(88,101):
        print(f'Letter Grade: A')
        next_grade = input('Would you like to enter a new grade? Yes / No ')
        user_number = input('Enter numberical grade from 0 - 100: ')
    elif int(user_number) in range(80, 88):
        print(f'Letter Grade: B')
        next_grade = input('Would you like to enter a new grade? Yes / No ')
        user_number = input('Enter numberical grade from 0 - 100: ')
    elif int(user_number) in range(67, 80):
        print(f'Letter Grade: C')
        next_grade = input('Would you like to enter a new grade? Yes / No ')
        user_number = input('Enter numberical grade from 0 - 100: ')
    elif int(user_number) in range(60, 67):
        print(f'Letter Grade: D')
        next_grade = input('Would you like to enter a new grade? Yes / No ')
        user_number = input('Enter numberical grade from 0 - 100: ')
    else:
        print(f'Letter Grade: F')
        next_grade = input('Would you like to enter a new grade? Yes / No ')
        user_number = input('Enter numberical grade from 0 - 100: ')
        
        
# 6 Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.

books_list = [
    {'title':'one', 'author': 'john', 'genre': 'science'},
    {'title':'two', 'author': 'smith', 'genre': 'fantasy'},
    {'title':'three', 'author': 'wills', 'genre': 'fiction'},
    {'title':'four', 'author': 'john', 'genre': 'fiction'},
    {'title':'five', 'author': 'freeman', 'genre': 'history'},
    ]

for book in books_list:
    print(book)

# 6A Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.

user_genre = input('Enter Genre (history, science, fantasy, fiction): ')

while user_genre.isdigit() or user_genre not in ['history', 'science', 'fantasy', 'fiction']:
        user_genre = input('Enter Genre (history, science, fantasy, fiction): ')
        
titles_per_genre = [dict['title'] for dict in books_list if dict['genre'] == user_genre]

print(f'Titles for Genre ({user_genre}): {titles_per_genre}')




























