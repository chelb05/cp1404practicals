minimum_length = 6

def main():
    password = input(f"Enter Password of at least {minimum_length} characters: ")
    while len(password) < minimum_length:
        password = input(f"Enter Password of at least {minimum_length} characters: ")
    print('*' * len(password))

main()