from datetime import datetime, timedelta, date
import calendar

def get_birthdays_per_week(users, today=None):
    # Получаем текущий день
    if today is None:
        today = datetime.now().date()
    
    # Создаем словарь для хранения имен пользователей по дням недели
    weekdays = {day: [] for day in calendar.day_name}
    
    # Проходим по всем пользователям
    for user in users:
        # Определяем день рождения этого года
        birth_date_this_year = user['birthday'].replace(year=today.year)
        
        # Определяем день рождения следующего года
        birth_date_next_year = user['birthday'].replace(year=today.year + 1)
        
        # Список для хранения дней рождений, которые нужно учесть
        upcoming_birthdays = []
        
        if today <= birth_date_this_year <= today + timedelta(days=6):
            upcoming_birthdays.append(birth_date_this_year)
            
        if today <= birth_date_next_year <= today + timedelta(days=6):
            upcoming_birthdays.append(birth_date_next_year)
        
        for upcoming_birthday in upcoming_birthdays:
            # Определяем день недели
            weekday = calendar.day_name[upcoming_birthday.weekday()]
            
            # Если день рождения на выходных, переносим на понедельник
            if weekday in ['Saturday', 'Sunday']:
                weekday = 'Monday'
            
            # Добавляем имя пользователя к соответствующему дню недели
            weekdays[weekday].append(user['name'])
    
    # Удаляем пустые дни
    weekdays = {k: v for k, v in weekdays.items() if v}
    
    return weekdays


# Тестовый список пользователей
test_users = [
    {'name': 'Bill', 'birthday': datetime(1985, 10, 3).date()},
    {'name': 'Jill', 'birthday': datetime(1990, 10, 6).date()},
    {'name': 'Kim', 'birthday': datetime(1995, 10, 7).date()},
    {'name': 'Jan', 'birthday': datetime(2000, 10, 10).date()},
    {'name': 'Sue', 'birthday': datetime(1975, 12, 25).date()},
]

# Тестируем функцию
get_birthdays_per_week(test_users)


# Тест 1: Все дни рождения уже прошли в этом году
print("Test 1:", get_birthdays_per_week([
    {'name': 'John', 'birthday': (datetime(2023, 12, 16)).date()},
    {'name': 'Doe', 'birthday': (datetime(2023, 12, 6)).date()}
], today=datetime(2023, 12, 26).date()))

# Тест 2: Пустой список пользователей
print("Test 2:", get_birthdays_per_week([], today=datetime(2023, 12, 26).date()))

# Тест 3: Дни рождения в будущем, не на выходных
print("Test 3:", get_birthdays_per_week([
    {'name': 'John', 'birthday': (datetime(2023, 12, 27)).date()},
    {'name': 'Doe', 'birthday': (datetime(2023, 12, 29)).date()},
    {'name': 'Alice', 'birthday': (datetime(2023, 12, 23)).date()}
], today=datetime(2023, 12, 26).date()))

# Тест 4: Некоторые дни рождения уже прошли, но будут на следующей неделе в следующем году
print("Test 4:", get_birthdays_per_week([
    {'name': 'John', 'birthday': (datetime(2023, 12, 21)).date()},
    {'name': 'Doe', 'birthday': (datetime(2023, 12, 20)).date()},
    {'name': 'Alice', 'birthday': (datetime(2021, 1, 1)).date()}
], today=datetime(2023, 12, 26).date()))

# Тест 5: Дни рождения на выходных
print("Test 5:", get_birthdays_per_week([
    {'name': 'John', 'birthday': (datetime(2023, 12, 31)).date()},
    {'name': 'Doe', 'birthday': (datetime(2024, 1, 1)).date()},
    {'name': 'Alice', 'birthday': (datetime(2023, 12, 29)).date()}
], today=datetime(2023, 12, 26).date()))
