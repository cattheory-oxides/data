from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.io import write
#Example
a=4.0782
slab = fcc111('Au', size=(4,4,3), a=a, vacuum=6.0)
c = FixAtoms(mask=[x >2  for x in slab.get_tags()])
slab.set_constraint(c)
write('POSCAR',slab,format='vasp',direct=True)
