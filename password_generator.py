import random

import string



def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True, exclude_chars=''):

    # Define character sets based on user preferences

    character_set = ''

    if use_uppercase:

        character_set += string.ascii_uppercase

    if use_lowercase:

        character_set += string.ascii_lowercase

    if use_digits:

        character_set += string.digits

    if use_special:

        character_set += string.punctuation



    # Exclude specified characters

    character_set = ''.join(c for c in character_set if c not in exclude_chars)



    # Check if the character set is empty

    if not character_set:

        raise ValueError("At least one character type must be selected.")



    # Generate a random password

    password = ''.join(random.choice(character_set) for _ in range(length))

    return password



