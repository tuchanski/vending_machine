class AdminSys:
    def __init__(self) -> None:
        pass

    def validation(self):
        print("\nTo enter in Admin mode, you must log-in.")
        password = int(input("Enter the password here: "))
        return password

    def show(self):
        print(
            "\n- Administrator Mode -\n[ 1 ] - Add products\n[ 2 ] - Remove products\n[ 3 ] - Edit products\n[ 4 ] - See products\n[ 5 ] - Edit Cash \n[ 0 ] - Back to menu")
        mode = int(input("Choose here: "))

        while mode != 1 and mode != 2 and mode != 3 and mode != 4 and mode != 5 and mode != 0:
            mode = int(input("Invalid input. Try again: "))

        else:
            return mode
