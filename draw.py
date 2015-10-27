import os, sys
import graphviz as gv

main_word_dir = sys.argv[1]
main_word = os.path.basename(main_word_dir)

graph = gv.Digraph(format='svg')
graph.node(main_word)

for file_name in os.listdir(main_word_dir):
    secondary_word = file_name[:-4]
    graph.node(secondary_word)
    graph.edge(main_word, secondary_word)
    with open(os.path.join(main_word_dir, file_name), encoding='utf-8') as file:
        for line in file:
            [count, tertiary_word] = line[:-1].split(',')
            graph.node(tertiary_word)
            graph.edge(secondary_word, tertiary_word, label=count)

graph.render('graph')
