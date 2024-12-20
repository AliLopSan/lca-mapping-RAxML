from setuptools import setup, find_packages

setup(
    name="lcamap",
    version="0.1.0",
    description="A package to build LCA maps for RAxML gene trees.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Alitzel Lopez Sanchez",
    author_email="alitzel.lopez.sanchez@usherbrooke.com",
    url="https://github.com/AliLopSan/lca-mapping-RAxML",
    packages=find_packages(where="src"),
    package_dir={"":"src"},
    classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT license",
    "Operating System :: OS Independent",]
    install_requires=[
        "tralda","asymmetree","pandas"
    ],
    python_requires=">=3.7",
)
