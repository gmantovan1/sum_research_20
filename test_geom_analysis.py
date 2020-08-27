import geom_analysis as ga
import pytest

def test_calculate_distance():
	coord1=[0, 0, 0]
	coord2=[1, 0, 0]
	expected=1.0
	observed=ga.calculate_distance(coord1, coord2)
	assert observed == expected

def test_bond_check():
	bond_distance=1.2
	expected=True
	observed=ga.bond_check(bond_distance)
	assert observed == expected


def test_bond_check_true():
    bond_distance = 1.2
    expected = True
    observed = ga.bond_check(bond_distance)
    assert observed == expected

def test_bond_check_false():
    bond_distance = 2.0
    expected = False
    observed = ga.bond_check(bond_distance)
    assert observed == expected

def test_bond_check_0():
    bond_distance = 0
    expected = False
    observed = ga.bond_check(bond_distance)
    assert observed == expected

def test_bond_check_1_5():
    bond_distance = 1.5
    expected = True
    observed = ga.bond_check(bond_distance)
    assert observed == expected


#Raising Errors
def bond_check(atom_distance, minimum_length=0, maximum_length=1.5):
    
    if atom_distance < 0:
        raise ValueError(F'Invalid atom distance {atom_distance}. Distance can not be less than 0!')

    if atom_distance > minimum_length and atom_distance <= maximum_length:
        return True
    else:
        return False

def test_bond_check_negative():
    distance = -1
    expected = False
    calculated = ga.bond_check(distance)
    assert expected == calculated

def test_bond_check_negative():
    distance = -1
    expected = False
    with pytest.raises(ValueError)
        calculated = ga.bond_check(distance)


#Write an exception into your open_xyz function where you check the file extension of the file name. Raise a ValueError if the file extension is not .xyz. Write a test to go with your new value error.
def open_xyz(filename):
    fpath, extension = os.path.splitext(filename)

    if extension.lower() != '.xyz':
        raise ValueError("Incorrect file type! File must be type xyz")

    xyz_file = numpy.genfromtxt(fname=filename, skip_header=2, dtype='unicode')
    symbols = xyz_file[:,0]
    coord = (xyz_file[:,1:])
    coord = coord.astype(numpy.float)
    return symbols, coord

with pytest.raises(ValueError):
    ga.open_xyz(fname)