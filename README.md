# LCA-map: A tool for phylogenetic Reconciliation
## Overview
The **reconciliation problem** is a challenge in evolutionary biology. It involves mapping gene trees onto species trees to infer the evolutionary history of gene families, including events such as **duplications**, **losses** and **horizontal gene transfers**( also known as HGTs or LGTs). Accurate reconciliation provides crucial insights into evolutionary processes and relationships.

**LCA-map** is a [tralda](https://github.com/david-schaller/tralda)-based python package designed to simplify reconciliation tasks by using the simplest method of reconciliation:
- It maps each node of a given gene tree $G$ to the **lowest common ancestor (LCA)** of its leaves.
- It minimizes the duplication $+$ loss cost in linear time.
- The resulting *label* of a node $v$ is the lca-mapping of $v$.

---

## Features
- Efficient computation of LCA mappings between gene trees and species trees.
- Input support for Newick and .nhx tree formats.
- Tools for validating and analyzing phylogenetic trees.
- Easy-to-use and modular structure for integration into larger workflows.

---

## Installation
Clone the repository:
``bash
git clone https:https://github.com/AliLopSan/lcamap
cd lca-map
``
Install dependencies:

``bash
pip- install -r requirements.txt
``
---
## Usage
### Main function: `build_lca_map`
The core function of the package is `build_lca_map`, which takes two trees as input: a **species tree** and a **gene tree**.

**Input requirements:**
1. **Species Tree:** A tree in `.nhx` format, where each leaf corresponds to a species.
2. **Gene Tree:** A tree in NHX format, where each leaf follows the naming conventions: `fam<n>gene<n>spec<n>`.
