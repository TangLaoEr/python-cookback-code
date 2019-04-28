record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_number = record


# phone_number 为列表
print(name, email, phone_number)