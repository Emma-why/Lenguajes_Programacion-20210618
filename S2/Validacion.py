import hashlib
import pprint
from typing import Optional

def validar_contrasena(contrasena: str) -> Optional[str]:
    if len(contrasena) < 8:
        raise ValueError("La contraseña debe tener al menos 8 caracteres.")
    if not any(c.isupper() for c in contrasena):
        raise ValueError("La contraseña debe contener al menos una letra mayúscula.")
    if not any(c.islower() for c in contrasena):
        raise ValueError("La contraseña debe contener al menos una letra minúscula.")
    if not any(c.isdigit() for c in contrasena):
        raise ValueError("La contraseña debe contener al menos un número.")

    hash_object = hashlib.md5(contrasena.encode())
    return hash_object.hexdigest()

try:
    resultado = validar_contrasena("Password123")
    pprint.pprint(resultado)
except ValueError as e:
    print(e)

try:
    resultado2 = validar_contrasena("pass")
    pprint.pprint(resultado2)
except ValueError as e:
    print(e)