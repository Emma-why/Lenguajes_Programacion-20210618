import hashlib
import pprint
from typing import List, Tuple

def process_data(names: List[str], numbers: List[int]) -> List[Tuple[str, int, str]]:

    try:
        if len(names) != len(numbers):
            raise ValueError("The lengths of names and numbers must be the same.")
        result = [
            (name, num**2, hashlib.sha1(f"{name}{num**2}".encode()).hexdigest())
            for name, num in zip(names, numbers)
            if len(name) > 5
        ]
        
        return result

    except ValueError as ve:
        print(f"ValueError: {ve}")
        raise  
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise  
names = ["Juan", "Mariana", "Luis", "Carmen", "Pedro", "Santiago"]
numbers = [23, 45, 12, 8, 19, 30]

try:
    hashes = process_data(names, numbers)
    pprint.pprint(hashes)
except ValueError:
    print("There was an error with the input data.")
except Exception as e:
    print(f"An error occurred: {e}")
