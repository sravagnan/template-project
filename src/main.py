"""summary
"""
from logs.logger import logger


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
    return string


if __name__ == "__main__":
    logger.info(say_hello("ciao"))
