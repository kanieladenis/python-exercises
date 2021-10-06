# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

def is_two(n):
    result = n in [2,'2']
    print(result)
    return result

is_two(2)

# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(s):
    result = s.lower() in 'aeiou'
    print(result)
    return(result)

is_vowel('A')

# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

def is_constant(s):
    result = s.lower() not in 'aeiou'
    print(result)
    return result

# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

def is_word(s):
    if s.lower()[0] not in 'aeiou':
        result = s.capitalize()
        print(result)
        return result
    else:
        print('not word')

# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(tip_percent, bill_total):
    if 0 <= tip_percent/100 <= 1:
        amount_to_tip = (tip_percent/100) * bill_total
        print(amount_to_tip)
        return amount_to_tip
    else:
        print('invalid')


# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

def apply_discount(orginal_price, discount_percent):
    if (int(orginal_price) > 0) and (0 <= discount_percent <= 1):
        price_after_discount = orginal_price - (orginal_price * discount_percent)
        print(price_after_discount)
        return price_after_discount
    else:
        print('invalid')

# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

def handle_commas(s):
    if ',' in s:
        output = s.replace(',', '')
        if output.isdigit():
            print(output)
            return output
        else:
            print('input not digit')
    elif s.isdigit():
        print(s)
        return s
    else:
        print('invalid')

# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).



# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.


# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
#     - anything that is not a valid python identifier should be removed
#     - leading and trailing whitespace should be removed
#     - everything should be lowercase
#     - spaces should be replaced with underscores
#     - for example:
#         - Name will become name
#         - First Name will become first_name
#         - % Completed will become completed

        
# 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
#     - cumulative_sum([1, 1, 1]) returns [1, 2, 3]
#     - cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]
# Additional Exercise
#     - Once you've completed the above exercises, follow the directions from https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886 in order to thouroughly comment your code to explain your code.

# Bonus
    # 1. Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.
    # 2. Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
#         * col_index('A') returns 1
#         * col_index('B') returns 2
#         * col_index('AA') returns 2