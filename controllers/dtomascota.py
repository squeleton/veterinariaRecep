from modelos.mascota import Mascota
from daos.daomascota import MascotaDAO
class MascotaDTO:
    def prepareMascota(self):
        daoMasc = MascotaDAO()
        result = daoMasc.prepareMascota()
        lista = []
        if result is not None:
            for msc in result:
                type = ""
                if msc[1] == 1:
                    type = "Perro"
                elif msc[1] == 2:
                    type = "Gato"
                mascota = Mascota(idMascota=msc[0], tipoMascota=type, nombre=msc[2], edad=msc[3])
                lista.append(mascota)
        Mascota().prepareMascota(lista)
    
    def syncListaMascota(self):
        Mascota().clearLista()
        self.prepareMascota()
        
    #Buscar todas las Mascotas:
    def listarMascotas(self):
        mascota = Mascota().getListaMascota()
        for msc in mascota:
            print(f"ID Mascota: {msc.getIdMascota()} Nombre: {msc.getNombMascota()} Edad: {msc.getEdad()} Tipo de Mascota: {msc.getTipoMascota()}")
        
    #Buscar solamente UNA Mascota    
    def buscarMascota(self, idMascota):
        mascota = Mascota()
        result = mascota.buscarMascota(idMascota)
        if result is None:
            return None
        else:
            return result
    #Agregar mascota
    def addMascota(self, idMascota, nombre, edad, tipo, cliente):
        daoMascota = MascotaDAO()
        result = daoMascota.addMascota(Mascota(idMascota=idMascota,nombre=nombre, edad=edad, tipoMascota=tipo, cliente=cliente))
        self.syncListaMascota()
        return result
    #Eliminar mascota
    def delMascota(self, idMascota):
        daoMasc = MascotaDAO()
        resultado = daoMasc.delMascota(Mascota(idMascota=idMascota))
        self.syncListaMascota()
        return resultado
    #Actualizar mascota
    def updateMascota(self, idMascota,nombMascota,edad,tipoMascota):
        mascota = self.buscarMascota(idMascota)
        if mascota is None:
            return "La Mascota no Existe."
        daoMascota = MascotaDAO()
        if nombMascota != '':
            mascota.setNombMascota(nombMascota)
        if edad != '':
            mascota.setEdad(edad)
        if tipoMascota != '':
            mascota.setTipoMascota(tipoMascota)
        resultado = daoMascota.updateMascota(mascota)
        return resultado