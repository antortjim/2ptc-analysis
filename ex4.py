from modules import Bio
from modules import np


def center_of_mass(chain):

    coordinates = []
    weights = []
    for res in chain:
        for atom in res:
            coords = atom.get_coord() 
            mass = atom.mass
            coordinates.append(coords)
            weights.append(mass)


    coordinates = np.array(coordinates)

    result = np.average(coordinates, weights = weights, axis = 0)    

    return result
