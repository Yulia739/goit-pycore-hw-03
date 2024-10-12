from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    # Ця функція повертає юзерів дні народження яких випадають вперед на 7 днів включаючи поточний день
    today = datetime.now().date()
    date_after7 = today + timedelta(days=7)

    congrats_list = []

    for user in users:
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_date = birthday_date.replace(year=today.year)
        if today <= birthday_date <= date_after7:
            # Частина завдання, а саме умова "Перевірте, чи вже минув день народження в цьому році
            # (if birthday_this_year < today). Якщо так, розгляньте дату на наступний рік."
            # була проігнорована через конфлікт з умовою "Функція повинна повернути список всіх у кого
            # день народження вперед на 7 днів включаючи поточний день."
            if birthday_date.weekday() == 5:
                birthday_date += timedelta(days=2)
            elif birthday_date.weekday() == 6:
                birthday_date += timedelta(days=1)
            format_date = datetime.strftime(birthday_date, "%Y.%m.%d")
            congrats_list.append({"name": user["name"], "congrats_date": format_date})

    return congrats_list


result = get_upcoming_birthdays(
    [
        {"name": "Alice", "birthday": "2001.10.07"},
        {"name": "Oliver", "birthday": "1999.12.25"},
        {"name": "Genry", "birthday": "1998.10.13"},
        {"name": "Sirius", "birthday": "2002.10.19"},
        {"name": "Alberto", "birthday": "2002.10.12"},
    ]
)
print(result)




def get_anomaly_dates(data):
    result = []
    for day_data in data:
        if day_data["temp"] < -30:
            result.append({"date": day_data["date"], "wear": "sharfick"})
        elif day_data["temp"] > 30:
            result.append({"date": day_data["date"], "wear": "kepka"})
    return result


res_f = get_anomaly_dates(
    [
        {"date": "15.03.2024", "temp": -200},
        {"date": "22.09.2024", "temp": 10},
        {"date": "05.12.2024", "temp": -5},
        {"date": "30.07.2024", "temp": 36},
        {"date": "18.01.2024", "temp": -39},
    ]
)
print(res_f)