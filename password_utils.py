import string

from password_generator import generate_password



def check_password_strength(password):

    """Check the strength of the password."""

    strength = "Weak"

    if len(password) >= 12 and (any(c.isdigit() for c in password) and

                                 any(c.islower() for c in password) and

                                 any(c.isupper() for c in password) and

                                 any(c in string.punctuation for c in password)):

        strength = "Strong"

    elif len(password) >= 8:

        strength = "Moderate"

    return strength



def generate_multiple_passwords(count, length, use_uppercase, use_lowercase, use_digits, use_special, exclude_chars):

    """Generate multiple passwords."""

    return [generate_password(length, use_uppercase, use_lowercase, use_digits, use_special, exclude_chars) for _ in range(count)]



def save_passwords_to_file(passwords, filename='passwords.txt'):

    """Save generated passwords to a file."""

    with open(filename, 'w') as file:

        for password in passwords:

            file.write(password + '\n')

    print(f"Passwords saved to {filename}")



