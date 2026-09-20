"""Clase base mínima para crear skills reutilizables."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class Skill(ABC):
    """Contrato que debe cumplir toda skill del repositorio."""

    name: str

    @abstractmethod
    def run(self, **kwargs: Any) -> Any:
        """Ejecuta la skill y devuelve su resultado."""

