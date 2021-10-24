import phonenumbers
from phonenumbers import geocoder


phone = input("Enter a phone number no formato +5511932235527:  ")

number = phonenumbers.parse(phone)  

print(geocoder.description_for_number(number, "pt"))