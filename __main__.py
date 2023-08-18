import datetime

def text_to_binary(text):
    binary_text = ' '.join(format(ord(char), '08b') for char in text)
    return binary_text

def binary_to_text(binary_text):
    binary_words = binary_text.split()
    text = ''.join(chr(int(binary, 2)) for binary in binary_words)
    return text

def get_current_date_formatted():
    current_date = datetime.datetime.now()
    return current_date.strftime('%m%d%y') + ".txt"

def main():
    choice = input("Enter 'encode' to encode text to binary or 'decode' to decode binary to text: ")

    if choice.lower() == 'encode':
        input_file_path = input("Enter the path to the input text file: ")
        output_file_path = get_current_date_formatted()

        with open(input_file_path, 'r') as file:
            content = file.read()

        binary_content = text_to_binary(content)

        with open(output_file_path, 'w') as file:
            file.write(binary_content)
        print("Text encoded to binary and saved to", output_file_path)

    elif choice.lower() == 'decode':
        input_file_path = input("Enter the path to the input binary file: ")
        output_file_path = "output.txt"

        with open(input_file_path, 'r') as file:
            binary_content = file.read()

        text_content = binary_to_text(binary_content)

        with open(output_file_path, 'w') as file:
            file.write(text_content)
        print("Binary decoded to text and saved to", output_file_path)

    else:
        print("Invalid choice. Please enter 'encode' or 'decode'.")

if __name__ == "__main__":
    main()
