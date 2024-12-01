#Ex.1
def display_menu():
    print("\nMenu:")
    print("1. Add a countries")
    print("2. Remove a countries")
    print("3. Search the countries for char")
    print("4. Check if a country is in the set.")
    print("5. Display all countries")
    print("6. Exit")

def add_country(countries):
    country = input("Enter a country: ")
    if country in countries:
        print(f"This '{country}' is already in set.")
    else:
        countries.add(country)
        print(f"This is {country} added to set")

    print(country, "added to the set.")

def remove_country(countries):
    country = input("Enter a country: ")
    if country in countries:
        country.remove(country)
        print(f"The '{country}' is removed from the set.")
    else:
        countries.add(country)
        print(f"This is {country} isn`t to set")

def search_country(countries):
    char = input("Enter a char: ")
    for country in countries:
        if char in country:
            print(country)
        else:
            print("This char isn`t in countries")

def check_country(countries):
    country = input("Enter a country: ")
    if country in countries:
        print(f"This '{country}' is in the set.")
        

def main():
    countries = set()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_country(countries)
        elif choice == "2":
            remove_country(countries)
        elif choice == "3":
            search_country(countries)
        elif choice == "4":
            check_country(countries)
        elif choice == "5":
            print(countries)
        elif choice == "6":
            print("Bye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()