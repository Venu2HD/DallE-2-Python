from json import load

def getsettings():
    while True:
        try:
            with open("settings.json") as settings_opened:
                settings = load(settings_opened)
        except FileNotFoundError:
            open("setttings.json", "w").close()
            input("ERROR: Settings file not found.\nPress enter to exit...")
            exit()
        else:
            break
    return settings