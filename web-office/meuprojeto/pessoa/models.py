from __future__ import unicode_literals

from django.db import models

class Pessoa(models.Model):
	primeiro_nome = models.CharField(max_length=30)
	ultimo_nome   = models.CharField(max_length=30)

	def __str__(self):
		return self.primeiro_nome