def calculate_ticket_price(age):
    student = input('Are you a student? please select y or n:')
    if student == 'y':
        print('Ticket price for student is $15 ')
    else:
        if age < 5:
            print(f'Ticket price for age {age} is $0')
        elif age >= 5 and age <= 18 or age >= 65:
            print(f'Ticket price for age {age} is $20')
        else:
            print(f'Ticket price for age {age} is $30')

# calculate_ticket_price(78)