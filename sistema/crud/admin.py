from django.contrib import admin
from .models import Veiculo
from .models import Motorista
from .models import Controle
# Register your models here.
admin.site.register(Veiculo)
admin.site.register(Motorista)
admin.site.register(Controle)