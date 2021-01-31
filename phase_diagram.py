#Draws phase diagram for chemical system
#!/usr/bin/env python

from pymatgen.ext.matproj import MPRester
from pymatgen.analysis.phase_diagram import *
from pymatgen.analysis.phase_diagram import PDPlotter

#This initializes the REST adaptor. Put your own API key in.
a = MPRester("API_ID") #Go to materialsproject.org to create account and get API key

#Entries are the basic unit for thermodynamic and other analyses in pymatgen.
#This gets all entries belonging to the Ca-C-O system.
# entries = a.get_entries_in_chemsys(['Ca', 'C', 'O'])
entries = a.get_entries_in_chemsys(['Li', 'Mn', 'O'])

#With entries, you can do many sophisticated analyses, like creating phase diagrams.
pd = PhaseDiagram(entries)
plotter = PDPlotter(pd)
plotter.show() 
