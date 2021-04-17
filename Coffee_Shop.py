
print("1.Coffee\n2.Tea")
a={"Coffee":"1.Coffee_small_size\n2.Coffee_medium_size\n3.Coffee_large_size", "Tea":"1.Tea_small_size\n2.Tea_medium_size\n3.Tea_large_size"}
for i in a.values():
    user=int(input("What do you want to drink? :"))
    if user == 1:
        user=int(input("Press 1 for Hot Coffee\nPress 2 for Cold Coffee\nChosse your variety :"))
        if user == 1 or 2:
            print(i)
            user=int(input("Enter your size :"))
            print("You paid 40 rs ") if user ==1 else print("You paid 60 rs ") if user==2 else print("You paid 80 rs ")
        break
    else:
        user=int(input("Press 1 for Lemmon Tea\nPress 2 for Milk Tea\nEnter your choice :"))
        if user == 1 or 2:
            print(a["Tea"])
            user=int(input("Enter your size :"))
            print("You paid 20 rs ") if user ==1 else print("You paid 30 rs ") if user==2 else print("You paid 40 rs ")
        break