import phonenumbers
from phonenumbers import geocoder

phone_number1 = phonenumbers.parse("+919148398684")
#phone_number1 = phonenumbers.parse("+919108293201")
#phone_number1 = phonenumbers.parse("+919353415236")

print("\nPhone Numbers Location\n")
print(geocoder.description_for_number(phone_number1,"en"));
# print(geocoder.description_for_number(phone_number2,"en"));
# print(geocoder.description_for_number(phone_number3,"en"));
# print(geocoder.description_for_number(phone_number4,"en"));