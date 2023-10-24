from typing import Tuple

UI = False

def main():
    formula_1, formula_2 = get_formulae()

    chemical_set_1 = get_chemicals_in_formula(formula_1)
    chemical_set_2 = get_chemicals_in_formula(formula_2)

    state_common_chemicals(chemical_set_1, chemical_set_2)

def get_formulae(user_interface: bool = UI) -> Tuple[str]:
    
    formula_1 = input()
    formula_2 = input()
    return formula_1, formula_2

def get_chemicals_in_formula(chemical_formula: str) -> set:
    
    components = set()
    i = 0
    while i < len(chemical_formula):
        element = chemical_formula[i]
        i += 1
        while i < len(chemical_formula) and chemical_formula[i].islower():
            element += chemical_formula[i]
            i += 1
        count = 1
        while i < len(chemical_formula) and chemical_formula[i].isdigit():
            count = count * 10 + int(chemical_formula[i])
            i += 1
        components.add(element)
    return components

def state_common_chemicals(chemical_set_1: set, chemical_set_2: set) -> None:
    common_chemicals = sorted(chemical_set_1.intersection(chemical_set_2))
    print(", ".join(common_chemicals))

if __name__ == "__main__":
    main()
