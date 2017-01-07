from Bio import PDB
parser = PDB.PDBParser()
import numpy as np

pdb_id = "2ptc"

# 1. Retrieve 2ptc file
pdbList = PDB.PDBList()
pdb_path = pdbList.retrieve_pdb_file(pdb_id)

# 2.
structure = parser.get_structure(pdb_id, pdb_path)
res = structure[0]["E"][20]
C = res['C']
print C

coordinates = C.get_coord()

print coordinates

# 3.
res_coordinates = np.array([atom.get_coord() for atom in res])
print res_coordinates

centroid = np.mean(res_coordinates, axis = 0)
print centroid

#4. Move the code from part 3 to a function called centroid that takes a residue as a parameter and returns the coordinates (not printing them).

def centroid(res):

    coordinates = np.array([atom.get_coord() for atom in res])
    centroid_coord = np.mean(coordinates, axis = 0)

    return centroid_coord


#5. Print out the 3D coordinates of the C-alpha atom of the amino acid with PDB residue number 13 in chain I.
res = structure[0]["I"][13]
print res["C"].get_coord()

#6. Calculate the geometric center (centroid) of the above amino acid and print it out.
print centroid(res)
