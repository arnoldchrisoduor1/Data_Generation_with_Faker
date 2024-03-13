from faker import Faker

fake = Faker()

names = [fake.unique.first_name() for i in range(10)]
assert len(set(names)) == len(names)

print(names)

for i in range(3):
    fake.unique.boolean()
    