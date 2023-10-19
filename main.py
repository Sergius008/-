import random
class Game:

    def __init__(self):
        with open('city.txt', encoding='utf-8') as file:
            self.cities = [line.strip() for line in file]

        self.use_word = []
        self.used_cities = []

        self.current_city = None

    def __is_valid(self, next_city):
        if not next_city.isalpha():
            return False
        if next_city[0].lower() != self.__right_letter(self.current_city):
            return False
        if next_city.lower().replace(' ', '') in [city.lower().replace(' ', '') for city in self.used_cities] or next_city.lower().replace(' ', '') not in [city2.lower().replace(' ', '') for city2 in self.cities]:
            return False
        else:
            return True
    def __is_game_over(self):
        return len(self.used_cities) == len(self.cities)
    def __bot_city(self):
        next_city = None
        cities = [i for i in self.cities if i[0].lower() == self.__right_letter(self.current_city).lower()]
        while True:
            next_city1 = random.choice(cities)
            if next_city1 not in self.used_cities:
                next_city = next_city1
                break
            else:
                continue
        if next_city == next_city1:
            return next_city
    def __right_letter(self, word,):
        letter = None
        word = word.replace(' ', '').lower()
        a = ['ь', 'ъ', 'ы', 'й']
        if self.use_word != []:
            for i2 in self.use_word:
               a.append(i2)

        for i in reversed(word):
            if i in a:
                continue
            else:
                letter = word.index(i)
                break
        return word[letter]


    def start_game(self):

        while True:
            start = input('Привет , сыграем в игру \'Города России\', Напиши Да или Нет: ')
            if start.lower() == 'да':
                print('''Правила игры: Я называю тебе случайный город из списка,
а ты должен назвать город, название которого начинается с его последней буквы.
Если название города заканчивается на "Й", "Ь", "Ъ" или "Ы",
то берется предпоследняя буква города.
Также если вы хотите закончить игру пропишите слово \'Стоп\'
''')
                self.current_city = random.choice(self.cities)

                self.used_cities.append(self.current_city)
                print(f'Начнём с города {self.current_city}')
                self.__play()
                break
            elif start.lower() == 'нет':
                print('Пока, Надеюсь сыграть с вами снова')
                break
            else:
                print('Введите да или нет')


    def __play(self):
        while True:
            next_city = input(f"Сейчас нужно назвать город, начинающийся с буквы \'{self.__right_letter(self.current_city)}\'").replace(' ', '')

            next_city_big = next_city.lower()

            if self.__is_valid(next_city_big):
                a1 = [city.lower().replace(' ', '') for city in self.cities]

                b = a1.index(next_city_big)
                self.current_city = self.cities[b]

                print(f'Верно, {self.current_city} существует')

                self.used_cities.append(self.current_city)
                if len([all_city3 for all_city3 in self.used_cities if next_city_big[0] == all_city3[0].lower()]) == len([all_city4 for all_city4 in self.cities if next_city_big[0] == all_city4[0].lower()]):
                    if self.current_city[0].lower() not in self.use_word:
                        self.use_word.append(self.current_city[0].lower())
                    print(f'Города на букву {next_city_big[0]} закончились,\n теперь город заканчивающийся на эту букву будет начинаться на предпоследнюю букву города')
                self.current_city = self.__bot_city()
                self.used_cities.append(self.current_city)

                print(f'Я выбрал город {self.current_city}')
                if len([all_city3 for all_city3 in self.used_cities if self.current_city[0].lower() == all_city3[0].lower()]) == len([all_city4 for all_city4 in self.cities if self.current_city[0].lower() == all_city4[0].lower()]):
                    if self.current_city[0].lower() not in self.use_word:
                        self.use_word.append(self.current_city[0].lower())
                    print(f'Города на букву {self.current_city[0].lower()} закончились,\n теперь город заканчивающийся на эту букву будет начинаться на предпоследнюю букву города')
                continue

            if next_city.lower() == 'стоп':
                print(f'Вы вышли из игры\nВ игре были названы следующие города:\n{self.used_cities}\nПока, Надеюсь сыграть с вами снова')
                break

            if self.__is_game_over():
                print('Поздравляю ты прошёл игру!')
                break
            if next_city_big.replace(' ', '') in [city2.lower().replace(' ', '') for city2 in self.used_cities]:
                a2 = [city3.lower().replace(' ', '') for city3 in self.cities]
                repeat_city = a2.index(next_city_big.replace(' ', ''))
                print(f'{self.cities[repeat_city]} уже был')
            else:
                print('Неверный город')



def main():
    game = Game()
    game.start_game()






if __name__ == '__main__':
    try:

        main()
    except KeyboardInterrupt:
        print('Вы вышли из игры')


