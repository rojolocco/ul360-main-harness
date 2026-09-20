"""Clase base mínima para crear hooks reutilizables."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class Hook(ABC):
    """Contrato que debe cumplir todo hook del repositorio."""

    name: str

    @abstractmethod
    def run(self, **kwargs: Any) -> None:
        """Ejecuta el hook."""

