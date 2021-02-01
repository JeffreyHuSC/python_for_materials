#with corrections from Ong's code to make it work with current pymatgen.

#!/usr/bin/env python

from pymatgen.ext.matproj import MPRester
from pymatgen import Composition
from pymatgen.entries.computed_entries import ComputedEntry
# from pymatgen.core.physical_constants import EV_PER_ATOM_TO_KJ_PER_MOL
from pymatgen.analysis.reaction_calculator import ComputedReaction

EV_PER_ATOM_TO_KJ_PER_MOL=96.49 

#This initializes the REST adaptor. Put your own API key in.
a = MPRester("cKbULdZ0J9ltE4Sa")

#This gets all entries belonging to the Ca-C-O system.
all_entries = a.get_entries_in_chemsys(['Ca', 'C', 'O'])

#This method simply gets the lowest energy entry for all entry with the same composition.
def get_most_stable_entry(formula):
    relevant_entries = [entry for entry in all_entries if entry.composition.reduced_formula == Composition(formula).reduced_formula]
    relevant_entries = sorted(relevant_entries, key=lambda e: e.energy_per_atom)
    return relevant_entries[0]

CaO = get_most_stable_entry("CaO")
CO2 = get_most_stable_entry("CO2")
CaCO3 = get_most_stable_entry("CaCO3")

reaction = ComputedReaction([CaO, CO2], [CaCO3])

print("Caculated")
print(reaction)
print("Reaction energy = {:.2f}".format(reaction.calculated_reaction_energy * EV_PER_ATOM_TO_KJ_PER_MOL)) #Conversion needed since our computed energies are in eV.
print()

# The following portions demonstrate how to get the experimental values as well.
exp_CaO = a.get_exp_entry("CaO")
exp_CaCO3 = a.get_exp_entry("CaCO3")

#Unfortunately, the Materials Project database does not have gas phase experimental entries. This is the value from NIST. We manually create the entry.
#Exp entries should be in kJ/mol.
exp_CO2 = ComputedEntry("CO2", -393.51)

exp_reaction = ComputedReaction([exp_CaO, exp_CO2], [exp_CaCO3])

print("Experimental")
print(exp_reaction)
print("Reaction energy = {}".format(exp_reaction.calculated_reaction_energy))
