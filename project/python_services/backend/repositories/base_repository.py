"""This module is used to handle data related to Transmilenio
data.

Author: Juan Esteban Bedoya <jebedoyal@udistrital.edu.co>

This file is part of SmartCommute project.

SmartCommute is free software: you can redistribute it and/or 
modify it under the terms of the GNU General Public License as 
published by the Free Software Foundation, either version 3 of 
the License, or (at your option) any later version.

SmartCommute is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
General Public License for more details.

You should have received a copy of the GNU General Public License 
along with SmartCommute. If not, see <https://www.gnu.org/licenses/>. 
"""

import json
from abc import ABC, abstractmethod

class BaseRepository(ABC):
    """Abstract base class for repositories handling Transmilenio data."""


    def __init__(self, path_file: str):
        """Initializes the repository and loads data from a file.

        Args:
            path_file (str): Path to the JSON file containing the data.
        """
        self.data: list = []
        self._load_data(path_file)

    def _load_data(self, path_file: str):
        """Loads data from the specified file.

        Args:
            path_file (str): Path to the JSON file containing the data.

        Raises:
            FileNotFoundError: If the file is not found.
            KeyError: If expected keys are missing in the JSON file.
        """
        try:
            with open(path_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.data = self._extract_data(data)
        except (FileNotFoundError, KeyError) as e:
            print(f"Error loading data: {e}")
            self.data = []

    @abstractmethod
    def _extract_data(self, data: dict):
        """Extracts and processes relevant data from the loaded JSON.

        Args:
            data (dict): The raw data loaded from the JSON file.

        Returns:
            list: A processed list of relevant data items.

        This method must be implemented by subclasses.
        """
        pass # pylint: disable=unnecessary-pass
