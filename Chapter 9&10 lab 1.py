#Chad Collard
#Chapter 9&10 Lab 1
#7/5/2025

print("Name Processor.\n")
name = input("Enter your name: ")

if "," in name:
    print(name)
else:
    names = name.split()
    if len(names) == 2:
        first_name = names[0]
        last_name = names[1]
        formatted_name = f"{last_name.capitalize()}, {first_name.capitalize()}"
        print(formatted_name)
    elif len(names) == 2:
        first_name = name[1]
        last_name = name[0]
        correct_name = f"{last_name.capitalize()}, {first_name.capitalize()}"
        print(correct_name)

    else:
        print("Please enter both your first and last name.")
