from faker import Faker
faker = Faker('ru_RU')

user_dict={
  "id": faker.random_int(min=1, max=99999999),
  "username": faker.user_name(),
  "firstName": faker.first_name(),
  "lastName":faker.last_name(),
  "email":faker.email(),
  "password":faker.password(),
  "phone":faker.phone_number()
}