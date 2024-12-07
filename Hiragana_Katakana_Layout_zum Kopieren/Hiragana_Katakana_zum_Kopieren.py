import os
import shutil


ziel_ordner = "Hiragana_Katakana_Copies" 
dateiname_original = "HiraganaKatakana_Original.pdf"
# original_pdf = os.path.join(quelle_ordner, dateiname_original)
original_pdf = os.path.join(dateiname_original)

if not os.path.exists(ziel_ordner):
    os.makedirs(ziel_ordner)


if __name__=="__main__":

    n = 50

    # Kopien erstellen
    for i in range(1, n + 1):
        if i < 10:
            neue_datei = os.path.join(ziel_ordner, f"0{i}_HiraganaKatakana.pdf")
            shutil.copyfile(original_pdf, neue_datei)
            print(f"Kopie 0{i} erstellt: {neue_datei}")
        else:
            neue_datei = os.path.join(ziel_ordner, f"{i}_HiraganaKatakana.pdf")
            shutil.copyfile(original_pdf, neue_datei)
            print(f"Kopie {i} erstellt: {neue_datei}")
