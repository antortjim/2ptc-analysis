# ex1
#Find all residue pairs in both proteins that have
#more than 2 atoms closer then 3.5 A from each
#other

# Define function checking whether or not
# 2 given residues are close
# Close criteria: > n atoms closer than distance (angstroms)
# If criteria is fulfilled, returns True
def is_close(res1, res2, distance, n):
    '''Returns True if res1 and res2 have > n atoms closer than distance in Angstroms'''
    close_atoms = 0
    for atom1 in res1:
        for atom2 in res2:
            if atom1 - atom2 < distance:
                close_atoms += 1

            if close_atoms == n + 1:
                return True


def analyze_residues(fun, *args):
    '''Analyze pairs of residues and output only those 
       that return True when passed to function fun with arguments **args'''


    # Initialize lists of res names and res id
    pairs = []
    pairs_id = []
    
    
    # Iterate over residues on enzyme
    for res1 in e.get_residues():
        # Iterate over residues on inhibitor 
        for res2 in i.get_residues():
            # Compare atoms on both residues and count how many are closer than 3.5
            if fun(res1, res2, args):
               # Save names
               name1 = res1.get_resname()
               name2 = res2.get_resname()
               pairs.append((name1, name2))
               
               # Save ids 
               res1id = res1.get_id()[1] 
               res2id = res2.get_id()[1]
               pairs_id.append((res1id, res2id))

    return pairs, pairs_id        
