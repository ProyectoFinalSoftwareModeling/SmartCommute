"""This module defines services and data transfer objects (DTOs) 
for handling Transmilenio stations.

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

from typing import List
from pydantic import BaseModel
from repositories.station import StationRepository, StationDAO # pylint: disable=import-error

class StationNameDTO(BaseModel):
    """
    Represents a Data Transfer Object (DTO) for Transmilenio station names.
    """

    name: str

class StationServices:
    """
    Provides services for searching Transmilenio stations.
    """

    def __init__(self):
        """Initializes the service with a station repository."""
        self.repository = StationRepository()

    def get_all(self) -> List[StationDAO]:
        """Retrieves all Transmilenio stations.

        Returns:
            List[StationDAO]: A list of all available Transmilenio stations.
        """
        return self.repository.get_stations()

    def get_by_name(self, name: str) -> StationDAO:
        """Retrieves Transmilenio stations that match a given name.

        Args:
            name (str): The name or partial name of the station.

        Returns:
            List[StationDAO]: A list of stations containing the given name.
        """
        response = []
        for station in self.repository.get_stations():
            if name.lower() in station.name.lower():
                response.append(station)
        return response
