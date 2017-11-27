from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

### Model for Country
class Country(models.Model):
	name = models.CharField(_('Name'), max_length=100, blank=False, null=False, unique=True)
	code_name = models.CharField(_('Country Code Name'), max_length=10, 
									blank=False, null=False, unique=True)

	class Meta:
		ordering = ['code_name']
		verbose_name = _('Country')
		verbose_name_plural = _('Countries')

	def __str__(self):
		return '%s' % self.name


### Model for Province
class Province(models.Model):
	name = models.CharField(_('Name'), max_length=100, blank=False, null=False, unique=True)
	code_name = models.CharField(_('Province Code Name'), max_length=10, 
									blank=False, null=False, unique=True)
	country = models.ForeignKey(Country, blank=False, null=False)

	class Meta:
		ordering = ['code_name']
		verbose_name = _('Province')
		verbose_name_plural = _('Provinces')

	def __str__(self):
		return '%s' % self.name


### Model for City/State
class City(models.Model):
	name = models.CharField(_('Name'), max_length=100, blank=False, null=False, unique=True)
	code_name = models.CharField(_('City Code Name'), max_length=10,
									blank=False, null=False, unique=True)
	province = models.ForeignKey(Province, blank=False, null=False)

	class Meta:
		ordering = ['code_name']
		verbose_name = _('City')
		verbose_name_plural = _('Cities')

	def __str__(self):
		return '%s' % self.name