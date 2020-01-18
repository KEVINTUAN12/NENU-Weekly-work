'''
读取json文件,读取networkx图
'''
import time
import json
import networkx as nx
from networkx.readwrite import json_graph
import matplotlib
import matplotlib.pyplot as plt
import os
'''
filename = "Graph.json"
with open(filename, 'r') as load_f:
    dkw = json.load(load_f)
    print(dkw)'''

from networkx.readwrite import json_graph
def save_json(filename,graph):
    g = graph
    g_json = json_graph.node_link_data(g)
    json.dump(g_json,open(filename,'w'),indent=2)

def read_json_file(filename):
    with open(filename) as f:
        js_graph = json.load(f)
    return json_graph.node_link_graph(js_graph)
#print(read_json_file('dkw.json'))
#print(type(read_json_file('dkw.json')))

#plt.figure(dpi=300,figsize=(20,10))
#nx.draw(read_json_file("dkw.json"), with_labels=True,pos=nx.random_layout(read_json_file("dkw.json")),font_size=10,node_size=40,width=0.2,node_color = ('r'))
#plt.show()
#t1 = time.time()
#path = nx.shortest_path(read_json_file("dkw.json"),'FGA', 'PRRC2A')
#t2 =time.time()
#print(path)
#print(type(path))
#print(t2-t1)
