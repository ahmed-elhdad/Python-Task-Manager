import string
import random
def generate_user_id(length):
    special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~" 
    all_characters = special_characters +string.ascii_letters + string.ascii_letters + string.digits + string.ascii_uppercase
    id = "".join(random.choice(all_characters) for _ in range(length))
    return id
