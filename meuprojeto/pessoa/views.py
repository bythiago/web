from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from pessoa.models import Pessoa
from pessoa.forms import CadastroForm

def index(request):
	primeiro_nome = Pessoa.objects.order_by('primeiro_nome')
	nomes = {'primeiro_nome': primeiro_nome}
	return render(request, 'index.html' , nomes)

def detalhes(request, id):
	nome = get_object_or_404(Pessoa, pk=id)
	return render(request, 'detalhes.html', {'nome':nome})

def cadastro(request):
	if request.method == "POST":
		form = CadastroForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return render(request, 'cadastro.html', {'form': form})
	else:
		form = CadastroForm()
	return render(request, 'cadastro.html', {'form': form})

def editar(request, id):
	post = get_object_or_404(Pessoa, pk=id)
	if request.method == 'POST':
		form = CadastroForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return render(request, 'detalhes.html', {'nome':post})
	else:
		form = CadastroForm(instance=post)
	return render(request, 'editar.html', {'form' : form})