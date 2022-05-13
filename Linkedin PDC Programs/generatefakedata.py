'''
pip install faker
Faker is used to generate Fake Data.
'''


from faker import Faker

fake = Faker()
print(fake.name())
print(fake.first_name_female())
print(fake.user_name())
print(fake.password())
print(fake.month())
print(len(dir(fake)))