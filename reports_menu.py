from machines import machine_report, machine_status_report
# from products import product_report
# from employees import employee_report
# from production import production_report
# from maintenance import maintenance_report


def reports_menu():
    """Submenu for main-menu option 7: open one of the six reports."""
    while True:
        print()
        print("--- REPORTS ---")
        print("1. Machine report")
        print("2. Machine status report")
        print("3. Product report")
        print("4. Employee report")
        print("5. Production report")
        print("6. Maintenance report")
        print("7. Back to main menu")
        choice = input("Choose a report: ").strip()

        if choice == "1":
            machine_report()
        elif choice == "2":
            machine_status_report()
        # elif choice == "3":
        #     product_report()
        # elif choice == "4":
        #     employee_report()
        # elif choice == "5":
        #     production_report()
        # elif choice == "6":
        #     maintenance_report()
        elif choice == "7":
            break
        else:
            print("Invalid choice.")