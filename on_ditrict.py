def diss(name):
    file = open(name)

    graph = []
    Graph = []
    s = file.readline()
    edges_list = list('a b c d e f g k m n o p 1 2 3 4 5 6 7 8 9 10'.split())

    while s != '':
        graph.append(list(map(float, s.replace(',', '.').split())))
        s = file.readline()
    for i in range(len(edges_list)):
        for j in range(len(edges_list)):
            if i != j and graph[i][j] != 0:
                Graph.append((edges_list[i], edges_list[j], graph[i][j]))
    return Graph, edges_list, len(graph)

