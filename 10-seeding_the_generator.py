from faker import Faker

fake = Faker()

Faker.seed(4321)

print(fake.name())

# Seeding the generator to ensure the same data is created everytime.

# using seed_instance to create and generate seeded content.

fake.seed_instance(4321)

print(fake.name())