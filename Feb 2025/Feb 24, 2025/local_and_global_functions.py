name_list = ["ronald", "sam", "paul", "brian"]


# Global function
def get_name():
    while True:
        try:
            name = input("Enter name: ").strip()
            return name
        except:
            print("Invalid entry. Try again")


def get_user_input():

    # Local function
    def get_roll_number():
        while True:
            try:
                roll_number = int(input("Enter roll number: "))
                return roll_number
            except:
                print("Invalid number. Try again.")

    def get_input_and_check_validity():
        while True:
            name = get_name()
            if name in name_list:
                while True:
                    roll_number = get_roll_number()
                    if roll_number > 0 and roll_number < 41:
                        return name, roll_number

    # name, roll_number = get_input_and_check_validity()
    # return name, roll_number

    return get_input_and_check_validity()


def main():
    name, roll = get_user_input()
    name = get_name()

    # Functionalities



main()
