from datetime import datetime
import random

# Перше завдання

def get_days_from_today(date):
    try:
        givendate = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        raznica = (today - givendate).days
        return raznica
    except (TypeError, ValueError): 
        return None


# Друге завдання

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity < min or quantity > max:
        return [] 
    else:
        numbers = random.sample(range(min, max + 1), quantity)

    return sorted(numbers)
    


    























