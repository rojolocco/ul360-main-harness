"""Ejemplo de hook: sirve de plantilla para crear nuevos hooks."""

from __future__ import annotations

from .base import Hook


class ExampleHook(Hook):
    """Hook de ejemplo que imprime un mensaje al ejecutarse."""

    name = "example"

    def run(self, **kwargs) -> None:
        print(f"Hook '{self.name}' ejecutado con: {kwargs}")
