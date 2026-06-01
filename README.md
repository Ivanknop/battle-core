# battle-core

Módulo base compartido para proyectos de batalla entre entidades.

## Propósito

`battle-core` define las abstracciones comunes que comparten todos los proyectos de batalla: superhéroes, pokémon, países, y cualquier dominio futuro. El objetivo es separar la lógica genérica de combate de los detalles específicos de cada dominio.

## Diseño

El módulo sigue un diseño orientado a objetos donde cada entidad combatiente hereda de una clase base abstracta. Las reglas de combate no conocen los detalles internos de cada entidad — solo interactúan con su interfaz común.

## Clase Entity

Clase base abstracta que representa cualquier entidad combatiente.

**Atributos:**
- `name` — nombre de la entidad
- `vitality` — puntos de vida actuales
- `characteristics` — diccionario con los atributos específicos del dominio, cargados desde CSV

**Métodos concretos:**
- `take_hit(damage)` — descuenta daño de la vitalidad
- `is_alive()` — retorna `True` si la vitalidad es mayor a cero
- `update_vitality(energy)` — suma o resta vitalidad (positivo para curar, negativo para dañar)

**Métodos abstractos** (obligatorios en cada subclase):
- `offensive_power()` — calcula el poder ofensivo según los atributos del dominio
- `defensive_power()` — calcula el poder defensivo según los atributos del dominio

## Estructura

battle-core/
├── core/
│   ├── init.py
│   └── entity.py
├── tests/
│   └── test_entity.py
├── requirements.txt
└── README.md


## Tests

```bash
python -m venv venv
source venv/bin/activate
pip install pytest
pytest tests/ -v
```
