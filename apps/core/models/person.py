from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy

from .places import City

class Person(models.Model):
	DOCUMENT_CHOICES = (
		(1, 'DNI'),)

	first_name = models.CharField(_('First Name'), max_length=50, null=False, blank=False)
	last_name = models.CharField(_('Last Name'), max_length=50, null=False, blank=False)
	document_type = models.PositiveSmallIntegerField(
		_('Document Type'), choices=DOCUMENT_CHOICES, null=False, blank=False, default=1)
	document_number = models.CharField(_('Document Number'), max_length=255, null=False, blank=False)
	address = models.CharField(_('Address'), max_length=100, null=False, blank=False)
	phone = models.CharField(_('Phone'), max_length=50, null=False, blank=False, unique=True)
	email = models.EmailField(_('Email Address'), null=True, blank=True, unique=True)
	city = models.ForeignKey(City, default=None, on_delete=models.CASCADE)