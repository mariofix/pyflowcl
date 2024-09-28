# Guía de Colaboración para pyflowcl

¡Gracias por tu interés en colaborar con pyflowcl! Este documento te guiará a través del proceso de contribución al proyecto.

## Formas de Colaborar

1. **Reportar bugs**: Si encuentras un error, por favor crea un issue en GitHub describiendo el problema.
2. **Sugerir mejoras**: Las ideas para nuevas características son bienvenidas. Crea un issue para discutirlas.
3. **Mejorar la documentación**: Ayúdanos a mantener la documentación clara y actualizada.
4. **Contribuir con código**: Sigue las instrucciones a continuación para enviar tus contribuciones de código.

## Proceso de Contribución

1. **Fork el repositorio** en GitHub.
2. **Clona tu fork** a tu máquina local.
3. **Crea una nueva rama** para tu contribución.
4. **Realiza tus cambios** y asegúrate de seguir las guías de estilo del proyecto.
5. **Prueba tus cambios** (ver sección de Pruebas).
6. **Haz commit de tus cambios** con mensajes claros y descriptivos.
7. **Push tus cambios** a tu fork en GitHub.
8. **Crea un Pull Request** desde tu fork al repositorio principal.

## Clonar el Repositorio

Puedes clonar el repositorio de dos maneras:

### Usando Git

```shell
git clone https://github.com/mariofix/pyflowcl.git
cd pyflowcl
```

### Usando GitHub CLI

```shell
gh repo clone mariofix/pyflowcl
cd pyflowcl
```

## Configuración del Entorno de Desarrollo

1. Asegúrate de tener Python 3.9+ y Poetry instalados.
2. Instala las dependencias del proyecto:

```shell
poetry install --with dev
```

## Pruebas, Cobertura y Estructura del Código

Antes de enviar tu Pull Request, asegúrate de que tu código pase todas las pruebas y siga las convenciones del proyecto.

### Ejecutar Pruebas

```shell
poetry run pytest
```

### Verificar Cobertura de Código

```shell
poetry run coverage run -m pytest
poetry run coverage report
```

### Verificar Estructura y Estilo del Código

Utilizamos pre-commit para mantener la consistencia del código:

```shell
poetry run pre-commit run --all-files
```

## Guías de Estilo

- Sigue la guía de estilo PEP 8 para el código Python.
- Utiliza docstrings para documentar funciones, clases y módulos.
- Mantén el código limpio y bien comentado.

## Proceso de Revisión

1. Un mantenedor revisará tu Pull Request.
2. Puede que se te pida realizar cambios o aclaraciones.
3. Una vez aprobado, tu código será fusionado en la rama principal.

## Informes de Calidad de Código

Al realizar tu Pull Request, recibirás un informe de Codacy que indicará si tu código cumple con los estándares de calidad del proyecto. Asegúrate de abordar cualquier problema señalado en este informe.

## Licencia

Al contribuir a este proyecto, aceptas que tus contribuciones se licenciarán bajo la licencia MIT del proyecto. Asegúrate de que cualquier nuevo archivo incluya el encabezado de licencia apropiado.

## Obtener Ayuda

Si tienes preguntas o necesitas ayuda, no dudes en crear un issue en GitHub.

¡Gracias por tu contribución a pyflowcl!
