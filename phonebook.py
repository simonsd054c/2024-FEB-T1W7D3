from pprint import pprint

'''
[
    {
        "name": "John Smith",
        "address": "Sydney",
        "phone": {
            "home": "1241",
            "mobile": "12512345"
        }
    },
    {
        "name": "Jane Doe",
        "address": "Brisbane",
        "phone": {
            "home": "1254123",
            "mobile": "12412"
        }
    }
]
'''

phonebook = [
    {
        "name": "John Smith",
        "address": "Sydney",
        "phone": {
            "home": "1241",
            "mobile": "12512345"
        }
    },
    {
        "name": "Jane Doe",
        "address": "Brisbane",
        "phone": {
            "home": "1254123",
            "mobile": "12412"
        }
    }
]

pprint(phonebook)

name = input("Enter name: ")
address = input("Enter address: ")
home = input("Enter home: ")
mobile = input("Enter mobile: ")

# person_to_add = {
#     "name": name,
#     "address": address,
#     "phone": {
#         "home": home,
#         "mobile": mobile
#     }
# }

# phonebook.append(person_to_add)
phonebook.append(
    {
        "name": name,
        "address": address,
        "phone": {
            "home": home,
            "mobile": mobile
        }
    }
)

pprint(phonebook)

number_to_find = input("Enter a number to find: ")

def find_number(number_to_find):
    for phone_entry in phonebook:
        for number_key in phone_entry["phone"]:
            if (number_to_find == phone_entry["phone"][number_key]):
                print("Number found")
                print(phone_entry["name"])
                return
    print("Number not found")


find_number(number_to_find)