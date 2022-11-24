from Models.Departamento import Departamento
from Repositorios.RepositorioDepartamento import RepositorioDepartamento

class ControladorDepartamento():
    def __init__(self):
        self.repositorioDepartamento = RepositorioDepartamento()

    def index(self):
        return self.repositorioDepartamento.findAll()

    def create(self, infoDepartamento):
        nuevoDepartamento = Departamento(infoDepartamento)
        return self.repositorioDepartamento.save(nuevoDepartamento)

    def show(self, id):
        elDepartamento = Departamento(self.repositorioDepartamento.findById(id))
        return elDepartamento.__dict__

    def update(self, id, infoDepartamento):
        departamentoActual = Departamento(self.repositorioDepartamento.findById(id))
        departamentoActual.nombre = infoDepartamento["nombre"]
        departamentoActual.descripcion = infoDepartamento["descripcion"]
        return self.repositorioDepartamento.save(departamentoActual)

    def delete(self, id):
        return self.repositorioDepartamento.delete(id)

