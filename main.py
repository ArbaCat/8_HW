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

    # Создаем список пользователей которые празднуют на этой неделе
    users_to_greet = []

    print("Next Monday:", next_monday)
    print("Next Sunday:", next_sunday)

    for user in users:
      time_obj = time()
      dt_next_monday = datetime.combine(next_monday, time_obj)
      dt_next_sunday = datetime.combine(next_sunday, time_obj)
      print("Next dtMonday:", dt_next_monday)
      print("Next dtSunday:", dt_next_sunday)
      print(user['birthday'])
      if dt_next_monday <= user['birthday'].replace(year=2023) <= dt_next_sunday:
          users_to_greet.append(user['name'])
      print(users_to_greet)
    print('Lets start')
    # Принтим список пользователей по дням 
    for i in range(7):
        day = next_monday + timedelta(days=i)
        day_name = day.strftime('%A')
        day_users = []
        for user in users_to_greet:
          user_birthday_day = user['birthday'].strftime('%A')
          if user_birthday_day == day_name:
            day_users.add(user['name'])
        print(f"{day_name}: {', '.join(day_users)}")
        if day_users:
            print(f"{day_name}: {', '.join(day_users)}")

#сгенерированный спсок словарей на тест 
if __name__ == "__main__":
    users = [
        {'name': 'Bill', 'birthday': datetime(1990, 10, 1)},
        {'name': 'Jill', 'birthday': datetime(1985, 10, 3)},
        {'name': 'Kim', 'birthday': datetime(1982, 10, 4)},
        {'name': 'Jan', 'birthday': datetime(1992, 10, 3)},
    ]

    get_birthdays_per_week(users)
