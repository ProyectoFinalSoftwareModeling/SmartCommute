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

from pydantic import BaseModel
from environment_variables import EnvironmentVariables # pylint: disable=import-error
from repositories.data.base_repository import BaseRepository # pylint: disable=import-error

class RouteDAO(BaseModel):
    """Represents the data structure for Transmilenio routes."""
    id: str
    name: str
    schedule: list[dict[str, str]]
    stations: list[str]


class RouteRepository(BaseRepository):
    """Repository for managing Transmilenio route data."""


    def __init__(self):
        """Initializes the repository and loads route data."""
        env = EnvironmentVariables()
        super().__init__(env.path_routes_data)

    def _extract_data(self, data: dict) -> list[dict]:
        """Extracts route data from the provided dictionary.

        Args:
            data (dict): The raw data containing route information.

        Returns:
            list[dict]: A list of dictionaries representing routes.
        """
        return data.get("routes", [])

    def get_routes(self) -> list[RouteDAO]:
        """Retrieves all Transmilenio routes.

        Returns:
            list[RouteDAO]: A list of route objects.
        """
        routes = []
        for route in self.data:
            route_temp = RouteDAO(
                id = route["id"],
                name = route["name"],
                schedule = route["schedule"],
                stations = route["stations"]
            )
            routes.append(route_temp)
        return routes
