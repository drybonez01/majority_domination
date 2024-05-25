from weightDef import weightDef

while True:
    print("")
    print("1 - Definisci i pesi")
    print("0 - Termina")
    n = int(input("Seleziona un'operazione da eseguire: "))

    if n == 1:
        weightDef()
    elif n == 0:
        print("Arrivederci.")
        break
    else:
        print("Operazione non valida. Riprovare.")
