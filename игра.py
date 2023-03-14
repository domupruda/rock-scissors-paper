import tkinter as tk
import random

# Создаем окно приложения
root = tk.Tk()
root.title("Камень-ножницы-бумага")

# Загружаем иконки
rock_img = tk.PhotoImage(file="rock.png")
paper_img = tk.PhotoImage(file="paper.png")
scissors_img = tk.PhotoImage(file="scissors.png")

# Создаем словарь, в котором каждой иконке соответствует номер
icons_dict = {rock_img: 0, paper_img: 1, scissors_img: 2}

# Создаем функцию, которая выбирает случайный выбор компьютера
def computer_choice():
    return random.randint(0, 2)

# Создаем функцию, которая сравнивает выбор игрока и компьютера
def compare_choices(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Ничья"
    elif player_choice == 0 and computer_choice == 1:
        return "Компьютер выиграл"
    elif player_choice == 1 and computer_choice == 2:
        return "Компьютер выиграл"
    elif player_choice == 2 and computer_choice == 0:
        return "Компьютер выиграл"
    else:
        return "Игрок выиграл"

# Создаем функцию, которая вызывается при нажатии на кнопку
def play(player_choice):
    # Получаем выбор компьютера
    computer = computer_choice()
    # Сравниваем выборы игрока и компьютера
    result = compare_choices(player_choice, computer)
    # Выводим результат в консоль и в окно приложения
    print(result)
    result_label.config(text=result)
    # Добавляем результат в файл
    with open("results.txt", "a") as f:
        f.write(f"Игрок: {player_choice}, Компьютер: {computer}, Результат: {result}\n")

# Создаем кнопки с иконками
rock_button = tk.Button(root, image=rock_img, command=lambda: play(0))
paper_button = tk.Button(root, image=paper_img, command=lambda: play(1))
scissors_button = tk.Button(root, image=scissors_img, command=lambda: play(2))

# Размещаем кнопки на окне приложения
rock_button.pack(side=tk.LEFT)
paper_button.pack(side=tk.LEFT)
scissors_button.pack(side=tk.LEFT)

# Создаем метку для вывода результата
result_label = tk.Label(root, text="")
result_label.pack()

# Запускаем главный цикл приложения
root.mainloop()
