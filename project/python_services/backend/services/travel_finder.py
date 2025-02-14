"""This module defines services for planning Transmilenio travels.

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

from repositories.route import RouteRepository  # pylint: disable=import-error
from repositories.station import StationRepository  # pylint: disable=import-error
from .travel.direct_travel import MinimizeTransfersStrategy  # pylint: disable=import-error
from .travel.transfer_travel import MinimizeStationsStrategy  # pylint: disable=import-error
from .travel.route_processor import RouteProcessor  # pylint: disable=import-error
from .travel.data_preparer import DataPreparer  # pylint: disable=import-error

class TravelFinder:
    """
    Class that finds optimal routes between an origin and destination station 
    based on the selected optimization strategy (e.g., minimizing stations or transfers).
    """

    def __init__(self):
        """
        Initializes the TravelFinder with required repositories, data preparer, 
        route processor, and strategies for optimization.
        """
        self.route_repo = RouteRepository()
        self.station_repo = StationRepository()
        self.data_preparer = DataPreparer(self.route_repo, self.station_repo)
        self.route_processor = RouteProcessor()
        self.strategies = {
            "min_stations": MinimizeStationsStrategy(),
            "min_transfers": MinimizeTransfersStrategy()
        }

    def find_routes(
        self,
        origin: str,
        destination: str,
        optimization: str = "min_stations"
    ) -> dict:
        """
        Finds the optimal routes between the origin and destination based on 
        the selected optimization strategy.
        
        Args:
            origin (str): The starting station.
            destination (str): The destination station.
            optimization (str): The optimization strategy (e.g., "min_stations" or "min_transfers").
        
        Returns:
            dict: A dictionary containing the selected routes or an error message.
        """

        stations_data, schedules, route_stations = self.data_preparer.prepare_data()

        if origin not in stations_data or destination not in stations_data:
            return {"error": "Station not found"}

        common_routes = stations_data[origin].intersection(stations_data[destination])

        direct_routes = self.route_processor.process_direct_routes(
            origin, destination, common_routes, schedules, route_stations
        )
        transfer_routes = self.route_processor.process_transfers(
            origin, destination, stations_data[origin], stations_data, schedules, route_stations
        )

        strategy = self.strategies.get(optimization, MinimizeStationsStrategy())
        return strategy.select_routes(direct_routes, transfer_routes,
                                      route_stations, origin, destination)
