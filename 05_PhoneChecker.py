#Application to get basic information of a phone number

import phonenumbers
from phonenumbers import geocoder, timezone, carrier

phone = input("Enter the phone in the following format '+5514991554141': ")

phone_number = phonenumbers.parse(phone)
time_zone = timezone.time_zones_for_number(phone_number)
carrier = carrier.name_for_number(phone_number, 'pt')
region = geocoder.description_for_number(phone_number, 'pt')

print(region)
print(time_zone)
print(carrier)
print(geocoder.description_for_number(phone_number, 'pt'))