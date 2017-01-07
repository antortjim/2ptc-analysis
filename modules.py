# Import required modules
import Bio
import Bio.PDB as PDB
from Bio.PDB.PDBParser import PDBParser
from Bio.PDB.Vector import calc_dihedral
import pandas as pd
import os
import numpy as np

DataFrame = pd.DataFrame
