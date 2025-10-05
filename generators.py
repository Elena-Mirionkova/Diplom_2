import datetime
from faker import Faker

fake = Faker('ru_RU')

def generate_login():
    return fake.user_name()
    
def generate_password():
    return fake.password(8)

def generate_email():
    return fake.email()

def generate_comment():
    return fake.text(20)
