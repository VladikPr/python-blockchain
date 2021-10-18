name = input("Please enter your name: ")
age = int(input("Enter your age: "))


def print_user_data(name, age):
    """This function prints user data"""
    print(f"Name: {name}, age: {age}")


def print_any_data(first_argument, second_argument):
    print(f"{first_argument}, {second_argument}")


def get_num_of_lived_decades(age):
    return age // 10


print_user_data(name, age)
print_any_data("John", "Doe")
print(get_num_of_lived_decades(int(age)))
