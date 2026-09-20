"""Ejemplo de skill: sirve de plantilla para crear nuevas skills."""

from __future__ import annotations

from .base import Skill


class ExampleSkill(Skill):
    """Skill de ejemplo que saluda al usuario."""

    name = "example"

    def run(self, nombre: str = "mundo") -> str:
        return f"Hola, {nombre}!"
