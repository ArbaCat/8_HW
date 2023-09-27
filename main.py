from datetime import datetime, timedelta, date, time

def get_birthdays_per_week(users):
    # Получаем сегодняшнюю дату
    today = datetime.today()

    # Находим день недели для сегдняшней даты
    current_day_of_week = today.weekday()

    # Определяем количество дней к следующему понедельнику
    days_until_next_monday = (7 - current_day_of_week) % 7

    # получаем дату следующего понедельника
    time_difference = timedelta(days=days_until_next_monday)
    next_monday = datetime.date(today + time_difference)

    # Получаем дату следующего воскресенья
    next_sunday = next_monday + timedelta(days=6)

    # Создаем список пользователей которые празднуют на следующей неделе
    users_to_greet = []

    for user in users:
      time_obj = time()
      dt_next_monday = datetime.combine(next_monday, time_obj)
      dt_next_sunday = datetime.combine(next_sunday, time_obj)
      day_users_dict = {day_name: [] for day_name in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']}

      for i in range(7):
        day = next_monday + timedelta(days=i)
        day_name = day.strftime('%A')
        day_users = []
        for user in users:
          user_birthday = user['birthday'].replace(year=2023)
          #обрабатываем дни рождения на выходных
          if user_birthday.weekday() in (5,6) and user['name'] not in day_users_dict['Monday']:
            day_users_dict['Monday'].append(user['name'])
          #проверяем находится ли др юзера на следюущей неделе 
          if dt_next_monday <= user_birthday <= dt_next_sunday and user_birthday.strftime('%A') == day_name:
            day_users_dict[day_name].append(user['name'])  
    print(day_users_dict)
    for day_name, user_names in day_users_dict.items():
      if user_names:
        print(f'{day_name}: {", ".join(user_names)}')

#сгенерированный спсок словарей на тест
if __name__ == "__main__":
    users = [
        {'name': 'Bill', 'birthday': datetime(1990, 10, 1)},
        {'name': 'Jill', 'birthday': datetime(1985, 10, 3)},
        {'name': 'Kim', 'birthday': datetime(1982, 10, 4)},
        {'name': 'Jan', 'birthday': datetime(1992, 10, 3)},
    ]

    get_birthdays_per_week(users)
