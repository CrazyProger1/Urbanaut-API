from abc import ABC, abstractmethod


class BaseAIAssistant(ABC):

    @abstractmethod
    def execute(self, query: str, instructions: str = None) -> str: ...


class BaseAISearchSearchEngine(ABC):

    @abstractmethod
    def search(self, query: str) -> dict: ...
