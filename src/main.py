"""summary
"""
from typing import List

from logs.logger import logger
from models.test_import import test_func


def say_hello(string: str) -> str:
    """_summary_

    Parameters
    ----------
    string : str
        _description_

    Returns
    -------
    str
        _description_
    """
    prova: List[str] = ["ciao"]
    test_func(prova)
    return string


if __name__ == "__main__":
    logger.info(say_hello("ciao"))
