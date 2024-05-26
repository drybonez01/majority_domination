Per eseguire tutti gli step sequenzialmente:  
`python main.py`

Per definire i costi della rete:  
`python main.py -w (path_to_graph)`

Per eseguire rispettivamente il primo, il secondo o il terzo algoritmo per calcolare il seed set:  
`python main.py -s1 (path_to_graph) (path_to_weights)`  
`python main.py -s2 (path_to_graph) (path_to_weights)`  
`python main.py -s3 (path_to_graph) (path_to_weights)`

Per calcolare l'influenza di uno specifico seed set:  
`python main.py -m (path_to_graph) (path_to_seedset)`
