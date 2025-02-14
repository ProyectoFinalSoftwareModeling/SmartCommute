"""This module defines a route selection strategy for travel
planning in Transmilenio.

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

from abc import ABC, abstractmethod
from typing import Dict, List, Any

class RouteStrategy(ABC):
    """Interface for route selection strategy."""

    @abstractmethod
    def select_routes(
        self,
        direct_routes: List[str],
        transfer_routes: List[Dict[str, Any]],
        route_stations: Dict[str, List[str]],
        origin: str,
        destination: str
    ) -> dict:
        """
        Selects routes based on the provided criteria.

        Args:
            direct_routes (List[str]): List of direct routes.
            transfer_routes (List[Dict[str, Any]]): List of transfer routes with
                station details.
            route_stations (Dict[str, List[str]]): Dictionary mapping route names
                to stations.
            origin (str): The origin station.
            destination (str): The destination station.

        Returns:
            dict: A dictionary containing the selected routes.
        """
        pass # pylint: disable=unnecessary-pass
