from django.contrib import messages
from django.core.mail import send_mail
from portifolio.forms import ContatoForm
from django.shortcuts import render, redirect
from core.models import DadosPessoais, Projeto

# Create your views here.

def home(request):
    dados = DadosPessoais.objects.first()
    return render(request, "portifolio/home.html", {'dados': dados})


def projetos(request):
    # Por herdar o base.html também tem q mandar os dados por conta do nome e da foto
    dados = DadosPessoais.objects.first()
    projetos = Projeto.objects.all()
    return render(request, "portifolio/projetos.html", {'projetos': projetos, 'dados': dados})


def contato(request):
    dados = DadosPessoais.objects.first()
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid(): 
            send_mail(
                subject=form.cleaned_data['assunto'],
                message=form.cleaned_data['mensagem'],
                from_email=form.cleaned_data['email'],
                recipient_list=[dados.email]
            )
            messages.success(request, "E-mail enviado com sucesso! Entraremos em contato em breve.")
        else:
            messages.error(request, "Erro ao enviar e-mail. Tente novamente mais tarde.")
        return redirect('portifolio:contato')
    else: 
        form = ContatoForm()
    return render(request, "portifolio/contato.html", {'dados': dados, 'form': form})
