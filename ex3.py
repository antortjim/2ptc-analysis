# Taken (and slightly modified) from
# http://stackoverflow.com/questions/11685716/how-to-extract-chains-from-a-pdb-file
# All credit to user David Cain

from modules import PDB
from modules import os


class ChainSplitter:
    # The object will be initialized with 2 methods inherited from PDB module
    # self.parser will call the PDB.PDBParser() method
    # self.writer will call the PDB.PDBIO() method
    # Plus, the object will have an attribute called out_dir (output directory)
    def __init__(self, out_dir = None):
        """ Create parsing and writing objects, specify output directory. """
        self.parser = PDB.PDBParser()
        self.writer = PDB.PDBIO()
        # Default out_dir is folder current_directory/chain_PDBs
        if out_dir is None:
            out_dir = os.path.join(os.getcwd(), "chain_PDBs")
        self.out_dir = out_dir

    def make_pdb(self, pdb_path, chain_letters, overwrite = False, struct = None):
        """ Create a new PDB file containing only the specified chains.

        Returns the path to the created file.

        :param pdb_path: full path to the crystal structure (generated by retrieve_pdb_file())
        :param chain_letters: iterable of chain characters (case insensitive)
        :param overwrite: write over the output file if it exists
        """
        # Make them all upper case so that the script is case insensitive to user input
        chain_letters = [chain.upper() for chain in chain_letters]

        # Input/output files
        (pdb_dir, pdb_fn) = os.path.split(pdb_path)

        # The filename generated by retrieve_pdb_file is not just the id
        # pdbXYYY.ent
        # The id can be accessed by [3:7]
        pdb_id = pdb_fn[3:7]

        out_name = "pdb%s_%s.ent" % (pdb_id, "".join(chain_letters))
        out_path = os.path.join(self.out_dir, out_name)
        print "OUT PATH:",out_path
        plural = "s" if (len(chain_letters) > 1) else ""  # for printing

        # Skip PDB generation if the file already exists
        if (not overwrite) and (os.path.isfile(out_path)):
            print("Chain%s %s of '%s' already extracted to '%s'." %
                    (plural, ", ".join(chain_letters), pdb_id, out_name))
            return out_path

        print("Extracting chain%s %s from %s..." % (plural,
                ", ".join(chain_letters), pdb_fn))

        # Get structure, write new file with only given chains
        # By default, the structure's ID will be the entry name
        # The struct variable will store a structure object following SMCRA
        # that is, is iterable by Model Chain Residue and Atom
        if struct is None:
            struct = self.parser.get_structure(pdb_id, pdb_path)

        # Set this structure as the structure which parsing functions will work with
        self.writer.set_structure(struct)
        
        # Save the structure generated by selecting the chains in the chain_letters list
        # to out_path
        self.writer.save(out_path, select = SelectChains(chain_letters))

        return out_path

## The argument to select in self.writer.save() has to be
## an object inheriting from class PDB.Select with specific
## accept (atom/chain/residue/model that return True when the
## desired atom/chain... is passed to it
## All possibilities are tested but *only those that return True
## when passed to accept_X() are selected*
class SelectChains(PDB.Select):
    """ Only accept the specified chains when saving. """
    def __init__(self, chain_letters):
        self.chain_letters = chain_letters

    def accept_chain(self, chain):
        ## Only chains whose get_id() output matches any of the letters
        ## inside the chain_letters list (which was supplied in the
        ## initialization of the select object)
        ## will return True and thus will be selected
        return (chain.get_id() in self.chain_letters)


if __name__ == "__main__":
    """ Parses PDB id's desired chains, and creates new PDB structures. """
    import sys
    if not len(sys.argv) == 2:
        print "Usage: $ python %s 'pdb.txt'" % __file__
        sys.exit()

    pdb_textfn = sys.argv[1]

    pdbList = PDB.PDBList()
    splitter = ChainSplitter("/home/antortjim/MEGA/Master/SB/week4/code/chain_pdbs")  # Change me.

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
