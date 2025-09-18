
fio = input("Введите ваше ФИО: ")
city = input("Введите город/страну, который хотели бы посетить: ")
dish = input("Введите ваше любимое блюдо: ")
phone_color = input("Введите цвет вашего телефона: ")
book = input("Введите название вашей любимой книги: ")

with open('text.txt', 'w', encoding='utf-8') as file:
    file.write(f"{fio}\n")
    file.write(f"{city}\n")
    file.write(f"{dish}\n")
    file.write(f"{phone_color}\n")
    file.write(f"{book}\n")

print("Данные успешно сохранены в файл text.txt")