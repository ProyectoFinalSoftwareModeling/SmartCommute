"""This module is used to handle data related to Transmilenio
routes.

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

class RouteDAO(BaseModel):
    """
    This class is used to define data structure related to
    Transmilenio routes.
    """
    id: str
    name: str
    schedule: list[dict[str, str]]
    stations: list[str]


class RouteRepository:
    """
    This class represents the behavior of a repository to handle 
    Transmilenio routes data.
    """

    def __init__(self):
        """This method is used to initialize the class."""
        env = EnvironmentVariables()
        path_file = env.path_routes_data
        self._load_data(path_file)

    def _load_data(self, path_file: str):
        """This method is used to load routes data from a file."""
        try:
            with open(path_file, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        except FileNotFoundError as e:
            print(f"Error loading routes data: {e}")
            self.data = []
    
    def get_routes(self) -> list[RouteDAO]:
        """This method is used to get all routes."""
        routes = []
        for route in self.data:
            route_temp = RouteDAO(
                id=route["id"],
                name=route["name"],
                schedule=route["schedule"],
                stations=route["stations"]
            )