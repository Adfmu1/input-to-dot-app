import re

GRAPH_INFO_PATTERN_OBJ = re.compile(r'([a-z]+)\s+(\d+)')
GRAPH_TYPES = ['d', 'g', 'dw', 'gw']

def get_multiline_input() -> list[str]:
    print('Please insert your data, when done use [Ctrl + D] shortcut')
    lines = []
    while True:
        try:
            params = input().strip()
            
            if len(lines) == 0:
                if check_fst_input(params):
                    g_type, nodes = find_type_nodes(params)

                    if not is_graph_type_valid(g_type):
                        print(f'choose the correct type of graph - {GRAPH_TYPES}')
                    elif nodes == 0:
                        print(f'current number of nodes not valid:', nodes)
                    else:
                        lines.append(params)

                else:
                    print('Input not valid, should follow the convention: "[graph type] [number of nodes]"')
                    
        except EOFError:
            break
    
    return lines


def check_fst_input(prmpt: str) -> bool:
    return GRAPH_INFO_PATTERN_OBJ.fullmatch(prmpt) is not None

def find_type_nodes(prmpt: str) -> tuple[str, int] | None:
    r1, r2 = GRAPH_INFO_PATTERN_OBJ.search(prmpt).groups()
    return r1, int(r2)
    
def is_graph_type_valid(prmpt: str) -> bool:
    return prmpt in GRAPH_TYPES

if __name__ == '__main__':
    usr_data = get_multiline_input()
    