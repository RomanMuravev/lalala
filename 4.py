import csv
import string
import random

def create_initials (s):
    """Описание функции create_initials

    s - строка, содержащая ФИО
    names - список, содержащий фамилию, имя и отчество

    Функция возвращает форматированную строку из Фамилии и первых букв имени и отчества, разделённых пробелом

    """
    names=s.split()
    return f'{names[0]}_{names[1][0]}{names[2][0]}'

def create_password():
    """
    characters - список всех букв и цифр
    password - строка, пароль

    Функция генерирует строку, состоящую из случацно выбранных букв и цифр
    """
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(8))
    return password

students_passwords=[]
with open('students.csv', encoding="utf8") as csvfile:
    reader = list(csv.DictReader(csvfile, delimiter=',', quotechar='"'))
    for row in reader:
        row['login']=create_initials(row['Name'])
        row['password']=create_password()
        students_passwords.append(row)

with open('students_new.csv', 'w', newline='', encoding='utf-8') as file:
    w = csv.DictWriter(file, fieldnames=['id', 'Name', 'titleProject_id',
'class', 'score', 'login', 'password'])
    w.writeheader()
    w.writerows(students_passwords)