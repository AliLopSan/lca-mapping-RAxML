import os
import sys
import pytest

# Add src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))

# Import the function to test
from lca_map_builder import build_lca_map
from tools import *

# Paths to the input data
data_dir = os.path.join(os.path.dirname(__file__), "../data")
species_tree_path = os.path.join(data_dir, "example_species_tree.nhx")
gene_tree_path = os.path.join(data_dir, "example_gene_tree_RAxML.nhx")
    
# Call the build_lca_map function and validate its output
G,result = build_lca_map(species_tree_path,gene_tree_path)

print("\n Reconciled gene tree newick: ",G.to_newick())
print("\n Reconciled gene tree in PARLE format:\n",to_renconc_string(G))
print("\n Reconciled gene tree in RF format:\n",to_renconc_string(G,"RF"))
print("\n Duplication cost of reconciled tree: ",calculate_dcost(G))

LDR = get_least_duplication_resolved_tree(G)
print("\n LDR gene tree newick: ",LDR.to_newick())
print("\n LDR gene tree in PARLE format:\n",to_renconc_string(LDR))
print("\n LDR gene tree in RF format:\n",to_renconc_string(LDR,"RF"))
print("\n Duplication cost of reconciled tree: ",calculate_dcost(LDR))

