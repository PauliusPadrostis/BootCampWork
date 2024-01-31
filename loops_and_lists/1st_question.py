"""
Create a list and:
* allow to check one item in the list.
* Allow to add an item.
* Allow to delete an item.
* Allow to change an item.
"""


lst = ["Hello", "Evening", "city", "making", "Lame", "Opinion", "cow"]

print(
    "Welcome to list modifier. Please select an option:\n\n1. Read an item from the list.\n2. Add an item to the"
    " list\n3. Change an item in the list.\n")

option = int(input("Please select an option: \n"))

if option == 1:
    choice = int(input(f"Please select the number of the item you want to view (the list has {len(lst)} items.): "))
    print(f"Item Nr.{choice} is: {lst[choice - 1]}")
elif option == 2:
    choice = str(input("Please enter the item you wish to add to the list: "))
    lst.append(choice)
    view = str(input("Would you like to view the list with your choice added? (Y/N): "))
    if view.casefold() == "y" or "yes":
        print(lst)
else:
    choice_change = input(f"Which item would you like to change? {lst}")

    for x in range(len(lst)):

        if lst[x] == choice_change:
            change = input("What would you like to change it to? ")
            lst[x] = change
