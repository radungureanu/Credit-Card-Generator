import tkinter as tk              # Importă modulul tkinter cu un alias scurt (tk), pentru a crea interfețe grafice.
from tkinter import ttk           # Importă modulul ttk din tkinter, care oferă widget-uri cu un aspect mai modern.
import random                     # Importă modulul random, utilizat pentru a genera valori la întâmplare.
from datetime import datetime, timedelta  # Importă clasele datetime și timedelta, folosite pentru a lucra cu date și perioade de timp.

def genereaza_card():
    import random
    from datetime import datetime, timedelta

    # Dicționar cu tipuri de card, fiecare având un prefix, lungimea numărului de card și lungimea CVV-ului.
    card_types = {
        'Visa': (4, 16, 3),
        'MasterCard': (5, 16, 3),
        'American Express': (34, 15, 4)
    }

    # Alege la întâmplare un tip de card din cheile dicționarului card_types.
    chosen_type = random.choice(list(card_types.keys()))
    # Extrage prefixul, lungimea numărului și lungimea CVV pentru tipul de card ales.
    prefix, length, cvv_length = card_types[chosen_type]

    # Generăm numărul de card:
    # Convertim prefixul într-o listă de cifre.
    card_number_digits = [int(d) for d in str(prefix)]
    # Cât timp lungimea listei de cifre este mai mică decât lungimea necesară, adăugăm cifre aleatorii.
    while len(card_number_digits) < length:
        card_number_digits.append(random.randint(0, 9))
    # Convertim lista de cifre în șir de caractere pentru a obține numărul complet de card.
    card_number = ''.join(str(d) for d in card_number_digits)

    # Generăm data de expirare:
    # Luăm data curentă, adăugăm un număr aleatoriu de zile între 365 (1 an) și 5*365 (5 ani),
    # apoi formatarea "mm/yy" pentru a obține data de expirare.
    expiration_date = (datetime.now() + timedelta(days=random.randint(365, 5*365))).strftime("%m/%y")

    # Generăm CVV-ul:
    # Creăm un șir de cifre aleatorii, lungimea depinde de tipul cardului (3 sau 4 cifre).
    cvv = ''.join(str(random.randint(0, 9)) for _ in range(cvv_length))

    # Generăm un nume de titular de card:
    # Avem liste cu prenume și nume, alegem la întâmplare câte unul din fiecare.
    first_names = ["Ion", "Mihai", "Andrei", "Ana", "Maria", "Elena"]
    last_names = ["Popescu", "Ionescu", "Stan", "Dumitru", "Georgescu", "Marin"]
    card_holder = f"{random.choice(first_names)} {random.choice(last_names)}"

    # Returnăm datele cardului (tip, număr, expirare, CVV, titular) pentru a le folosi în interfață.
    return chosen_type, card_number, expiration_date, cvv, card_holder

def genereaza_si_afiseaza():
    # Apelează funcția genereaza_card() pentru a obține datele unui card nou.
    card_type, card_number, expiration_date, cvv, card_holder = genereaza_card()
    # Actualizează etichetele din interfață cu valorile primite.
    label_type_val.config(text=card_type)
    label_number_val.config(text=card_number)
    label_expiration_val.config(text=expiration_date)
    label_cvv_val.config(text=cvv)
    label_holder_val.config(text=card_holder)


# Creăm fereastra principală (root) pentru interfața grafică.
root = tk.Tk()
# Setăm titlul ferestrei.
root.title("Generator de Carduri")

# Creăm un cadru (frame) principal cu padding, pentru a organiza widget-urile.
frame = ttk.Frame(root, padding="10")
# Plasăm cadrul în grilă, pe rândul 0, coloana 0, și îl întindem în ambele direcții (nsew).
frame.grid(row=0, column=0, sticky="nsew")

# Creăm etichete (Labels) și le plasăm în cadrul creat, pentru a afișa textele fixe și valorile dinamic.
label_type = ttk.Label(frame, text="Card Type:")
label_type.grid(row=0, column=0, sticky="w", padx=5, pady=5)
label_type_val = ttk.Label(frame, text="")
label_type_val.grid(row=0, column=1, sticky="w", padx=5, pady=5)

label_number = ttk.Label(frame, text="Card Number:")
label_number.grid(row=1, column=0, sticky="w", padx=5, pady=5)
label_number_val = ttk.Label(frame, text="")
label_number_val.grid(row=1, column=1, sticky="w", padx=5, pady=5)

label_expiration = ttk.Label(frame, text="Expiration Date:")
label_expiration.grid(row=2, column=0, sticky="w", padx=5, pady=5)
label_expiration_val = ttk.Label(frame, text="")
label_expiration_val.grid(row=2, column=1, sticky="w", padx=5, pady=5)

label_cvv = ttk.Label(frame, text="CVV:")
label_cvv.grid(row=3, column=0, sticky="w", padx=5, pady=5)
label_cvv_val = ttk.Label(frame, text="")
label_cvv_val.grid(row=3, column=1, sticky="w", padx=5, pady=5)

label_holder = ttk.Label(frame, text="Card Holder:")
label_holder.grid(row=4, column=0, sticky="w", padx=5, pady=5)
label_holder_val = ttk.Label(frame, text="")
label_holder_val.grid(row=4, column=1, sticky="w", padx=5, pady=5)

# Creăm un buton care, la apăsare, apelează funcția genereaza_si_afiseaza().
button_generate = ttk.Button(frame, text="Generează Card", command=genereaza_si_afiseaza)
button_generate.grid(row=5, column=0, columnspan=2, pady=10)

# Setăm ca fereastra principală să se redimensioneze automat, distribuind spațiul în mod egal.
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Pornim bucla principală (loop) a aplicației Tkinter, care afișează fereastra și așteaptă interacțiuni.
root.mainloop()



button_generate = ttk.Button(frame, text="Generează Card", command=genereaza_si_afiseaza)
button_generate.grid(row=5, column=0, columnspan=2, pady=10)
