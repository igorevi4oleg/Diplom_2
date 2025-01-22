import random
import string

class Generate:
    @staticmethod
    def generate_random_string(length=8):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    @staticmethod
    def generate_mail(length=8):
        return ''.join(random.choice(string.ascii_lowercase) for i in range(length)) + '@rambler.ru'



