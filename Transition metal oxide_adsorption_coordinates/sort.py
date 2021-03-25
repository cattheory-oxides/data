from ase.build import sort
from ase.io import read,write

#re-order POSCAR elements
slab=read('POSCAR',format='vasp')
slab=sort(slab)
write('POSCAR',slab,format='vasp',direct=True)
