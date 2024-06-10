import matplotlib.pyplot as plt
import os

directory_path = "C:/Users/Josef/Desktop/Uni/RS/Progetto/risorse/plotting"
output_directory = "C:/Users/Josef/Desktop/Uni/RS/Progetto/risorse/tmp_grafici"

if not os.path.exists(directory_path):
    print(f"Errore: la directory {directory_path} non esiste.")
else:
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    def read_influenced_nodes(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return int(lines[0].strip().split(':')[1])

    influenced_nodes_counts = []

    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory_path, filename)
            influenced_nodes_counts.append(read_influenced_nodes(file_path))

    x_values = range(1, 6)
    x_labels = ['5%', '7.5%', '10%', '15%', '20%']

    plt.figure(figsize=(10, 6))
    plt.plot(x_values, influenced_nodes_counts, marker='o', linestyle='-', color='b')

    plt.xlabel('Budget (%)')
    plt.ylabel('Numero di nodi influenzati')
    plt.grid(True)

    plt.xticks(ticks=x_values, labels=x_labels)

    output_file = os.path.join(output_directory, "grafico.png")
    plt.savefig(output_file)
    print(f"Grafico salvato in: {output_file}")

    plt.show()
