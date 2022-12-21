import os
import random
import string

from dotenv import load_dotenv

load_dotenv()

email = os.getenv('email')
password = os.getenv('password')
main_url = os.getenv('main_url')


def generate_random_name(length):
    rand_name = ''.join(random.choice('абвгдеёжзийклмнопрстуфхцчшщъыьэюя') for i in range(length))
    return rand_name


def generate_random_password(length):
    letters_and_digits = string.ascii_letters + string.digits
    rand_password = ''.join(random.choice(letters_and_digits) for i in range(length))
    return rand_password


