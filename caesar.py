def caesar_encrypt(text, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    secret_text = ""
    
    text = text.lower()
    
    for letter in text:
        if letter in alphabet:
            position = alphabet.find(letter)
            new_letter = alphabet[position + shift]
            secret_text = secret_text + new_letter
        else:
            secret_text = secret_text + letter
            
    return secret_text


def caesar_decrypt(text, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    normal_text = ""
    
    text = text.lower()
    
    for letter in text:
        if letter in alphabet:
            position = alphabet.find(letter)

            new_letter = alphabet[position - shift] 
            normal_text = normal_text + new_letter
        else:
            normal_text = normal_text + letter
            
    return normal_text

message = "Network Security"
shift_amount = 3

encrypted_message = caesar_encrypt(message, shift_amount)
print("Encrypted:", encrypted_message)

decrypted_message = caesar_decrypt(encrypted_message, shift_amount)
print("Decrypted:", decrypted_message)