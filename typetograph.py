# 
# typetograph.py - Convert a Python data type into a 'graph'
# 
# Note: Currently, the only supported representation
#       of a graph is an 'edge list'
#

# external modules

import json



def dictToGraph(dict_value, depth):

    res = []

    for key, value in dict_value.items():

        if 'dict' in str(type(value)):

            for sub_key in value.keys():

                res.extend( [(str(depth) + "_" + str(key), str(depth+1) + "_" + str(sub_key))] )

            recurr_res = dictToGraph(value, depth+1)

            res.extend(recurr_res)

        elif 'list' in str(type(value)):

            dictFromList = {}

            for i in range(len(value)):

                res.extend( [(str(depth) + "_" + str(key), str(depth+1) + "_" + str(i))] )

                dictFromList[i] = value[i]

            recurr_res = dictToGraph(dictFromList, depth+1)

            res.extend(recurr_res)

        else:

            res.extend( [(str(depth) + "_" + str(key), str(depth) + "_" + str(value))] )

    return res



def getAdjTable(json_dict):

    edge_list = dictToGraph(json_dict, 0)

    res = {}

    for (v, n) in edge_list:

        res[v] = []

    for (v, n) in edge_list:

        res[v].append(n)

    return res



# exeperimental...

def json_file_to_graph(json_filename):

    json_file = open(json_filename)

    res = ""

    for line in json_file:

        res += line.strip()

    json_dict = json.loads(res)

    json_adj_table = getAdjTable(json_dict)

    #return json_adj_table

    out_list = []

    for key in json_adj_table.keys():

        out_list.append(str(key) + ": " + str(json_adj_table[key]))

    out_list.sort()

    return out_list

    #print json_dict.keys()



def json_file_to_dict(json_filename):

    json_file = open(json_filename)

    res = ""

    for line in json_file:

        res += line.strip()

    json_dict = json.loads(res)

    return json_dict



def DFS(curr_state, path_prefix, visited):

    if "dict" in str(type(curr_state)):

        # given state is a 'directory' object

        for k in curr_state.keys():

            DFS(curr_state[k], path_prefix + "/" + str(k), visited)

        return

    elif "list" in str(type(curr_state)):

        # given state is a 'directory' object

        for i in range(0, len(curr_state)):

            DFS(curr_state[i], path_prefix + "/" + str(i), visited)

        return

    else:

        # given state is a 'file' object

        visited.append(path_prefix + "/" + str(curr_state))

        return


def findDailyProgrammer(json_filename):

    # apply DFS to the given json object

    json_dict = json_file_to_dict(json_filename)

    path_prefix = ""

    visited = []

    DFS(json_dict, path_prefix, visited)

    res = ""

    # find raw path to 'dailyprogrammer' string

    for path in visited:

        if 'dailyprogrammer' in path:

            res = path
            
            break

    # reformat path string to conform to requested output format

    res = res[res.find("/")+1:res.find('/dailyprogrammer')]

    final = ""

    for char in res:

        if char == "/":

            final += " -> "

        else:

            final += char

    return final
