#Chad Collard
#Chapter 9&10 Lab 1
#7/5/2025

print("Name Processor.\n")
name = input("Enter your name: ")



if "," in name:
    correct_form = name.split(",")
    if len (correct_form) == 2:
        last_name = correct_form[0].strip().lower()
        first_name = correct_form[1].strip().lower()
        formatted_last_name = last_name[:1].upper() + last_name[1:]
        formatted_first_name = first_name[:1].upper() + first_name[1:]
        formatted_name = f"{formatted_last_name}, {formatted_first_name}"
        print(formatted_name)
else:
    names = name.split()
    if len(names) == 2:
        first_name = names[0].strip().lower()
        last_name = names[1].strip().lower()
        formatted_first_name = first_name[:1].upper() + first_name[1:]
        formatted_last_name = last_name[:1].upper() + last_name[1:]
        formatted_name = f"{formatted_last_name}, {formatted_first_name}"
        print(formatted_name)
    
    else:
        print("Please enter both your first and last name.")
