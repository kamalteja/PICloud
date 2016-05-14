from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class services(models.Model):
	service_name = models.CharField(max_length = 40)
	current_status = models.CharField(max_length = 15)
	prev_status = models.CharField(max_length = 15)
	last_updated_time = models.DateTimeField(auto_now=False, auto_now_add=True)
	pid = models.TextField()


	def __unicode__(self):
		return self.service_name

	def get_absolute_url(self):
		return reverse("services:detail", kwargs={"id": self.id})
