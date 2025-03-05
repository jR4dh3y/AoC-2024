import networkx as nx
# input = []

# with open("./xyz.txt", "r") as f:
#     for line in f.readlines():
#         input.append(line.strip())

# i = input.index('');
# rules = input[:i]
# pages = input[i+1:]

# for i in range(len(rules)):
#     rules[i] = list(map(int, rules[i].split('|')))

# for i in range(len(pages)):
#     pages[i] = list(map(int, pages[i].split(',')))





# graph = nx.DiGraph()
# graph.add_edges_from(rules)

# topo_sort = list(nx.topological_sort(graph))

# valid_pages = []
# for page in pages:
#     sub_order = [page for page in topo_sort if page in page]
    
#     if sub_order == page:
#         valid_pages.append(page)


# middle_pages = [update[len(update) // 2] for update in valid_pages]

# middle_pages_sum = sum(middle_pages)
# print("Sum of Middle Pages:", middle_pages_sum)




# File parsing and solving the problem

def parse_input(file_path):
    """
    Parses the input file to separate ordering rules and updates.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Separate rules and updates
    ordering_rules = []
    updates = []
    for line in lines:
        line = line.strip()
        if '|' in line:
            # Parse rules (e.g., 47|53 → (47, 53))
            a, b = map(int, line.split('|'))
            ordering_rules.append((a, b))
        elif ',' in line:
            # Parse updates (e.g., 75,47,61 → [75, 47, 61])
            updates.append(list(map(int, line.split(','))))

    return ordering_rules, updates


def solve_with_topological_sort_from_file(file_path):
    """
    Solves the problem using topological sort with inputs from a file.
    """
    # Parse the input file
    ordering_rules, updates = parse_input(file_path)

    # Create a directed graph for the ordering rules
    graph = nx.DiGraph()
    graph.add_edges_from(ordering_rules)

    # Perform a full topological sort of the graph
    try:
        topo_sort = list(nx.topological_sort(graph))
    except nx.NetworkXUnfeasible:
        return "Graph has cycles, no valid topological sort possible."

    # Validate updates and compute middle pages
    valid_updates = []
    middle_pages = []

    for update in updates:
        # Filter the topological order for pages in the update
        sub_order = [page for page in topo_sort if page in update]
        
        # Check if the update matches the filtered topological order
        if sub_order == update:
            valid_updates.append(update)
            middle_pages.append(update[len(update) // 2])  # Middle page

    # Compute the sum of the middle pages
    middle_pages_sum = sum(middle_pages)

    return valid_updates, middle_pages, middle_pages_sum


# Specify the path to the input text file
file_path = "xyz.txt"  # Replace with the actual file path

# Solve the problem using the file
result = solve_with_topological_sort_from_file(file_path)
(result)
