from pdbfixer import PDBFixer
from openmm.app import PDBFile

# Load the fixed PDB
print("Loading 4OBE_fixed.pdb...")
fixer = PDBFixer(filename='4OBE_fixed.pdb')

# 1. Search for missing residues (entire loops/backbone gaps)
fixer.findMissingResidues()
missing_residues = fixer.missingResidues

print("\n--- Structural Integrity Assessment ---")
if not missing_residues:
    print("Backbone Status: COMPLETE. No missing loops or internal residues detected.")
else:
    print(f"Backbone Status: INCOMPLETE. Found {len(missing_residues)} missing residue gaps.")
    for key, value in missing_residues.items():
        print(f"  - Gap in Chain {key[0]} at position {key[1]}: {value}")

# 2. Search for missing heavy atoms in existing residues (side-chains)
fixer.findMissingAtoms()
missing_atoms = fixer.missingAtoms

if not missing_atoms:
    print("Side-chain Status: All heavy atoms are present.")
else:
    print(f"Side-chain Status: Missing heavy atoms detected in {len(missing_atoms)} residues.")
    for residue, atoms in missing_atoms.items():
        atom_names = [atom.name for atom in atoms]
        print(f"  - Residue {residue.name}{residue.id} (Chain {residue.chain.id}) is missing: {', '.join(atom_names)}")

# 3. Perform the repair
print("\nExecuting repair...")
fixer.addMissingAtoms()

# 4. Save the repaired structure
with open('4OBE_repaired.pdb', 'w') as f:
    PDBFile.writeFile(fixer.topology, fixer.positions, f)

print("\nSuccess: '4OBE_repaired.pdb' has been generated with all missing heavy atoms rebuilt.")