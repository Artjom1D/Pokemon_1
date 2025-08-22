from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer, level=1, types=None, hungry=False):

        self.pokemon_trainer = pokemon_trainer   
        self.types = []
        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.type = self.get_type()
        self.abilities = self.get_abilities()
        self.level = level
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
        if self.hungry:
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
        if self.types > 1 or self.types != "water" or "fire" or "wind" or "earth":
            self.level += 3
            return "Редкий покемон. Ваш уровень повышен на 3!"
        else:
            return "Обычный покемон. Неудача, но в следующий раз повезет!"


    def level_up(self):
        return f"Уровень вашего покемона {self.name} повышен до {self.level}!"
    # Метод класса для получения информации
    def info(self):
        return (f"Имя твоего покемона: {self.name}\n"
                f"Способности: {', '.join(self.abilities)}")

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
    def type_pokemon(self):
        return f"Тип вашего покемона: {self.type}"



