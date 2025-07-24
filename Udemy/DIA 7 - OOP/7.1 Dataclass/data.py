from dataclasses import dataclass
from typing import Optional

@dataclass
class Persona:
    nombre: str
    edad: int
    # anadir campo opcional
    direccion: Optional[str] = None
def __str__():
    print(f"Mi nombre es {}")

luis = Persona("culo",21)
print(luis)

"""
Son una forma mas elegante de declarar clases

"""
