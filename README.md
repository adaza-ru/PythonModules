

<div align="center">

# Python Modules

**Python exercises from 42's curriculum, organized by what they demonstrate: real architecture and design-pattern work under `highlights/`, and guided practice in syntax, tooling, and libraries under `exercises/`.**

![Python](https://img.shields.io/badge/language-Python_3.10+-3776AB?logo=python&logoColor=white)
![flake8](https://img.shields.io/badge/linting-flake8-yellow)
![mypy](https://img.shields.io/badge/typing-mypy-blue)


*This project has been created as part of the 42 curriculum by adaza-ru.*
</div>

---

## Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Highlights](#highlights)
  - [Design Patterns: Polymorphism, Abstract Factory & Strategy](#design-patterns-polymorphism-abstract-factory--strategy)
  - [Functional Programming: Closures, functools & Decorators](#functional-programming-closures-functools--decorators)
- [Additional Exercises](#additional-exercises)
- [Notes](#notes)

---

## Overview

This repository collects the Python modules from 42's curriculum. Not all of them involve the same kind of work: some are guided practice in syntax, standard-library usage, or tooling, with function signatures and outputs largely specified by the exercise; a couple of them are genuine exercises in software design, where the interesting part is the architecture rather than the syntax.

Rather than flatten all of that into a single undifferentiated list, this repo is split in two:

- **`highlights/`** — modules built around real design decisions: abstract interfaces, composition, decoupling. Each one is documented below.
- **`exercises/`** — the rest of the curriculum: syntax fundamentals, exception handling, collections, file I/O, packaging, environment tooling, and data validation. Still real, working code — just not the part of this repo meant to carry the portfolio.

Every module follows 42's required per-exercise layout (`ex0/`, `ex1/`, ...) and general constraints: Python 3.10+, `flake8`-compliant, fully type-hinted and checked with `mypy`.

## Repository Structure

```
python-modules/
├── README.md
├── highlights/
│   ├── design-patterns/
│   │   ├── 05-polymorphism/           # abstract classes & polymorphic dispatch
│   │   └── 07-factories-and-strategy/ # abstract factory, capabilities, strategy pattern
│   └── 10-functional-programming/     # closures, functools, decorators
└── exercises/
    ├── 00-python-fundamentals/
    ├── 01-oop-basics/
    ├── 02-exception-handling/
    ├── 03-collections-and-generators/
    ├── 04-file-io/
    ├── 06-imports-and-packaging/
    ├── 08-environments-and-config/
    └── 09-data-validation-pydantic/
```

## Highlights

### Design Patterns: Polymorphism, Abstract Factory & Strategy

Two consecutive modules that build on each other, moving from basic polymorphism to a small set of composable design patterns.

**Polymorphism** starts with an abstract `DataProcessor` interface, implemented by three unrelated concrete processors, each accepting a different data shape:

```python
class DataProcessor(ABC):
    @abstractmethod
    def validate(self, data: Any) -> bool: ...

    @abstractmethod
    def ingest(self, data: Any) -> None: ...

    def output(self) -> tuple[int, str]: ...
```

A `DataStream` class then routes arbitrary elements to whichever registered processor can `validate` them, without ever knowing the processors' concrete types — classic polymorphic dispatch. An `ExportPlugin` built on `typing.Protocol` extends this with structural typing: a CSV or JSON export plugin only needs to match the expected method signature, no inheritance required, to be accepted by the pipeline.

**Factories and Strategy** builds directly on that foundation. A `CreatureFactory` abstract factory hides concrete `Creature` subclasses behind `create_base()` / `create_evolved()`, so the package only ever exposes factories, never concrete types. Optional behaviors (`HealCapability`, `TransformCapability`) are deliberately kept independent of `Creature` and composed in via multiple inheritance, so they could apply to other class hierarchies later. On top of that, a `BattleStrategy` abstract class — with `NormalStrategy`, `AggressiveStrategy`, and `DefensiveStrategy` implementations — decouples the battle logic from any specific capability, validating compatibility upfront (`is_valid()`) and raising a typed exception on an invalid strategy/creature pairing rather than failing silently.

Together, these two modules are less "solve the exercise" and more "here's how you'd structure a system where new data types, new creature families, or new battle strategies can be added without touching existing code" — the actual point of these patterns.

### Functional Programming: Closures, functools & Decorators

Python's functional side, covered through three progressively deeper exercises.

**Closures** — functions that hold private state without relying on globals: a call counter with independent state per instance, a power accumulator, and a small in-memory key/value store exposed only through `store`/`recall` closures, with no attribute on any object holding the data directly.

**`functools` and `operator`** — `functools.reduce` combined with `operator` functions for generic aggregation, `functools.partial` for pre-filling arguments into specialized callables, `functools.lru_cache` for memoized Fibonacci, and `functools.singledispatch` to route a single function call to type-specific behavior (`int`, `str`, `list`) without an `if isinstance()` chain.

**Decorators** — a timing decorator, a parameterized validation decorator *factory* (a decorator that itself takes arguments), and a retry decorator that re-invokes a failing function up to N times — all using `functools.wraps` to preserve the wrapped function's metadata, plus a `@staticmethod` example inside a class that also uses one of the decorators on an instance method.

These are the functional-programming tools that show up in real Python codebases — a retry decorator or a memoized function is something you reach for on an actual project, not just a syntax demonstration.

## Additional Exercises

The rest of the curriculum, kept in the repository and fully working, indexed here rather than described in detail:

| Module | Topic |
|---|---|
| [`00-python-fundamentals`](exercises/00-python-fundamentals) | Syntax, functions, control flow, recursion |
| [`01-oop-basics`](exercises/01-oop-basics) | Classes, encapsulation, inheritance, a simple factory |
| [`02-exception-handling`](exercises/02-exception-handling) | `try`/`except`/`finally`, custom exception hierarchies |
| [`03-collections-and-generators`](exercises/03-collections-and-generators) | Lists, tuples, sets, dicts, generators, comprehensions |
| [`04-file-io`](exercises/04-file-io) | File operations, standard streams, context managers |
| [`06-imports-and-packaging`](exercises/06-imports-and-packaging) | Packages, `__init__.py`, absolute vs. relative imports, breaking circular imports |
| [`08-environments-and-config`](exercises/08-environments-and-config) | Virtual environments, pip vs. Poetry, environment variables and `.env` |
| [`09-data-validation-pydantic`](exercises/09-data-validation-pydantic) | Pydantic models, field constraints, custom and nested validation |
