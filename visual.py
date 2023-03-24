import networkx as nx
import matplotlib.pyplot as plt


def show(weighted_edge, start, end):
    g = nx.DiGraph()
    g.add_weighted_edges_from(weighted_edge)
    # расчет кратчайших путей для ВСЕХ пар вершин
    predecessors, _ = nx.floyd_warshall_predecessor_and_distance(g)
    # кратчайший путь от вершины [s] к вершине [v]
    shortest_path_s_v = nx.reconstruct_path(start, end, predecessors)
    # список ребер кратчайшего пути
    edges = [(a, b) for a, b in zip(shortest_path_s_v, shortest_path_s_v[1:])]
    # список всех весов ребер
    weights = nx.get_edge_attributes(g, 'weight')
    # позиции вершин для визуализации графа
    # pos = nx.spring_layout(G)
    pos = nx.random_layout(g)
    # рисуем граф
    nx.draw_networkx(g, pos=pos)
    # рисуем веса ребер
    nx.draw_networkx_edge_labels(g, pos, edge_labels=weights)
    # рисуем кратчайший путь: [s] -> [v]
    nx.draw_networkx_edges(g, pos=pos, edgelist=edges, edge_color="r", width=3.5)
    # заголовок графика
    title = "Shortest path between [{}] and [{}]: {}" \
        .format(start, end, " -> ".join(shortest_path_s_v))
    plt.title(title)
    plt.show()

# show(weighted_edges='', start='s', end='x')
