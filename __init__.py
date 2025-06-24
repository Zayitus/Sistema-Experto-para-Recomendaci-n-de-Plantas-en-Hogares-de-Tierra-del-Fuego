"""
Sistema Experto para Recomendación de Plantas en Tierra del Fuego

Este módulo contiene la lógica principal del sistema experto que recomienda
plantas adaptadas a las condiciones específicas de Tierra del Fuego.
"""

__version__ = "0.1.0"
__author__ = "Gaston Schvartz"
__description__ = "Sistema Experto para recomendación de plantas fueguinas"

# Importaciones principales del módulo
from .plants_data import PLANTAS
from .rules import *

# Información del proyecto
PROJECT_INFO = {
    "name": "PlantAdvisor Tierra del Fuego",
    "version": __version__,
    "description": __description__,
    "status": "En desarrollo - Fase 2 completada"
}