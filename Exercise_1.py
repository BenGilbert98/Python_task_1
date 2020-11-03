first_name = input("What is your first name?    ")
middle_name = input("What is your middle name?    ")
last_name = input("What is your last name?    ")
age = input("How old are you?    ")
address = input("What is the first line of your address?    ")
postcode = input("What is your postcode?    ")
ni_number = input("What is your national insurance number?    ")
course = input("What course did you apply to?   ")
education = input("What is your most recent education?    ")
# These inputs will be assigned to their respective variables

full_name = first_name.capitalize() + ' ' + middle_name.capitalize() + ' ' + last_name.capitalize()
# making a variable of full name to make the print statement more readable

print("Hello", full_name, "!", "You are {} years old.".format(age), "You live at", address.capitalize(), ",", postcode.upper() + ".", "NI number:", ni_number.upper())
# print statement to show user information
print("Recent Education:", education.capitalize())
# prints recent education
print("Course:", course.capitalize())
# prints the course the user applied to
