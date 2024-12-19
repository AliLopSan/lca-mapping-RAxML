import tralda

from itertools import combinations_with_replacement
from tralda.datastructures.Tree import Tree

#..........................................................
# Calculate reconciliation map and labels
#..........................................................
def build_lca_map(G,S):
    def _all_pairs_lca(children,lca_S):
        species = set()
        for child in children:
            species.add(child.reconc)
        comparisons = list(combinations_with_replacement(species, 2))
        if len(comparisons) == 1:
            return(lca_S(comparisons[0][0],comparisons[0][1]))
        else:
            test_pair = comparisons.pop()
            current_lca = lca_S(test_pair[0],test_pair[1])
            flag = True
            while flag == True:
                pair = comparisons.pop()
                test_lca = lca_S(pair[0],pair[1])
                if lca_S.ancestor_not_equal(test_lca, current_lca):
                    current_lca = test_lca
                if len(comparisons) == 0:
                    flag = False
            return(current_lca)
    def _assign_event_label(node):
        species = set()
        children = [u.label for u in node.children]
        for child in node.children:
            species.add(child.reconc)
        if node.reconc in species:
            node.event = 'D'
        else:
            node.event = 'S'
    lca_S = LCA(S)
    for v in G.postorder():
        if v.is_leaf():
            v.reconc = lca_S(v.reconc,v.reconc)
        else:
            v.reconc = _all_pairs_lca(v.children,lca_S)
            _assign_event_label(v)

    #check if all inner nodes have a label
    labels = ['D','S']
    for v in G.inner_nodes():
        if v.event not in labels:
            _assign_event_label(v)
