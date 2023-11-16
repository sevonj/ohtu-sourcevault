class AppUI:
    def __init__(self):
        self.value = 1

    def run_app(self):
        while True:
            command = input("1 : create new\n2 : read sources\n3 : create bibtext\n4 : stop\n")

            """
            match command:
                case 1:
                    title = input("insert title")
                    ...
                    root.create_new(title,...)

            """

            if command == "4":
                break

if __name__ == "__main__":
    ui = AppUI()
    ui.run_app()

