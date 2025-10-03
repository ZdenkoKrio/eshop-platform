from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, TypeVar, Optional

T = TypeVar("T")
E = TypeVar("E", bound=str)

@dataclass(slots=True)
class Result(Generic[T]):
    ok: bool
    value: Optional[T] = None
    error: Optional[E] = None

    @staticmethod
    def Ok(value: T) -> "Result[T]":
        return Result(ok=True, value=value)

    @staticmethod
    def Err(error: E) -> "Result[T]":
        return Result(ok=False, error=error)