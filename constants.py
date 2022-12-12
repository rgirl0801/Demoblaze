from faker import Faker

faker = Faker()
POSITIVE_LOGIN_CREDS = {
    "name": "KateFox1",
    "password": "KateFox"
}

POSITIVE_SIGNUP_CREDS = {
    "name": faker.text(5),
    "password": "KateFox"
}

# POSITIVE_CREDENTIALS = {
#     "name": "testKate",
#     "country": "countryName",
#     "city": "cityName",
#     "card": "cardData",
#     "month": "Month",
#     "year": "validYear"
# }

# NEGATIVE_CREDENTIALS = [("", "!QAZ2wsx"), ("qa_test@test.ru", ""), ("qa_test", "!QAZ2wsx"),
#     ("test@test.ru", "1QAZ2wsx")]
