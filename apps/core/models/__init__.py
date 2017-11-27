from __future__ import absolute_import

from .places import Country, Province, City
from .hospital import Hospital
from .person import Person
from .medic import Medic
from .patient import Patient

__all__ = (

	Country.__name__,
	Province.__name__,
	City.__name__,
	Hospital.__name__,
	Person.__name__,
	Medic.__name__,
	Patient.__name__,
)