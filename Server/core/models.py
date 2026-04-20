from django.db import models

# Create your models here.

class DadosPessoais(models.Model): 
    nome = models.CharField(max_length=100)
    nome_social = models.CharField(max_length=50, default='José Nickolas')
    idade = models.IntegerField(default=20)
    descricao = models.TextField()
    curso = models.CharField(max_length=50)
    periodo = models.CharField(max_length=20)
    email = models.EmailField()
    github = models.URLField()
    linkedin = models.URLField()
    telefone = models.CharField(max_length=15)
    foto = models.ImageField(upload_to='fotos/')

    def __str__(self):
        return self.nome

# Fiquei em dúvida se podia fazer os modelos todos aqui, ent por via das dúvidas decidi fazer aqui

class Projeto(models.Model): 
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    tecnologias = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default="Em Desenvolvimento")
    link = models.URLField()
    imagem = models.ImageField(upload_to='projetos/')

    def __str__(self):
        return self.titulo

class Certificado(models.Model): 
    nome_curso = models.CharField(max_length=100)
    empresa = models.CharField(max_length=50)
    duracao = models.CharField(max_length=50)
    descricao = models.TextField(null=True, blank=True)
    link_certificado = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nome_curso
    