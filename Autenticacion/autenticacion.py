from modelo.Usuarios import Usuarios
from controlador.Usuarios import consultas

def verificar_usuario(email, password):
    usuario = Usuarios()
    usuario.mail = email
    consulta_usuario = consultas("select id_usuario, U.id_rol, R.tipo_rol from usuarios as U inner join roles as R on R.id_rol = U.id_rol where mail='"+email+"'")
    if consulta_usuario:
        rol_usuario = consulta_usuario[0][1]
        tipo_rol = consulta_usuario[0][2]
        consulta_pwd = consultas("select pwd from usuarios where mail='"+email+"'")
        pwd_usuario = consulta_pwd[0][0]
        if pwd_usuario == password:
            return [rol_usuario, tipo_rol]
        else:
            print("Contraseña incorrecta")
    else:
        print("Usuario inexistente")
    return [False, False]