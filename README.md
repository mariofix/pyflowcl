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
p = Payment.PaymentRequest()
p.set_env(pyflowcl.__sandbox__)
p.set_auth("token", "key")
p.get_payment_url('Payment', 5000, Payment.CLP, Payment.ALL_METHODS)
print(p)
```

---

## License
>You can check out the full license [here](https://github.com/mariofix/pyflowcl/blob/stable-v3/LICENSE)

This project is licensed under the terms of the **MIT** license.  
FlowAPI is licensed under the terms of the **Apache 2.0** license.
