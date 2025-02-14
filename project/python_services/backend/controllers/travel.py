"""This module is used to handle API endpoints related to 
Transmilenio travels.

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

from typing import Dict, Any
from fastapi import APIRouter, HTTPException, Query

from services.travel_finder import TravelFinder  # pylint: disable=import-error

router = APIRouter()

route_service = TravelFinder()

@router.get("/route/find", response_model=Dict[str, Any])
def find_route(
    origin: str = Query(..., description="Name of the origin station"),
    destination: str = Query(..., description="Name of the destination station"),
    optimization: str = Query(
        "min_stations", 
        description="Optimization criteria: 'min_stations' or 'min_transfers'"
    )
) -> Dict[str, Any]:
    """
    Endpoint to find routes between two Transmilenio stations.

    Args:
        origin (str): The origin station.
        destination (str): The destination station.
        optimization (str): The optimization criterion. Can be "min_stations"
            (fewer stations visited) or "min_transfers" (fewer transfers).

    Returns:
        Dict[str, Any]: A dictionary with the found routes or an error message
            if no routes are found.
    """
    result = route_service.find_routes(origin, destination, optimization)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result
