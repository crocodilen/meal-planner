import art
import pickle
import random

class Dish:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self) -> str:
        return self.name
    

def save_list(list, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(list, file)

def load_list(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)

# all_dishes = [
#     Dish('Köttbullar med pasta'),
#     Dish('Plättar'),
#     Dish('Vegofärs med pasta'),
# ]

# save_list(all_dishes, '.\\data\\all_dishes.pkl')

all_dishes = []

def main_menu():
    main_title = "What's for dinner?"
    prompt_menu = """1: Vad ska vi äta?
2: Visa alla maträtter
3: Lägg till maträtt
q: Avbryt
"""

    art.tprint(main_title)
    print(prompt_menu)
    all_dishes = load_list('.\\data\\all_dishes.pkl')

    while True:
        user_input = input("""
[Välj 1-3 eller q, sen <enter>]: """)
    
        if user_input == '1':
            print()
            print("********************************************")
            print(f"""{random.choice(all_dishes)}!""")
            print("********************************************")
        elif user_input == '2':
            print()
            print("""********************************************""")
            for dish in all_dishes:
                print(f"""{dish}""")
            print("********************************************")
        elif user_input == '3':
            print()
            new_dish_input = input("[Skriv in en ny maträtt, avsluta med <enter>]: ")
            all_dishes.append(Dish(new_dish_input))
            print()
            print("""********************************************""")
            print(f"{new_dish_input} har lagts till, bra idé!")
            print("********************************************")
        elif user_input == 'q':
            save_list(all_dishes, '.\\data\\all_dishes.pkl')
            print()
            print("""********************************************""")
            print("""Tack för maten, den var go', mitt i maten stod en ko.""")
            print("********************************************")
            art.tprint("""Bon   Appetit!   Bye   bye!""")
            break
        else:
            print()
            print("""********************************************""")
            print(f"""Hmm, {user_input} var visst inget alternativ, prova igen!""")
            print("********************************************")

if __name__ == "__main__":
    main_menu()
