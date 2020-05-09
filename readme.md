# Aplicacion web responsive

Se debe desarrollar una aplicacion web para observar el TEAM de una empresa. Realizar servicios Rest API almacenadas en mysql con conexion a azure; para cada contacto se tiene en cuenta los siauientes criterios: nombres y apellidos, edad, celular (+519xxxxxxxx) solo numeros del 0 al 9, sede,  programa de especializacion.

# Concideraciones

- Buscar contacto: Se debe devolver la lista deacuerdo al campo de busqueda.
- Editar contacto: Se debe editar sus datos de registro de todos los campos, añadir o cambiar foto del    usuario y validar los cambios efectuados
- Listar contactos:Se debe visualizar toda la lista de todo el personal empresarial registrado.
- Listar usuario: Se devuelven los datos deacuerdo al userIDy la imagen en formato CND
- Cambios de estado: Se debe devolver una lista de usuarios conectados y desconectados, exponer la ultima hora de conexion activa, si el usuario desea se puede cambiar los estados a "Conectado, Ocupado, Ausente, No disponible, Desconectado"

## Aplicacion y librerias a usar

- Usar tags por cada punto realizado. (GIT)
- Crear Readme para levantar servicio y detallar para que sirve la aplicación.
- Crear intancia en azure para la base de datos en MYSQL.
- Usar programación orientada a objetos. (Clases)
- Usar la libreria Flask y Flask_RestX (Resource)
- Usar Postman o Swagger para documentar.
- Usar variables de entorno.
- Usar JSON TOKEN para el logueo del usuario
- Usar servidores.
- Mostrar archivo requirements, con las librerias a usar.