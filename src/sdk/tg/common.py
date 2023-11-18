from dataclasses import dataclass
from enum import Enum
from typing import Coroutine, Any, Callable

from telegram import Update


class Lang(Enum):
    rus = "rus"
    eng = "eng"


@dataclass
class BilingualString:
    eng: str
    rus: str


@dataclass
class Command:
    name: str
    description: BilingualString
    handler: Callable[[Update, Any], Coroutine]

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other: "Command"):
        return self.name == other.name
