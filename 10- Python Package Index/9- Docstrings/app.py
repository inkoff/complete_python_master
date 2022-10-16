""" One line description."""

from msilib.schema import Class
from pathlib import Path


class Converter:
    """Simpli converter"""

    def convert(self, path: Path) -> str:
        """
        Convert the given the text.

        Parameters:
        path (str): The path to a PDF file.

        Returns:
        str: The content of the PDF file as text.
        """
        print("Convert")
