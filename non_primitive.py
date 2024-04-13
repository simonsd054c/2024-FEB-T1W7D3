# Non-primitive Data Types

# List - collection of data - mutable (change) - indexed

numbers = [ 12, 32, 2, 4, 56, 78 ]
#           0   1   2  3  4   5

print(numbers)
print(numbers[4])

numbers.append(12)
print(numbers)

numbers[1] = 25
print(numbers)

numbers.pop()
print(numbers)


# Tuples - collection of data - immutable (cannot change) - indexed

days = ( "Monday", "Tuesday", "Wednesday" )
#           0           1           2

print(days)
print(days[1])

# days[2] = "Friday"     - Cannot do this

# days.append("Friday")     - Cannot do this



# Sets - collection of data - mutable (change) - not indexed - no repeated items

names = { "John", "Jane", "Mike", "Jane", "Mike", "Mike" }

print(names)

names.add("Smith")
print(names)

names.remove("John")
print(names)

names.add("Jane")
print(names)


a = { 5, 3, 1, 2, 4 } # { 1, 2, 3, 4, 5 }
b = { 5, 7, 8, 4, 6 } # { 4, 5, 6, 7, 8 }

u = a.union(b) # b.union(a)
print(u)

i = a.intersection(b) # b.intersection(a)
print(i)

dab = a.difference(b) # A - B
print(dab)

dba = b.difference(a) # B - A
print(dba)

print(2 in a)
print(10 in a)

for number in a:
    print(number)


# Dictionary - collection of data - mutable (change) - keyed - key value pair

person1 = {
    "name": "John",
    "surname": "Smith",
    "age": 32
}

print(person1)
print(person1["name"])
print(person1.get("name"))

# print(person1["phone"])
print(person1.get("phone", "No phone number provided"))

person1["address"] = "Melbourne"
print(person1)

person1["age"] = 33
print(person1)

person1.pop("surname")
print(person1)

print("Loop started here: \n")

# Loop
for key in person1:
    print(f"Key: {key}")
    print(f"Value: {person1[key]}")


person2 = {
        "name": "Person2",
        "address": "Perth",
        "phone": {
            "home": "12414",
            "mobile": "15412421"
        }
    }

persons = [
    person1, # 0
    person2, # 1
    {
        "name": "Person3",       # 2
        "address": "Hobart"
    }
]

print(persons[0])