from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):

    birthdays_by_weekday = {i: [] for i in range(7)}  # Дикт для сохранения именинников по дням недели
    for user in users:
        birthday = user["birthday"].date() # получения дня рождения юзера в формате даты(оригинальный формат datatime)
        birthday_day_of_week = birthday.weekday() # Находим день недели для даты рождения.

        if birthday_day_of_week >= 5:  # Проверка на выходной( индексы 5(сб) и 6(вс))            
            birthday_day_of_week = 0 # переносим день поздравления на понедельник(нулевой индекс)
            
    current_date = datetime.now()

    week_later_date = current_date + timedelta(days=7)

    birthdays_per_week = {}  #Список пользователей для поздравлений по дням
    for i in range(7):
        birthdays_per_week[i] = []

    for user in users:  # превращаем в дататайм с пустыми значениями времени(только дата). Для совпадения типов
        user["birthday"] = datetime(user["birthday"].year, user["birthday"].month, user["birthday"].day)

    for user in users: 
        birthday = user["birthday"]
        name = user["name"]
        birthday = birthday.replace(year=current_date.year) #переносим дату дня рождения на актуальный год 

        birthdays_by_weekday[birthday.weekday()].append(user["name"]) # Добавляем имена к нужным дням
        if current_date <= birthday < week_later_date: 
            day_of_week = birthday.weekday()
            if day_of_week >= 5:  
                day_of_week = 0

            birthdays_per_week[day_of_week].append(name)

    day_names = [    # создаем список названия дней недели
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    for i in range(7):  # выводим результат с помощью джоинов
        day_name = datetime(2000, 1, 3 + i).strftime('%A')  
        if birthdays_by_weekday[i]:
            print(f"{day_name}: {', '.join(birthdays_by_weekday[i])}")
    for day_index, names in birthdays_per_week.items():
        if names:
            day_name = day_names[day_index]
            names_str = ", ".join(names)
            print(f"{day_name}: {names_str}")


# Сгенерированные с помощью ГПТ 3.5 тестовые данные 
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
get_birthdays_per_week(users)

if __name__ == "__main__":
    get_birthdays_per_week(users)
