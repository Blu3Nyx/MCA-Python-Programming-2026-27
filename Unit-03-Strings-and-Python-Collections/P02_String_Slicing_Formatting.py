# Unit 3 - P02
# Program for string slicing and string formatting using student details

full_name = input("Enter full name: ")
email = input("Enter email address: ")
mobile = input("Enter mobile number: ")

# first name and last name using slicing
space = full_name.find(" ")
first_name = full_name[:space]
last_name = full_name[space + 1:]

# reverse of the name
reverse_name = full_name[::-1]

# username and domain from email
at = email.find("@")
username = email[:at]
domain = email[at + 1:]

# last four digits of mobile number
last_four = mobile[-4:]

print()
print("First name:", first_name)
print("Last name:", last_name)
print("Reversed name:", reverse_name)
print("Username:", username)
print("Domain:", domain)
print("Last four digits of mobile:", last_four)

# different formatting techniques
print()
print("---- f-string ----")
print(f"Name: {full_name}, Email: {email}, Mobile: {mobile}")

print("---- format() method ----")
print("Name: {}, Email: {}, Mobile: {}".format(full_name, email, mobile))

print("---- % formatting ----")
print("Name: %s, Email: %s, Mobile: %s" % (full_name, email, mobile))

# positive and negative indexing
print()
print("---- Indexing ----")
print("First character (index 0):", full_name[0])
print("Last character (index -1):", full_name[-1])
print("Second last character (index -2):", full_name[-2])
