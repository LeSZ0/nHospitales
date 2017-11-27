from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy

from .places import City

class Hospital(models.Model):
	STATUS_CHOICES =   ((1, _('Up')),
						(2, _('Down')))

	name = models.CharField(_('Name'), blank=False, null=False, unique=True, max_length=100)
	slug = models.SlugField(_('Slug'), blank=False, null=False, unique=True, 
								max_length=150, help_text=_('Used to build hospital URL.'))
	address = models.CharField(_('Address'), blank=False, null=False, max_length=255)
	email = models.EmailField(_('Email'), blank=True, null=True, unique=True)
	status = models.PositiveSmallIntegerField(_('Status'), choices=STATUS_CHOICES, default=1)
	created_at = models.DateTimeField(_('Creation Date'), auto_now_add=True)
	updated_at = models.DateTimeField(_('Updated Date'), auto_now_add=False, auto_now=True)
	city = models.ForeignKey(City, blank=False, null=False, help_text=_('Hospital City'))

	class Meta:
		ordering = ['name']
		verbose_name = _('Hospital')
		verbose_name_plural = _('Hospitals')

	def __str__(self):
		return '%s' % self.name

	def get_absolute_url(self):
		return reverse_lazy('hospital_show', kwargs={'slug': self.slug,})