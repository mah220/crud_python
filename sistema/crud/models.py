from django.db import models

# Create your models here.

###############
# DB VEICULO
###############

class Veiculo(models.Model):
    id = models.AutoField(primary_key=True)
    placa = models.CharField(max_length=100, verbose_name='Placa')
    marca = models.CharField(max_length=100, verbose_name='Marca')
    veiculo = models.CharField(max_length=100, verbose_name='Veículo')
    km = models.IntegerField(verbose_name='Km_Troca_Óleo')
    imagem = models.ImageField(upload_to='imagens/',verbose_name="Imagem", null=True)

    def __str__(self):
        fileira = "Placa: " + self.placa + " - " + "Veículo: " + self.veiculo
        return fileira
    
    def delete(self, using=None, keep_parents=False):
        self.imagem.storage.delete(self.imagem.name)
        super().delete()

###############
# DB MOTORISTA
###############

class Motorista(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, verbose_name='Nome')
    telefone = models.CharField(max_length=100, verbose_name='Telefone')
    cnh = models.CharField(max_length=100, verbose_name='CNH')

    def __str__(self):
        fileira = "Nome: " + self.nome + " - " + "Telefone: " + self.telefone
        return fileira

###############
# DB CONTROLE
###############

class Controle(models.Model):
    id = models.AutoField(primary_key=True)
    veiculo = models.ForeignKey( Veiculo, on_delete=models.CASCADE, verbose_name='ID_Veiculo')
    motorista = models.ForeignKey( Motorista, on_delete=models.CASCADE, verbose_name='ID_Motorista')
    data_saida = models.DateField(verbose_name='Data_Saida')
    hora_saida = models.TimeField(verbose_name='Hora_Saida')
    km_saida = models.IntegerField(verbose_name='Km_Saida')
    destino = models.CharField(max_length=100, verbose_name='Destino')
    data_retorno = models.DateField(verbose_name='Data_Retorno')
    hora_retorno = models.TimeField(verbose_name='Hora_Retorno')
    km_retorno = models.IntegerField(verbose_name='Km_Retorno')
    km_percorrido = models.IntegerField(verbose_name='Km_Percorrido')

    def __str__(self):
        fileira = " " + str(self.veiculo) + " - " + " " + str(self.motorista)
        return fileira

    