import art
import random

class Dish:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self) -> str:
        return self.name

all_dishes = [
    Dish('Köttbullar med pasta'),
    Dish('Plättar'),
    Dish('Vegofärs med pasta'),
]

def main_menu():
    main_title = "What's for dinner?"
    prompt_menu = """1: Vad ska vi äta?
2: Visa alla maträtter
3: Lägg till maträtt [ToDo: Denna funkar inte heller...]
q: Avbryt
"""

    art.tprint(main_title)
    print(prompt_menu)

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
            print("""********************************************""")
            print("""Funkar tyvärr inte än :-(""")
            print("********************************************")
        elif user_input == 'q':
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
