import os
import sys
import pytest

# Add src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))

# Import the function to test
from lca_map_builder import build_lca_map

def test_build_lca_map():
    # Paths to the input data
    data_dir = os.path.join(os.path.dirname(__file__), "../data")
    species_tree_path = os.path.join(data_dir, "example_species_tree.nhx")
    gene_tree_path = os.path.join(data_dir, "example_gene_tree_RAxML.nhx")
    
    # Call the build_lca_map function and validate its output
    try:
        G,result = build_lca_map(species_tree_path,gene_tree_path)
        print("LCA Map Built Successfully:", result)
        assert result is not None  # Ensure the result is not None
        # Add more meaningful assertions based on your function's expected output
    except Exception as e:
        print(f"Test failed with error: {e}")
        assert False  # Fail the test if an exception is raised


test_build_lca_map()
