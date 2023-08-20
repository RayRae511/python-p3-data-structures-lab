spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [foods['name'] for foods in spicy_foods]
get_names(spicy_foods)
# => ["Green Curry", "Buffalo Wings", "Mapo Tofu"]

def get_spiciest_foods(spicy_foods):
    return [foods for foods in spicy_foods if foods.get('heat_level') > 5]
get_spiciest_foods(spicy_foods)
# [{"name": "Green Curry", "cuisine": "Thai", "heat_level": 9}, {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6}]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = '🌶' * food['heat_level']
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")
    

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food.get('cuisine') == cuisine:
            return food
    pass

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    for food in spiciest_foods:
        heat_level = '🌶' * food['heat_level']
        print(f"{food.get('name')} {food.get('cuisine')} | Heat Level: {heat_level}")
# Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶
# Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶

def get_average_heat_level(spicy_foods):
    total_heat = sum(food['heat_level'] for food in spicy_foods)
    num_foods = len(spicy_foods)
    if num_foods == 0:
        return 0
    avg = total_heat/num_foods
    return int(avg)
    

def create_spicy_food(spicy_foods, spicy_food):
    new_spicy = spicy_foods.copy()
    new_spicy.append(spicy_food)
    return new_spicy
