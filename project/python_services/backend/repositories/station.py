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

from pydantic import BaseModel
from environment_variables import EnvironmentVariables # pylint: disable=import-error
from repositories.data.base_repository import BaseRepository # pylint: disable=import-error

class StationDAO(BaseModel):
    """Data structure representing a Transmilenio station."""
    id: str
    name: str
    routes: list[str]


class StationRepository(BaseRepository):
    """Repository for managing Transmilenio station data."""

    def __init__(self):
        """Initializes the repository and loads station data."""
        env = EnvironmentVariables()
        super().__init__(env.path_stations_data)

    def _extract_data(self, data: dict) -> list[dict]:
        """Extracts station data from the provided dictionary.

        Args:
            data (dict): The raw data containing station information.

        Returns:
            list[dict]: A list of dictionaries representing stations.
        """
        return data.get("stations", [])

    def get_stations(self) -> list[StationDAO]:
        """Retrieves all Transmilenio stations.

        Returns:
            list[StationDAO]: A list of station objects.
        """
        stations = []
        for station in self.data:
            route_temp = StationDAO(
                id = station["id"],
                name = station["name"],
                routes = station["routes"]
            )
            stations.append(route_temp)
        return stations
