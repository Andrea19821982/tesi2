Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from faker import Faker
... import pandas as pd
... import sqlite3
... 
... # Inizializza Faker per generare dati casuali
... fake = Faker()
... 
... # Imposta il seed per garantire che i dati generati siano sempre uguali
... Faker.seed(12345)
... 
... # Genera dati casuali per 10 utenti (nome, cognome, email, telefono) 
... users = [{"Nome": fake.first_name(),
...           "Cognome": fake.last_name(),
...           "Email": fake.email(),
...           "Telefono": fake.phone_number()} for _ in range(10)]
... 
... # Crea un DataFrame e salva i dati in un file Excel
... df = pd.DataFrame(users)
... df.to_excel("utenti.xlsx", index=False)
... print("File Excel 'utenti.xlsx' generato con successo!")
... 
