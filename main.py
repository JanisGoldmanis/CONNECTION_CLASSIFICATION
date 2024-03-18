import csv
import traceback
from tqdm import tqdm
import json


from treelib import Tree

import connection
import classify_connection

file_path = 'input/NACKA.csv'


def get_connections_from_file(file_location):
    # headers = ["GUID1", "GUID2", "PROFILE1", "PROFILE2", "MATERIAL1", "MATERIAL2", "CLASS1", "CLASS2", "ANGLE"]
    connections = []
    id = 1

    with open(file_location, encoding='UTF-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')

        header = next(reader)
        print(header)

        for row in tqdm(reader):
            this_connection = connection.Connection(id, *row)
            connections.append(this_connection)
            id += 1

    return connections


connections = get_connections_from_file(file_path)

print(f'Total connections: {len(connections)}')

config_path = 'config.json'

with open(config_path) as f:
    branch_config = json.load(f)

lists_path = 'lists.json'

with open(lists_path) as f:
    lists = json.load(f)['lists']

list_dict = {}
for object in lists:
    for key in object:
        list_dict[key] = object[key]

data_tree = {}

for connection in connections:
    classify_connection.classify_connection(data_tree, connection, branch_config, list_dict)

tree = Tree()
tree.create_node(f"{len(connections)}", "root")



def add_root_to_tree_plot(tree, branch, parent, data_tree):

    tree.create_node(f"{len(data_tree[branch]['connections']):>5} | {branch}", branch, parent)
    leaf = data_tree[branch]
    if len(leaf['children']) > 0:
        for object in leaf['children']:
            add_root_to_tree_plot(tree, object, branch, leaf['children'])

for object in data_tree:
    add_root_to_tree_plot(tree, object, "root", data_tree)


filepath = 'Results.csv'
with open(filepath, 'w', encoding='utf8', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['TYPE', 'START', 'END',
                     'GUID1', 'GUID2', 'PROFILE1', 'PROFILE2'])
    for connection in connections:
        part1 = connection.part1
        part2 = connection.part2
        writer.writerow([connection.connection_type, connection.connection_start, connection.connection_end,
                         part1.guid, part2.guid, part1.profile, part2.profile])


print(tree)

# print(len(data_tree))
