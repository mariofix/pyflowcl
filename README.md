# Bienvenido a pyflowcl

pyflowcl es una biblioteca de Python que proporciona una interfaz para interactuar con la API de Flow en Chile. Con pyflowcl, puedes realizar diversas operaciones, como crear pagos, obtener información de pagos, realizar reembolsos y más.

![PyPI - Status](https://img.shields.io/pypi/status/pyflowcl)
[![Tests&Coverage](https://github.com/mariofix/pyflowcl/actions/workflows/tests_coverage.yml/badge.svg?branch=main)](https://github.com/mariofix/pyflowcl/actions/workflows/tests_coverage.yml)
[![Downloads](https://pepy.tech/badge/pyflowcl)](https://pepy.tech/project/pyflowcl)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/7254d825df2d4292bf68563548d41f64)](https://app.codacy.com/gh/mariofix/pyflowcl/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/7254d825df2d4292bf68563548d41f64)](https://app.codacy.com/gh/mariofix/pyflowcl/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_coverage)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/mariofix/pyflowcl/main.svg)](https://results.pre-commit.ci/latest/github/mariofix/pyflowcl/main)
![PyPI](https://img.shields.io/pypi/v/pyflowcl)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyflowcl)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/pyflowcl)
![PyPI - License](https://img.shields.io/pypi/l/pyflowcl)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Instalación

Para instalar `pyflowcl`, asegúrate de tener Python instalados. Luego, puedes instalar la biblioteca utilizando tu administrador favorito.

## Uso Básico

Aquí hay un ejemplo básico de cómo usar pyflowcl para crear un pago:

```python
from pyflowcl import Payment
from pyflowcl.Clients import ApiClient

api = ApiClient(
    api_url="https://www.flow.cl/api",
    api_key="tu_api_key",
    api_secret="tu_api_secret",
)
pago = {
    "subject": "Asunto Email",
    "commerceOrder": "1234",
    "amount": 5000,
    "email": "mariofix@pm.me",
    "urlConfirmation": "https://mariofix.com",
    "urlReturn": "https://mariofix.com",
}

llamada = Payment.create(api, pago)
print(f"{llamada = }")
> llamada = { "flowOrder": 123456, "url": "https://www.flow.cl/app/pay.php", "token": "tok_123456" }

# Obtiene la URL de pago
print(f"URL de pago: {pago.url}?token={pago.token}")
> URL de pago: https://www.flow.cl/app/pay.php?token=tok_123456
```

## Documentación

Para obtener más información sobre cómo usar pyflowcl y todas las funcionalidades disponibles, consulta la documentación completa en [https://mariofix.github.io/pyflowcl](https://mariofix.github.io/pyflowcl).

## Contribuir

¡Tú contribución es bienvenida! Si encuentras errores, tienes sugerencias o deseas agregar nuevas características, por favor, crea un problema o envía una solicitud de extracción en el repositorio de GitHub: [Repositorio de pyflowcl](https://github.com/mariofix/pyflowcl).

## Licencia

Pyflowcl se distribuye bajo la Licencia MIT. Consulta el archivo [LICENSE](https://github.com/mariofix/pyflowcl/blob/main/LICENSE) para obtener más información.
