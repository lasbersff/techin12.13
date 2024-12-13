def greet(name):
    customer_data = {
        'Joe': {"visits": 1},
        'Carol': {"visits": 2},
        'Howard': {"visits": 3},
        'Carrie': {"visits": 4}
    }

    if name not in customer_data:
        return 'Welcome to the North Pole Café! Is this your first time? ❄️'

    visits = customer_data[name]["visits"]

    if visits == 1:
        return f"Ho ho ho! Welcome back, {name}! We're glad you enjoyed your first visit! 🎅"
    elif visits > 1:
        return f"Merry greetings, {name}! So wonderful to see you again! 🎄"

print(greet('Joe'))
print(greet('Carol'))
print(greet('Howard'))
print(greet('Carrie'))
print(greet('Emily'))
