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