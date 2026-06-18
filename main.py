import re
def check_password_strength(password):
    if  len(password)<8:
        return "Week:password must be at least 8 characters"
    if not any(char.isdigit() for char in password):
        return "Week:password must contain a digit"
    if not any(char.isupper() for char in password):
        return "Week:password must contain a upper char"
    if not any(char.islower() for char in password):
        return "Week:password must contain a lower char"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Week:password must contain a special char"
    return "Strong:password is strong"

def password_checker():
    while True:
        password = input("Enter your password: (or type'exit' to quit) ")
        if password == 'exit':
            print("Thank you for using the password checker.")
            break
        strength = check_password_strength(password)
        print(strength)

if __name__ == "__main__":
    password_checker()
