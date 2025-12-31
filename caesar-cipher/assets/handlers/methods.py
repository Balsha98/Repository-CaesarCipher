from ..data.alphabet import letters

def process(option, message, shift):
    result = []

    for letter in message:
        # Guard clause.
        if letter == " ":
            result.append(letter)

            continue

        index = letters.index(letter)

        if option == "encode":
            if index + shift >= len(letters):
                result.append(letters[(index + shift) % len(letters)])
            else:
                result.append(letters[index + shift])
        elif option == "decode":
            if index - shift < 0 and (index - shift) * -1 > len(letters):
                modulo = ((index - shift) * -1) % len(letters)
                result.append(letters[modulo * -1])
            else:
                result.append(letters[index - shift])

    return "".join(result)