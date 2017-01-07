from Bio.PDB.Vector import calc_dihedral
from pandas import *

## ex2
def calc_phi(res0, res1):
    C_previous = res0["C"]
    N = res1["N"]
    CA = res1["CA"]
    C = res1["C"]

    atoms = [C_previous, N, CA, C] 
    vectors = [i.get_vector() for i in atoms]
    angle = calc_dihedral(*vectors)
    return angle

def calc_psi(res0, res1):
    N = res0["N"]
    CA = res0["CA"]
    C = res0["C"]
    N_next = res1["N"]

    atoms = [N, C, CA, N_next] 
    vectors = [i.get_vector() for i in atoms]
    angle = calc_dihedral(*vectors)
    return angle

def check_heteroatom(atom):
    '''Returns True if supplied atom object represents a heteroatom.
    Atoms are considered HA if their heteroatom flag contains either "H_" or "W"'''

    atom_id = atom.get_id()
    result = atom_id[0][0:2] == "H_" or atom_id[0] == "W"
    return result

def compute_angles(chain):
    '''Computes phi and psi angles for every pair of residues along the supplied chain'''
    g = chain.get_residues()
    
    psi_angles = []
    phi_angles = []
    
    res0 = next(g)
    
    while g:
        ## Extract residues
        res1 = next(g, False)
        
        # check generator was not exhausted    
        if not res1:
            break
        
        # check res1 is not an heteroatom (and hence won't error when accessing C or N atoms)
        if check_heteroatom(res1):
            # if it's a heteroatom, switch to the next one
            continue
    
        ## Compute angles
        phi = calc_phi(res0, res1)
        psi = calc_psi(res0, res1)
    
        # Store angles
        psi_angles.append(psi)
        phi_angles.append(phi)
        
        # Prepare for next loop. res0 becomes res1
        # because res1 will be pushed forward
        res0 = res1
    
    return (psi_angles, phi_angles)
    
def table_to_df(table, header):

    df = DataFrame(table)
    df = df.transpose()
    df.columns = header
    return df
