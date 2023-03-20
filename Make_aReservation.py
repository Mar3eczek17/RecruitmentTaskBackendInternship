"""
Specification
Program should prompt user what to do.
What do you want to do:

1. Make a reservation
2. Cancel a reservation
3. Print schedule
4. Save schedule to a file
5. Exit
"""


class ReservationSystem:
    def make_reservation(self):
        pass

    def cancel_reservation(self):
        pass

    def print_schedule(self):
        pass

    def save_schedule(self):
        pass

    def run(self):
        while True:
            print("Specification:")
            action = input("1. Make a reservation\n"
                           "2. Cancel a reservation\n"
                           "3. Print schedule\n"
                           "4. Save schedule to a file\n"
                           "5. Exit\n")
            if action == "1":
                self.make_reservation()
                print()
            elif action == "2":
                self.cancel_reservation()
                print()
            elif action == "3":
                self.print_schedule()
                print()
            elif action == "4":
                self.print_schedule()
                print()
            elif action == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
                print()


reservation_system = ReservationSystem()
reservation_system.run()
