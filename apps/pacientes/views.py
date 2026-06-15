from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente, EPS, RepresentanteLegal, Alergia
from django.contrib.auth.decorators import login_required

@login_required
def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/lista.html', {'pacientes': pacientes})

@login_required
def registrar_paciente(request):
    if request.method == 'POST':
        rep = RepresentanteLegal.objects.create(
            nombre_completo=request.POST.get('rep_nombre'),
            telefono=request.POST.get('rep_telefono'),
            parentesco=request.POST.get('rep_parentesco'),
        )
        paciente = Paciente.objects.create(
            nombre_completo=request.POST.get('nombre_completo'),
            fecha_nacimiento=request.POST.get('fecha_nacimiento'),
            peso_kg=request.POST.get('peso_kg'),
            talla_cm=request.POST.get('talla_cm'),
            nivel_socioeconomico=request.POST.get('nivel_socioeconomico'),
            nivel_actividad=request.POST.get('nivel_actividad'),
            institucion=request.POST.get('institucion'),
            representante=rep,
        )
        alergias = request.POST.get('alergias', '')
        for a in alergias.split(','):
            if a.strip():
                Alergia.objects.create(paciente=paciente, descripcion=a.strip())

        return redirect('lista_pacientes')

    eps_list = EPS.objects.all()
    return render(request, 'pacientes/registro.html', {'eps_list': eps_list})

@login_required
def detalle_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    return render(request, 'pacientes/detalle.html', {'paciente': paciente})