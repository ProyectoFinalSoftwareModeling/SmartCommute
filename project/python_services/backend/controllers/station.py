"""This module is used to handle API endpoints related to 
Transmilenio stations.

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
from services.station import StationServices # pylint: disable=import-error
from repositories.station import StationDAO # pylint: disable=import-error

router = APIRouter()

services = StationServices()

@router.get("/station/all")
def get_all() -> List[StationDAO]:
    """This method is used to get all Transmilenio stations."""
    return services.get_all()


@router.get("/station/by_name/{name}")
def get_by_name(name: str) -> List[StationDAO]:
    """This method is used to get Transmilenio stations by name."""
    if name == "":
        raise HTTPException(status_code=400,
                            detail="The name cannot be empty.")
    return services.get_by_name(name)
