from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy

from .person import Person

class Medic(Person):
	speciality = models.CharField(_('Speciality'), blank=False, 
		null=False, help_text=_('Medic Speciality'), max_length=150)

	def __str__(self):
		return '{0} {1}'.format(self.first_name, self.last_name)

	def get_absolute_url(self):
		return reverse_lazy('show_medic', kwargs={'pk': self.id,})
