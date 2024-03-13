from faker import Faker
from faker.providers import internet

fake = Faker()
fake.add_provider(internet)

for _ in range(10):
    print(fake.ipv4_private())
