import os
import networkx as nx
import matplotlib.pyplot as plt
import warnings
import operator

print(os.listdir('.'))

fb = nx.read_edgelist('./facebook-combined.txt', create_using = nx.Graph(), nodetype = int)

print(nx.info(fb))

# for making the graph
# pos = nx.spring_layout(fb)
# warnings.filterwarnings('ignore')
# plt.style.use('fivethirtyeight')
# plt.rcParams['figure.figsize'] = (20, 15)
# plt.axis('off')
# nx.draw_networkx(fb, pos, with_labels = False, node_size = 35)
# plt.show()

# for finding page rank of each user
pageranks = nx.pagerank(fb)
print(pageranks)

# for printing the sorted page rank
sorted_pagerank = sorted(pageranks.items(), key=operator.itemgetter(1),reverse = True)
print(sorted_pagerank[:5])
