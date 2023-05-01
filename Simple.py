def caesar_cipher(message, shift):
    encoded_message = ""
    for char in message:
        if char.isalpha():  # Process only alphabetic characters
            if char.isupper():
                encoded_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encoded_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encoded_message += encoded_char
        else:
            encoded_message += char
    return encoded_message

shift = int(input("Enter the shift amount: "))
message = input("Enter the message: ")
encoded_message = caesar_cipher(message, shift)
print("Encoded message:", encoded_message)