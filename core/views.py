from django.shortcuts import render
from apps.pacientes.models import Paciente
from apps.valoracion.models import Consulta
from apps.recomendaciones.models import Recomendacion
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    total_pacientes = Paciente.objects.count()
    total_consultas = Consulta.objects.count()
    total_recomendaciones = Recomendacion.objects.count()

    # Últimos 5 pacientes registrados
    ultimos_pacientes = Paciente.objects.order_by('-fecha_registro')[:5]

    # Distribución por clasificación IMC
    severos = Paciente.objects.filter(peso_kg__isnull=False)
    desnutricion_severa = sum(1 for p in severos if p.imc < 16)
    desnutricion_moderada = sum(1 for p in severos if 16 <= p.imc < 18.5)
    normal = sum(1 for p in severos if 18.5 <= p.imc <= 24.9)
    sobrepeso = sum(1 for p in severos if p.imc > 24.9)

    context = {
        'total_pacientes': total_pacientes,
        'total_consultas': total_consultas,
        'total_recomendaciones': total_recomendaciones,
        'ultimos_pacientes': ultimos_pacientes,
        'desnutricion_severa': desnutricion_severa,
        'desnutricion_moderada': desnutricion_moderada,
        'normal': normal,
        'sobrepeso': sobrepeso,
    }
    return render(request, 'dashboard.html', context)