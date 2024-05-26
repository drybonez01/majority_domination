import os
import sys

from weightDef import weightDef

'''while True:
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
        print("Operazione non valida. Riprovare.")'''

if len(sys.argv) > 1:
    if sys.argv[1] == "-w" or sys.argv[1] == "--weightDef":
        try:
            weightDef(sys.argv[2])
        except:
            print("ERRORE. Percorso errato o inesistente.")
else:
    graph_path = input("Inserisci il percorso del file .gml: ")
    while not os.path.exists(graph_path):
        print("ERRORE. Percorso errato o inesistente. Riprovare")
        graph_path = input("Inserisci il percorso del file .gml: ")
    weights_file_path = weightDef(graph_path)
