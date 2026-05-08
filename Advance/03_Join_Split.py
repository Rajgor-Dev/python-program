name = input("Enter your full name: ")
# Split the name into first and last name
first_name, last_name = name.split()
print("First Name:", first_name)
print("Last Name:", last_name)

# Join the first and last name back together
full_name = " ".join([first_name, last_name])
print("Full Name:", full_name)