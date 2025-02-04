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

from typing import List
from pydantic import BaseModel
from repositories.route import RouteRepository, RouteDAO # pylint: disable=import-error

class NameDTO(BaseModel):
    """
    This is a data class to move data into the devices.
    """
    
    name: str

class RouteServices:
    """
    This class has the services for route searches.
    """

    def __init__(self):
        self.repository = RouteRepository()

    def get_all(self) -> List[RouteDAO]:
        """This method returns all routes.

        Returns:
            A list of routes.
        """
        return self.repository.get_routes()
    
    def get_by_name(self, name: str) -> RouteDAO:
        """This method returns a route by its name.

        Args:
            name (str): The name of the route.

        Returns:
            A list of routes with that name.
        """
        response = []
        for route in self.repository.get_routes():
            if name.lower() in route.name.lower():
                response.append(route)
        return response
