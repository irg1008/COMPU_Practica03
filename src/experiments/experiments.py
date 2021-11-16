from typing import List, Tuple
import sys
sys.path.append("..")
sys.path.append("../sol")
from sol.main import execute


FloatList = List[float]
Experiment = Tuple[str, FloatList]


def create_experiments():
    names = (
        "Max_Tree_Height",
        "Max_Subtree_Height",
        "Max_Mutation_Subtree_Height",
        "Crossover_Probability",
        "Mutation_Probability"
    )

    MTH: FloatList = [2, 6, 8, 10]
    MSH: FloatList = [1, 2, 4, 5]
    MMSH: FloatList = [1, 2, 4, 5]
    CXPB: FloatList = [0.5, 0.6, 0.8, 0.9]
    MUTPB: FloatList = [0.1, 0.15, 0.25, 0.3]

    base: FloatList = [5, 3, 3, 0.7, 0.2]
    comb: List[FloatList] = [MTH, MSH, MMSH, CXPB, MUTPB]
    
    experiments: List[Experiment] = [("Base", base)]
    
    for i, (name, element_to_test) in enumerate(zip(names, comb)):
        for value in element_to_test:
            updated_base: FloatList = list(base)
            updated_base[i] = value
            experiments.append((name, updated_base))
            
    return experiments
            

def test_experiemnts(experiments):
    for name, value in experiments:
        MTH, MSH, MMSH, CXPB, MUTPB = value
        str_value = "_".join(str(v) for v in value)
        exp_name = f"{name}_{str_value}"
        
        execute(CXPB=CXPB, MUTPB=MUTPB,
                use_binary=True, exp_name=exp_name,
                max_tree_height=MTH, max_subtree_height=MSH, max_mutated_subtree_height=MMSH)
        

def main():
    experiments = create_experiments()
    test_experiemnts(experiments)
    
if __name__ == "__main__":
    main()
