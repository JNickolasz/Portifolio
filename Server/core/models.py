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

class Projeto(models.Model): 
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    tecnologias = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default="Em Desenvolvimento")
    link = models.URLField()
    imagem = models.ImageField(upload_to='projetos/')

    def __str__(self):
        return self.titulo