# Brain Games

[![Maintainability](https://qlty.sh/gh/MiguelJoya-01/projects/python-project-140/maintainability.svg)](https://qlty.sh/gh/MiguelJoya-01/projects/python-project-140)

Brain Games is a collection of command-line games written in Python. The games
include even-number checks, arithmetic calculations, finding the greatest
common divisor, completing an arithmetic progression, and identifying prime
numbers.

## Requirements

- Python 3.12 or later
- [uv](https://docs.astral.sh/uv/) for dependency management and project execution
- Git

## Installation

Clone the repository and enter the project directory:

```bash
git clone https://github.com/MiguelJoya-01/python-project-140.git
cd python-project-140
```

Install the project and its dependencies:

```bash
uv sync
```

## Available games

Run the welcome program:

```bash
uv run brain-games
```

Start any of the five games:

```bash
uv run brain-even
uv run brain-calc
uv run brain-gcd
uv run brain-progression
uv run brain-prime
```

Each game asks questions in the terminal. Answer correctly for three rounds
to win.

## Demonstrations

### Brain Even
[![Brain Even demo](https://asciinema.org/a/DDll9Co68XYCa3JS.svg)](https://asciinema.org/a/DDll9Co68XYCa3JS)

### Brain Calc
[![Brain Calc demo](https://asciinema.org/a/DLWVkyt6ujCwhTNa.svg)](https://asciinema.org/a/DLWVkyt6ujCwhTNa)

### Brain GCD
[![Brain GCD demo](https://asciinema.org/a/3xsIFgRCvOKHcz7a.svg)](https://asciinema.org/a/3xsIFgRCvOKHcz7a)

### Brain Progression
[![Brain Progression demo](https://asciinema.org/a/96ZJN9j9DGEn2tJY.svg)](https://asciinema.org/a/96ZJN9j9DGEn2tJY)

### Brain Prime
[![Game Prime demo](https://asciinema.org/a/v8oDf7UUnKXHkxBr.svg)](https://asciinema.org/a/v8oDf7UUnKXHkxBr)

## Quality checks

[![GitHub Actions](https://github.com/MiguelJoya-01/python-project-140/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/MiguelJoya-01/python-project-140/actions)

[![SonarCloud Quality Gate](https://sonarcloud.io/api/project_badges/quality_gate?project=MiguelJoya-01_python-project-140)](https://sonarcloud.io/summary/new_code?id=MiguelJoya-01_python-project-140)

[![SonarCloud Maintainability](https://sonarcloud.io/api/project_badges/measure?project=MiguelJoya-01_python-project-140&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=MiguelJoya-01_python-project-140)

[![SonarCloud Reliability](https://sonarcloud.io/api/project_badges/measure?project=MiguelJoya-01_python-project-140&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=MiguelJoya-01_python-project-140)

[![SonarCloud Security](https://sonarcloud.io/api/project_badges/measure?project=MiguelJoya-01_python-project-140&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=MiguelJoya-01_python-project-140)
