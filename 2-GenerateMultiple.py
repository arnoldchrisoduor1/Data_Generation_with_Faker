from faker import Faker

fake = Faker()

for _ in range(10):

    sim_person={"name":fake.name(),
         "location":fake.address(),
         "proffesion":fake.job(),
         "comp_description":fake.user_agent()
         }
    
    print(sim_person)