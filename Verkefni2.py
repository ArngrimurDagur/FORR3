# Arngrímur Dagur Arnarsson
import csv
from klasi import Felag_Tækniskolans
felagsskr=[]
def opnaskra(felagsskr):
    with open("felagsskra.csv","r",newline="",encoding="utf-8") as file:
        reader=csv.reader(file,delimiter=";")
        for row in reader:
            felagi=Felag_Tækniskolans(row[0],row[1],row[2],row[3],row[4])
            felagsskr.append(felagi)
while True:
    print("┌───────────────────────────────────────────────────────────────┐")
    print("│ Veldu tölu til að fara í viðkomandi lið. Veldu 0 til að hætta │")
    print("│ 1. val1                                                       │")
    print("│ 2. val2                                                       │")
    print("│ 3. val3                                                       │")
    print("│ 4. val4                                                       │")
    print("│ 5. val5                                                       │")
    print("│ 6. val6                                                       │")
    print("│ 7. val7                                                       │")
    print("│ 0. hætta                                                      │")
    print("└───────────────────────────────────────────────────────────────┘")
    val=int(input("Veldu hér:"))
    if val == 1:
        
    elif val == 2:
        print(" ")
    elif val == 3:
        print(" ")
    elif val == 4:
        print(" ")
    elif val == 5:
        print(" ")
    elif val == 6:
        print(" ")
        
    elif val == 0:
        print("Takk fyrir")
        break
    else:
        print("Þú valdir vitlaust vinsamlegast byrjaðu aftur")