from faker import Faker
fake = Faker()

my_word_list = [
    'danish','cheesecake','sugar',
'Lollipop','wafer','Gummies',
'sesame','Jelly','beans',
'pie','bar','Ice','oat'
]

print(fake.sentence())

print(fake.sentence(ext_word_list=my_word_list))