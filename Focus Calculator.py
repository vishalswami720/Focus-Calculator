def wake_up_time():
    while True:
        time = input("Enter your wake-up time (AM hour): ")

        if time.isdigit():
            time = int(time)
            if 0 < time < 12:
                return time
            else:
                print("The input must be greater than 0 and less than 12.")
        else:
            print("Please enter a valid number!")

def study_hours():
    while True:
        time = input("Enter your study hours: ")

        if time.isdigit():
            time = int(time)
            if 0 < time < 12:
                return time
            else:
                print("The input must be greater than 0 and less than 12.")
        else:
            print("Please enter a valid number!")


def exercise_time():
    while True:
        time = input("Enter your exercise/sports time (hours): ")

        if time.isdigit():
            time = int(time)
            if 0 <= time <= 8:
                return time
            else:
                print("The input must be between 0 and 8 hours.")
        else:
            print("Please enter a valid number!")


def screen_time():
    while True:
        time = input("Enter your mobile screen time (hours): ")

        if time.isdigit():
            time = int(time)
            if 0 <= time <= 12:
                return time
            else:
                print("The input must be between 0 and 12 hours.")
        else:
            print("Please enter a valid number!")

def sleep_time():
    while True:
        time = input("Enter your sleep time (PM hour): ")

        if time.isdigit():
            time = int(time)
            if 0 <= time <= 12:
                return time
            else:
                print("The input must be between 0 and 12.")
        else:
            print("Please enter a valid number!")


def main():
    wake = wake_up_time()
    study = study_hours()
    exercise = exercise_time()
    screen = screen_time()
    sleep = sleep_time()

    work = (sleep + 12) - wake

    percentage = ((study + exercise) - (screen * 0.5)) / work * 100
    percentage = max(0, min(100, percentage))

    def reduce():
        if percentage < 50 :
            print("\nYour focus level is low.")

            if work < 15:
                print("- Fix your sleep schedule. Around 8 hours of sleep is recommended.")
            elif study < 5:
                print("- Increase your study time.")
                if screen >5:
                    print("- Reduce your mobile screen time.")
        else:
            print("\nYour focus level is good. Keep it up!")

    print(f"\nYour Focus Percentage: {percentage:.2f}%")

    reduce()
    
main()
