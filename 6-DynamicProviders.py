from faker import Faker

from faker.providers import DynamicProvider

medical_professions_provider = DynamicProvider(
    provider_name = "medical_profession",
    elements=["dr.", "Doctor", "Nurse", "Surgeon", "clerk"],
)

fake = Faker()

# then add ne provider to fake instance
fake.add_provider(medical_professions_provider)

#now we can use:
print(fake.medical_profession())