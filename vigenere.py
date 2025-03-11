import helper 

def vigenere_cipher(txt_list, key_list, encrypt=True):
    vkey =  helper.get_repeating_key(txt_list, key_list) if len(txt_list) != len(key_list) else key_list
    vigenere = []
    if encrypt:
        for i in range(len(txt_list)): vigenere.append((txt_list[i] + vkey[i]) % 26)
    else: 
        for i in range(len(txt_list)): vigenere.append((txt_list[i] - vkey[i]) % 26)
    return vigenere

def vigenere_encrypt():
    user_text = helper.str_validation("Enter text to encrypt: ")
    key = helper.str_validation("Enter encryption key (lowercase only): ")
    encrypted_text = helper.convert_to_char_lower(
        vigenere_cipher(helper.char_to_num_lower(user_text), helper.char_to_num_lower(key), True)
    )

    print(f"""
=============================================================================
                           ENCRYPTION SUCCESSFUL 
=============================================================================
              
RESULTS:                            
              
Encrypted Text:     {encrypted_text}

=============================================================================

IMPORTANT NOTICE:

- The Vigenère cipher is stronger than Caesar but still vulnerable to cryptanalysis.
- Ensure the key is kept secret and is sufficiently complex.
- A longer key improves security significantly.

=============================================================================
""")


def vigenere_decrypt():
    user_text = helper.str_validation("Enter text to decrypt: ")
    key = helper.str_validation("Enter decryption key (lowercase only): ")
    decrypted_text = helper.convert_to_char_lower(
        vigenere_cipher(helper.char_to_num_lower(user_text), helper.char_to_num_lower(key), False)
    )

    print(f"""
=============================================================================
                            DECRYPTION SUCCESSFUL 
=============================================================================
              
RESULTS:              
              
Decrypted Text:     {decrypted_text}

=============================================================================

SECURITY NOTE:

- The key must match exactly for proper decryption.
- The Vigenère cipher is resistant to frequency analysis but can be broken with known-plaintext attacks.
- For better security, consider using modern encryption algorithms.

=============================================================================
""")

def print_vigenere_info():
    print("""\n=============================================================================
          \nVersion 1.0.0\n\nOrigin:

    The **Vigenère Cipher** was introduced in the 16th century by **Giovan Battista 
    Bellaso** and later attributed to **Blaise de Vigenère**, a French diplomat. 
    It improves upon the Caesar Cipher by using a keyword to apply multiple 
    shifting patterns, making it resistant to simple frequency analysis.
          
Use Case:         
          
    A private messaging app encrypts conversations using the Vigenère Cipher 
    with a unique user-defined keyword, preventing basic decryption attempts.
          
Pros:
          
    - More secure than the Caesar cipher due to its polyalphabetic nature.
    - Harder to break using frequency analysis.
          
Cons:

    - Vulnerable to repeated key attacks if the key is short.
    - Requires key management for encryption and decryption.

=============================================================================\n""")

def run():
    print("""Version 1.0.0\n\nOrigin:

    The VIGENERE ALGORITHM\n""")
    
    while True:
        choice = helper.get_menu_choice()
        
        if choice == 1:
            vigenere_encrypt()
        elif choice == 2:
            vigenere_decrypt()
        elif choice == 3: 
            print_vigenere_info()
        elif choice == 4:
            print("Returning to the Main Menu...")
            break 

