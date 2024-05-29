import os
import networkx as nx


def preprocess_gml(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    nodes = set()
    edges = set()
    clean_lines = []
    in_node_section = False
    in_edge_section = False

    for line in lines:
        stripped_line = line.strip()
        if stripped_line.startswith('node'):
            in_node_section = True
            node = [line]
        elif stripped_line.startswith('edge'):
            in_edge_section = True
            edge = [line]
        elif in_node_section:
            node.append(line)
            if stripped_line.endswith(']'):
                node_id = None
                for part in node:
                    if part.strip().startswith('id'):
                        node_id = part.strip()
                        break
                if node_id and node_id not in nodes:
                    nodes.add(node_id)
                    clean_lines.extend(node)
                in_node_section = False
        elif in_edge_section:
            edge.append(line)
            if stripped_line.endswith(']'):
                source, target = None, None
                for part in edge:
                    if part.strip().startswith('source'):
                        source = part.strip()
                    elif part.strip().startswith('target'):
                        target = part.strip()
                if source and target:
                    edge_tuple = (source, target)
                    if edge_tuple not in edges:
                        edges.add(edge_tuple)
                        clean_lines.extend(edge)
                in_edge_section = False
        else:
            clean_lines.append(line)

    temp_file_path = file_path + '.temp'
    with open(temp_file_path, 'w') as temp_file:
        temp_file.writelines(clean_lines)

    return temp_file_path


def count_nodes_and_edges(file_path):
    try:
        temp_file_path = preprocess_gml(file_path)
        graph = nx.read_gml(temp_file_path)
        num_nodes = graph.number_of_nodes()
        num_edges = graph.number_of_edges()
        os.remove(temp_file_path)  # Rimuovi il file temporaneo dopo l'uso
        return num_nodes, num_edges
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None, None


def process_gml_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.gml'):
            file_path = os.path.join(directory, filename)
            num_nodes, num_edges = count_nodes_and_edges(file_path)
            if num_nodes is not None and num_edges is not None:
                print(f"File: {filename}")
                print(f"Number of nodes: {num_nodes}")
                print(f"Number of edges: {num_edges}")
                print()


# Percorso della cartella con i file .gml
directory_path = r'C:\Users\josef\OneDrive\Desktop\Datasets\gmls'
process_gml_files(directory_path)
