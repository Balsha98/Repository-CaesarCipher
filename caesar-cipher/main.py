from assets.handlers.methods import process

while True:
    option = input("\nType 'encode' or 'decode' to continue: ")

    if option != 'encode' and option != 'decode':
        print("Invalid Option - Try again...\n")

        continue

    while True:
        message = input("\nType your message: ")

        if message == "":
            print("Empty Message - Try again...\n")

            continue

        break

    while True:
        shift = int(input("\nType the shift number: "))

        if shift == 0:
            print("Invalid Shift - Try again...\n")

            continue

        break

    result = process(option, message, shift)
    print(f"\nHere is the {option}d result: {result}\n")

    again = input("Do you want to continue? (y/n): ")

    if again == "y":
        continue
    else:
        break

print("\nThe End - See you next time...")