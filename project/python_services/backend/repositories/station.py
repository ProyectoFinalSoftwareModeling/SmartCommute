"""This module is used to handle data related to Transmilenio
stations.

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
from pydantic import BaseModel
from environment_variables import EnvironmentVariables # pylint: disable=import-error

class StationDAO(BaseModel):
    """
    This class is used to define data structure related to
    Transmilenio stations.
    """
    id: str
    name: str
    routes: list[str]


class StationRepository:
    """
    This class represents the behavior of a repository to handle 
    Transmilenio stations data.
    """

    def __init__(self):
        """This method is used to initialize the class."""
        env = EnvironmentVariables()
        path_file = env.path_stations_data
        self._load_data(path_file)

    def _load_data(self, path_file: str):
        """This method is used to load stations data from a file."""
        try:
            with open(path_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.data = data["stations"]
        except (FileNotFoundError, KeyError) as e:
            print(f"Error loading stations data: {e}")
            self.data = []

    def get_stations(self) -> list[StationDAO]:
        """This method is used to get all Transmilenio stations."""
        stations = []
        for station in self.data:
            route_temp = StationDAO(
                id = station["id"],
                name = station["name"],
                routes = station["routes"]
            )
            stations.append(route_temp)
        return stations
