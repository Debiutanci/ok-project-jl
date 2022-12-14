from graphviz import Digraph

dot = Digraph()
dot.node('A', 'A')
dot.node('B', 'B')
dot.node('C', 'C')
dot.edges(['AB', 'AB', 'AB', 'BC', 'BA', 'CB'])

print(dot.source)
dot.render(view=True)

def get_disgraph_by_data(data, mapping_var):
    d = Digraph()
    for k, _ in mapping_var.items():
        d.node(k, k)
    edges = []
    for arr in data:
        edges.append(f"{arr[0]}{arr[1][0]}")
    dot.edges(edges)
    print(dot.source)
    dot.render(view=True)
