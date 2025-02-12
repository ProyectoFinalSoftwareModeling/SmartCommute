"""This module is used to handle API endpoints related to 
Transmilenio routes.

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
from fastapi import APIRouter, HTTPException
from services.route import RouteServices # pylint: disable=import-error
from repositories.route import RouteDAO # pylint: disable=import-error

router = APIRouter()

services = RouteServices()

@router.get("/route/all")
def get_all() -> List[RouteDAO]:
    """Retrieves all Transmilenio routes.

    Returns:
        List[RouteDAO]: A list of all available Transmilenio routes.
    """
    return services.get_all()


@router.get("/route/by_name/{name}")
def get_by_name(name: str) -> List[RouteDAO]:
    """Retrieves Transmilenio routes that match the given name.

    Args:
        name (str): The name of the route to search for.

    Returns:
        List[RouteDAO]: A list of routes matching the given name.

    Raises:
        HTTPException: If the name is empty.
    """
    if not name:
        raise HTTPException(status_code=400,
                            detail="The name cannot be empty.")
    return services.get_by_name(name)
