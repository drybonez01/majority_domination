import matplotlib.pyplot as plt
import os

# Directory paths
directory_path = "C:/Users/Josef/Desktop/Uni/RS/Progetto/risorse/plotting"
output_directory = "C:/Users/Josef/Desktop/Uni/RS/Progetto/risorse/tmp_grafici"

# Verifica che la directory esista
if not os.path.exists(directory_path):
    print(f"Errore: la directory {directory_path} non esiste.")
else:
    # Verifica che la directory di output esista, altrimenti la crea
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Function to read the number of influenced nodes from the file
    def read_influenced_nodes(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return int(lines[0].strip().split(':')[1])

    # List to store influenced nodes counts
    influenced_nodes_counts = []

    # Iterate through all files in the directory and read influenced nodes count
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory_path, filename)
            influenced_nodes_counts.append(read_influenced_nodes(file_path))

    # Generate x values (assuming they represent different scenarios)
    x_values = range(1, len(influenced_nodes_counts) + 1)

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, influenced_nodes_counts, marker='o', linestyle='-', color='b')

    # Adding titles and labels
    plt.title('Numero di nodi influenzati con varaizione di budget')
    plt.xlabel('Budget')
    plt.ylabel('Numero di nodi influenzati')
    plt.grid(True)

    # Save the plot
    output_file = os.path.join(output_directory, "grafico.png")
    plt.savefig(output_file)
    print(f"Grafico salvato in: {output_file}")

    # Show plot
    plt.show()
