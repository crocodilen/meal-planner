from art import *
import random

def main_menu():
    main_title = "What's for dinner?"

    tprint(main_title)

    dishes = [
        "Plättar",
        "Vegobullar med broccoli",
        "Räkpanna"
    ]

    while True:
        user_input = input("""
                           1: Vad ska vi äta?
                           2: Visa veckans matsedel [ToDo: Denna funkar inte än...]
                           3: Lägg till maträtt [ToDo: Denna funkar inte heller...]
                           q: Avbryt

                           """)
    
        if user_input == '1':
            print(f"""
                  *** {random.choice(dishes).upper()}! ***
                  """)
        elif user_input == '2':
            print("""
                  Funkar tyvärr inte än :-(
                  """)
        elif user_input == '3':
            print("""
                  Funkar tyvärr inte än :-(
                  """)
        elif user_input == 'q':
            print("""
                  Tack för maten, den var go', mitt i maten stod en ko.
                  """)
            tprint("""Bon   Appetit!   Bye   bye!""")
            break
        else:
            print(f"""
                  Hmm, {user_input} var visst inget alternativ, prova igen!
                  """)
            
if __name__ == "__main__":
    main_menu()
