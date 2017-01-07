import Bio
import Bio.PDB as PDB
from Bio.PDB.PDBParser import PDBParser
from Bio.PDB import PPBuilder
from Bio.PDB.Vector import calc_dihedral
from Pandas import *
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
pairs, pairs_id = analyze_residues(is_close, 3.5, 2)

print pairs
print len(pairs)
print pairs_id


# ex2
e_psi, e_phi = compute_angles(e)
i_psi, i_phi = compute_angles(i)

e_pairs = range(1, len(e_psi) + 1)
i_pairs = range(1, len(i_psi) + 1)

pairs = e.tolist() * 2 + i.tolist() * 2

table = [pairs,  ["E"] * len(e_psi + e_phi) + ["I"] * len(i_psi + i_phi), ["psi"] * len(e_psi) + ["phi"] * len(e_phi) + ["psi"] * len(i_psi) + ["phi"] * len(i_phi), e_psi + e_phi + i_psi + i_phi]
header = ['pair_id', 'chain', 'angle', 'value']


## Generate Pandas DataFrame and export to csv for R visualization
df = table_to_df(table, header)
df.to_csv("2ptc.csv")

# ex3
