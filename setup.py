from setuptools import setup, find_packages

setup(
    name="lca-map-RAxML",
    version="0.1.0",
    description="A package to build LCA maps for RAxML gene trees.",
    author="Alitzel Lopez Sanchez",
    author_email="alitzel.lopez.sanchez@usherbrooke.com",
    url="https://github.com/AliLopSan/lca-mapping-RAxML",
    packages=find_packages(),
    install_requires=[
        "tralda","asymmetree"  # Example dependency for Newick parsing
    ],
    python_requires=">=3.7",
)
