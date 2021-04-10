from rdkit.Chem.Lipinski import NumRotatableBonds
from reinvent_scoring.scoring.component_parameters import ComponentParameters
from reinvent_scoring.scoring.score_components.physchem.base_physchem_component import BasePhysChemComponent


class RotatableBonds(BasePhysChemComponent):
    def __init__(self, parameters: ComponentParameters):
        super().__init__(parameters)

    def _calculate_phys_chem_property(self, mol):
        return NumRotatableBonds(mol)
