from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer, level=None, types=None, hungry=False):

        self.pokemon_trainer = pokemon_trainer   
        self.pokemon_number = randint(1,1000)
        self.types = []
        self.type = self.get_type()
        self.img = self.get_img()
        self.name = self.get_name()
        self.abilities = self.get_abilities()
        self.hp = randint(10,100)
        self.power = randint(2,10)
        self.level = 0
        self.hungry = hungry
        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"

    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            picture = response.json()
            return (picture['sprites']['other']['official-artwork']['front_default'])
        else:
            return "сегодня нет картинок ))"
    def get_type(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['types'][0]['type']['name']
        else:
            return "unknowm"

    def get_types(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return [t['type']['name'] for t in data['types']]
        else:
            return []

    def get_abilities(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return [a['ability']['name'] for a in data['abilities']]
        else:
            return []

    def feed(self):
        if self.hungry == False:
            return f"Ваш покемон {self.name} сыт!"
        else:    
            self.hungry = False
            return f"Ваш покемон {self.name} накормлен!"
    
    def play(self):
        if self.hungry == True:
            return f"Ваш покемон {self.name} голоден и не хочет играть!"
        else:
            self.hungry = True
            self.level += 1
            return f"Ваш покемон {self.name} играет и проголодался!"

    def rarity(self):
        if len(self.types) >= 1 or self.types != "water" or "fire" or "wind" or "earth" or "normal":
            self.level += 3
            return "Редкий покемон. Ваш уровень повышен на 3!"
        else:
            return "Обычный покемон. Неудача, но в следующий раз повезет!"        

    def level_up(self):
        return f"Уровень вашего покемона {self.name} {self.level}!"
    # Метод класса для получения информации
    def info(self):
        return (f"Имя твоего покемона: {self.name}\n"
                f"Способности: {', '.join(self.abilities)}\n"
                f"Тип покемона: {', '.join(self.types)}\n"
                f"HP: {self.hp}\n"
                f"Attack: {self.attack}\n"
                f"Уровень: {self.level}\n"
                f"Голоден: {'Да' if self.hungry == True else 'Нет'}\n"
                f"{self.rarity()}\n"
                f"{self.img}"
                f"Класс покемона: {self.class_name()}\n")
    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
    def type_pokemon(self):
        return f"Тип вашего покемона: {self.type}"
    
    def class_name(self):
        chance = randint(1,5)
        if chance == 1:
            return Warrior(self.pokemon_trainer)
        elif chance == 2: 
            return Wizard(self.pokemon_trainer)
        else:
            return Pokemon(self.pokemon_trainer)
        
    def hospital(self):
        self.hp += 10
        return f"Покемон {self.name} вылечен в больнице! Его HP увеличен на 10."

    def attack(self, enemy):
        if isinstance(enemy, Wizard):
            chance = randint(1,5)
            if chance == 1:
                return f"Покемон-волшебник применил щит в сражении"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            self.level += 2
            self.hungry = True
            self.power += 1
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "
        
class Warrior(Pokemon):    
    def init__(self, pokemon_trainer):
        super().__init__(pokemon_trainer)
        self.power += 6

    def attack(self, enemy):
        супер_сила = randint(5,15)
        self.power += супер_сила
        результат = super().attack(enemy)
        self.power -= супер_сила
        return результат + f"\nБоец применил супер-атаку силой:{супер_сила} "

class Wizard(Pokemon):
    def init__(self, pokemon_trainer):
        super().__init__(pokemon_trainer)
        self.hp += 20

    def attack(self, enemy):
        return super().attack(enemy)