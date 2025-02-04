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

import os
from dotenv import load_dotenv

DOTENV_PATH = "/app/.env"
load_dotenv(DOTENV_PATH)

#pylint: disable=too-few-public-methods
class EnvironmentVariables:
    """
    This class is used to define environment variables.
    """

    def __init__(self):
        """This method is used to initialize the class."""
        self.path_routes_data = os.getenv("PATH_ROUTES_DATA")
        self.path_stations_data = os.getenv("PATH_STATIONS_DATA")
