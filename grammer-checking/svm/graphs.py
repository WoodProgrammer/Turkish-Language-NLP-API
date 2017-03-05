import os
system_connection_graphs={
"a1":["a4","a5"],
"a2":["a3","a4"],
"a3":["a2","a5"],
"a4":["a2","a3","a5"],
"a5":["a1","a3","a4"],
"a6":[]
}

def show_device_comunucation_graph(graphs):
    for i in graphs:
        for t in graphs[i]:
            print i+""+t

    print "-----"
def find_alone_node(graphs):
    alone_node=[]
    for node in graphs:
        if not graphs[node]:
            alone_node.append(node)
    return alone_node

#def find_way(graphs,start_node,target_node):
#    for node in graphs:



#    return

show_device_comunucation_graph(system_connection_graphs)
#not_connected_device(system_connection_graphs)
