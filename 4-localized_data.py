from faker import Faker

fake = Faker(['it_IT', 'en_US', 'ja_JP'])

for _ in range(10):
    print(fake.name())

# Localization allows one to generate data depending on a particular location.