# Factory Automation Management 
# Welcome to SmartTech Manufacturing Ltd


#STEP 1: LOGIN FUNCTION
def login():
    correct_username = "admin"
    correct_password = "Factory123!"

    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == correct_username and password == correct_password:
            print("Login successful!")
            return True

        attempts += 1
        print("Incorrect username or password.")

        remaining_attempts = max_attempts - attempts

        if remaining_attempts > 0:
            print("Attempts remaining:", remaining)
            
    print("Maximum login attempts reached.")
    return False


#STEP 2: DAISPLAY THE MENU
def display_menu():
    print("\nFACTORY AUTOMATION MANAGEMENT SYSTEM")
    print("1. Start Production Order")
    print("2. Add Machine(s)")
    print("3. Add/Update Product")
    print("4. Add Operator/Technician")
    print("5. Update Machine Status")
    print("6. Record Maintenance")
    print("7. Print Report")
    print("8. Exit")

    #STEP 3: PROCESS MENU CHOICES
    def main_menu():
        while True:
            display_menu()

            choice = input("Enter your choice (1-8):").strip()

            if choice == "1":
                print("Start Production Order selected.")

            elif choice == "2":
                print("Add Machine selected.")

            elif choice == "3":
                print("Add/Update Product selected.")

            elif choice == "4":
                print("Add Operator/Technician selected.")

            elif choice == "5":
                print("Update Machine Status selected.")

            elif choice == "6":
                print("Record Maintenance selected.")

            elif choice == "7":
                print("Print Report selected.")

            elif choice == "8":
                print("Exiting the system. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter 1-8.")



# STEP 4: START THE PROGRAM
def main():
    print("Welcome to SmartTech Manufacturing Ltd.")

    if login():
        def main_menu():
            ...

        main_menu()

    else:
        print("Access denied>")



# STEP 5: RUN THE PROGRAM
if __name__ == "__main__":
    main() 
