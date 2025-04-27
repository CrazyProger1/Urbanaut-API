import gc
import inspect
from typing import Generator


def subclasses(cls: type, max_level: int = -1, ignore_abstract: bool = False) -> Generator:
    if max_level == 0:
        return

    for subcls in cls.__subclasses__():
        if ignore_abstract:
            if not inspect.isabstract(subcls):
                yield subcls

        else:
            yield subcls
        yield from subclasses(subcls, max_level - 1, ignore_abstract=ignore_abstract)


def instances(cls: type, precise: bool = True) -> Generator:
    for instance in gc.get_objects():
        if isinstance(instance, cls):
            instance_cls = instance.__class__
            if not precise:
                yield instance
            elif instance_cls == cls:
                yield instance
