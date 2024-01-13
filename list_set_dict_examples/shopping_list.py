

# print menu
def print_menu():
    print(" shopping list menu, choose following digit to continue: ")
    print(" 1 to add item to the shopping list")
    print(" 2 to remove item from the shopping list")
    print(" 3 to view the shopping list")
    print(" 4 to clear the shopping list")
    print(" 5 to quit")


print("Welcome to use our shopping list")

shopping_list = {}

while True:
    print(" \n ")
    print_menu()
    menu_select = input("please choose the what you want to do: ")
    # add 
    if menu_select == '1':
        item = input("please input what you want to add: ")
        item_count = shopping_list.get(item, 0 )
        item_count += 1
        shopping_list.update({item: item_count})
    # remove
    elif menu_select == '2':
        item = input("please input what you want to remove: ")
        item_count = shopping_list.get(item, 0 )
        item_count -= 1
        if item_count > 0 :
            shopping_list.update({item: item_count})
        elif item_count == 0 :
            del shopping_list[item]
        else:
            print("not found your item, invalid item to remove")
    # view the wholelist
    elif menu_select == '3':
        print("here is the content of your list:")
        for item in shopping_list.items():
            print(item)
    # clear list
    elif menu_select == '4':
        shopping_list.clear()
        print("Your shopping list cleared")
    elif menu_select == '5':
        print("Quitted")
        break
    else:
        print(" invalid choice, please try again ")

print("Thanks for using our shopping list software")