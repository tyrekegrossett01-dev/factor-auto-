from data_store import machines, MACHINE_STATUSES
from helpers import (get_text, get_positive_int, get_non_negative_number,
                     choose_from, generate_id, get_existing_id)


def add_machine():
    """Add a new machine to the machines dictionary with status AVAILABLE."""
    print("--- Add Machine ---")
    name = get_text("Machine name: ")
    machine_type = get_text("Machine type: ")
    capacity = get_positive_int("Capacity: ")
    cost_per_hour = get_non_negative_number("Cost per hour: ")

    machine_id = generate_id("M", machines)
    machines[machine_id] = {
        "name": name,
        "type": machine_type,
        "capacity": capacity,
        "cost_per_hour": cost_per_hour,
        "hours": 0,
        "status": "AVAILABLE"
    }
    print("Machine added with ID", machine_id)


def update_machine_status():
    """Change the status of an existing machine."""
    print("--- Update Machine Status ---")
    machine_id = get_existing_id("Machine ID", machines, "Machine")
    if machine_id is None:
        return

    current = machines[machine_id]["status"]
    print("Current status:", current)

    if current == "IN PRODUCTION":
        print("Cannot change a machine that is IN PRODUCTION. "
              "Complete the order first.")
        return

    new_status = choose_from("Choose the new status: ", MACHINE_STATUSES)

    if new_status == "IN PRODUCTION":
        print("IN PRODUCTION is set automatically when a production order starts.")
        return

    machines[machine_id]["status"] = new_status
    print("Status updated to", new_status)


def machine_report():
    """Show all machines and the total number of machines."""
    print("--- Machine Report ---")
    if len(machines) == 0:
        print("No machines recorded yet.")
        return

    for machine_id, m in machines.items():
        print(machine_id, "|", m["name"], "|", m["type"],
              "| capacity", m["capacity"],
              "| cost/hr", m["cost_per_hour"],
              "|", m["hours"], "hours |", m["status"])
    print("Total machines:", len(machines))


def machine_status_report():
    """Show machines grouped by status with a total for each group."""
    print("--- Machines by Status ---")
    if len(machines) == 0:
        print("No machines recorded yet.")
        return

    for status in MACHINE_STATUSES:
        group = []
        for machine_id, m in machines.items():
            if m["status"] == status:
                group.append(machine_id)

        print(status, "-", len(group), "machine(s)")
        for machine_id in group:
            print("   ", machine_id, machines[machine_id]["name"])


def machines_menu():
    """Submenu for main-menu option 2: add and view machines."""
    while True:
        print()
        print("--- MACHINES ---")
        print("1. Add machine")
        print("2. View machines")
        print("3. Back to main menu")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_machine()
        elif choice == "2":
            machine_report()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")


def machine_status_menu():
    """Submenu for main-menu option 5: update and view machine status."""
    while True:
        print()
        print("--- MACHINE STATUS ---")
        print("1. Update machine status")
        print("2. Show machines by status")
        print("3. Back to main menu")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            update_machine_status()
        elif choice == "2":
            machine_status_report()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")