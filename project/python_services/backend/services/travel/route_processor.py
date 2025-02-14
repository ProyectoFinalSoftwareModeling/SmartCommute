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

from typing import Dict, List, Any, Set
from services.travel.route_validator import RouteValidator # pylint: disable=import-error

class RouteProcessor:
    """
    Processes routes to find direct and transfer routes between origin and destination.
    """

    def process_direct_routes(
        self,
        origin: str,
        destination: str,
        common_routes: Set[str],
        schedules: Dict[str, Dict[str, str]],
        route_stations: Dict[str, List[str]]
    ) -> List[str]:
        """
        Processes and returns direct routes between origin and destination.

        Args:
            origin (str): The origin station.
            destination (str): The destination station.
            common_routes (Set[str]): A set of routes that are common between the origin
                and destination.
            schedules (Dict[str, Dict[str, str]]): A dictionary containing the schedule
                data for the routes.
            route_stations (Dict[str, List[str]]): A dictionary mapping routes to their
                list of stations.

        Returns:
            List[str]: A list of direct routes that are available and validated.
        """
        direct_routes = [
            route for route in common_routes
            if RouteValidator.validate_direction(route, origin, destination, route_stations)
            and RouteValidator.check_route_availability(schedules, route)
        ]
        direct_routes.sort(key=lambda x: (not RouteValidator.is_bidirectional_route(x), x))
        return direct_routes

    def process_transfers(
        self,
        origin: str,
        destination: str,
        origin_routes: Set[str],
        stations_data: Dict[str, Set[str]],
        schedules: Dict[str, Dict[str, str]],
        route_stations: Dict[str, List[str]]
    ) -> List[Dict[str, Any]]:
        """
        Processes and returns transfer routes between origin and destination.

        Args:
            origin (str): The origin station.
            destination (str): The destination station.
            origin_routes (Set[str]): A set of routes originating from the origin station.
            stations_data (Dict[str, Set[str]]): A dictionary mapping stations to the set
                of routes that pass through them.
            schedules (Dict[str, Dict[str, str]]): A dictionary containing the schedule
                data for the routes.
            route_stations (Dict[str, List[str]]): A dictionary mapping routes to their
                list of stations.

        Returns:
            List[Dict[str, Any]]: A list of transfer routes, each containing the routes
                taken, the transfer stations, and the total stations traveled.
        """
        transfers = []
        station_cache = {}

        for first_route in origin_routes:
            if not RouteValidator.check_route_availability(schedules, first_route):
                continue

            if first_route not in station_cache:
                try:
                    route_stops = route_stations[first_route]
                    origin_index = route_stops.index(origin)
                    possible_stations = route_stops[:origin_index] \
                        + route_stops[origin_index + 1:] \
                        if RouteValidator.is_bidirectional_route(first_route) \
                            else route_stops[origin_index + 1:]
                    station_cache[first_route] = possible_stations
                except (ValueError, KeyError):
                    continue
            else:
                possible_stations = station_cache[first_route]

            for transfer_station in possible_stations:
                if transfer_station not in stations_data:
                    continue

                for second_route in stations_data[transfer_station].intersection(stations_data[destination]):
                    if not RouteValidator.check_route_availability(schedules, second_route):
                        continue
                    if RouteValidator.validate_direction(second_route, transfer_station,
                                                         destination, route_stations):
                        first_distance = abs(route_stations[first_route].index(origin)
                                              - route_stations[first_route].index(transfer_station))
                        second_distance = abs(route_stations[second_route].index(transfer_station)
                                               - route_stations[second_route].index(destination))
                        transfers.append({
                            "score": first_distance + second_distance,
                            "details": {
                                "first_segment": {
                                    "route": first_route,
                                    "type": "bidirectional" if first_route.strip().isdigit() \
                                        else "unidirectional",
                                    "from": origin,
                                    "to": transfer_station,
                                    "intermediate_stations": first_distance
                                },
                                "second_segment": {
                                    "route": second_route,
                                    "type": "bidirectional" if second_route.strip().isdigit() \
                                        else "unidirectional",
                                    "from": transfer_station,
                                    "to": destination,
                                    "intermediate_stations": second_distance
                                },
                                "total_stations": first_distance + second_distance,
                                "transfer_station": transfer_station
                            }
                        })

        return sorted(transfers, key=lambda x: x["score"])[:5]
