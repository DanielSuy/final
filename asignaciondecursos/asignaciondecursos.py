class Asignaciondecursos:

    def __init__(self, request):
        self.request=request
        self.session=request.session
        asignaciondecursos=self.session.get("asignaciondecursos")
        if not asignaciondecursos:
            asignaciondecursos=self.session["asignaciondecursos"]={}
        
        self.asignaciondecursos=asignaciondecursos

    def agregar(self, curso):
        if(str(curso.id) not in self.asignaciondecursos.keys()):
            self.asignaciondecursos[curso.id]={

                "curso_id":curso.id,
                "nombre":curso.nombre,
                "precio":str(curso.precio),
                "cantidad":1,
                "imagen":curso.imagen.url
            }

        self.guardar_asignaciondecursos()

    def guardar_asignaciondecursos(self):
        self.session["asignaciondecursos"]=self.asignaciondecursos
        self.session.modified=True

    def eliminar(self,curso):
        curso.id=str(curso.id) 
        if curso.id in self.asignaciondecursos:
            del self.asignaciondecursos[curso.id]
            self.guardar_asignaciondecursos()

    def restar_curso(self, curso):
        for key, value in self.asignaciondecursos.items():
                if key==str(curso.id):
                    value["precio"]=float(value["precio"])-curso.precio
                    value["cantidad"]=value["cantidad"]-1
                    #value["precio"]=float(value["precio"])+curso.precio
                    if value["cantidad"]<1:
                        self.eliminar(curso)
                    break
        self.guardar_asignaciondecursos()

    def limpiar_asignaciondecursos(self):
        self.session["asignaciondecursos"]={}
        self.session.modified=True
