def count_letters(input_string):
    letter_count = {}

    for letter in input_string:
        if letter != '\n':
            letter_count[letter] = letter_count.get(letter, 0) + 1

    return letter_count

def main():
    input_line = input("Enter a line of text (end with '\\n'): ")
    letter_frequency = count_letters(input_line)

    print("\nLetter frequencies:")
    for letter, count in sorted(letter_frequency.items()):
        print(f"{letter}: {count}")

if __name__ == "__main__":
    main()
