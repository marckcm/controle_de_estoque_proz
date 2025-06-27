from django.db import models

class Material(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    quantidade = models.PositiveIntegerField(default=0)
    foto = models.ImageField(upload_to='materiais/', blank=True, null=True)
    validade = models.DateField(blank=True, null=True)
    descartado = models.BooleanField(default=False)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Movimentacao(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=[('entrada', 'Entrada'), ('saida', 'Saída'), ('descarte', 'Descarte')])
    quantidade = models.PositiveIntegerField()
    em_uso = models.BooleanField(default=False)
    professor_responsavel = models.CharField(max_length=100, blank=True, null=True)
    estoque_minimo = models.PositiveIntegerField(default=0)
    estoque_maximo = models.PositiveIntegerField(default=0)
    data = models.DateTimeField(auto_now_add=True)
    observacao = models.TextField(blank=True)

    def __str__(self):
        return f"{self.tipo} - {self.material.nome} - {self.quantidade}"
