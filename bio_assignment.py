# Biopython Assignment
# Student: Antonio Ortega Jimenez
# Structural Bioinformatics
# University of Copenhagen
# 07-01-2017

# Import modules
from Bio import PDB
parser = PDB.PDBParser()
import numpy as np

# Define class to format decimal digits
class prettyfloat(float):
    def __repr__(self):
        return "%0.4f" % self

# PDB key
pdb_id = "2ptc"


# 1. Retrieve pdb file under 2ptc key
pdbList = PDB.PDBList()
pdb_path = pdbList.retrieve_pdb_file(pdb_id)

# Get structure from pdb file
structure = parser.get_structure(pdb_id, pdb_path)


# 2. Print out the 3D coordinates of the C-alpha atom of the amino acid with PDB residue number 20 in chain E
# Define the corresponding residue
res = structure[0]["E"][20]

# Extract the coordinates of the CA atom in that residue
coordinates = res['CA'].get_coord()


# 3. Calculate the geometric center (centroid) of the above amino acid and print it out
# Generate a numpy array of size n x 3
   # n = number of atoms in residue
   # columns represent x y and z axis
coordinates = np.array([atom.get_coord() for atom in res])

# Get the centroid by computing the mean of all the coordinates
centroid = np.mean(coordinates, axis = 0)


#4. Move the code from part 3 to a function called centroid that takes a residue as a parameter and returns the coordinates (not printing them).
def centroid(res):

    coordinates = np.array([atom.get_coord() for atom in res])
    centroid_coord = np.mean(coordinates, axis = 0)

    return centroid_coord


#5. Print out the 3D coordinates of the C-alpha atom of the amino acid with PDB residue number 13 in chain I.
# Define the corresponding residue
res = structure[0]["I"][13]

# Formatted print of the coordinates of the CA atom in that residue
print map(prettyfloat, res["CA"].get_coord())

#6. Calculate the geometric center (centroid) of the above amino acid and print it out.
# Formatted print of the coordinates of that residues' centroid,
# as computed with the centroid() function
print map(prettyfloat, centroid(res))
