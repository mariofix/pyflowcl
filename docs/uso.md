# Cómo usar

## Instalación

=== "Usando Poetry"
    ```shell
    poetry add pyflowcl
    ```
=== "Usando pip"
    ```shell
    pip install pyflowcl
    ```
=== "Clonar con git"
    ```shell
    git clone https://github.com/mariofix/pyflowcl.git
    ```


## Configuración

La aplicación CLI utiliza las siguientes variables de entorno para la autenticación con la API de Flow:

- `PYFLOWCL_API_KEY`: Clave de API para autenticación.
- `PYFLOWCL_API_SECRET`: Secreto de API para autenticación.
- `PYFLOWCL_ENDPOINT`: El entorno de las llamadas a la API. Puede ser "live" o "sandbox" (valor por defecto: live).

Asegúrate de configurar estas variables de entorno antes de utilizar la aplicación.

## Operaciones disponibles

Luego de inicializar la clase con
``` py title="Inicialización Clase"
api = FlowAPI(api_key="tu llave flow", api_secret="tu secreto flow")
```

puedes llamarla con cualquiera de las operaciones disponibles, por ejemplo para obtener el estado de un pago

``` py title="Inicialización Clase"
api = FlowAPI(api_key="tu llave flow", api_secret="tu secreto flow")
status = api.objetos.call_payment_getstatus(parameters={"token": "token_del_pago_a_consultar"})
```

Cada operacion tiene sus parametros definidos, te sugerimos revisar [la API de flow](https://www.flow.cl/docs/api.html) para ver cuales son

| Operación | Uso | Descripción |
| ----------|-----| ----------- |
| payment_getstatus | ```api.objetos.call_payment_getstatus()``` | Este método se utiliza para obtener el estado de un pago.
| payment_getstatusbycommerceid | ```api.objetos.call_payment_getstatusbycommerceid()``` | Este método permite obtener el estado de un pago en base al ... |
| payment_getstatusbyfloworder|```api.objetos.call_payment_getstatusbyfloworder()```|Este método permite obtener el estado de un pago en base
| payment_getpayments|```api.objetos.call_payment_getpayments()```|Este método permite obtener la lista paginada de pagos
| payment_getstatusextended|```api.objetos.call_payment_getstatusextended()```|Este método se utiliza para obtener el estado de un pago.
| payment_getstatusbyfloworderextended |```api.objetos.call_payment_getstatusbyfloworderextended()``` |Este método permite obtener el estado de un pago en base
| payment_create|```api.objetos.call_payment_create()```|Este método permite crear una orden de pago a **Flow** y
| payment_createemail|```api.objetos.call_payment_createemail()```|Permite generar un cobro por email. **Flow** emite un email
| refund_create|```api.objetos.call_refund_create()```|Este servicio permite crear una orden de reembolso. Una vez
| refund_cancel|```api.objetos.call_refund_cancel()```|Este servicio permite cancelar una orden de reembolso
| refund_getstatus|```api.objetos.call_refund_getstatus()```|Permite obtener el estado de un reembolso solicitado.
| customer_create|```api.objetos.call_customer_create()```|Permite crear un nuevo cliente.
| customer_edit|```api.objetos.call_customer_edit()```|Este servicio permite editar los datos de un client
| customer_delete|```api.objetos.call_customer_delete()```|Permite eliminar un cliente. Para eliminar un cliente,
| customer_get|```api.objetos.call_customer_get()```|Permite obtener los datos de un cliente en base a su **custo... |
| customer_list|```api.objetos.call_customer_list()```|Permite obtener la lista de clientes paginada de acuerdo a l... |
| customer_register|```api.objetos.call_customer_register()```|Envía a un cliente a registrar su tarjeta de crédito para po... |
| customer_getregisterstatus|```api.objetos.call_customer_getregisterstatus()```|Elte servicio retorna el resultado del registro de la tarjet... |
| customer_unregister|```api.objetos.call_customer_unregister()```|Este servicio permite eliminar el registro de la tarjeta de ... |
| customer_charge|```api.objetos.call_customer_charge()```|Este servicio permite efectuar un cargo automático en la tar... |
| customer_collect|```api.objetos.call_customer_collect()```|Este servicio envía un cobro a un cliente. Si el cliente tie... |
| customer_batchcollect|```api.objetos.call_customer_batchcollect()```|Este servicio envía de forma masiva un lote de cobros a clie... |
| customer_getbatchcollectstatus|```api.objetos.call_customer_getbatchcollectstatus()```|Este servicio permite consultar el estado de un lote de cobr... |
| customer_reversecharge|```api.objetos.call_customer_reversecharge()```|Este servicio permite reversar un cargo previamente efectuad... |
| customer_getcharges|```api.objetos.call_customer_getcharges()```|Este servicio obtiene la lista paginada de los cargos efectu... |
| customer_getchargeattemps|```api.objetos.call_customer_getchargeattemps()```|Este servicio obtiene la lista paginada de los intentos de c... |
| customer_getsubscriptions|```api.objetos.call_customer_getsubscriptions()```|Este servicio obtiene la lista paginada de las suscripciones... |
| plans_create|```api.objetos.call_plans_create()```|  Este servicio permite crear un nuevo Plan de Suscripción...   |
| plans_get|```api.objetos.call_plans_get()```|Este servicio permite obtener los datos de un Plan de Suscri... |
| plans_edit|```api.objetos.call_plans_edit()```|Este servicio permite editar los datos de un Plan de Suscrip... |
| plans_delete|```api.objetos.call_plans_delete()```|Este servicio permite eliminar un Plan de Suscripción. El el... |
| plans_list|```api.objetos.call_plans_list()```|Permite obtener la lista de planes de suscripción paginada d... |
| subscription_create|```api.objetos.call_subscription_create()```|Este servicio permite crear una nueva suscripción de un clie... |
| subscription_get|```api.objetos.call_subscription_get()```|Este servicio permite obtener los datos de una suscripción....  |
| subscription_list|```api.objetos.call_subscription_list()```|Permite obtener la lista de suscripciones paginada de acuerd... |
| subscription_changetrial|```api.objetos.call_subscription_changetrial()```|Este servicio permite modificar los días de Trial de una sus... |
| subscription_cancel|```api.objetos.call_subscription_cancel()```|Este servicio permite cancelar una suscripción. Existen form... |
| subscription_addcoupon|```api.objetos.call_subscription_addcoupon()```|Este servicio permite agregar un descuento a la suscripción.... |
| subscription_deletecoupon|```api.objetos.call_subscription_deletecoupon()```|Este servicio permite eliminar el descuento que tenga
| coupon_create|```api.objetos.call_coupon_create()```|Este servicio permite crear un cupón de
| coupon_edit|```api.objetos.call_coupon_edit()```|Este servicio permite editar un cupón de descuento.
| coupon_delete|```api.objetos.call_coupon_delete()```|Este servicio permite eliminar un cupón de descuento.
| coupon_get|```api.objetos.call_coupon_get()```|Este servicio permite obtener los datos de un cupón de
| coupon_list|```api.objetos.call_coupon_list()```|Este servicio permite la lista de cupones de
| invoice_get|```api.objetos.call_invoice_get()```|Este servicio permite obtener los datos de un
| invoice_cancel|```api.objetos.call_invoice_cancel()```|Este servicio permite cancelar un Importe (Invoice)
| invoice_outsidepayment|```api.objetos.call_invoice_outsidepayment()```|Este servicio permite dar por pagado un Importe (Invoice)
| invoice_getoverdue|```api.objetos.call_invoice_getoverdue()```|Este servicio permite obtener la lista de invoices
| invoice_retrytocollect|```api.objetos.call_invoice_retrytocollect()```|Este servicio permite reintentar el cobro de un Invoice
| settlement_getbydate|```api.objetos.call_settlement_getbydate()```|Este método se utiliza para obtener la liquidación de la
| settlement_getbyid|```api.objetos.call_settlement_getbyid()```|Este método se utiliza para obtener el objeto Settlement
| settlement_search|```api.objetos.call_settlement_search()```|Este método se utiliza para obtener el(los) encabezado(s)
| settlement_getbyidv2|```api.objetos.call_settlement_getbyidv2()```|Este método se utiliza para obtener el objeto
| merchant_create|```api.objetos.call_merchant_create()```|Este método permite crear un nuevo comercio asociado
| merchant_edit|```api.objetos.call_merchant_edit()```|Este método permite modificar un comercio asociado
| merchant_delete|```api.objetos.call_merchant_delete()```|Este método permite eliminar un comercio asociado
| merchant_get|```api.objetos.call_merchant_get()```|Este método permite obtener la información de un comercio
| merchant_list|```api.objetos.call_merchant_list()```|Permite obtener la lista de comercios paginada de acuerdo a

## Crear un pago

La API nos entrega dos opciones para generar un pago:

* payment_create
* payment_createemail

Usaremos `payment_create` para simular la operacion mas común.

``` py title="Generacion de un pago"
from pyflowcl import FlowAPI
from pyflowcl.utils import genera_parametros

api = FlowAPI(api_key="tu llave flow", api_secret="tu secreto flow")
parametros = {
    "apiKey": api.api_key,
    "amount": 10000,
    "currency": "CLP",
    "subject": "Ejemplo de Pago",
    "email": "correo@example.com",
    "urlConfirmation": "https://mariofix.github.io/pyflowcl/uso/#crear-un-pago",
    "urlReturn": "https://mariofix.github.io/pyflowcl/uso/#crear-un-pago",
    "commerceOrder": "order_1234",
}
pago = api.objetos.call_payment_create(parameters=genera_parametros(parametros, api.api_secret))
print(pago)
> { "flowOrder": 123456, "url": "https://www.flow.cl/app/pay.php", "token": "tok_123456" }

# Obtiene la URL de pago
print(f"URL de pago: {pago.url}?token={pago.token}")
> URL de pago: https://www.flow.cl/app/pay.php?token=tok_123456
```

## Obtener estado de un pago

Existen varias operaciones que nos permiten obtener el estado de un pago:

* payment_getstatus
* payment_getstatusbycommerceid
* payment_getstatusbyfloworder
* payment_getstatusextended
* payment_getstatusbyfloworderextended

Usaremos `payment_getstatusbycommerceid` para buscar el estado del pago generado en el paso anterior.

``` py
from pyflowcl import FlowAPI
from pyflowcl.utils import genera_parametros

api = FlowAPI(api_key="tu llave flow", api_secret="tu secreto flow")
parametros = {"apiKey": api.api_key, "token": "tok_123456"}
estado = api.objetos.call_get_payment_getstatus(parameters=genera_parametros(parametros, api.secretKey))
print(estado)
> { "flowOrder": 123456, "commerceOrder": "com_123456", "status": 2, ...}
```
