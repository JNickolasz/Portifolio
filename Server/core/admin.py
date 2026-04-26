from django.contrib import admin
from .models import DadosPessoais, Projeto, Certificado,Tecnologia

# Register your models here.

admin.site.register(DadosPessoais)
admin.site.register(Projeto)
admin.site.register(Certificado)
admin.site.register(Tecnologia)