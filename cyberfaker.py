from faker import Faker

faker = Faker()
name = faker.name()
age = faker.address()
email = faker.email()
country = faker.country()
city = faker.city()

print( " Faker values " )
print ( name , " Age : ", age, " eMail :", email , "country :", country , " City :", city) 