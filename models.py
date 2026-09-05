from dataclasses import dataclass


@dataclass
class Recipe:
    name: str
    description: str
    ingredients: list[str]
    cooking_time: int
    difficulty: str
    instructions: list[str]

