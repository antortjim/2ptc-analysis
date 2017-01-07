# Import exercise functions

from modules import PDB
from modules import np
from ex1 import *
from ex2 import *
from ex3 import *

filename = "2ptc.pdb"

# Create parser
parser = PDB.PDBParser()

# Get structure form file
structure = parser.get_structure("Trypsin", filename)

## Access chain enzyme and chain inhibitor
e = structure[0]["E"] 
i = structure[0]["I"]


# ex1
pairs, pairs_id = analyze_residues(e, i, is_close, 3.5, 2)
print pairs

# ex2
e_psi, e_phi = compute_angles(e)
i_psi, i_phi = compute_angles(i)

e_pairs = range(1, len(e_psi) + 1)
i_pairs = range(1, len(i_psi) + 1)


e = np.repeat(e_pairs, 2, axis = 0)
i = np.repeat(i_pairs, 2, axis = 0)

pairs = e.tolist() * 2 + i.tolist() * 2

table = [pairs,  ["E"] * len(e_psi + e_phi) + ["I"] * len(i_psi + i_phi), ["psi"] * len(e_psi) + ["phi"] * len(e_phi) + ["psi"] * len(i_psi) + ["phi"] * len(i_phi), e_psi + e_phi + i_psi + i_phi]
header = ['pair_id', 'chain', 'angle', 'value']


## Generate Pandas DataFrame and export to csv for R visualization
df = table_to_df(table, header)

df.to_csv("2ptc.csv")

# ex3
pdb_textfn = "./pdb.txt"

pdbList = PDB.PDBList()
splitter = ChainSplitter("./chain_pdbs")

with open(pdb_textfn) as pdb_textfile:
    # PDB_textfn contains several lines where everyline is a PDB id + chain id
    # For example
    #   2ptcE
    #   2ptcI
    #   XXXXY
    for line in pdb_textfile:
        # Select PDB ID
        pdb_id = line[:4].lower()
        # Select chain
        chain = line[4]
        pdb_path = pdbList.retrieve_pdb_file(pdb_id)

        # Pass pdb_path (pdb file path as returned by retrieving function)
        # and chain (parsed from pdb.txt input file) to make_pdb()
        splitter.make_pdb(pdb_path, chain)
