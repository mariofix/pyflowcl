PyFlowCL
============

Cliente API para operaciones con el servicio de pagos Flow.cl  
[FlowAPI-3.0.1](https://www.flow.cl/docs/api.html) 

---

## Features
- Currently the "[Payment](https://www.flow.cl/docs/api.html#tag/payment)" command is available


---

## Setup
This project is managed by Poetry (a requierements.txt file is also provided)

---

## Usage
```python
from pyflowcl import Payment
from pyflowcl.Clients import ApiClient

API_URL = "https://sandbox.flow.cl/api"
API_KEY = "your_key"
API_SECRET = "your_secret"
FLOW_TOKEN = "your_payment_token"
api = ApiClient(API_URL, API_KEY, API_SECRET)

call = Payment.get_status(api, FLOW_TOKEN)
print(call)
```

---

## License
>You can check out the full license [here](https://github.com/mariofix/pyflowcl/blob/stable-v3/LICENSE)

This project is licensed under the terms of the **MIT** license.  
FlowAPI is licensed under the terms of the **Apache 2.0** license.
