# -*- coding: utf-8 -*-
from django import forms
from models import Pessoa

class CadastroForm(forms.ModelForm):
	class Meta:
		model = Pessoa
		fields = ('primeiro_nome' , 'ultimo_nome')