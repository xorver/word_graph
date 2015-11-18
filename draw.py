import os, sys
import graphviz as gv
import subprocess
import plp

def get_base_word(word):
    try:
        id = plp.plp_rec(word.encode('UTF-8'))
        return plp.plp_bform(id[0])
    except:
        return "undefined"

main_word_dir = sys.argv[1]
main_word = os.path.basename(main_word_dir)
plp.plp_init()

graph = gv.Digraph(format='svg')
graph.node(main_word, center="true")
weight = dict()

for file_name in os.listdir(main_word_dir):
    secondary_word = file_name[:-4]
    graph.node(secondary_word)
    graph.edge(main_word, secondary_word)
    with open(os.path.join(main_word_dir, file_name), encoding='utf-8') as file:
        for line in file:
            [count, tertiary_word] = (line[:-1] if line.endswith('\n') else line).split(',')
            graph.node(tertiary_word)
            base_secondary_word = get_base_word(secondary_word)
            base_tertiary_word = get_base_word(tertiary_word)
            weight[(base_secondary_word, base_tertiary_word)] = float(count)/900
            graph.edge(secondary_word, tertiary_word, len=str(5*(1-weight[(base_secondary_word, base_tertiary_word)])))

# graph.render('graph')
# subprocess.check_output(['neato', '-Tpdf', 'graph', '-o', 'graph.pdf'])

with open('sentences', encoding='utf-8') as file:
    for line in file:
        for word1 in line.split():
            for word2 in line.split():
                w = weight.get((get_base_word(word1), get_base_word(word2)))
                print(line.encode('utf-8'))
                if w and get_base_word(word1) != 'undefined' and get_base_word(word2) != 'undefined':
                    print(get_base_word(word1).encode('utf-8'))
                    print(get_base_word(word2).encode('utf-8'))
                    print(str(w))
