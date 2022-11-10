import random

game_map = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

name_value = {}


def print_menu_game() -> str:
    """
    Функция выводит игоровое меню на печать
    """

    print("""
  Здравствуйте!
  Это игра 'Крестики нолики', это лучшая игра на свете! 
  Правила: 
  1. Вы вводите имена игроков!
  2. Рандомизатор определят кто чем будет ходить! 'X' или 'O' 
  3. Вы ходите по очереди! До тех пор, пока кто-то не выиграл

  Удачи!
  """)


def start_game(name_value_dict: dict) -> dict:
    """
    Функция определяет старт игры:
    1. Определяет имена игроков
    2. Определяет кто чем ходит: кто X, а кто O
    Возвращает словарь с результатами
    """

    print("Имя игрока для номера 1 - ")
    name_1 = input()
    print("Имя игрока для номера 2 - ")

    name_2 = input()
    list_go = ['X', 'O']
    result = random.randint(0, 1)
    if result == 0:
        name_value_dict[name_1] = list_go[result]
        name_value_dict[name_2] = list_go[result + 1]
    else:
        name_value_dict[name_1] = list_go[result - 1]
        name_value_dict[name_2] = list_go[result]
    return name_value_dict


def print_map(game_map: list) -> None:
  """
  Функция печатает игровое поле на экран
  """
  count = 0
  for result_element_row in range(len(game_map)):
      if count == 3:
        print()
        count = 0
      else:
        print(game_map[result_element_row])
        count += 1


def save_result(game_map: list) -> None:
  count = 0
  item_str = ""
  with open('result.txt', 'w') as file_w:
    for item_row in game_map:
      file_w.write(str(item_row) + "\n")


def check_row(game_list: list) -> bool:
  """
  game_list: игровое поле
  функция возвращает 1 или 0 в зависимости от того: были ли все крестики или нолики в строке
  1. были все крестики и нолики в строке, то возвращает 1
  2. не было всех ноликов и крестиков в строке, то возвращает 0
  """
  count = 0
  for row in game_list:
    for item in range(len(row)-1):
      if row[item] == row[item+1]:
        count += 1
    if count == 2:
      return 1
    else:
      count = 0
  if count == 0:
    return 0


def check_diag(game_list: list) -> bool:
    """
    game_list: игровое поле
    функция возвращает 1 или 0 в зависимости от того: были ли все крестики или нолики на диагонали
    1. были все крестики и нолики на диагонали, то возвращает 1
    2. не было всех ноликов и крестиков на диагонали, то возвращает 0
    """
    top_left = 0
    top_right = 2
    result_diag_left = []
    result_diag_right = []

    for row in game_list:
        result_diag_left.append(row[top_left])
        top_left += 1

    for row in game_list:
        result_diag_right.append(row[top_right])
        top_right -= 1

    count_win = 0

    for value in range(len(result_diag_left) - 1):
        if result_diag_left[value] == result_diag_left[value + 1]:
            count_win += 1
    if count_win == 2:
        return 1
    else:
        count_win = 0
        for value in range(len(result_diag_right) - 1):
            if result_diag_right[value] == result_diag_right[value + 1]:
                count_win += 1
            if count_win == 2:
                return 1
            else:
                return 0


def check_column(game_list: list) -> bool:
  """
  game_list: игровое поле
  функция возвращает 1 или 0 в зависимости от того: были ли все крестики или нолики в столбце
  1. были все крестики и нолики в столбце, то возвращает 1
  2. не было всех крестиков и ноликов в столбце, то возвращает 0
  """
  top = 0
  count = 0
  count_win = 0
  column = []
  while count != 3:
    for row in game_list:
      column.append(row[top])
    for item in range(len(column)-1):
      if column[item] == (column[item+1]):
        count_win += 1
    if count_win == 2:
      return 1
    else:
      column = []
      top += 1
      count += 1
  if count_win == 0:
    return 0

def check_win(game_list: list) -> bool:
  """
  game_list: игоровое поле
  функция возвращает 1 или 0 в зависимости от того: были ли все крестики или нолики
  1. на диагонали
  2. в столбце
  3. в строчке
  """
  if check_row(game_list) == 1 and check_diag(game_list) == 1 and check_column(game_list) == 1:
    return 1
  else:
    return 0 