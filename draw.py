import os, sys
import graphviz as gv
import subprocess

main_word_dir = sys.argv[1]
main_word = os.path.basename(main_word_dir)

graph = gv.Digraph(format='svg')
graph.node(main_word, center="true")

for file_name in os.listdir(main_word_dir):
    secondary_word = file_name[:-4]
    graph.node(secondary_word)
    graph.edge(main_word, secondary_word)
    with open(os.path.join(main_word_dir, file_name), encoding='utf-8') as file:
        for line in file:
            [count, tertiary_word] = (line[:-1] if line.endswith('\n') else line).split(',')
            graph.node(tertiary_word)
            weight = float(count)/900
            graph.edge(secondary_word, tertiary_word, len=str(5*(1-weight)))

graph.render('graph')
subprocess.check_output(['neato', '-Tpdf', 'graph', '-o', 'graph.pdf'])
