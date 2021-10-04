# You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?

price_per_day = 3
days_rented = [3,5,1]

total_price = sum(x * price_per_day for x in days_rented)


# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

google_pph = 400
amazon_pph = 380
facebook_pph = 350

week_pay = (google_pph * 6) + (amazon_pph * 4) + (facebook_pph * 10)


# A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.

enroll = (class_schedule != current_schedule) and not class_full


# A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.

product_offer = (item > 2 and not offer_expired) or premium_member

# Needed code
username = 'codeup'
password = 'notastrongpassword'

# Create a variable that holds a boolean value for each of the following conditions:

pw_pass = (len(password) >= 5) and (len(username) <= 20) and (password != username) and (username.strip() == username and password.strip() == password)

# the password must be at least 5 characters

len(password) >= 5

# the username must be no more than 20 characters

len(username) <= 20

# the password must not be the same as the username

password != username

# bonus neither the username or password can start or end with whitespace

username.strip() == username and password.strip() == password



