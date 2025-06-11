import datetime as dt
import nepali_datetime as ndt
import os

def header():
    print("** Welcome to the Date Conversion Tool **")

def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def english_to_nepali(year, month, day):
    try:
        eng_date = dt.date(year, month, day)
        nep_date = ndt.date.from_datetime_date(eng_date)
        return nep_date
    except Exception as e:
        return f"Invalid English date: {e}"

def nepali_to_english(year, month, day):
    try:
        nep_date = ndt.date(year, month, day)
        eng_date = nep_date.to_datetime_date()
        return eng_date
    except Exception as e:
        return f"Invalid Nepali date: {e}"

def main():
    while True:
        clearscreen()
        header()
        print("\nDate Conversion Options:")
        print("1) English To Nepali Date Conversion")
        print("2) Nepali To English Date Conversion")
        print("3) Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            print("\nEnter the English date (Year/Month/Day):")
            try:
                y = int(input("Year: "))
                m = int(input("Month: "))
                d = int(input("Day: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                input("Press Enter to continue...")
                continue

            nep_date = english_to_nepali(y, m, d)

            if isinstance(nep_date, ndt.date):
                print(f"\nEnglish date: {y}-{m:02d}-{d:02d}")
                print(f"Nepali date: {nep_date.year}-{nep_date.month:02d}-{nep_date.day:02d}")
            else:
                print(f"\nError: {nep_date}")

        elif choice == "2":
            print("\nEnter the Nepali date (Year/Month/Day):")
            try:
                y = int(input("Year: "))
                m = int(input("Month: "))
                d = int(input("Day: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                input("Press Enter to continue...")
                continue

            eng_date = nepali_to_english(y, m, d)

            if isinstance(eng_date, dt.date):
                print(f"\nNepali date: {y}-{m:02d}-{d:02d}")
                print(f"English date: {eng_date.year}-{eng_date.month:02d}-{eng_date.day:02d}")
            else:
                print(f"\nError: {eng_date}")

        elif choice == "3":
            print("\nExiting. Good Bye!")
            break

        else:
            print("\nInvalid choice! Please enter 1, 2, or 3.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
