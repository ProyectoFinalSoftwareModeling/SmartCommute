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

from typing import Dict, List, Set
from repositories.route import RouteRepository, RouteDAO # pylint: disable=import-error
from repositories.station import StationRepository, StationDAO # pylint: disable=import-error

class DataPreparer:
    """Class responsible for preparing data related to routes and stations."""

    def __init__(self, route_repo: RouteRepository, station_repo: StationRepository):
        """
        Initializes the DataPreparer with route and station repositories.

        Args:
            route_repo (RouteRepository): The repository to fetch route data.
            station_repo (StationRepository): The repository to fetch station data.
        """
        self.route_repo = route_repo
        self.station_repo = station_repo

    def prepare_data(
        self
    ) -> (Dict[str, Set[str]], Dict[str, Dict[str, str]], Dict[str, List[str]]):
        """
        Prepares data for stations, schedules, and route-station relationships.

        Args:
            None

        Returns:
            Tuple:
                - stations_data (Dict[str, Set[str]]): A dictionary mapping station
                  names to sets of routes passing through them.
                - schedules (Dict[str, Dict[str, str]]): A dictionary mapping route IDs
                  to dictionaries of schedule days and corresponding start-end times.
                - route_stations (Dict[str, List[str]]): A dictionary mapping route IDs
                  to lists of stations on each route.
        """
        routes: List[RouteDAO] = self.route_repo.get_routes()
        stations: List[StationDAO] = self.station_repo.get_stations()

        stations_data: Dict[str, Set[str]] = {
            station.name: set(station.routes) for station in stations
        }

        schedules: Dict[str, Dict[str, str]] = {}
        route_stations: Dict[str, List[str]] = {}
        for route in routes:
            schedules[route.id] = {
                sched.get("day", "").lower(): f"{sched.get('start_time', '')} - {sched.get('end_time', '')}"
                for sched in route.schedule
                if sched.get("start_time") and sched.get("end_time")
            }
            route_stations[route.id] = route.stations

        return stations_data, schedules, route_stations
