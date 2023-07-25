# Bienvenido a pyflowcl

Pyflowcl es una biblioteca de Python que proporciona una interfaz para interactuar con la API de Flow en Chile. Con pyflowcl, puedes realizar diversas operaciones, como crear pagos, obtener información de pagos, realizar reembolsos y más.

[![Tests&Coverage](https://github.com/mariofix/pyflowcl/actions/workflows/tests_coverage.yml/badge.svg?branch=main)](https://github.com/mariofix/pyflowcl/actions/workflows/tests_coverage.yml)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/7254d825df2d4292bf68563548d41f64)](https://app.codacy.com/gh/mariofix/pyflowcl/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/7254d825df2d4292bf68563548d41f64)](https://app.codacy.com/gh/mariofix/pyflowcl/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_coverage)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/mariofix/pyflowcl/main.svg)](https://results.pre-commit.ci/latest/github/mariofix/pyflowcl/main)
![PyPI](https://img.shields.io/pypi/v/pyflowcl)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyflowcl)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/pyflowcl)
![PyPI - License](https://img.shields.io/pypi/l/pyflowcl)
![PyPI - Status](https://img.shields.io/pypi/status/pyflowcl)


## Instalación

Para instalar pyflowcl, asegúrate de tener Python y pip instalados. Luego, puedes instalar la biblioteca utilizando pip:

```shell
pip install pyflowcl
```

## Uso Básico

Aquí hay un ejemplo básico de cómo usar pyflowcl para crear un pago:

```shell
from pyflowcl import FlowAPI
from pyflowcl.utils import genera_parametros

api = FlowAPI(api_key="tu llave flow", api_secret="tu secreto flow")
parametros = {
    "apiKey": api.api_key,
    "amount": 10000,
    "currency": "CLP",
    "subject": "Ejemplo de Pago",
    "email": "correo@example.com",
    "url_confirmation": "https://mi-sitio.com/confirmacion",
}
pago = api.objetos.call_payment_create(parameters=genera_parametros(parametros, api.api_secret))
print(pago)
> { "flowOrder": 123456, "url": "https://www.flow.cl/app/pay.php", "token": "tok_123456" }

# Obtiene la URL de pago
url_pago = pago.get("url")
token_pago = pago.get("url")
print(f"URL de pago: {url_pago}?token={token_pago}")
```

## Documentación

Para obtener más información sobre cómo usar pyflowcl y todas las funcionalidades disponibles, consulta la documentación completa en [https://mariofix.github.io/pyflowcl](https://mariofix.github.io/pyflowcl).

## Contribuir

¡Tú contribución es bienvenida! Si encuentras errores, tienes sugerencias o deseas agregar nuevas características, por favor, crea un problema o envía una solicitud de extracción en el repositorio de GitHub: [Repositorio de pyflowcl](https://github.com/mariofix/pyflowcl).

## Licencia

Pyflowcl se distribuye bajo la Licencia MIT. Consulta el archivo [LICENSE](https://github.com/mariofix/pyflowcl/blob/main/LICENSE) para obtener más información.
