def importe_total_asignaciondecursos(request):
    total = 0

    # Verificar si la clave 'asignaciondecursos' está presente en request.session
    if 'asignaciondecursos' in request.session:
        for key, value in request.session["asignaciondecursos"].items():
            total = total + float(value["precio"])
    else:
        total = "Debes hacer login"

    return {"importe_total_asignaciondecursos": total}
