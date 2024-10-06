"""Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.

Вимоги до завдання:
Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' 
(наприклад, '2020-10-09').

Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної. 
Якщо задана дата пізніша за поточну, результат має бути від'ємним.

У розрахунках необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).
Для роботи з датами слід використовувати модуль datetime Python.

Рекомендації для виконання:
Імпортуйте модуль datetime.
Перетворіть рядок дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime.
Отримайте поточну дату, використовуючи datetime.today().
Розрахуйте різницю між поточною датою та заданою датою.
Поверніть різницю у днях як ціле число."""

from datetime import datetime


def get_days_from_today(date: str) -> int:
    # Calculates the number of days between the entered date and the current date.
    # date = '2024-11-06'
    today = datetime.today()

    date_obj = datetime.strptime(date, "%Y-%m-%d")
    result = today - date_obj
    days_only = result.days

    print(days_only)


date = input(f"Enter a date in YYYY-MM-DD format: ")
get_days_from_today(date)
