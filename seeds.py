from datetime import datetime
from random import randint, choice
import sqlite3

from faker import Faker



NUMBER_TEACHERS = 5
NUMBER_STUDENTS = 50

subjects = [
    "Математика",
    "Теоретична інформатика",
    "Архітектура комп'ютерів",
    "Алгоритми та структури даних",
    "Мови програмування",
    "Бази даних",
    "Інформаційні мережі",
    "Криптографія та інформаційна безпека"
]

groups = ["мт-11-3", "мм-13-1", "кн-12-2"]

fake = Faker()

if __name__ == "__main__":
    pass