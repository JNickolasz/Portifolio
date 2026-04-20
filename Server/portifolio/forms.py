from django import forms

class ContatoForm(forms.Form): 
    nome = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=254, required=True)
    assunto = forms.CharField(max_length=100, required=True)
    mensagem = forms.CharField(widget=forms.Textarea, required=True)