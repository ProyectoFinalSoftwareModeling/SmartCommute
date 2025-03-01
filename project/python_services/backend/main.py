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

from fastapi import FastAPI
from controllers import route_router, station_router, travel_router # pylint: disable=import-error

app = FastAPI(
    title="SmartCommute",
    description="This project is used to manage stations, routes and \
    plan trips on Transmilenio.",
    version="0.0.1",
)

app.include_router(route_router)
app.include_router(station_router)
app.include_router(travel_router)
