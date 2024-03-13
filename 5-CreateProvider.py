from faker import Faker

fake = Faker()

# First we import a similar Provider or use the default one.
from faker.providers import BaseProvider

# Create new provider class.
class MyProvider(BaseProvider):
    def foo(self) -> str:
        return 'bar'

# Create add new provider to faker instance.
fake.add_provider(MyProvider)

# Using the prvider.
print(fake.foo())