graph = {'A': ['B', 'C'],
         'C': ['D'],
         'B': ['C', 'D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}

def find_path(graph, start, end, path=[]):
	path = path + [start]
	if start == end:
		return path
	if not graph.has_keys(start):
		return None
	for node in graph[start]:
		new_path = find_path(graph, node, end, path)	
        return None

print find_path(graph, 'A', 'D')
