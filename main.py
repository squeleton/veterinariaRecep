from controllers.validations import inicial, validarLogin

# login
intentos = 1

print("""
      
--------------------------------------------------
---Bienvenido/a a la Veterinaria Patitas amadas---
--------------------------------------------------
      
""")
while intentos <= 3:
    try:
        result = validarLogin()
        #result = 1
        if result is not None:
            print("Acceso Permitido")
            inicial()
            break
        else:
            print("Usuario o contraseña incorrecto, 2 intentos restantes")
            intentos += 1
    except Exception as ex:
        print(ex)
        print("Intente nuevamente...")
if intentos == 4:
    print("Acceso Bloqueado")