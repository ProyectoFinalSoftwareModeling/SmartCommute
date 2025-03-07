"""This module defines a various routes for travel
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

from typing import List, Dict, Any
from services.travel.base_travel import RouteStrategy  # pylint: disable=import-error

class MinimizeStationsStrategy(RouteStrategy):
    """
    Strategy that optimizes route selection by choosing the one with the least 
    total number of stations traveled, whether direct or with transfers.
    """

    def select_routes(
        self,
        direct_routes: List[str],
        transfer_routes: List[Dict[str, Any]],
        route_stations: Dict[str, List[str]],
        origin: str,
        destination: str
    ) -> dict:
        """
        Select the optimal routes based on the least number of stations traveled.
        
        Args:
            direct_routes (List[str]): List of direct routes.
            transfer_routes (List[Dict[str, Any]]): List of transfer routes.
            route_stations (Dict[str, List[str]]): Dictionary mapping routes to station lists.
            origin (str): Origin station.
            destination (str): Destination station.
        
        Returns:
            dict: A dictionary containing the best routes based on the least stations traveled.
        """
        options = []

        for route in direct_routes:
            try:
                distance = abs(route_stations[route].index(origin) 
                               - route_stations[route].index(destination))
            except Exception:
                distance = float('inf')
            options.append({
                "route": route,
                "type": "bidirectional" if route.strip().isdigit() else "unidirectional",
                "transfers": 0,
                "stations_traveled": distance,
                "details": {
                    "from": origin,
                    "to": destination,
                    "total_stations": len(route_stations[route])
                }
            })

        for transfer in transfer_routes:
            transfer_details = transfer["details"]
            transfer_details["transfers"] = 1
            options.append({
                "route": f"{transfer_details['first_segment']['route']} + {transfer_details['second_segment']['route']}",
                "type": f"{transfer_details['first_segment']['type']} + {transfer_details['second_segment']['type']}",
                "transfers": 1,
                "stations_traveled": transfer["score"],
                "details": transfer_details
            })

        options.sort(key=lambda x: x["stations_traveled"])
        return {"routes": options[:5]} if options else {"error": "No available routes found"}
