"""
1. Make a reservation:
User should be prompted to give his full name, and date of a reservation
this should fail if:

User has more than 2 reservations already this week
Court is already reserved for the time user specified
The date user gives is less than one hour from now

If the court is reserved the system should suggest the user to make a reservation on the closest possible time.
For example:

$ Make a reservation

What's your Name?

$ Jeff Spicoli

When would you like to book? {DD.MM.YYYY HH:MM}

$ 1.04.2023 15:00

The time you chose is unavailable, would you like to make a reservation for 16:00 instead? (yes/no)
# If the user chooses No, take them back to the previous step.

$ Yes

How long would you like to book court?  # Display possible periods in 30 minute intervals up to 90 minutes.
If the court is reserved from 17:00 you should only show the first 2 options.
1) 30 Minutes
2) 60 Minutes
3) 90 Minutes
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


ReservationSystem().run()
