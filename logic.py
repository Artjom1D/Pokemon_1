from random import randint
from datetime import timedelta, datetime
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer, level=None, types=None, hungry=False, last_feed_time=None):

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
        self.last_feed_time = last_feed_time if last_feed_time else datetime.now()
        
        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения имени покемона через API
    def class_name(self):
        return self.__class__.__name__
        
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

    def feed(self, feed_interval = 20, hp_increase = 10):
        current_time = datetime.now()  
        delta_time = timedelta(seconds=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        elif self.hungry == True:
            self.hp += hp_increase
            self.last_feed_time = current_time
            self.hungry = False
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            return f"Следующее время кормления покемона: {self.last_feed_time+delta_time}"


    def play(self, feed_interval=20):
        if self.hungry == True or self.last_feed_time + timedelta(seconds=feed_interval) < datetime.now():
            return f"Ваш покемон {self.name} голоден и не хочет играть!"
        else:
            self.hungry = True
            self.level += 1
            return f"Ваш покемон {self.name} играет и проголодался!"

    def rarity(self):
        if len(self.types) >= 1 or self.types != "water" or "fire" or "wind" or "earth" or "normal":
            self.level += 3
            return "Редкий покемон!"
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
                f"Attack: {self.power}\n"
                f"{self.rarity()}\n"
                f"Уровень: {self.level}\n"
                f"Голоден: {'Да' if self.hungry == True else 'Нет'}\n"
                f"Класс покемона: {self.class_name()}\n")
    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
    def type_pokemon(self):
        return f"Тип вашего покемона: {self.type}"
        
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
    def __init__(self, pokemon_trainer):
        super().__init__(pokemon_trainer)
        self.power += 6

    def attack(self, enemy):
        супер_сила = randint(5,15)
        self.power += супер_сила
        результат = super().attack(enemy)
        self.power -= супер_сила
        return результат + f"\nБоец применил супер-атаку силой:{супер_сила} "
    
    def feed(self, feed_interval=10, hp_increase=10):
        super().feed(feed_interval, hp_increase)

class Wizard(Pokemon):
    def __init__(self, pokemon_trainer):
        super().__init__(pokemon_trainer)
        self.hp += 20

    def attack(self, enemy):
        return super().attack(enemy)
    
    def feed(self, feed_interval=20, hp_increase=20):
        super().feed(feed_interval, hp_increase)