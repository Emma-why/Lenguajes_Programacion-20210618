import hashlib
import pprint
from typing import Tuple

def convert_temperature(value: float, scale: str) -> Tuple[float, str]:
    try:
        if scale not in ['C', 'F']:
            raise ValueError("Scale must be Celsius(C) or Fahrenheit(F).")
        if type(value) is not int:
            raise ValueError("the value is no a intenger or float")
        
        if scale == 'C':
            converted = (value * 9/5) + 32
        else:
            converted = (value - 32) * 5/9
        str = f"{converted:.2f}"
        
        temperature_hash = hashlib.sha256(str.encode()).hexdigest()
        
        return converted, temperature_hash

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

try:
    converted, hash = convert_temperature(100, 'C')
    pprint.pprint(f"{converted} , {hash}")
except TypeError:
    print("There was an issue with the provided data types.")
