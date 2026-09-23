def vigenere(message, key, mode="encrypt"):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    message = message.lower()
    key = key.lower()
    
    result_text = ""
    key_index = 0

    for letter in message:
        if letter in alphabet:
            # STEP 1: Get current key letter (repeats key if message is longer)
            current_key_letter = key[key_index % len(key)]

            # STEP 2: Turn both letters into numbers (a=0, b=1, c=2...)
            message_number = alphabet.find(letter)
            key_number = alphabet.find(current_key_letter)

            # STEP 3: Add for ENCRYPT, Subtract for DECRYPT
            if mode == "encrypt":
                new_number = (message_number + key_number) % 26
            else:
                new_number = (message_number - key_number) % 26

            # STEP 4: Turn the new number back into a letter
            result_text += alphabet[new_number]

            # Move to the next key letter
            key_index += 1
        else:
            # Leave spaces and punctuation unchanged
            result_text += letter

    return result_text


# --- TRY IT OUT ---
secret_message = vigenere("dog", "bad", mode="encrypt")
print("Encrypted:", secret_message)  # Output: eoj

original_message = vigenere("eoj", "bad", mode="decrypt")
print("Decrypted:", original_message)  # Output: dog