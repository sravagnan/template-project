"""This module contains the nox setup and workflow."""

import nox
from nox.sessions import Session


package = "test_db_api"
nox.options.sessions = "lint", "black", "mypy", "isort"
locations = "src", 
# TOFIX: we would like to move ideally to ["3.8", "3.9", "3.10"]
python_versions = ["3.10"]


@nox.session(python=python_versions)
def tests(session: Session) -> None:
    """Run tests and coverage."""
    session.run("python", "-m", "pip", "install", ".[dev]")
    session.run("pytest", "tests/")
    # TOFIX: restart the coverage reporting once tests are in
    # args = session.posargs or ["--cov"]
    # session.run("coverage", "run", "-m", "pytest", *args)


@nox.session(python=python_versions)
def black(session: Session) -> None:
    """Run black code formatter."""
    args = session.posargs or locations
    config_file = "pyproject.toml"  # Percorso del tuo file di configurazione black
    session.install("black")
    session.run("black", "--config", config_file, *args)


@nox.session(python=python_versions)
def lint(session: Session) -> None:
    """Run linting."""
    args = session.posargs or locations
    config_file = "src/configs/pylintrc"
    session.install("pylint")
    session.run("pylint", "--rcfile", config_file, *args)

@nox.session(python=python_versions)
def mypy(session: Session) -> None:
    """Run mypy."""
    args = session.posargs or locations
    config_file = "src/configs/mypy.ini"
    session.install("mypy")
    session.run("mypy", "--config-file", config_file, *args)

@nox.session(python=python_versions)
def isort(session: Session) -> None:
    """Run isort."""
    args = session.posargs or locations
    config_file = "src/configs/mypy.ini"
    session.install("isort")
    session.run("isort", *args)
