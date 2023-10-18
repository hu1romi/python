class Calculator:


    def evaluate_expression(self, expression):
        try:
            result = eval(expression)
            return result
        except Exception as e:
            return f"Ошибка: {str(e)}"

    def get_user_input(self,expression):
        result = self.evaluate_expression(expression)
        return result


def calculator():
    calc = Calculator()

    while True:
        print("Введите математическое выражение или 'выход' для завершения:")

        user_input = input()

        if user_input.lower() == 'выход':
            break

        result = calc.get_user_input(user_input)
        print(f"Результат: {result}")


class Animal:
    def __init__(self, breed, cost):
        self.breed = breed
        self.cost = cost

    def move(self):
        pass


class Fish(Animal):
    def move(self):
        return "Плавание"


class Bird(Animal):
    def move(self):
        return "Летание"


class Zooshop:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)

    def get_most_expensive_breed(self):
        if not self.animals:
            return None

        most_expensive_animal = max(self.animals, key=lambda animal: animal.cost)
        return most_expensive_animal.breed

    def write_to_file(self, filename):
        with open(filename, 'w') as file:
            for animal in self.animals:
                file.write(f'Порода: {animal.breed}, Стоимость: {animal.cost} рублей\n')



def zoo_shop():
    zooshop = Zooshop()

    while True:
        print("Введите информацию о животном (порода стоимость) или введите 'выход' для завершения:")
        user_input = input()

        if user_input.lower() == 'выход':
            break

        try:
            breed, cost = user_input.split()
            cost = int(cost)
            animal = Animal(breed, cost)
            zooshop.add_animal(animal)
        except ValueError:
            print("Ошибка: Неправильный формат данных. Введите породу и стоимость через пробел.")

    most_expensive_breed = zooshop.get_most_expensive_breed()
    if most_expensive_breed:
        print(f"Самая дорогая порода: {most_expensive_breed}")
    else:
        print("Нет данных о животных.")

        zooshop.write_to_file("animal_info.txt")


import pygame


class TrafficLightSimulator:
    def __init__(self):

        pygame.init()


        self.width, self.height = 200, 600


        self.screen = pygame.display.set_mode((self.width, self.height))


        self.colors = {
            "красный": (255, 0, 0),
            "жёлтый": (255, 255, 0),
            "зелёный": (0, 255, 0)
        }

        self.current_color = "красный"
        self.running = False

    def draw_traffic_light(self):
        self.screen.fill((0, 0, 0))  # Задний фон - черный
        pygame.draw.rect(self.screen, self.colors[self.current_color], (50, 50, 100, 300))
        pygame.display.flip()

    def run(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False

            self.draw_traffic_light()


            if self.current_color == "красный":
                pygame.time.wait(7000)
                self.current_color = "жёлтый"
            elif self.current_color == "жёлтый":
                pygame.time.wait(2000)
                self.current_color = "зелёный"
            elif self.current_color == "зелёный":
                pygame.time.wait(5000)
                self.current_color = "красный"







def traffic_light():
        traffic_light = TrafficLightSimulator()
        traffic_light.run()


def main():
    while True:
        print("\nМеню выбора задачи:")
        print("1. Калькулятор")
        print("2. Зоомагазин")
        print("3. Светофор")
        print("4. Выход")

        choice = input("Выберите задачу (1-4): ")

        if choice == '1':
            calculator()
        elif choice == '2':
            zoo_shop()
        elif choice == '3':
            traffic_light()
        elif choice == '4':
            print("Программа завершена.")
            break
        else:
            print("Пожалуйста, выберите корректную задачу (1-4).")


main()