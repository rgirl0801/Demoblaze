import base64

from faker import Faker


password = base64.b64encode(b'KateFox').decode('utf-8')
POSITIVE_API_CREDS = {
    "username": "KateFox1",
    "password": password
}

NEGATIVE_API_CREDS = [{
    "username": "KateFox1",
    "password": 'password'
},
    {"username": "KateFox",
     "password": 'password'}
]

faker = Faker()
POSITIVE_LOGIN_CREDS = {"name": "KateFox1", "password": "KateFox"}
NEGATIVE_LOGIN_CREDS = [
    ("", "KateFox"),
    ("KateFox1", ""),
    ("Test", "Test")
]

POSITIVE_SIGNUP_CREDS = {"name": faker.text(5), "password": "KateFox"}

PURCHASE_DATA = {
    "name": "testKate",
    "country": "countryName",
    "city": "cityName",
    "card": "cardData",
    "month": "Month",
    "year": "validYear"
}

TEXT_ABOUT = "We believe performance needs to be validated at every stage of the software development cycle and our open source compatible, massively scalable platform makes that a reality."
