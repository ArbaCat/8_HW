from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    current_date = datetime.now()
    next_monday = current_date + timedelta(days=(7 - current_date.weekday()))
    last_monday = current_date - timedelta(days=current_date.weekday())
    # Создаем слвоарь с днями недели
    days_of_week = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }
    #Создаем пустые словари для каждого дня недели
    birthdays_per_week = {day: [] for day in days_of_week.values()}
    current_week_birthdays = []
    next_week_birthdays = []
    last_week_birthdays = []
    # Цикл обработки пользователя
    for user in users:
        name = user.get('name')
        birthday = user.get('birthday')
        if name and birthday:
            #Узнаем день недели для дня рождения
            birthday_weekday = birthday.weekday()
            day_of_week = days_of_week.get(birthday_weekday)
            #Перенос с выходных на понедельник
            if birthday_weekday >= 5:  # 5 - Saturday, 6 - Sunday
                day_of_week = 'Monday'
            next_birthday = birthday.replace(year=current_date.year)
            if next_birthday < current_date:
                if next_birthday >= last_monday and next_birthday < next_monday:
                    last_week_birthdays.append(f"{day_of_week}: {name}")
            elif next_birthday >= next_monday:
                next_week_birthdays.append(f"{day_of_week}: {name}")
            else:
                current_week_birthdays.append(f"{day_of_week}: {name}")
            birthdays_per_week[day_of_week].append(name)
   
    return birthdays_per_week



# Рандомно сгенерированный датасет для теста 
if __name__ == "__main__":
    users = [
        {"name": "Alice_0", "birthday": datetime(1995, 3, 12)},
        {"name": "Bob_1", "birthday": datetime(1987, 9, 18)},
        {"name": "Carol_0", "birthday": datetime(2000, 1, 5)},
        {"name": "David_1", "birthday": datetime(1992, 8, 21)},
        {"name": "Eve_2", "birthday": datetime(1985, 6, 30)},
        {"name": "Frank_1", "birthday": datetime(1998, 4, 15)},
        {"name": "Grace_3", "birthday": datetime(1989, 7, 27)},
        {"name": "Henry_4", "birthday": datetime(1976, 12, 9)},
        {"name": "Ivy_4", "birthday": datetime(1982, 5, 19)},
        {"name": "Jack_5", "birthday": datetime(1970, 11, 3)},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
