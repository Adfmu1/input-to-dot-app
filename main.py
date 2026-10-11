import re

GRAPH_INFO_PATTERN_OBJ = re.compile(r'([a-z]+)\s+(\d+)')
GRAPH_TYPES = ['d', 'g', 'dw', 'gw']

class Graph:
    def __init__(self, type: str, max_edges: int):
        self.type = type
        self.max_edges = max_edges
        self.connections = {}
        self.edge_count = 0

    def add_node(self, relation: str):
        if len(self.type) == 1:
            match_rel_pattern = re.compile(r'(\w+)\s+(\w+)')
            match = match_rel_pattern.fullmatch(relation.strip())

            if match is not None:
                parent_node, child_node = match.groups()

                if parent_node not in self.connections:
                    self.connections[parent_node] = [child_node]
                else:
                    self.connections[parent_node].append(child_node)
                
                self.edge_count += 1
            else:
                print('Line error')

    def print_relation(self):
        if len(self.type) == 1:
            if self.type == 'd':
                print('digraph {')
                operator = '->'
            else:
                print('graph {')
                operator = '--'

            for parent, children in self.connections.items():
                for child in children:
                    print(f'{parent} {operator} {child};')

            print('}')


def get_multiline_input() -> Graph:
    print('Please insert your data, when done use [Ctrl + D] shortcut')
    first_line, r_graph = True, None
    while True:
        try:
            params = input().strip()
            
            if not params:
                continue            
            if first_line:
                if check_fst_input(params):
                    g_type, max_edges = find_graph_info(params)
                    if not is_graph_type_valid(g_type):
                        print(f'choose the correct type of graph - {GRAPH_TYPES}')
                    elif not 1 <= max_edges <= 100:
                        print(f'There should be beetween 1 and a 100 edges')
                    else:
                        r_graph = Graph(g_type, max_edges)
                        first_line = False
                else:
                    print('Input not valid, should follow the convention: "[graph type] [number of edges]"')
            else:
                r_graph.add_node(params)
                
                if r_graph.edge_count == r_graph.max_edges:
                    print(f'There can be only {r_graph.max_edges} edges in graph!')
                    return r_graph
                
                    
        except EOFError:
            break
    
    return r_graph


def check_fst_input(prmpt: str) -> bool:
    return GRAPH_INFO_PATTERN_OBJ.fullmatch(prmpt) is not None

def find_graph_info(prmpt: str) -> tuple[str, int] | None:
    r1, r2 = GRAPH_INFO_PATTERN_OBJ.search(prmpt).groups()
    return r1, int(r2)
    
def is_graph_type_valid(prmpt: str) -> bool:
    return prmpt in GRAPH_TYPES

if __name__ == '__main__':
    grph = get_multiline_input()
    grph.print_relation()