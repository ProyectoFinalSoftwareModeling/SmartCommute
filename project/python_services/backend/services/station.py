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
    This is a data class to move data into the devices.
    """

    name: str

class StationServices:
    """
    This class has the services for Transmilenio stations searches.
    """

    def __init__(self):
        self.repository = StationRepository()

    def get_all(self) -> List[StationDAO]:
        """This method returns all Transmilenio stations.

        Returns:
            A list of stations.
        """
        return self.repository.get_stations()

    def get_by_name(self, name: str) -> StationDAO:
        """This method returns a Transmilenio station by its name.

        Args:
            name (str): The name of the station.

        Returns:
            A list of stations with that name.
        """
        response = []
        for station in self.repository.get_stations():
            if name.lower() in station.name.lower():
                response.append(station)
        return response
