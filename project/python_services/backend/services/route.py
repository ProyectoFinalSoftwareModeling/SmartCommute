"""This module defines services and data transfer objects (DTOs) 
for handling Transmilenio routes.

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
from repositories.route import RouteRepository, RouteDAO # pylint: disable=import-error

class RouteNameDTO(BaseModel):
    """
    Represents a Data Transfer Object (DTO) for Transmilenio route names.
    """

    name: str

class RouteServices:
    """
    Provides services for searching Transmilenio routes.
    """

    def __init__(self):
        """Initializes the service with a route repository."""
        self.repository = RouteRepository()

    def get_all(self) -> List[RouteDAO]:
        """Retrieves all Transmilenio routes.

        Returns:
            List[RouteDAO]: A list of all available Transmilenio routes.
        """
        return self.repository.get_routes()

    def get_by_name(self, name: str) -> RouteDAO:
        """Retrieves Transmilenio routes that match a given name.

        Args:
            name (str): The name or partial name of the route.

        Returns:
            List[RouteDAO]: A list of routes containing the given name.
        """
        response = []
        for route in self.repository.get_routes():
            if name.lower() in route.name.lower():
                response.append(route)
        return response
