# Operaciones CLI

## Descripción

La aplicación CLI para Flow Chile es una herramienta que te permite interactuar con la API de Flow a través de la línea de comandos. Esta aplicación está basada en Typer, lo que hace que su uso sea muy sencillo y fácil de entender.


## Comandos Disponibles

### Listar Operaciones

Muestra las operaciones disponibles en un recurso de la API de Flow.

```shell
flow-cli listar-operaciones
```

### Buscar Operaciones

Muestra las operaciones disponibles en un recurso de la API de Flow.

```shell
flow-cli buscar-operaciones [STRING]
```

### Información de Operación

Muestra información de una operación específica de la API de Flow.

```shell
flow-cli info-operacion
```


## Ejemplos de Uso

### Listar Operaciones

Para listar las operaciones disponibles en un recurso específico de la API de Flow, ejecuta el siguiente comando:

```
flow-cli listar-operaciones
```

Esto mostrará una tabla con las operaciones disponibles.

### Buscar Operaciones

Si quieres buscar todas las operaciones relacionadas con correos, ejecuta el siguiente comando:

```
flow-cli buscar-operaciones email
```

Esto mostrará una tabla con las operaciones disponibles que contengan el nombre `email`.

### Información de Operación

Para obtener información detallada sobre una operación específica de la API de Flow, ejecuta el siguiente comando:

```
flow-cli info-operacion payment_create
```

Esto mostrará la descripción y otros detalles de la operación "payment_create".

## Configuración

La aplicación CLI utiliza las siguientes variables de entorno para la autenticación con la API de Flow:

- `PYFLOWCL_API_KEY`: Clave de API para autenticación.
- `PYFLOWCL_API_SECRET`: Secreto de API para autenticación.
- `PYFLOWCL_ENDPOINT`: El entorno de las llamadas a la API. Puede ser "live" o "sandbox" (valor por defecto: live).

Asegúrate de configurar estas variables de entorno antes de utilizar la aplicación.
