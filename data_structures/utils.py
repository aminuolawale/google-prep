from random import sample
from typing import List

def generate_random_array(size:int) -> List[int]:
    return sample(range(-1000, 1000), size)