from Models.Inscripcion import Inscripcion
from Models.Estudiante import Estudiante
from Models.Materia import Materia
from Repositorios.RepositorioInscripcion import RepositorioInscripcion
from Repositorios.RepositorioEstudiante import RepositorioEstudiante
from Repositorios.RepositorioMateria import RepositorioMateria

class ControladorInscripcion():
    def __init__(self):
        self.repositorioInscripcion = RepositorioInscripcion()
        self.repositorioEstudiante = RepositorioEstudiante()
        self.repositorioMateria = RepositorioMateria()

    def index(self):
        return self.repositorioInscripcion.findAll()

    def create(self, infoInscripcion,id_estudiante,id_materia):
        nuevoInscripcion = Inscripcion(infoInscripcion)
        elEstudiante = Estudiante(self.repositorioEstudiante.findById(id_estudiante))
        laMateria = Materia(self.repositorioMateria.findById(id_materia))
        nuevoInscripcion.estudiante = elEstudiante
        nuevoInscripcion.materia = laMateria
        return self.repositorioInscripcion.save(nuevoInscripcion)

    def show(self, id):
        laInscripcion = Inscripcion(self.repositorioInscripcion.findById(id))
        return laInscripcion.__dict__

    def update(self, id, infoInscripcion, id_estudiante, id_materia):
        inscripcionActual = Inscripcion(self.repositorioInscripcion.findById(id))
        inscripcionActual.ano = infoInscripcion["año"]
        inscripcionActual.semestre = infoInscripcion["semestre"]
        inscripcionActual.nota_final = infoInscripcion["nota final"]
        elEstudiante = Estudiante(self.repositorioEstudiante.findById(id_estudiante))
        laMateria = Materia(self.repositorioMateria.findById(id_materia))
        inscripcionActual.estudiante = elEstudiante
        inscripcionActual.materia = laMateria
        return self.repositorioInscripcion.save(inscripcionActual)

    def delete(self, id):
        return self.repositorioInscripcion.delete(id)

    #"Obtener todos los inscritos en una materia"

    def listarInscritosEnMateria(self, id_materia):
        return self.repositorioInscripcion.getListadoInscritosEnMateria(id_materia)

    #"Obtener notas mas altas por curso"

    def notasMasAltasPorCurso(self):
        return self.repositorioInscripcion.getMayorNotaPorCurso()

    #"Obtener promedio de notas en materia"

    def promedioNotasEnMateria(self, id_materia):
        return self.repositorioInscripcion.promedioNotasEnMateria(id_materia)