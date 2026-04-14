try:
    open("message.txt", "x")
    print("File created Successfully!")
    file.close()
except:
    print("Error: File Already Exists.")
    
    while True:
        print("\n ===== File Messaging Menu =====")
        print("1.Send Message")
        print("2.View All Message")
        print("3.Exit")
        
        choice = input("Enter your choice (1/2/3).")
        if choice == "1":
            try:
                file = open("message.txt", "a")
                message = input("Enter your message:")
                file.write(message+"\n")
                file.close()
                print("Your Message Successfully Saved!")
            except:
                 print("Error writing to file.")
    
    
        elif choice == "2":
            try:
                file = open("message.txt", "r")
                print("\n === Messages ===")
                content = file.read()
                print(content)
                file.close()
            except:
                print("Error reading the file.")
                
        elif choice == "3":
            print("Exiting the program...")
            break
    else:
        print("Invalid choice. Try again!")