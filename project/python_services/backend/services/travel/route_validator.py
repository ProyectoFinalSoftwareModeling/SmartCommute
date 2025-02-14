"""This module defines services and other utilities for travel
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

from datetime import datetime
from typing import Dict, List

class RouteValidator:
    """
    A class to validate various aspects of a route, including its bidirectionality,
    availability based on schedules, and its direction between origin and destination.
    """

    @staticmethod
    def is_bidirectional_route(route_id: str) -> bool:
        """
        Determines if a route is bidirectional based on the route ID.

        Args:
            route_id (str): The ID of the route.

        Returns:
            bool: True if the route is bidirectional (i.e., the route ID is numeric),
                otherwise False.
        """
        return route_id.strip().isdigit()

    @staticmethod
    def check_route_availability(
        schedules: Dict[str, Dict[str, str]], route_id: str
    ) -> bool:
        """
        Checks if a route is available based on the current time and the route's schedule.

        Args:
            schedules (Dict[str, Dict[str, str]]): A dictionary of route schedules where
                the key is the route ID and the value is another dictionary with the
                days of the week as keys and schedule time ranges as values.
            route_id (str): The ID of the route to check.

        Returns:
            bool: True if the route is available based on the current day and time,
                otherwise False.
        """
        now = datetime.now()
        current_day = now.strftime("%A").lower()
        current_time = now.strftime("%H:%M")
        if route_id not in schedules or current_day not in schedules[route_id]:
            return False
        schedule = schedules[route_id][current_day]
        try:
            start, end = schedule.split(" - ", 1)
            return start <= current_time <= end
        except ValueError:
            return False

    @staticmethod
    def validate_direction(
        route_id: str, origin: str, destination: str, route_stations: Dict[str, List[str]]
    ) -> bool:
        """
        Validates if a route is valid for travel from the origin station to the destination station.

        Args:
            route_id (str): The ID of the route.
            origin (str): The origin station.
            destination (str): The destination station.
            route_stations (Dict[str, List[str]]): A dictionary mapping route IDs to lists
                of stations.

        Returns:
            bool: True if the route is valid for the given origin and destination, otherwise False.
        """
        try:
            stations = route_stations[route_id]
            if origin not in stations or destination not in stations:
                return False
            if RouteValidator.is_bidirectional_route(route_id):
                return True
            return stations.index(origin) < stations.index(destination)
        except (KeyError, ValueError):
            return False
