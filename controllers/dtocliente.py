from modelos.cliente import Cliente
from daos.daocliente import ClienteDAO
class ClienteDTO:
    def prepareCliente(self):
        daoCli = ClienteDAO()
        result = daoCli.prepareCliente()
        lista = []
        if result is not None:
            for cli in result:
                cliente = Cliente(run=cli[0], nombre=cli[1], apellido=cli[2], telefono=cli[3], correo=cli[4])
                lista.append(cliente)
        Cliente().prepareCliente(lista)

    def listarClientes(self):
        cliente = Cliente().getLista()
        return cliente
    
    # Sincro busca clientes

    def syncListaCliente(self):
        Cliente().clearLista()
        self.prepareCliente()
        
    def buscarCliente(self, run):
        cliente = Cliente()
        result = cliente.buscarCliente(run)
        if result is None:
            return None
        else:
            return result

    #Agregar Cliente
    def addCliente(self, run, nombre, apellido, telefono, correo):
        daoCli = ClienteDAO()
        cliente = Cliente(run=run, nombre=nombre, apellido=apellido, telefono=telefono, correo=correo)
        resultado = daoCli.addCliente(cliente)
        self.syncListaCliente()
        return resultado
    
    #Eliminar Cliente
    def delCliente(self, run):
        daoCli = ClienteDAO()
        resultado = daoCli.delCliente(Cliente(run=run))
        self.syncListaCliente()
        return resultado
    
    #Cambiar Cliente
    def updateCliente(self, run, nombre, apellido, telefono, correo):
        cliente = self.buscarCliente(run)
        if cliente is None:
            return "El Cliente no existe"
        daoCli = ClienteDAO()
        if nombre != '':
            cliente.setNombre(nombre)
        if apellido != '':
            cliente.setApellido(apellido)
        if telefono != '':
            cliente.setTelefono(telefono)
        if correo != '':
            cliente.setCorreo(correo)
        resultado = daoCli.updateCliente(cliente)
        return resultado
