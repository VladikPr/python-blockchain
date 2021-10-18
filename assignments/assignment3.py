# Create a list of 'person' dictionaries with a name, age and list of hobbies for each person. Fill in any data you want.
users = [
    {
        'name': 'Markus',
        'age': 48,
        'hobbies': ['sport', 'reading', 'diving']
    },
    {
        'name': 'Anna',
        'age': 35,
        'hobbies': ['yoga', 'dancing', 'languages']

    },
    {
        'name': 'John',
        'age': 22,
        'hobbies': ['BJJ', 'programming', 'singing']

    }
]
# Use a list comprehension to convert this list of persons into a list of names (of the persons).
users_names = [user['name'] for user in users]
print(users_names)
# Use a list comprehension to check wether all persons are older than 20.
are_users_older_20 = all([user['age'] > 20 for user in users])
print(are_users_older_20)
# Copy the person list such that you can safely edit the name of the first person (without changing the original list).
import copy
copied_users = [copy.deepcopy(user) for user in users]
copied_users[0]['name'] = 'Lucas'
print(copied_users)
print(users)
# Upack the persons of the original list into different vriables and output these variables.
markus, anna, john = users
print(markus)
print(anna)
print(john)