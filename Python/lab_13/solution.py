inventory = ["Notebook","Pen","Eraser","Ruler"]
print("==========================================================")
print("                INVENTORY CONTROL SYSTEM                  ")
print("==========================================================")
while True:
    x=int(input("Select an operation: \n1. View Inventory \n2.Add Item \n3.Remove Item \n4.Sort Inventory \n5.Exit \n"))
    if x==1:
        print("--- Current Inventory ---")
        for i in range(0,len(inventory)):
            print(f"{i+1}. {inventory[i]}")
    elif x==2:
        new_item = input("Enter the item you want to add: ")
        inventory.append(new_item)
        print(f"Success {new_item} added to inventory")
    elif x==3:
        remove_item = input("Enter the item you want to remove: ")
        if remove_item in inventory:
            inventory.remove(remove_item)
            print(f"Success {remove_item} is removed from inventory")
        else:
            print(f"{remove_item} not found in inventory")
    elif x==4:
        inventory.sort
        print("[SUCCESS] Inventory sorted alphabetically")
        print("YOUR UPDATED INVENTORY IS --->")
        for i in range(0,len(inventory)):
            print(f"{i+1}. {inventory[i]}")
    elif x==5:
        print("THANK YOU FOR USING OUR INVENTORY SYSTEM ---> \n BYEEEEEEEEEEEEEEEEEEEEEEEE")
        break
    else:
        print("Please enter a valid number!!!!!")
    
    
    