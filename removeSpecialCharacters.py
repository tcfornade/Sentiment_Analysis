import re

def remove_special_characters(text):
    # Verificați dacă valoarea este un șir de caractere
    if isinstance(text, str):
        # Definim expresia regulată care identifică caracterele nedorite (virgule și alte semne)
        pattern = r'[^\w\s]'  # Va elimina toate caracterele care nu sunt alfanumerice, spații sau sublinieri

        # Înlocuim caracterele nedorite cu un șir gol
        clean_text = re.sub(pattern, '', text)
        return clean_text
    else:
        return text  # Returnăm valoarea originală dacă nu este un șir de caractere
