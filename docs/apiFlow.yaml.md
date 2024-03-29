Archivo original extraido desde [https://www.flow.cl/docs/apiFlow.yaml?v=6](https://www.flow.cl/docs/apiFlow.yaml?v=6)
```yaml
openapi: 3.0.0
servers:
  - url: 'https://www.flow.cl/api'
    description: Production server (uses live data)
  - url: 'https://sandbox.flow.cl/api'
    description: Sandbox server (uses test data)
info:
  description: |
    # Introducción

    Bienvenido a la documentacion de referencia del **API REST** de Flow!
    [REST](http://en.wikipedia.org/wiki/REST_API) es un protocolo de servicio web que se presta para un desarrollo rápido mediante el uso de la tecnología HTTP y JSON.

    La API REST de Flow proporciona un amplio conjunto de operaciones y recursos para:

    - Payments (Pagos)

    - Customer (Clientes, cobros, cargos automáticos)

    - Refunds (Reembolsos)

    - Subscriptions (Suscripciones, cobros recurrentes)

    - Coupons (Cupones de descuento para subscripciones)

    - Settlement (Liquidaciones de pagos, reembolsos y comisiones,)

    - Merchants (Gestión de comercios asociados)

    ## Versionamiento
    La API se encuentra en constante crecimiento, añadiendo nuevos servicios y/o mejorando funcionalidades existentes para que nuestros clientes puedan sacar el mayor provecho posible a sus integraciones. Por lo mismo, cada vez que se hacen cambios en la API se considera que son <b>compatibles con la versiones anteriores</B>.

    Ahora bien, FLOW considera los siguientes cambios como compatibles con versiones anteriores:

    - Añadir nuevos servicios
    - Añadir nuevos parámetros opcionales a servicios existentes
    - Añadir nuevas propiedades a respuestas de servicios existentes
    - Modificar el orden de las propiedades en respuestas existentes

    Debido a lo anterior es que instamos a nuestros clientes a que consideren estos aspectos en sus integraciones, para evitar inconvenientes con nuevas versiones.

    Para más información en relación a los cambios pueden revisar el <a href='api_changelog.txt' download target='_blank'>API changelog</a> y suscribirse a nuestra <a href='https://groups.google.com/d/forum/api-list-flow-cl' download target='_blank'>lista de correos</a> para enterarse de anuncios de la API.

    ## Acceso al API

    SI tienes una cuenta en Flow, puedes acceder al API REST mediante los siguientes endpoints:

    <table>
      <thead>
        <tr>
          <th>Site</th>
          <th>Base URL for Rest Endpoints</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Production</td>
          <td>https://www.flow.cl/api</td>
        </tr>
         <tr>
          <td>Sandbox</td>
          <td>https://sandbox.flow.cl/api</td>
        </tr>
      </tbody>
    </table>

    El endpoint de Producción proporciona acceso directo para generar transacciones reales. El endpoint Sandbox permite probar su integración sin afectar los datos reales.

    ## Autenticación y Seguridad

    El API soporta como método de autenticación el **APIKey** y como seguridad, los datos que usted envíe siempre deberían estar firmado con su **SecretKey**. De esta forma, Flow verifica que los datos enviados le pertenecen y que no fueron adulterados durante la transmisión de red.
    Además, los datos viajan encriptados con un canal seguro mediante **SSL.**

    Tanto su ApiKey como su SecretKey se obtienen desde su cuenta de Flow:
    <table>
      <thead>
        <tr>
          <th>Sitio</th>
          <th>Mi cuenta Flow</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Production</td>
          <td><a href='https://www.flow.cl/app/web/misDatos.php'>https://www.flow.cl/app/web/misDatos.php</a> </td>
        </tr>
         <tr>
          <td>Sandbox</td>
          <td><a href='https://sandbox.flow.cl/app/web/misDatos.php'>https://sandbox.flow.cl/app/web/misDatos.php</a></td>
        </tr>
      </tbody>
    </table>

    ## ¿Cómo firmar con su SecretKey?
    Se deben firmar todos los parámetros menos el parámetro **s** que es donde va la firma.
    Primero se deben ordenar los parámetros de forma alfabética ascendente en base al nombre del parámetro.

    Una vez ordenados, se deben concatenar en un string los parámetros de la siguiente forma:

    Nombre_del_parametro  **valor**  nombre_del_parametro  **valor**.

    **Ejemplo:**

    Si sus parámetros son:
    - "apiKey" = "XXXX-XXXX-XXXX"
    - "currency" = "CLP"
    - "amount" = 5000

    El string ordenado para firmar deberia ser:

    **"amount5000apiKeyXXXX-XXXX-XXXXcurrencyCLP"**



    El string concatenado se debe firmar con la función **hmac** utilizando el algoritmo **sha256** y su **secretKey** como llave.


    ### Ejemplo PHP
    Ordenando los parámetros:
    ```php
    $params = array(
      "apiKey" => "1F90971E-8276-4715-97FF-2BLG5030EE3B,
      "token" = "AJ089FF5467367"
    );
    $keys = array_keys($params);
    sort($keys);
    ```
    Concatenando:
    ```php
    $toSign = "";
    foreach($keys as $key) {
      $toSign .= $key . $params[$key];
    };
    ```
    Firmando:
    ```php
    $signature = hash_hmac('sha256', $toSign , $secretKey);
    ```
    ### Ejemplos de firmado:

    **PHP:**
    ```php
    $sign = hash_hmac('sha256', $string_to_sign, $secretKey);
    ```

    **Java:**
    ```java
    String sign = hmacSHA256(secretKey, string_to_sign);
    ```

    **Ruby:**
    ```ruby
    OpenSSL::HMAC.hexdigest(OpenSSL::Digest.new('sha256'),secret_key,string_to_sign);
    ```

     **Javascript:**
    ```javascript
    var sign = CryptoJS.HmacSHA256(stringToSign, secretKey);
    ```

    ## Consumiendo servicios método GET
    Una vez obtenida la firma de los parámetros, agregue al resto de los parámetros el parámetro **s** con el valor del hash obtenido en el proceso de firma.
    ### Ejemplo PHP:
    ```php
    $url = 'https://www.flow.cl/api';
    // Agrega a la url el servicio a consumir
    $url = $url . '/payment/getStatus';
    // agrega la firma a los parámetros
    $params["s"] = $signature;
    //Codifica los parámetros en formato URL y los agrega a la URL
    $url = $url . "?" . http_build_query($params);
    try {
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
        $response = curl_exec($ch);
        if($response === false) {
          $error = curl_error($ch);
          throw new Exception($error, 1);
        }
        $info = curl_getinfo($ch);
        if(!in_array($info['http_code'], array('200', '400', '401')) {
          throw new Exception('Unexpected error occurred. HTTP_CODE: '.$info['http_code'] , $info['http_code']);
        }
        echo $response;
        } catch (Exception $e) {
          echo 'Error: ' . $e->getCode() . ' - ' . $e->getMessage();
        }
    ```

    ## Consumiendo servicios método POST
    Una vez obtenida la firma de los parámetros, agregue al resto de los parámetros el parámetro **s** con el valor del hash obtenido en el proceso de firma.

    ### Ejemplo PHP:
    ```php
    $url = 'https://www.flow.cl/api';
    // Agrega a la url el servicio a consumir
    $url = $url . '/payment/create';
    //Agrega la firma a los parámetros
    $params["s"] = $signature;
    try {
      $ch = curl_init();
      curl_setopt($ch, CURLOPT_URL, $url);
      curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
      curl_setopt($ch, CURLOPT_POST, TRUE);
      curl_setopt($ch, CURLOPT_POSTFIELDS, $params);
      $response = curl_exec($ch);
      if($response === false) {
        $error = curl_error($ch);
        throw new Exception($error, 1);
      }
      $info = curl_getinfo($ch);
      if(!in_array($info['http_code'], array('200', '400', '401')) {
        throw new Exception('Unexpected error occurred. HTTP_CODE: '.$info['http_code'] , $info['http_code']);
      }
      echo $response;
    } catch (Exception $e) {
      echo 'Error: ' . $e->getCode() . ' - ' . $e->getMessage();
    }
    ```

    ## Notificaciones de Flow a su comercio
    Para todas las transaciones asíncronas **Flow** envía a su comercio notificaciones a sus páginas de callback, por medio de request via **POST**, content-type: **application/x-www-form-urlencoded**, enviando como parámetro un **token**, con este token el comercio debe invocar el servicio correspondiente que responde con los datos. Por ejemplo:
    Para crear un pago, en el servicio **payment/create** el comercio envía como uno de los parámetros **urlConfirmation**, que corresponde a la url donde **Flow** notificará el estado del pago. En esta página, el comercio recibirá el **token** y deberá invocar el servicio **payment/getStatus** para obtener el resultado del pago.
    ### Transacciones asíncronas:

    <table>
      <thead>
        <tr>
          <th>Servicio</th>
          <th>Url callback</th>
          <th>Método para obtener el resultado</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>payment/create</td>
          <td>urlConfirmation</td>
          <td>payment/getStatus</td>
        </tr>
         <tr>
          <td>payment/createEmail</td>
          <td>urlConfirmation</td>
          <td>payment/getStatus</td>
        </tr>
        <tr>
          <td>refund/create</td>
          <td>urlCallback</td>
          <td>refund/getStatus</td>
        </tr>
        <tr>
          <td>customer/register</td>
          <td>url_return</td>
          <td>customer/getRegisterStatus</td>
        </tr>
        <tr>
          <td>customer/collect</td>
          <td>urlConfirmation</td>
          <td>payment/getStatus</tr>
        </tr>
          <td>customer/batchCollect</td>
          <td>urlCallback</td>
          <td>customer/getBatchCollectStatus</td>
        </tr>
        <tr>
          <td>customer/batchCollect</td>
          <td>urlConfirmation</td>
          <td>payment/getStatus</td>
        </tr>
      </tbody>
    </table>

    ## Códigos de error de intentos de pago
    Al utilizar los servicios extendidos **payment/getStatusExtended** y **payment/getStatusByFlowOrderExtended** se puede obtener la información de error en el último intento de pago. Los códigos existentes son:

    <table>
      <thead>
        <tr>
          <th>Código</th>
          <th>Descripción</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>-1</td>
          <td>Tarjeta inválida</td>
        </tr>
        <tr>
          <td>-11</td>
          <td>Excede límite de reintentos de rechazos</td>
        </tr>
        <tr>
          <td>-2</td>
          <td>Error de conexión</td>
        </tr>
        <tr>
          <td>-3</td>
          <td>Excede monto máximo</td>
        </tr>
        <tr>
          <td>-4</td>
          <td>Fecha de expiración inválida</td>
        </tr>
        <tr>
          <td>-5</td>
          <td>Problema en autenticación</td>
        </tr>
        <tr>
          <td>-6</td>
          <td>Rechazo general</td>
        </tr>
        <tr>
          <td>-7</td>
          <td>Tarjeta bloqueada</td>
        </tr>
        <tr>
          <td>-8</td>
          <td>Tarjeta vencida</td>
        </tr>
        <tr>
          <td>-9</td>
          <td>Transacción no soportada</td>
        </tr>
        <tr>
          <td>-10</td>
          <td>Problema en la transacción</td>
        </tr>
        <tr>
          <td>999</td>
          <td>Error desconocido</td>
        </tr>
      </tbody>
    </table>

    ## Paginación
    Todos los servicios cuyo resultado son listas **Flow** entrega los resultados paginados. La cantidad de registros por página y la navegación por las distintas páginas se controlan con los siguientes parámetros:

    <table>
      <thead>
        <tr>
          <th>Parámetro</th>
          <th>Descripción</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>start</td>
          <td>número de registro de inicio de la página. Si se omite el valor por omisión es 0.</td>
        </tr>
        <tr>
          <td>limit</td>
          <td>número de registros por página. Si se omite el valor por omisón es 10. El valor máximo es de 100 registros por página.</td>
        </tr>
      </tbody>
    </table>

    Todos los servicios de paginación retornan un objeto JSON con los siguientes datos:
    ```
    {
      "total": número de registros totales,
      "hasMore": 1 Si hay más páginas, 0 si no hay,
      "data": [{}] arreglo con los registros
    }
    ```

    Para recorrer las páginas, si como resultado **hasMore** es 1, entonces suma el valor del parámetro **limit** al parámetro **start** y vuelve a invocar el servicio hasta que **hasMore** retorne 0

    ## Clientes API
    Disponemos de los siguientes clientes API Rest que facilitan la integración con Flow:
    <table>
      <thead>
        <tr>
          <th>Lenguage</th>
          <th>URL de descarga</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>PHP</td>
          <td><a href='https://github.com/flowcl/PHP-API-CLIENT' target='_blank'>https://github.com/flowcl/PHP-API-CLIENT</a></td>
        </tr>
      </tbody>
    </table>

    ## Postman
    Disponemos de Collections de Postman para probar el consumo de los distintos servicios del API. Estas colecciones están agrupadas por funcionalidades y vienen con el algoritmo de firmado pre-programado.

    **¿Que es Postman?** Postman es una herramienta que permite crear peticiones sobre APIs de una forma muy sencilla y poder, de esta manera, probar las APIs

    Puede descargar Postman aquí: <a href='https://www.getpostman.com/downloads/' target='_blank'>Postman download</a>

    Para utilizarlos, deberá crear **Environment** con las siguientes variables de ambiente:
    - apiKey: apiKey obtenida de su cuenta Flow
    - secretKey: secretKey obtenida de su cuenta Flow
    - Hosting: **sandbox.flow.cl** para ambiente sandbox o **www.flow.cl** para ambiente productivo.


    Puede descargar los archivos Collections para Postman aquí:
    <table>
      <thead>
        <tr>
          <th>Collection</th>
          <th>URL de descarga</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Flow Payment</td>
          <td><a href='Flow Payment.postman_collection.json' download target='_blank'>Flow Payment.postman_collection.json</a></td>
        </tr>
        <tr>
          <td>Flow Customer</td>
          <td><a href='Flow Customer.postman_collection.json' download target='_blank'>Flow Customer.postman_collection.json</a></td>
        </tr>
        <tr>
          <td>Flow Plans</td>
          <td><a href='Flow Plans.postman_collection.json' download target='_blank'>Flow Plans.postman_collection.json</a></td>
        </tr>
        <tr>
          <td>Flow Subscription</td>
          <td><a href='Flow Subscription.postman_collection.json' download target='_blank'>Flow Subscription.postman_collection.json</a></td>
        </tr>
        <tr>
          <td>Flow Coupon</td>
          <td><a href='Flow Coupon.postman_collection.json' download target='_blank'>Flow Coupon.postman_collection.json</a></td>
        </tr>
        <tr>
          <td>Flow Invoices</td>
          <td><a href='Flow Invoices.postman_collection.json' download target='_blank'>Flow Invoices.postman_collection.json</a></td>
        </tr>
        <tr>
          <td>Flow Refund</td>
          <td><a href='Flow Refund.postman_collection.json' download target='_blank'>Flow Refund.postman_collection.json</a></td>
        </tr>
        <tr>
          <td>Flow Settlements</td>
          <td><a href='Flow Settlements.postman_collection.json' download target='_blank'>Flow Settlements.postman_collection.json</a></td>
        </tr>
        <tr>
          <td>Flow Merchant</td>
          <td><a href='Flow Merchant.postman_collection.json' download target='_blank'>Flow Merchant.postman_collection.json</a></td>
        </tr>
      </tbody>
    </table>

    ## Realizar pruebas en nuestro ambiente Sandbox
    Puede realizar pruebas en nuestro ambiente Sandbox para los distintos medios de pagos.

    Para realizar pruebas de pago con Webpay o registrar una tarjeta de crédito para cargo automático utilice los siguientes datos:

    ### Tarjeta de crédito

    <table>
      <thead>
        <tr>
          <th>Dato</th>
          <th>Valor</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>N° tarjeta de crédito</td>
          <td>4051885600446623</td>
        </tr>
        <tr>
          <td>Año de expiración</td>
          <td>Cualquiera</td>
        </tr>
        <tr>
          <td>Mes de expiración</td>
          <td>Cualquiera</td>
        </tr>
        <tr>
          <td>CVV</td>
          <td>123</td>
        </tr>
      </tbody>
    </table>

    ### En la simulación del banco usar:

    <table>
      <thead>
        <tr>
          <th>Dato</th>
          <th>Valor</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Rut</td>
          <td>11111111-1</td>
        </tr>
        <tr>
          <td>Clave</td>
          <td>123</td>
        </tr>
      </tbody>
    </table>

    ### Para los medios de pago:
    - Servipag
    - Multicaja
    - Mach
    - Cryptocompra

    Se presentan simuladores de pago, donde sólo debe hacer clic en el botón aceptar.

  version: "3.0.1"
  title: Flow API
  termsOfService: "https://www.flow.cl/terminos.php"
  contact:
    email: soporte@flow.cl
  license:
    name: Apache 2.0
    url: 'http://www.apache.org/licenses/LICENSE-2.0.html'
  x-logo:
    url: 'https://www.flow.cl/images/header/logo-flow.svg'
tags:
  - name: payment
    description: |
      Creación de transacciones de pagos y cobros por email. Utilice el servicio **payment/create** para crear links de pagos o **payment/createEmail** para crear cobros por email.
  - name: refund
    description: 'Permite generar reembolsos y obtener el estado de estos.'
  - name: customer
    description: "Permite crear clientes para efectuarles cargos recurrentes o suscribirlos a un planes de suscripción. Una vez creado un cliente, **Flow** lo identificará por un hash denominado **customerId**, ejemplo:\n\n **customerId**: cus_onoolldvec "
  - name: plans
    description: 'Permite crear planes de suscripción'
  - name: subscription
    description: 'Permite suscribir clientes a un plan de suscripción.'
  - name: coupon
    description: "Permite crear cupones de descuento para ser aplicados a suscripciones o clientes"
  - name: invoice
    description: 'Permite obtener los importes que se han generado por medio de las suscripciones.'
  - name: settlement
    description: 'Permite obtener las liquidaciones de pagos efectuadas por Flow'
  - name: merchant
    description: 'Permite gestionar los comercios asociados'
paths:
  /payment/getStatus:
    get:
      tags:
        - payment
      summary: Obtiene el estado de una orden de pago.
      description: 'Este método se utiliza para obtener el estado de un pago. Se debe utilizar en la página callback del comercio para recibir notificaciones de pagos. Cada vez que el pagador efectúe un pago, **Flow** enviará vía POST una llamada a la página del comercio, pasando como parámetro un **token** que deberá utilizarse en este servicio.'
      parameters:
        - in: query
          name: apiKey
          description: apiKey del comercio
          required: true
          schema:
            type: string
        - in: query
          name: token
          description: token de la transacción enviado por Flow
          required: true
          schema:
            type: string
        - in: query
          name: s
          description: la firma de los parámetros efectuada con su secretKey
          required: true
          schema:
            type: string
      responses:
        '200':
          description: El objeto PaymentStatus
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PaymentStatus'
        '400':
          description: error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: error interno de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'

  /payment/getStatusByCommerceId:
    get:
      tags:
        - payment
      summary: 'Obtiene el estado de un pago en base al commerceId'
      description: 'Este método permite obtener el estado de un pago en base al **commerceId**'
      parameters:
        - in: query
          name: apiKey
          description: apiKey del comercio
          required: true
          schema:
            type: string
        - in: query
          name: commerceId
          description: Orden del comercio
          required: true
          schema:
            type: string
        - in: query
          name: s
          description: la firma de los parámetros efectuada con su secretKey
          required: true
          schema:
            type: string
      responses:
        '200':
          description: El objeto PaymentStatus
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PaymentStatus'
        '400':
          description: error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: error interno de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'

  /payment/getStatusByFlowOrder:
    get:
      tags:
        - payment
      summary: 'Obtiene el estado de un pago en base al número de orden Flow'
      description: 'Este método permite obtener el estado de un pago en base al **flowOrder**'
      parameters:
        - in: query
          name: apiKey
          description: apiKey del comercio
          required: true
          schema:
            type: string
        - in: query
          name: flowOrder
          description: número de orden Flow
          required: true
          schema:
            type: number
            example: 68977654
        - in: query
          name: s
          description: la firma de los parámetros efectuada con su secretKey
          required: true
          schema:
            type: string
      responses:
        '200':
          description: El objeto PaymentStatus
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PaymentStatus'
        '400':
          description: error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: error interno de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'

  /payment/getPayments:
    get:
      tags:
        - payment
      summary: 'Obtiene el listado de pagos recibidos en un día'
      description: 'Este método permite obtener la lista paginada de pagos recibidos en un día.Los objetos pagos de la lista tienen la misma estructura de los retornados en los servicios payment/getStatus'
      parameters:
        - in: query
          name: apiKey
          description: apiKey del comercio
          required: true
          schema:
            type: string
        - in: query
          name: date
          description: fecha de los pagos en formato yyyy-mm-dd
          required: true
          schema:
            type: string
        - in: query
          name: start
          description: Número de registro de inicio de la página. Si se omite el valor por omisión es 0.
          required: false
          schema:
            type: integer
        - in: query
          name: limit
          description: Número de registros por página. Si se omite el valor por omisón es 10. El valor máximo es de 100 registros por página.
          required: false
          schema:
            type: integer
        - in: query
          name: s
          description: la firma de los parámetros efectuada con su secretKey
          required: true
          schema:
            type: string
      responses:
        '200':
          description: "Lista paginada de pagos"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
  /payment/getStatusExtended:
    get:
      tags:
        - payment
      summary: Obtiene el estado extendido de una orden de pago.
      description: 'Este método se utiliza para obtener el estado de un pago. A diferencia del /payment/getStatus este servicio retorna el tipo de pago, los 4 últimos dígitos de la tarjeta (si el pago se hizo con tarjeta) y la información del último intento de pago. Se debe utilizar en la página callback del comercio para recibir notificaciones de pagos. Cada vez que el pagador efectúe un pago, **Flow** enviará vía POST una llamada a la página del comercio, pasando como parámetro un **token** que deberá utilizarse en este servicio.'
      parameters:
        - in: query
          name: apiKey
          description: apiKey del comercio
          required: true
          schema:
            type: string
        - in: query
          name: token
          description: token de la transacción enviado por Flow
          required: true
          schema:
            type: string
        - in: query
          name: s
          description: la firma de los parámetros efectuada con su secretKey
          required: true
          schema:
            type: string
      responses:
        '200':
          description: El objeto PaymentStatusExtended
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PaymentStatusExtended'
        '400':
          description: error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: error interno de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
  /payment/getStatusByFlowOrderExtended:
    get:
      tags:
        - payment
      summary: 'Obtiene el estado extendido de un pago en base al número de orden Flow'
      description: 'Este método permite obtener el estado de un pago en base al **flowOrder**. A diferencia del /payment/getStatusByFlowOrder este servicio retorna el tipo de pago, los 4 últimos dígitos de la tarjeta (si el pago se hizo con tarjeta) y la información del último intento de pago.'
      parameters:
        - in: query
          name: apiKey
          description: apiKey del comercio
          required: true
          schema:
            type: string
        - in: query
          name: flowOrder
          description: número de orden Flow
          required: true
          schema:
            type: number
            example: 68977654
        - in: query
          name: s
          description: la firma de los parámetros efectuada con su secretKey
          required: true
          schema:
            type: string
      responses:
        '200':
          description: El objeto PaymentStatusExtended
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PaymentStatusExtended'
        '400':
          description: error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: error interno de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'

  /payment/create:
    post:
      tags:
        - payment
      summary: Genera una orden de pago
      description: "Este método permite crear una orden de pago a **Flow** y recibe como respuesta la **URL** para redirigir el browser del pagador y el **token** que identifica la transacción. La url de redirección se debe formar concatenando los valores recibidos en la respuesta de la siguiente forma:\n\n **url** + \"?token=\" +**token**\n\n
      Una vez que el pagador efectúe el pago, **Flow** notificará el resultado a la página del comercio que se envió en el parámetro **urlConfirmation**."
      responses:
        '200':
          description: "url y token para redirigir el browser del pagador La url de redirección se debe formar concatenando los valores recibidos en la respuesta de la siguiente forma:\n\n **url** + \"?token=\" +**token**"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PayResponse'
        '400':
          description: "Error del Api"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: "Error de negocio"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
      requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              properties:
                apiKey:
                  description: apiKey del comercio
                  type: string
                commerceOrder:
                  description: Orden del comercio
                  type: string
                subject:
                  description: Descripción de la orden
                  type: string
                currency:
                  description: Moneda de la orden
                  type: string
                amount:
                  description: Monto de la orden
                  type: number
                email:
                  description: email del pagador
                  type: string
                  format: email
                paymentMethod:
                  description: |
                    Identificador del medio de pago. Si se envía el identificador, el pagador será redireccionado directamente al medio de pago que se indique, de lo contrario Flow le presentará una página para seleccionarlo. El medio de pago debe haber sido previamente contratado. Podrá ver los identificadores de sus medios de pago en la sección "Mis Datos" ingresando a Flow con sus credenciales. Para indicar todos los medios de pago utilice el identificador:
                    - 9 Todos los medios
                  type: integer
                urlConfirmation:
                  description: url callback del comercio donde Flow confirmará el pago
                  type: string
                  format: uri
                urlReturn:
                  description: url de retorno del comercio donde Flow redirigirá al pagador
                  type: string
                  format: uri
                optional:
                  description: |
                    Datos opcionales en formato JSON clave = valor, ejemplo:
                      {"rut":"9999999-9","nombre":"cliente 1"}
                  type: string
                timeout:
                  description: tiempo en segundos para que una orden expire después de haber sido creada. Si no se envía este parámetro la orden no expirará y estará vigente para pago por tiempo indefinido. Si envía un valor en segundos, la orden expirará x segundos después de haber sido creada y no podrá pagarse.
                  type: integer
                merchantId:
                  description: Id de comercio asociado. Solo aplica si usted es comercio integrador.
                  type: string
                payment_currency:
                  description: Moneda en que se espera se pague la orden
                  type: string
                s:
                  description: la firma de los parámetros efectuada con su secretKey
                  type: string
              required:
                - apiKey
                - commerceOrder
                - subject
                - amount
                - email
                - urlConfirmation
                - urlReturn
                - s
      callbacks:
        paymentConfirmation:
          '{$request#/urlConfirmation}':
            post:
              requestBody:
                content:
                  application/x-www-form-urlencoded:
                    schema:
                      type: object
                      properties:
                        token:
                          description: hash token que identifica la transacción
                          type: string
              responses:
                '200':
                  description: Your server returns this code if it accepts the callback



  /payment/createEmail:
    post:
      tags:
        - payment
      summary: Genera un cobro por email
      description: "Permite generar un cobro por email. **Flow** emite un email al pagador que contiene la información de la Orden de pago y el link de pago correspondiente. Una vez que el pagador efectúe el pago, **Flow** notificará el resultado a la página del comercio que se envió en el parámetro **urlConfirmation**."
      responses:
        '200':
          description: "Al crear un cobro por email, Flow enviará el email directamente al pagador con un link de pago. El link de pago se forma  concatenando los valores recibidos en la respuesta de la siguiente forma:\n\n **url** + \"?token=\" +**token**"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PayResponse'
        '400':
          description: Error del api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
      requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              properties:
                apiKey:
                  description: apiKey del comercio
                  type: string
                commerceOrder:
                  description: Orden del comercio
                  type: string
                subject:
                  description: Descripción de la orden
                  type: string
                currency:
                  description: Moneda de la orden
                  type: string
                amount:
                  description: Monto de la orden
                  type: number
                email:
                  description: email del pagador
                  type: string
                  format: email
                urlConfirmation:
                  description: url callbak del comercio donde Flow confirmará el pago
                  type: string
                  format: uri
                urlReturn:
                  description: url de retorno del comercio donde Flow redirigirá al pagador
                  type: string
                  format: uri
                forward_days_after:
                  description: Número de días posteriores al envío del cobro para enviar una nueva notificación de persistencia si la orden no está pagada.
                  type: number
                forward_times:
                  description: Número de veces de envío de mail de persistencia.
                  type: number
                optional:
                  description: |
                    Datos opcionales en formato JSON clave = valor, ejemplo:
                      {"rut":"9999999-9","nombre":"cliente 1"}
                  type: string
                timeout:
                  description: tiempo en segundos para que una orden expire después de haber sido creada. Si no se envía este parámetro la orden no expirará y estará vigente para pago por tiempo indefinido. Si envía un valor en segundos, la orden expirará x segundos después de haber sido creada y no podrá pagarse.
                  type: integer
                merchantId:
                  description: Id de comercio asociado. Solo aplica si usted es comercio integrador.
                  type: string
                payment_currency:
                  description: Moneda en que se espera se pague la orden
                  type: string
                s:
                  description: la firma de los parámetros efectuada con su secretKey
                  type: string
              required:
                - apiKey
                - commerceOrder
                - subject
                - amount
                - email
                - urlConfirmation
                - urlReturn
                - s

  /refund/create:
    post:
      tags:
        - refund
      summary: "Permite crear un reembolso"
      description: "Este servicio permite crear una orden de reembolso. Una vez que el receptor del reembolso acepte o rechaze el reembolso, **Flow** notificará vía POST a la página del comercio identificada en **urlCallback** pasando como parámetro **token**\n\n
      En esta página, el comercio debe invocar el servicio **refund/getStatus** para obtener el estado del reembolso."
      responses:
        '200':
          description: El objeto RefundStatus
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RefundStatus'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
      requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              properties:
                apiKey:
                  description: apiKey del comercio
                  type: string
                refundCommerceOrder:
                  description: La orden de reembolso del comercio
                  type: string
                receiverEmail:
                  description: Email del receptor del reembolso
                  type: string
                amount:
                  description: Monto del reembolso
                  type: number
                urlCallBack:
                  description: La url callback del comercio donde Flow comunica el estado del reembolso
                  type: string
                commerceTrxId:
                  description: Identificador del comercio de la transacción original que se va reembolsar
                  type: string
                flowTrxId:
                  description: Identificador de Flow de la transacción original que se va reembolsar.
                  type: string
                s:
                  description: la firma de los parámetros efectuada con su secretKey
                  type: string
              required:
                - apiKey
                - refundCommerceOrder
                - receiverEmail
                - amount
                - urlCallBack
                - s

  /refund/cancel:
    post:
      tags:
        - refund
      summary: "Permite cancelar un reembolso"
      description: "Este servicio permite cancelar una orden de reembolso pendiente"
      responses:
        '200':
          description: El objeto RefundStatus
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RefundStatus'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
      requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              properties:
                apiKey:
                  description: apiKey del comercio
                  type: string
                token:
                  description: El token devuelto al crear el reembolso
                  type: string
                s:
                  description: la firma de los parámetros efectuada con su secretKey
                  type: string
              required:
                - apiKey
                - token
                - s

  /refund/getStatus:
    get:
      tags:
        - refund
      summary: "Obtiene el estado de un reemboso."
      description: "Permite obtener el estado de un reembolso solicitado. Este servicio se debe invocar desde la página del comercio que se señaló en el parámetro **urlCallback** del servicio **refund/create**."
      parameters:
        - in: query
          name: apiKey
          description: apiKey del comercio
          required: true
          schema:
            type: string
        - in: query
          name: token
          description: token de la solicitud de reembolso enviado por Flow
          required: true
          schema:
            type: string
        - in: query
          name: s
          description: la firma de los parámetros efectuada con su secretKey
          required: true
          schema:
            type: string
      responses:
        '200':
          description: El objeto RefundStatus
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RefundStatus'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'

  #<--- Customer
  /customer/create:
    post:
      tags:
        - customer
      summary: "Crear un cliente"
      description: "Permite crear un nuevo cliente. El servicio retorna el objeto cliente creado."
      responses:
        '200':
          description: El objeto Customer
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Customer'
        '400':
          description: error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
      requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              properties:
                apiKey:
                  description: apiKey del comercio
                  type: string
                name:
                  description: Nombre del cliente (nombre y apellido)
                  type: string
                email:
                  description: Email del cliente
                  type: string
                externalId:
                  description: Identificador externo del cliente, es decir, el identificador con el que su sistema lo reconoce.
                  type: string
                s:
                  description: la firma de los parámetros efectuada con su secretKey
                  type: string
              required:
                - apiKey
                - name
                - email
                - externalId
                - s
  /customer/edit:
    post:
      tags:
        - customer
      summary: "Edita un cliente"
      description: "Este servicio permite editar los datos de un cliente"
      responses:
        '200':
          description: "El objeto cliente"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Customer'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
      requestBody:
        description: "Los campos: name, email y externalId son opcionales. Si desea modificar solo el nombre, envíe solo en campo name."
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              properties:
                apiKey:
                  description: apiKey del comercio
                  type: string
                customerId:
                  description: Identificador del cliente
                  type: string
                name:
                  description: Nombre del cliente
                  type: string
                email:
                  description: Email del cliente
                  type: string
                externalId:
                  description: Identificador externo del cliente, es decir, el identificador con el que su sistema lo reconoce.
                  type: string
                s:
                  description: la firma de los parámetros efectuada con su secretKey
                  type: string
              required:
                - apiKey
                - customerId
                - s

  /customer/delete:
    post:
      tags:
        - customer
      summary: "Eliminar un cliente"
      description: "Permite eliminar un cliente. Para eliminar un cliente, este no debe tener suscripciones activas o importes pendientes de pago."
      responses:
        '200':
          description: "El objeto cliente"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Customer'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
      requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              properties:
                apiKey:
                  description: apiKey del comercio
                  type: string
                customerId:
                  description: Identificador del cliente
                  type: string
                s:
                  description: la firma de los parámetros efectuada con su secretKey
                  type: string
              required:
                - apiKey
                - customerId
                - s
  /customer/get:
    get:
      tags:
        - customer
      summary: "Obtiene los datos de un cliente"
      description: "Permite obtener los datos de un cliente en base a su **customerId**."
      parameters:
        - in: query
          name: apiKey
          description: apiKey del comercio
          required: true
          schema:
            type: string
        - in: query
          name: customerId
          description: Identificador del cliente
          required: true
          schema:
            type: string
        - in: query
          name: s
          description: la firma de los parámetros efectuada con su secretKey
          required: true
          schema:
            type: string
      responses:
        '200':
          description: "El objeto cliente"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Customer'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
  /customer/list:
    get:
      tags:
        - customer
      summary: "Lista de clientes"
      description: "Permite obtener la lista de clientes paginada de acuerdo a los parámetros de paginación. Además, se puede definir los siguientes filtros:\n\n
      * filter: filtro por nombre del cliente\n
      * status: filtro por estado del cliente"
      parameters:
        - in: query
          name: apiKey
          description: apiKey del comercio
          required: true
          schema:
            type: string
        - in: query
          name: start
          description: Número de registro de inicio de la página. Si se omite el valor por omisión es 0.
          required: false
          schema:
            type: integer
        - in: query
          name: limit
          description: Número de registros por página. Si se omite el valor por omisón es 10. El valor máximo es de 100 registros por página.
          required: false
          schema:
            type: integer
        - in: query
          name: filter
          description: Filtro por nombre del cliente
          required: false
          schema:
            type: string
        - in: query
          name: status
          description: Filtro por estado del cliente
          required: false
          schema:
            type: integer
        - in: query
          name: s
          description: la firma de los parámetros efectuada con su secretKey
          required: true
          schema:
            type: string
      responses:
        '200':
          description: "Lista paginada de clientes"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
  /customer/register:
    post:
      tags:
        - customer
      summary: "Envía a un cliente a registrar su tarjeta de crédito"
      description: |
        Envía a un cliente a registrar su tarjeta de crédito para poder efectuarle cargos automáticos.
        El servicio responde con la **URL** para redirigir el browser del pagador y el **token** que identifica la transacción. La **url** de redirección se debe formar concatenando los valores recibidos en la respuesta de la siguiente forma:
          > **url** + "?token=" +**token**

        Una vez redirigido el browser del cliente, Flow responderá por medio de una llamada POST a la url callback del comercio indicada en el parámetro **url_return** pasando como parámetro **token**. El comercio debe implementar una página y capturar el parámetro token enviado por Flow para luego consumir el servicio "customer/getRegisterStatus" para obtener el resultado del registro.
      responses:
        '200':
          description: "Url y token para redireccionar el browser del cliente a registrar su tarjeta de crédito"
          content:
            application/json:
              schema:
                type: object
                properties:
                  url:
                    type: string
                    example: 'https://www.flow.cl/app/webpay/disclaimer.php'
                  token:
                    type: string
                    example: 41097C28B5BD78C77F589FE4BC59E18AC333F9EU
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
      requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              properties:
                apiKey:
                  description: apiKey del comercio
                  type: string
                customerId:
                  description: Identificador del cliente
                  type: string
                url_return:
                  description: "Url de página callback donde Flow notifica el resultado del registro"
                  type: string
                s:
                  description: la firma de los parámetros efectuada con su secretKey
                  type: string
              required:
                - apiKey
                - customerId
                - url_return
                - s
  /customer/getRegisterStatus:
    get:
      tags:
        - customer
      summary: "Resultado de registro de tarjeta de crédito de un cliente"
      description: "Elte servicio retorna el resultado del registro de la tarjeta de crédito de un cliente."
      parameters:
        - in: query
          name: apiKey
          description: apiKeydel comercio
          required: true
          schema:
            type: string
        - in: query
          name: token
          description: El token enviado por Flow a su página callback.
          required: true
          schema:
            type: string
        - in: query
          name: s
          description: la firma de los parámetros efectuada con su secretKey
          required: true
          schema:
            type: string
      responses:
        '200':
          description: "Resultado del registro de tarjeta de crédito"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RegisterResult'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'

  /customer/unRegister:
    post:
      tags:
        - customer
      summary: "Elimina el registro de la tarjeta de crédito de un cliente"
      description: "Este servicio permite eliminar el registro de la tarjeta de crédito de un cliente. Al eliminar el registro no se podrá hacer cargos automáticos y Flow enviará un cobro por email."
      responses:
        '200':
          description: "El objeto cliente"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Customer'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
      requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              properties:
                apiKey:
                  description: apiKey del comercio
                  type: string
                customerId:
                  description: Identificador del cliente
                  type: string
                s:
                  description: la firma de los parámetros efectuada con su secretKey
                  type: string
              required:
                - apiKey
                - customerId
                - s

  /customer/charge:
    post:
      tags:
        - customer
      summary: "Efectúa un cargo en la tarjeta de crédito un cliente"
      description: "Este servicio permite efectuar un cargo automático en la tarjeta de crédito previamente registrada por el cliente. Si el cliente no tiene registrada una tarjeta el metodo retornará error."
      responses:
        '200':
          description: El objeto PaymentStatus
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PaymentStatus'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
      requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              properties:
                apiKey:
                  description: apiKey del comercio
                  type: string
                customerId:
                  description: Identificador del cliente
                  type: string
                amount:
                  description: El monto del cargo
                  type: number
                subject:
                  description: Descripción del cargo
                  type: string
                commerceOrder:
                  description: Identificador de la orden del comercio
                  type: string
                currency:
                  description: Moneda del cargo (CLP, UF)
                  type: string
                optionals:
                  description: |
                    Datos opcionales en formato JSON clave = valor, ejemplo:
                      {"rut":"9999999-9","nombre":"cliente 1"}
                  type: string
                s:
                  description: la firma de los parámetros efectuada con su secretKey
                  type: string
              required:
                - apiKey
                - customerId
                - amount
                - subject
                - commerceOrder
                - s

  /customer/collect:
    post:
      tags:
        - customer
      summary: "Envía un cobro a un cliente."
      description: "Este servicio envía un cobro a un cliente. Si el cliente tiene registrada una tarjeta de crédito se le hace un cargo automático, si no tiene registrada una tarjeta de credito se genera un cobro. Si se envía el parámetro byEmail = 1, se genera un cobro por email."
      responses:
        '200':
          description: El objeto CollectResponse
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CollectResponse'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
      requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              properties:
                apiKey:
                  description: apiKey del comercio
                  type: string
                customerId:
                  description: Identificador del cliente
                  type: string
                commerceOrder:
                  description: Identificador de la orden del comercio
                  type: string
                subject:
                  description: Descripción del cobro
                  type: string
                amount:
                  description: El monto del cobro
                  type: number
                urlConfirmation:
                  description: url callbak del comercio donde Flow confirmará el pago
                  type: string
                  format: uri
                urlReturn:
                  description: url de retorno del comercio donde Flow redirigirá al pagador
                  type: string
                  format: uri
                currency:
                  description: Moneda del cargo (CLP, UF)
                  type: string
                paymentMethod:
                  description: |
                    Identificador del medio de pago. Si se envía el identificador, el pagador será redireccionado directamente al medio de pago que se indique, de lo contrario Flow le presentará una página para seleccionarlo. El medio de pago debe haber sido previamente contratado. Podrá ver los identificadores de sus medios de pago en la sección "Mis Datos" ingresando a Flow con sus credenciales. Para indicar todos los medios de pago utilice el identificador:
                    - 9 Todos los medios
                  type: integer
                byEmail:
                  description: Si se desea que Flow envíe cobros por email, este parámetro debe enviarse con valor 1
                  type: integer
                forward_days_after:
                  description: Número de días posteriores al envío del cobro para enviar una nueva notificación de persistencia si la orden no está pagada.
                  type: integer
                forward_times:
                  description: Número de veces de envío de mail de persistencia.
                  type: integer
                ignore_auto_charging:
                  description: Si se envía este parámetro con valor 1 entonces ignora el método de cargo automático aunque el cliente tenga registrada una tarjeta de crédito
                  type: integer
                optionals:
                  description: |
                    Datos opcionales en formato JSON clave = valor, ejemplo:
                      {"rut":"9999999-9","nombre":"cliente 1"}
                  type: string
                timeout:
                  description: tiempo en segundos para que una orden expire después de haber sido creada. Si no se envía este parámetro la orden no expirará y estará vigente para pago por tiempo indefinido. Si envía un valor en segundos, la orden expirará x segundos después de haber sido creada y no podrá pagarse.
                  type: integer
                s:
                  description: la firma de los parámetros efectuada con su secretKey
                  type: string
              required:
                - apiKey
                - customerId
                - amount
                - subject
                - commerceOrder
                - urlConfirmation
                - urlReturn
                - s

  /customer/batchCollect:
    post:
      tags:
        - customer
      summary: "Envía de forma masiva un lote de cobros a  clientes."
      description: Este servicio envía de forma masiva un lote de cobros a clientes. Similar al servicio collect pero masivo y asíncrono. Este servicio responde con un token identificador del lote y el número de filas recibidas.
      responses:
        '200':
          description: El objeto BatchCollectResponse
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BatchCollectResponse'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
      requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              properties:
                apiKey:
                  description: apiKey del comercio
                  type: string
                urlCallBack:
                  description: url callback del comercio donde Flow avisará cuando el lote ha sido procesado.
                  type: string
                  format: uri
                urlConfirmation:
                  description: url callbak del comercio donde Flow confirmará el pago
                  type: string
                  format: uri
                urlReturn:
                  description: url de retorno del comercio donde Flow redirigirá al pagador
                  type: string
                  format: uri
                batchRows:
                  description: Arreglo en formato JSON del lote de cargos CollectObject
                  type: array
                  items:
                    $ref: '#/components/schemas/CollectObject'
                byEmail:
                  description: Si se desea que Flow envíe cobros por email, este parámetro debe enviarse con valor 1
                  type: integer
                forward_days_after:
                  description: Número de días posteriores al envío del cobro para enviar una nueva notificación de persistencia si la orden no está pagada.
                  type: integer
                forward_times:
                  description: Número de veces de envío de mail de persistencia.
                  type: integer
                timeout:
                  description: tiempo en segundos para que una orden expire después de haber sido creada. Si no se envía este parámetro la orden no expirará y estará vigente para pago por tiempo indefinido. Si envía un valor en segundos, la orden expirará x segundos después de haber sido creada y no podrá pagarse.
                  type: integer
                s:
                  description: la firma de los parámetros efectuada con su secretKey
                  type: string
              required:
                - apiKey
                - commerceBatchId
                - urlCallBack
                - urlConfirmation
                - urlReturn
                - batchRows
                - s
      callbacks:
        batchCollectProcessConfirmation:
          '{$request#/urlCallBack}':
            post:
              requestBody:
                content:
                  application/x-www-form-urlencoded:
                    schema:
                      type: object
                      properties:
                        token:
                          description: hash token que identifica el lote procesado
                          type: string
              responses:
                '200':
                  description: Your server returns this code if it accepts the callback
        batchCollectPaymentConfirmatio:
          '{$request#/urlConfirmation}':
            post:
              requestBody:
                content:
                  application/x-www-form-urlencoded:
                    schema:
                      type: object
                      properties:
                        token:
                          description: hash token que identifica el pago
                          type: string
              responses:
                '200':
                  description: Your server returns this code if it accepts the callback
        batchCollectReturn:
          '{$request#/urlReturn}':
            post:
              requestBody:
                content:
                  application/x-www-form-urlencoded:
                    schema:
                      type: object
                      properties:
                        token:
                          description: hash token que identifica el pago
                          type: string
              responses:
                '200':
                  description: Your server returns this code if it accepts the callback

  /customer/getBatchCollectStatus:
    get:
      tags:
        - customer
      summary: "Obtiene el estado de un lote de cobros enviados por el servicio batchCollect"
      description: "Este servicio permite consultar el estado de un lote de cobros enviados por medio del servicio batchCollect."
      parameters:
        - in: query
          name: apiKey
          description: apiKey del comercio
          required: true
          schema:
            type: string
        - in: query
          name: token
          description: El token enviado por Flow a su página callback del servicio batchCollect.
          required: true
          schema:
            type: string
        - in: query
          name: s
          description: la firma de los parámetros efectuada con su secretKey
          required: true
          schema:
            type: string
      responses:
        '200':
          description: "Resultado del lote de cargos enviados por el servicio batchCollect"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BatchCollectStatusResponse'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'

  /customer/reverseCharge:
    post:
      tags:
        - customer
      summary: "Reversa un cargo efectuado en la tarjeta de crédito de un cliente"
      description: |
        Este servicio permite reversar un cargo previamente efectuado a un cliente. Para que el cargo se reverse, este servicio debe ser invocado dentro de las 24 horas siguientes a efectuado el cargo, las 24 horas rigen desde las 14:00 hrs, es decir, si el cargo se efectuó a las 16:00 hrs, este puede reversarse hasta las 14:00 hrs del día siguiente.\n\n
          Puede enviar como parámetros el **commerceOrder** o el **flowOrder**.
      responses:
        '200':
          description: El objeto ReverseChargeResponse
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ReverseChargeResponse'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
      requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              properties:
                apiKey:
                  description: apiKey del comercio
                  type: string
                commerceOrder:
                  description: Identificador de la orden del comercio
                  type: string
                flowOrder:
                  description: Identificador de la orden de Flow
                  type: number
                s:
                  description: la firma de los parámetros efectuada con su secretKey
                  type: string
              required:
                - apiKey
                - s
  /customer/getCharges:
    get:
      tags:
        - customer
      summary: "Lista paginada de los cargos efectuados a un cliente"
      description: "Este servicio obtiene la lista paginada de los cargos efectuados a un cliente."
      parameters:
        - in: query
          name: apiKey
          description: apiKey del comercio
          required: true
          schema:
            type: string
        - in: query
          name: customerId
          description: Identificador del cliente
          required: true
          schema:
            type: string
        - in: query
          name: start
          description: Número de registro de inicio de la página. Si se omite el valor por omisión es 0.
          required: false
          schema:
            type: integer
        - in: query
          name: limit
          description: Número de registros por página. Si se omite el valor por omisón es 10. El valor máximo es de 100 registros por página.
          required: false
          schema:
            type: integer
        - in: query
          name: filter
          description: Filtro por descripción del cargo
          required: false
          schema:
            type: string
        - in: query
          name: fromDate
          description: Filtro por fecha de inicio
          required: false
          schema:
            type: string
            format: yyyy-mm-dd
        - in: query
          name: status
          description: Filtro por estado del cargo
          required: false
          schema:
            type: integer
        - in: query
          name: s
          description: la firma de los parámetros efectuada con su secretKey
          required: true
          schema:
            type: string
      responses:
        '200':
          description: "Lista paginada de los cargos efectuados a un cliente"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'

  /customer/getChargeAttemps:
    get:
      tags:
        - customer
      summary: "Lista paginada de intentos de cargos fallidos a un cliente"
      description: "Este servicio obtiene la lista paginada de los intentos de cargos fallidos a un cliente."
      parameters:
        - in: query
          name: apiKey
          description: apiKey del comercio
          required: true
          schema:
            type: string
        - in: query
          name: customerId
          description: Identificador del cliente
          required: true
          schema:
            type: string
        - in: query
          name: start
          description: Número de registro de inicio de la página. Si se omite el valor por omisión es 0.
          required: false
          schema:
            type: integer
        - in: query
          name: limit
          description: Número de registros por página. Si se omite el valor por omisón es 10. El valor máximo es de 100 registros por página.
          required: false
          schema:
            type: integer
        - in: query
          name: filter
          description: Filtro por descripción del error
          required: false
          schema:
            type: string
        - in: query
          name: fromDate
          description: Filtro por fecha de inicio
          required: false
          schema:
            type: string
            format: yyyy-mm-dd
        - in: query
          name: commerceOrder
          description: Filtro por el número de la orden del comercio
          required: false
          schema:
            type: integer
        - in: query
          name: s
          description: la firma de los parámetros efectuada con su secretKey
          required: true
          schema:
            type: string
      responses:
        '200':
          description: "Lista paginada de los intentos de cargos fallidos efectuados a un cliente"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'

  /customer/getSubscriptions:
    get:
      tags:
        - customer
      summary: "Lista paginada de suscripciones de un cliente"
      description: "Este servicio obtiene la lista paginada de las suscripciones de un cliente."
      parameters:
        - in: query
          name: apiKey
          description: apiKey del comercio
          required: true
          schema:
            type: string
        - in: query
          name: customerId
          description: Identificador del cliente
          required: true
          schema:
            type: string
        - in: query
          name: start
          description: Número de registro de inicio de la página. Si se omite el valor por omisión es 0.
          required: false
          schema:
            type: integer
        - in: query
          name: limit
          description: Número de registros por página. Si se omite el valor por omisón es 10. El valor máximo es de 100 registros por página.
          required: false
          schema:
            type: integer
        - in: query
          name: filter
          description: filtro por el identificador de la suscripción
          required: false
          schema:
            type: string
        - in: query
          name: s
          description: la firma de los parámetros efectuada con su secretKey
          required: true
          schema:
            type: string
      responses:
        '200':
          description: "Lista de las suscripciones de un cliente"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'

  /plans/create:
    post:
      tags:
        - plans
      summary: "Crea un Plan de Suscripción"
      description: "Este servicio permite crear un nuevo Plan de Suscripción"
      responses:
        '200':
          description: El objeto Plan
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Plan'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
      requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              properties:
                apiKey:
                  description: apiKey del comercio
                  type: string
                planId:
                  description: |
                    Identificador del Plan. Un texto identificador del Plan, sin espacios, ejemplo: PlanMensual
                  type: string
                name:
                  description: Nombre del Plan
                  type: string
                currency:
                  description: Moneda del Plan, por omisión CLP
                  type: string
                amount:
                  description: Monto del Plan
                  type: number
                interval:
                  description: |
                    Especifica la frecuencia de cobros (generación de importe)
                      - 1 diario
                      - 2 semanal
                      - 3 mensual
                      - 4 anual
                  type: number
                interval_count:
                  description: |
                    Número de intervalos de frecuencia de cobros, por ejemplo:
                      - interval = 2 y interval_count = 2 la frecuancia será quincenal. El valor por omisión es 1.
                  type: number
                trial_period_days:
                  description: Número de días de Trial. El valor por omisón es 0.
                  type: number
                days_until_due:
                  description: Número de días pasados, después de generar un importe, para considerar el importe vencido. Si no se especifica el valor será 3.
                  type: number
                periods_number:
                  description: Número de períodos de duración del plan. Si el plan tiene vencimiento, entonces ingrese aquí el número de periodos de duración del plan
                  type: number
                urlCallback:
                  description: URL donde Flow notificará al comercio los pagos efectuados por este plan.
                  type: string
                charges_retries_number:
                  description: El número de reintentos de cargo, por omisión Flow utilizará 3
                  type: number
                currency_convert_option:
                  description: |
                    Si hay conversión de moneda, en qué momento hará la conversión:
                    - 1 al pago (default)
                    - 2 al importe (invoice)
                s:
                  description: la firma de los parámetros efectuada con su secretKey
                  type: string
              required:
                - apiKey
                - planId
                - name
                - amount
                - interval
                - s

  /plans/get:
    get:
      tags:
        - plans
      summary: "Obtiene los datos de un Plan de Suscripción"
      description: "Este servicio permite obtener los datos de un Plan de Suscripción"
      parameters:
        - in: query
          name: apiKey
          description: apiKey del comercio
          required: true
          schema:
            type: string
        - in: query
          name: planId
          description: Identificador del Plan
          required: true
          schema:
            type: string
        - in: query
          name: s
          description: la firma de los parámetros efectuada con su secretKey
          required: true
          schema:
            type: string
      responses:
        '200':
          description: "El objeto Plan"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Plan'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
  /plans/edit:
    post:
      tags:
        - plans
      summary: "Edita un Plan de Suscripción"
      description: "Este servicio permite editar los datos de un Plan de Suscripción. Si el plan tiene clientes suscritos sólo se puede modificar el campo **trial_period_days**."
      responses:
        '200':
          description: "El objeto Plan"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Plan'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
      requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              properties:
                apiKey:
                  description: apiKey del comercio
                  type: string
                planId:
                  description: Identificador del Plan
                  type: string
                name:
                  description: Nombre del Plan
                  type: string
                currency:
                  description: Moneda del Plan
                  type: string
                amount:
                  description: Monto del Plan
                  type: number
                interval:
                  description: |
                    Especifica la frecuencia de cobros (generación de importe)
                      - 1 diario
                      - 2 semanal
                      - 3 mensual
                      - 4 anual
                  type: number
                interval_count:
                  description: |
                    Número de intervalos de frecuencia de cobros, por ejemplo:
                      - interval = 2 y interval_count = 2 la frecuancia será quincenal. El valor por omisión es 1.
                  type: number
                trial_period_days:
                  description: Número de días de Trial. El valor por omisón es 0.
                  type: number
                days_until_due:
                  description: Número de días pasados, después de generar un importe, para considerar el importe vencido.
                  type: number
                periods_number:
                  description: Número de períodos de duración del plan. Si el plan tiene vencimiento, entonces ingrese aquí el número de periodos de duración del plan
                  type: number
                urlCallback:
                  description: URL donde Flow notificará al comercio los pagos efectuados por este plan.
                  type: string
                charges_retries_number:
                  description: El número de reintentos de cargo, por omisión Flow utilizará 3
                  type: number
                currency_convert_option:
                  description: |
                    Si hay conversión de moneda, en qué momento hará la conversión:
                    - 1 al pago (default)
                    - 2 al importe (invoice)
                s:
                  description: la firma de los parámetros efectuada con su secretKey
                  type: string
              required:
                - apiKey
                - planId

  /plans/delete:
    post:
      tags:
        - plans
      summary: "Elimina un Plan de Suscripción"
      description: "Este servicio permite eliminar un Plan de Suscripción. El eliminar un Plan significa que ya no podrá suscribir nuevos clientes al plan. Pero las suscripciones activas continuarán su ciclo de vida mientras estas no sean cancelas."
      responses:
        '200':
          description: "El objeto Plan"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Plan'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
      requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              properties:
                apiKey:
                  description: apiKey del comercio
                  type: string
                planId:
                  description: Identificador del Plan
                  type: string
                s:
                  description: la firma de los parámetros efectuada con su secretKey
                  type: string
              required:
                - apiKey
                - planId

  /plans/list:
    get:
      tags:
        - plans
      summary: "Lista paginada de planes de suscripción"
      description: "Permite obtener la lista de planes de suscripción paginada de acuerdo a los parámetros de paginación. Además, se puede definir los siguientes filtros:\n\n
      * filter: filtro por nombre del plan\n
      * status: filtro por estado del plan"
      parameters:
        - in: query
          name: apiKey
          description: apiKey del comercio
          required: true
          schema:
            type: string
        - in: query
          name: start
          description: Número de registro de inicio de la página. Si se omite el valor por omisión es 0.
          required: false
          schema:
            type: integer
        - in: query
          name: limit
          description: Número de registros por página. Si se omite el valor por omisón es 10. El valor máximo es de 100 registros por página
          required: false
          schema:
            type: integer
        - in: query
          name: filter
          description: Filtro por el nombre del Plan
          required: false
          schema:
            type: string
        - in: query
          name: status
          description: Filtro por el estado del Plan 1-Activo 0-Eliminado
          required: false
          schema:
            type: integer
        - in: query
          name: s
          description: la firma de los parámetros efectuada con su secretKey
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Lista paginada de Planes
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'

  /subscription/create:
    post:
      tags:
        - subscription
      summary: Crea una nueva suscripción a un Plan
      description: "Este servicio permite crear una nueva suscripción de un cliente a un Plan.\n
      Para crear una nueva suscripción, basta con enviar los  parámetros **planId** y **customerId**, los parámetros opcionales son:\n\n
      <table>
  <thead>
    <tr>
      <th>Parámetro</th>
      <th>Descripción</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>subscription_start</td>
      <td>Fecha de inicio de la suscripción</td>
    </tr>
     <tr>
      <td>couponId</td>
      <td>Identificador de cupón de descuento</td>
    </tr>
    <tr>
      <td>trial_period_days</td>
      <td>Número de días de Trial</td>
    </tr>
  </tbody>
</table>"
      responses:
        '200':
          description: "El objeto Subscription"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Subscription'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
      requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              properties:
                apiKey:
                  description: apiKey del comercio
                  type: string
                planId:
                  description: Identificador del Plan
                  type: string
                customerId:
                  description: Identificador del cliente
                  type: string
                subscription_start:
                  description: La fecha de inicio de la suscripción
                  type: string
                  format: yyyy-mm-dd
                couponId:
                  description: Si quiere aplicarle un descuento, el identificador del cupón de descuento.
                  type: number
                trial_period_days:
                  description: Número de días de Trial. Si el Plan tiene días de Trial, este valor modificará los días para esta suscripción.
                  type: number
                periods_number:
                  description: Número de períodos de duración de la subscripción. Si null, entonces tomará el periods_number del plan.
                  type: number
                s:
                  description: la firma de los parámetros efectuada con su secretKey
                  type: string
              required:
                - apiKey
                - planId
                - customerId
                - s

  /subscription/get:
    get:
      tags:
        - subscription
      summary: "Obtiene una Suscripción en base al subscriptionId"
      description: "Este servicio permite obtener los datos de una suscripción."
      parameters:
        - in: query
          name: apiKey
          description: apiKeyel comercio
          required: true
          schema:
            type: string
        - in: query
          name: subscriptionId
          description: Identificador de la suscripción
          required: true
          schema:
            type: string
        - in: query
          name: s
          description: la firma de los parámetros efectuada con su secretKey
          required: true
          schema:
            type: string
      responses:
        '200':
          description: "El objeto Subscription"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Subscription'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'

  /subscription/list:
    get:
      tags:
        - subscription
      summary: Obtiene la lista de suscripciones para un Plan
      description: "Permite obtener la lista de suscripciones paginada de acuerdo a los parámetros de paginación. Además, se puede definir los siguientes filtros:\n\n
      * filter: filtro por nombre del plan\n
      * status: filtro por estado de la suscripción."
      parameters:
        - in: query
          name: apiKey
          description: apiKeyel comercio
          required: true
          schema:
            type: string
        - in: query
          name: planId
          description: Identificador del Plan
          required: true
          schema:
            type: string
        - in: query
          name: start
          description: número de registro de inicio de la página. Si se omite el valor por omisión es 0.
          required: false
          schema:
            type: integer
        - in: query
          name: limit
          description: Número de registros por página. Si se omite el valor por omisón es 10. El valor máximo es de 100 registros por página.
          required: false
          schema:
            type: integer
        - in: query
          name: filter
          description: filtro por el nombre del cliente
          required: false
          schema:
            type: string
        - in: query
          name: status
          description: Filtro por el estado de la suscripción
          required: false
          schema:
            type: integer
        - in: query
          name: s
          description: la firma de los parámetros efectuada con su secretKey
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Lista paginada de suscripciones de un Plan
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'

  /subscription/changeTrial:
    post:
      tags:
        - subscription
      summary: Modifica los días de Trial de una suscripción
      description: |
        Este servicio permite modificar los días de Trial de una suscripción.
        Sólo se puede modificar los días de Trial a una suscripción que aún no se ha iniciado o que todavía está vigente el Trial.
      responses:
        '200':
          description: "El objeto Subscription"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Subscription'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
      requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              properties:
                apiKey:
                  description: apiKeyel comercio
                  type: string
                subscriptionId:
                  description: Identificador de la suscripción
                  type: string
                trial_period_days:
                  description: Número de días de Trial
                  type: number
                s:
                  description: la firma de los parámetros efectuada con su secretKey
                  type: string
              required:
                - apiKey
                - subscriptionId
                - trial_period_days
                - s

  /subscription/cancel:
    post:
      tags:
        - subscription
      summary: "Cancela una suscripción"
      description: |
        Este servicio permite cancelar una suscripción. Existen formas de cancelar una suscripción:
        - inmediatamente. Es decir, en este instante
        - al terminar el perído vigente.

        Si desea cancelar la suscripción inmediatamente, envíe el parámetro **at_period_end** con valor 0, si desea cancelarla al final del período vigente envíe el valor 1.
      responses:
        '200':
          description: "El objeto Subscription"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Subscription'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
      requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              properties:
                apiKey:
                  description: apiKey del comercio
                  type: string
                subscriptionId:
                  description: Identificador de la suscripción.
                  type: string
                at_period_end:
                  description: 1 Si la cancelación será al finalizar el período vigente 0 Si la cancelación será inmediata.
                  type: number
                s:
                  description: la firma de los parámetros efectuada con su secretKey
                  type: string
              required:
                - apiKey
                - subscriptionId
                - s

  /subscription/addCoupon:
    post:
      tags:
        - subscription
      summary: "Agrega un descuento a la suscripción"
      description: "Este servicio permite agregar un descuento a la suscripción. Si la suscripción ya tenía un descuento, será reemplazado por este."
      responses:
        '200':
          description: "El objeto Subscription"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Subscription'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
      requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              properties:
                apiKey:
                  description: apiKey del comercio
                  type: string
                subscriptionId:
                  description: Identificador de la suscripción
                  type: string
                couponId:
                  description: Identificador del cupón de descuento.
                  type: number
                s:
                  description: la firma de los parámetros efectuada con su secretKey
                  type: string
              required:
                - apiKey
                - subscriptionId
                - couponId
                - s

  /subscription/deleteCoupon:
    post:
      tags:
        - subscription
      summary: "Elimina un descuento a la suscripción"
      description: "Este servicio permite eliminar el descuento que tenga la suscripción. El eliminar el descuento de la suscripción, no elimina el descuento que podría tenar asociado el cliente."
      responses:
        '200':
          description: "El objeto Subscription"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Subscription'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
      requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              properties:
                apiKey:
                  description: apiKey del comercio
                  type: string
                subscriptionId:
                  description: Identificador de la suscripción
                  type: string
                s:
                  description: la firma de los parámetros efectuada con su secretKey
                  type: string
              required:
                - apiKey
                - subscriptionId
                - s

  /coupon/create:
    post:
      tags:
        - coupon
      summary: "Crea un cupón de descuento"
      description: "Este servicio permite crear un cupón de descuento"
      responses:
        '200':
          description: "El objeto Coupon"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Coupon'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
      requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              properties:
                apiKey:
                  description: apiKey del comercio
                  type: string
                name:
                  description: Nombre del cupón
                  type: string
                percent_off:
                  description: Porcentaje del cupon. Número entre 0 y 100. Permite 2 decimales con punto decimal. Ejemplo 10.2. No se agrega el signo %
                  type: number
                currency:
                  description: Moneda del descuento. Solo agregue la moneda para cupones de monto.
                  type: string
                amount:
                  description: Monto del descuento
                  type: number
                duration:
                  description: |
                    Duración del cupón:
                    - 1 definida
                    - 0 indefinida
                  type: number
                times:
                  description: |
                    Si la duración del cupón es definida, este campo indica las veces de duración del cupón. Si el cupón se aplica a un cliente veces corresponderá a meses. Si l cupón se aplica a una suscripción, veces corresponderá a los períodos del Plan.
                  type: number
                max_redemptions:
                  description: Número de veces de aplicación del cupón.
                  type: number
                expires:
                  description: Fecha de expiración del cupón en formato yyyy-mm-dd
                  type: string
                s:
                  description: la firma de los parámetros efectuada con su secretKey.
                  type: string
              required:
                - apiKey
                - name
                - s

  /coupon/edit:
    post:
      tags:
        - coupon
      summary: Edita un cupón de descuento
      description: Este servicio permite editar un cupón de descuento. Sólo se puede editar el nombre de un cupón.
      responses:
        '200':
          description: "El objeto Coupon"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Coupon'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
      requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              properties:
                apiKey:
                  description: apiKey del comercio
                  type: string
                couponId:
                  description: Identificador del cupón
                  type: string
                name:
                  description: Nombre del cupón
                  type: string
                s:
                  description: la firma de los parámetros efectuada con su secretKey.
                  type: string
              required:
                - apiKey
                - couponId
                - name
                - s

  /coupon/delete:
    post:
      tags:
        - coupon
      summary: "Elimina un cupón de descuento"
      description: "Este servicio permite eliminar un cupón de descuento. Eliminar un cupón de descuento no elimina los descuentos aplicados a clientes o suscripciones, sólo no permite volver a aplicar este cupón"
      responses:
        '200':
          description: "El objeto Coupon"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Coupon'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
      requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              properties:
                apiKey:
                  description: apiKey del comercio
                  type: string
                couponId:
                  description: Identificado del cupón
                  type: string
                s:
                  description: la firma de los parámetros efectuada con su secretKey.
                  type: string
              required:
                - apiKey
                - couponId
                - s

  /coupon/get:
    get:
      tags:
      - coupon
      summary: "Obtiene un cupón de descuento"
      description: "Este servicio permite obtener los datos de un cupón de descuento"
      parameters:
        - in: query
          name: apiKey
          description: apiKey del comercio
          required: true
          schema:
            type: string
        - in: query
          name: couponId
          description: Identificador del cupón
          required: true
          schema:
            type: string
        - in: query
          name: s
          description: la firma de los parámetros efectuada con su secretKey.
          required: true
          schema:
            type: string
      responses:
          '200':
            description: "El objeto Coupon"
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/Coupon'
          '400':
            description: Error del Api
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/Error'
          '401':
            description: Error de negocio
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/Error'

  /coupon/list:
    get:
      tags:
      - coupon
      summary: "Lista los cupones de descuento"
      description: "Este servicio permite la lista de cupones de descuento"
      parameters:
        - in: query
          name: apiKey
          description: apiKey del comercio
          required: true
          schema:
            type: string
        - in: query
          name: start
          description: Número de registro de inicio de la página. Si se omite el valor por omisión es 0.
          required: false
          schema:
            type: integer
        - in: query
          name: limit
          description: Número de registros por página. Si se omite el valor por omisón es 10. El valor máximo es de 100 registros por página.
          required: false
          schema:
            type: integer
        - in: query
          name: filter
          description: Filtro por el nombre del cupón
          required: false
          schema:
            type: string
        - in: query
          name: status
          description: |
            Filtro por el estado del cupón:
            - 1 Activo
            - 0 Inactivo
          required: false
          schema:
            type: integer
        - in: query
          name: s
          description: la firma de los parámetros efectuada con su secretKey.
          required: true
          schema:
            type: string
      responses:
          '200':
            description: "El objeto Coupon"
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/List'
          '400':
            description: Error del Api
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/Error'
          '401':
            description: Error de negocio
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/Error'

  /invoice/get:
    get:
      tags:
        - invoice
      summary: "Obtiene los datos de un Invoice (Importe)"
      description: "Este servicio permite obtener los datos de un Importe."
      parameters:
        - in: query
          name: apiKey
          description: apiKey del comercio
          required: true
          schema:
            type: string
        - in: query
          name: invoiceId
          description: Identificador del Invoice
          required: true
          schema:
            type: number
        - in: query
          name: s
          description: la firma de los parámetros efectuada con su secretKey.
          required: true
          schema:
            type: string
      responses:
        '200':
          description: "El objeto Invoice"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Invoice'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'

  /invoice/cancel:
    post:
      tags:
        - invoice
      summary: "Cancela un Importe (Invoice) pendiente de pago"
      description: "Este servicio permite cancelar un Importe (Invoice) pendiente de pago."
      responses:
        '200':
          description: "El objeto Invoice"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Invoice'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
      requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              properties:
                apiKey:
                  description: apiKey del comercio
                  type: string
                invoiceId:
                  description: Identificador del Invoice (Importe)
                  type: number
                s:
                  description: la firma de los parámetros efectuada con su secretKey.
                  type: string
              required:
                - apiKey
                - invoiceId
                - s

  /invoice/outsidePayment:
      post:
        tags:
          - invoice
        summary: "Ingresa un pago por fuera y da por pagado el Importe (Invoice) "
        description: "Este servicio permite dar por pagado un Importe (Invoice) cuando el pago no se realiza por Flow."
        responses:
          '200':
            description: "El objeto Invoice"
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/Invoice'
          '400':
            description: Error del Api
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/Error'
          '401':
            description: Error de negocio
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/Error'
        requestBody:
          content:
            application/x-www-form-urlencoded:
              schema:
                type: object
                properties:
                  apiKey:
                    description: apiKey del comercio
                    type: string
                  invoiceId:
                    description: Identificador del Invoice (Importe)
                    type: number
                  date:
                    description: Fecha del pago en formato "yyyy-mm-dd"
                    type: string
                  comment:
                    description: descripción del pago por fuera
                    type: string
                  s:
                    description: la firma de los parámetros efectuada con su secretKey.
                    type: string
                required:
                  - apiKey
                  - invoiceId
                  - date
                  - s

  /invoice/getOverDue:
     get:
      tags:
        - invoice
      summary: "Obtiene los invoices vencidos"
      description: "Este servicio permite obtener la lista de invoices vencidos, es decir, aquellos no pagados cuyo due_date este vencido."
      parameters:
        - in: query
          name: apiKey
          description: apiKey del comercio
          required: true
          schema:
            type: string
        - in: query
          name: start
          description: Número de registro de inicio de la página. Si se omite el valor por omisión es 0.
          required: false
          schema:
            type: integer
        - in: query
          name: limit
          description: Número de registros por página. Si se omite el valor por omisón es 10. El valor máximo es de 100 registros por página.
          required: false
          schema:
            type: integer
        - in: query
          name: filter
          description: Filtro
          required: false
          schema:
            type: string
        - in: query
          name: planId
          description: Identificador del Plan, si se agrega se filtrará para los invoices de este plan.
          required: false
          schema:
            type: string
        - in: query
          name: s
          description: la firma de los parámetros efectuada con su secretKey
          required: true
          schema:
            type: string
      responses:
        '200':
          description: "El objeto Invoice"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Invoice'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'

  /invoice/retryToCollect:
    post:
      tags:
        - invoice
      summary: "Reintenta el cobro de un invoice vencido"
      description: "Este servicio permite reintentar el cobro de un Invoice vencido."
      responses:
        '200':
          description: "El objeto Invoice"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Invoice'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
      requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              properties:
                apiKey:
                  description: apiKey del comercio
                  type: string
                invoiceId:
                  description: Identificador del Invoice (Importe)
                  type: number
                s:
                  description: la firma de los parámetros efectuada con su secretKey.
                  type: string
              required:
                - apiKey
                - invoiceId
                - s
  /settlement/getByDate:
    get:
      tags:
        - settlement
      summary: Obtiene la liquidación efectuada para esa fecha.
      description: 'Este método se utiliza para obtener la liquidación de la fecha enviada como parámetro. <br>Nota: Si su liquidación es anterior al 01-06-2021 utilizar este servicio, en caso contrario se recomienda utilizar el servicio /settlement/search'
      deprecated: true
      parameters:
        - in: query
          name: apiKey
          description: apiKey del comercio
          required: true
          schema:
            type: string
        - in: query
          name: date
          description: Fecha de la liquidación
          required: true
          schema:
            type: string
            format: yyyy-mm-dd
        - in: query
          name: s
          description: la firma de los parámetros efectuada con su secretKey.
          required: true
          schema:
            type: string
      responses:
        '200':
          description: "Arreglo de objetos Settlement"
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Settlement'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'

  /settlement/getById:
    get:
      tags:
        - settlement
      summary: Obtiene la Liquidación efectuada con ese identificador
      description:  'Este método se utiliza para obtener el objeto Settlement correspondiente al identificador. <br>Nota: Si su liquidación es anterior al 01-06-2021 utilizar este servicio, en caso contrario se recomienda utilizar el servicio /settlement/getByIdv2'
      deprecated: true
      parameters:
        - in: query
          name: apiKey
          description: apiKey del comercio
          required: true
          schema:
            type: string
        - in: query
          name: id
          description: Identificador de la liquidación
          required: true
          schema:
            type: string
        - in: query
          name: s
          description: la firma de los parámetros efectuada con su secretKey.
          required: true
          schema:
            type: string
      responses:
        '200':
          description: "El objeto Settlement"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Settlement'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
  /settlement/search:
    get:
      tags:
        - settlement
      summary: Busca liquidaciones en el un determinado rango de fechas.
      description: 'Este método se utiliza para obtener el(los) encabezado(s) de liquidación(es) dentro del rango de fechas ingresado (permite filtrar también por la moneda). Para obtener la liquidación completa (encabezado y detalles) utilizar el servicio /settlement/getByIdv2'
      parameters:
        - in: query
          name: apiKey
          description: apiKey del comercio
          required: true
          schema:
            type: string
        - in: query
          name: startDate
          description: Fecha inicio de rango
          required: true
          schema:
            type: string
            format: yyyy-mm-dd
        - in: query
          name: endDate
          description: Fecha fin de rango
          required: true
          schema:
            type: string
            format: yyyy-mm-dd
        - in: query
          name: currency
          description: Moneda de liquidación
          schema:
            type: string
        - in: query
          name: s
          description: la firma de los parámetros efectuada con su secretKey.
          required: true
          schema:
            type: string
      responses:
        '200':
          description: "Arreglo de objetos SettlementBase"
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/SettlementBaseV2'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
  /settlement/getByIdv2:
    get:
      tags:
        - settlement
      summary: Obtiene la liquidación efectuada con ese identificador en el formato nuevo
      description:  'Este método se utiliza para obtener el objeto Settlement correspondiente al identificador'
      parameters:
        - in: query
          name: apiKey
          description: apiKey del comercio
          required: true
          schema:
            type: string
        - in: query
          name: id
          description: Identificador de la liquidación
          required: true
          schema:
            type: string
        - in: query
          name: s
          description: la firma de los parámetros efectuada con su secretKey.
          required: true
          schema:
            type: string
      responses:
        '200':
          description: "El objeto SettlementV2"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SettlementV2'
        '400':
          description: Error del Api
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Error de negocio
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
  /merchant/create:
    post:
      tags:
        - merchant
      summary: Crea un comercio asociado
      description: "Este método permite crear un nuevo comercio asociado en **Flow**"
      responses:
        '200':
          description: "Objeto con información del comercio asocioado en Flow"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Merchant'
        '400':
          description: "Error del Api"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: "Error de negocio"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
      requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              properties:
                apiKey:
                  description: apiKey del comercio
                  type: string
                id:
                  description: Id de comercio asociado
                  type: string
                name:
                  description: Nombre de comercio asociado
                  type: string
                url:
                  description: Url del comercio asociado
                  type: string
                s:
                  description: la firma de los parámetros efectuada con su secretKey
                  type: string
              required:
                - apiKey
                - id
                - name
                - url
                - s
  /merchant/edit:
    post:
      tags:
        - merchant
      summary: Edita un comercio asociado
      description: "Este método permite modificar un comercio asociado previamente creado en **Flow**"
      responses:
        '200':
          description: "Objeto con información del comercio asociado en Flow"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Merchant'
        '400':
          description: "Error del Api"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: "Error de negocio"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
      requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              properties:
                apiKey:
                  description: apiKey del comercio
                  type: string
                id:
                  description: Id de comercio asociado
                  type: string
                name:
                  description: Nombre de comercio asociado
                  type: string
                url:
                  description: Url del comercio asociado
                  type: string
                s:
                  description: la firma de los parámetros efectuada con su secretKey
                  type: string
              required:
                - apiKey
                - id
                - name
                - url
                - s
  /merchant/delete:
    post:
      tags:
        - merchant
      summary: Elimina un comercio asociado
      description: "Este método permite eliminar un comercio asociado previamente creado en **Flow**"
      responses:
        '200':
          description: "Objeto con información de la orden generada en Flow"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/MerchantDeleteResponse'
        '400':
          description: "Error del Api"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: "Error de negocio"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
      requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              properties:
                apiKey:
                  description: apiKey del comercio
                  type: string
                id:
                  description: Id de comercio asociado
                  type: string
                s:
                  description: la firma de los parámetros efectuada con su secretKey
                  type: string
              required:
                - apiKey
                - id
                - s
  /merchant/get:
    get:
      tags:
        - merchant
      summary: Obtener comercio asociado
      description: "Este método permite obtener la información de un comercio asociado previamente creado en **Flow**"
      responses:
        '200':
          description: "Objeto con información del comercio asocioado en Flow"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Merchant'
        '400':
          description: "Error del Api"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: "Error de negocio"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
      parameters:
        - in: query
          name: apiKey
          description: apiKey del comercio
          required: true
          schema:
            type: string
        - in: query
          name: id
          description: Id de comercio asociado
          required: true
          schema:
            type: string
        - in: query
          name: s
          description: la firma de los parámetros efectuada con su secretKey
          required: true
          schema:
            type: string
  /merchant/list:
    get:
      tags:
        - merchant
      summary: Lista de comercios asociados
      description: "Permite obtener la lista de comercios paginada de acuerdo a los parámetros de paginación. Además, se puede definir los siguientes filtros:\n\n
      * filter: filtro por nombre del comercio asociado\n
      * status: filtro por estado del comercio asociado"
      responses:
        '200':
          description: "Objeto con información del comercio asocioado en Flow"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List'
        '400':
          description: "Error del Api"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: "Error de negocio"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
      parameters:
        - in: query
          name: apiKey
          description: apiKey del comercio
          required: true
          schema:
            type: string
        - in: query
          name: start
          description: Número de registro de inicio de la página. Si se omite el valor por omisión es 0.
          required: false
          schema:
            type: integer
        - in: query
          name: limit
          description: Número de registros por página. Si se omite el valor por omisón es 10. El valor máximo es de 100 registros por página.
          required: false
          schema:
            type: integer
        - in: query
          name: filter
          description: Filtro por nombre del comercio asociado
          required: false
          schema:
            type: string
        - in: query
          name: status
          description: "Filtro por estado del comercio asociado. Valores posibles:\n\n0: Pendiente de aprobación\n\n1: Aprobado\n\n2: Rechazado"
          required: false
          schema:
            type: integer
        - in: query
          name: s
          description: la firma de los parámetros efectuada con su secretKey
          required: true
          schema:
            type: string
components:
  schemas:
    PaymentStatus:
      description: Objeto que representa un cobro y si está pagado su correspondiente pago
      type: object
      nullable: true
      properties:
        flowOrder:
          type: integer
          description: El número de la orden de Flow
          example: 3567899
        commerceOrder:
          type: string
          description: El número de la orden del comercio
          example: sf12377
        requestDate:
          type: string
          description: La fecha de creación de la orden
          format: 'yyyy-mm-dd hh:mm:ss'
          example: '2017-07-21 12:32:11'
        status:
          type: integer
          description: |
            El estado de la order
            - 1 pendiente de pago
            - 2 pagada
            - 3 rechazada
            - 4 anulada
          example: 1
        subject:
          type: string
          description: El concepto de la orden
          example: game console
        currency:
          type: string
          description: La moneda
          example: CLP
        amount:
          type: number
          format: float
          description: El monto de la orden
          example: 12000
        payer:
          type: string
          description: El email del pagador
          example: pperez@gamil.com
        optional:
          type: string
          nullable: true
          description: datos opcionales enviados por el comercio en el request de creación de pago en el parámetro optional en formato JSon
          example:
            RUT: "7025521-9"
            ID: "899564778"
        pending_info:
          type: object
          description: Información para un pago pendiente cuando se generó un cupón de pago. Si no existen datos es que no se generó un cupón de pago.
          properties:
            media:
              type: string
              nullable: true
              description: El medio de pago utilizado para emitir el cupón de pago
              example: Multicaja
            date:
              type: string
              nullable: true
              description: La fecha de emisión del cupón de pago
              example: '2017-07-21 10:30:12'
        paymentData:
          description: Los datos del pago
          type: object
          properties:
            date:
              type: string
              nullable: true
              description: La fecha de pago
              example: '2017-07-21 12:32:11'
            media:
              type: string
              nullable: true
              description: El medio de pago utilizado
              example: webpay
            conversionDate:
              type: string
              nullable: true
              description: La fecha de conversión de la moneda
              example: '2017-07-21'
            conversionRate:
              type: number
              nullable: true
              format: float
              description: La tasa de conversión.
              example: 1.1
            amount:
              type: number
              nullable: true
              format: float
              description: El monto pagado
              example: 12000
            currency:
              type: string
              nullable: true
              description: La moneda con que se pagó
              example: CLP
            fee:
              type: number
              nullable: true
              format: float
              description: El costo del servicio
              example: 551
            taxes:
              type: number
              nullable: true
              format: float
              description: Impuestos
              example: 28
            balance:
              type: number
              nullable: true
              format: float
              description: El saldo a depositar
              example: 11499
            transferDate:
              type: string
              nullable: true
              description: La fecha de transferencia de los fondos a su cuenta bancaria.
              example: '2017-07-24'
        merchantId:
          description: Id de comercio asociado. Solo aplica si usted es comercio integrador.
          type: string
          nullable: true
    PaymentStatusExtended:
      description: Objeto que representa un cobro y si está pagado su correspondiente pago
      type: object
      nullable: true
      properties:
        flowOrder:
          type: integer
          description: El número de la orden de Flow
          example: 3567899
        commerceOrder:
          type: string
          description: El número de la orden del comercio
          example: sf12377
        requestDate:
          type: string
          description: La fecha de creación de la orden
          format: 'yyyy-mm-dd hh:mm:ss'
          example: '2017-07-21 12:32:11'
        status:
          type: integer
          description: |
            El estado de la order
            - 1 pendiente de pago
            - 2 pagada
            - 3 rechazada
            - 4 anulada
          example: 1
        subject:
          type: string
          description: El concepto de la orden
          example: game console
        currency:
          type: string
          description: La moneda
          example: CLP
        amount:
          type: number
          format: float
          description: El monto de la orden
          example: 12000
        payer:
          type: string
          description: El email del pagador
          example: pperez@gamil.com
        optional:
          type: string
          nullable: true
          description: datos opcionales enviados por el comercio en el request de creación de pago en el parámetro optional en formato JSon
          example:
            RUT: "7025521-9"
            ID: "899564778"
        pending_info:
          type: object
          description: Información para un pago pendiente cuando se generó un cupón de pago. Si no existen datos es que no se generó un cupón de pago.
          properties:
            media:
              type: string
              nullable: true
              description: El medio de pago utilizado para emitir el cupón de pago
              example: Multicaja
            date:
              type: string
              nullable: true
              description: La fecha de emisión del cupón de pago
              example: '2017-07-21 10:30:12'
        paymentData:
          description: Los datos del pago
          type: object
          properties:
            date:
              type: string
              nullable: true
              description: La fecha de pago
              example: '2017-07-21 12:32:11'
            media:
              type: string
              nullable: true
              description: El medio de pago utilizado
              example: webpay
            conversionDate:
              type: string
              nullable: true
              description: La fecha de conversión de la moneda
              example: '2017-07-21'
            conversionRate:
              type: number
              nullable: true
              format: float
              description: La tasa de conversión.
              example: 1.1
            amount:
              type: number
              nullable: true
              format: float
              description: El monto pagado
              example: 12000
            currency:
              type: string
              nullable: true
              description: La moneda con que se pagó
              example: CLP
            fee:
              type: number
              nullable: true
              format: float
              description: El costo del servicio
              example: 551
            balance:
              type: number
              nullable: true
              format: float
              description: El saldo a depositar
              example: 11499
            transferDate:
              type: string
              nullable: true
              description: La fecha de transferencia de los fondos a su cuenta bancaria.
              example: '2017-07-24'
            mediaType:
              type: string
              nullable: true
              description: Tipo de pago
              example: 'Crédito'
            cardLast4Numbers:
              type: string
              nullable: true
              description: 4 últimos dígito de la tarjeta (si el pago fue con tarjeta).
              example: '9876'
        merchantId:
          description: Id de comercio asociado. Solo aplica si usted es comercio integrador.
          type: string
          nullable: true
        lastError:
          description: Error del último intento
          type: object
          properties:
            code:
              type: string
              nullable: true
              description: Código de error
              example: '01'
            message:
              type: string
              nullable: true
              description: Mensaje de error
              example: 'Tarjeta inválida'
            medioCode:
              type: string
              nullable: true
              description: Código de error del medio de pago
              example: '005'
    PayResponse:
      description: "Datos de retorno de la creación de un link de pago"
      type: object
      properties:
        url:
          type: string
          description: |
            URL ha redireccionar. Para formar el link de pago a esta URL se debe concatenar el token de la siguiente manera:
              url + "?token=" + token
          example: 'https://api.flow.cl'
        token:
          type: string
          description: token de la transacción
          example: "33373581FC32576FAF33C46FC6454B1FFEBD7E1H"
        flowOrder:
          type: number
          description: Número de order de cobro Flow
          example: 8765456

    Customer:
      type: object
      properties:
        customerId:
          type: string
          description: Identificador del cliente
          example: cus_onoolldvec
        created:
          type: string
          format: 'yyyy-mm-dd hh:mm:ss'
          description: La fecha de creación
          example: '2017-07-21 12:33:15'
        email:
          type: string
          description: email del cliente
          example: customer@gmail.com
        name:
          type: string
          description: nombre del cliente
          example: Pedro Raul Perez
        pay_mode:
          type: string
          description: |
            modo de pago del cliente:
            - auto (cargo automático)
            - manual (cobro manual)
        creditCardType:
          type: string
          description: La marca de la tarjeta de crédito registrada
          example: Visa
        last4CardDigits:
          type: string
          description: Los últimos 4 dígitos de la tarjeta de crédito registrada
          example: '4425'
        externalId:
          type: string
          description: El identificador del cliente en su negocio
          example: 14233531-8
        status:
          type: string
          description: |
            El estado del cliente:
            - 0 Eliminado
            - 1 Activo
          example: '1'
        registerDate:
          type: string
          format: 'yyyy-mm-dd hh:mm:ss'
          description: La fecha en que el cliente registro su tarjeta de crédito.
          example: '2017-07-21 14:22:01'
    List:
      type: object
      properties:
        total:
          type: number
          description: El número total de registros encontrados
          example: 200
        hasMore:
          type: boolean
          description: |
            - 1 Si existen más páginas
            - 0 Si es la última página
          example: 1
        data:
          type: array
          items:
            type: object
          description: arreglo de registros de la página
          example: '[{item list 1}{item list 2}{item list n..}'

    RegisterResult:
      type: object
      properties:
        status:
          type: string
          description: El estado del registro
            - 1 registrado
            - 0 no registrado
          example: '1'
        customerId:
          type: string
          description: Identificador del cliente
          example: cus_onoolldvec
        creditCardType:
          type: string
          description: Marca de la tarjeta de crédito
          example: Visa
        last4CardDigits:
          type: string
          description: Últimos 4 dígitos de la tarjeta de crédito
          example: '0366'

    RefundStatus:
      type: object
      properties:
        token:
          type: string
          description: Token del reembolso
          example: C93B4FAD6D63ED9A3F25D21E5D6DD0105FA8CAAQ
        flowRefundOrder:
          type: string
          description: Número de orden de reembolso
          example: '122767'
        date:
          type: string
          format: 'yyyy-mm-dd hh:mm.ss'
          description: Fecha de solicitud de reembolso
          example: '2017-07-21 12:33:15'
        status:
          type: string
          description: |
            Estado del reembolso, los estado pueden ser:
            - created Solicitud creada
            - accepted Reembolso aceptado
            - rejected Reembolso rechazado
            - refunded Reembolso reembolsado
            - canceled Reembolso cancelado
          example: created
        amount:
          type: number
          description: Monto del reembolso
          example: '12000.00'
        fee:
          type: number
          description: Costo del servicio de reembolso
          example: '240.00'

    CollectResponse:
      type: object
      properties:
        type:
          type: number
          description: |
            Tipo de cobro:
            - 1 Cobro automático
            - 2 Cobro normal (link de pago)
            - 3 Cobro por email
          example: '1'
        commerceOrder:
          type: string
          description: El número de la orden del comercio
          example: 'zc23456'
        flowOrder:
          type: number
          description: El número de la orden de Flow
        url:
          type: string
          description: |
            URL ha redireccionar. Los cargos automaticos no tienen url por ser síncronos. Para formar el link de pago a esta URL se debe concatenar el token de la siguiente manera:
              url + "?token=" + token
          example: 'https://api.flow.cl'
        token:
          type: string
          description: token de la transacción
          example: "33373581FC32576FAF33C46FC6454B1FFEBD7E1H"
        status:
          type: integer
          description: |
            Estado de emisión del cobro, es decir si se emitió el cobro, no indica si hubo pago:
            - 0 Cobro no emitido (uncollected)
            - 1 Cobro emitido (collected)
        paymenResult:
          $ref: '#/components/schemas/PaymentStatus'


    CollectObject:
      type: object
      description: Objeto de cobro para un lote de cobros
      properties:
        customerId:
          type: string
          description: Identificador del cliente en Flow
          example: cus_onoolldvec
        commerceOrder:
          type: string
          description: Identificador de la orden del comercio
          example: zc23456
        subject:
          type: string
          description: descripción de la orden de cobro
          example: cobro de factura
        amount:
          type: number
          description: monto del cobro
          example: 8000
        currency:
          type: string
          description: moneda del cobro, por omisón CLP
          example: CLP
        paymentMethod:
          type: number
          description: medio de pago en el caso de cobros tipo 2, por omisión 9 todos los medios de pago disponibles por el comercio
          example: 9
        optional:
          type: string
          description: Valores opcionales en formato JSON
          example: {"factura":"123456", "clave": "Valor"}
      required:
        - customerId
        - commerceOrder
        - subject
        - amount

    BatchCollectResponse:
      type: object
      properties:
        token:
          type: string
          description: hash token identificador del lote recibido
          example: "33373581FC32576FAF33C46FC6454B1FFEBD7E1H"
        receivedRows:
          type: integer
          description: Número de filas de collects recibidas
          example: '112'
        acceptedRows:
          type: integer
          description: Número de filas de collects aceptadas
          example: '111'
        rejectedRows:
          type: array
          description: Arreglo de filas de collects rechazadas
          items:
            $ref: '#/components/schemas/BatchCollectRejectedRow'


    BatchCollectRejectedRow:
      type: object
      properties:
        customerId:
          type: string
          description: Identificador del cliente en Flow
          example: cus_onoolldvec
        commerceOrder:
          type: string
          description: Identificador de la orden del comercio
          example: zc23456
        rowNumber:
          type: integer
          description: Número de la fila en el lote
          example: 3
        parameter:
          type: string
          description: nombre del parametros con error
          example: commerceOrder
        errorCode:
          type: integer
          description: |
            código del error:
            - 100 Mandatory field not sent
            - 101 Value is empty or cero
            - 102 Invalid field
            - 103 customer not exist or deleted
            - 104 CommerceOrder already sent
            - 105 CommerceOrder has been previously paid
            - 106 Currency is not soported
            - 107 Amount is not numeric
            - 108 Amount can not contain decimals for this currency
            - 109 The minimum amount is $value CLP
            - 110 Optional values are not in JSON format
          example: 104
        errorMsg:
          type: string
          description: descripción del error
          example: commerceOrder already sent

    BatchCollectStatusResponse:
      type: object
      properties:
        token:
          type: string
          description: hash token identificador del lote recibido
          example: "33373581FC32576FAF33C46FC6454B1FFEBD7E1H"
        createdDate:
          type: string
          format: 'yyyy-mm-dd hh:mm:ss'
          description: Fecha de creación del lote
          example: '2019-07-05 14:23:56'
        processedDate:
          type: string
          format: 'yyyy-mm-dd hh:mm:ss'
          description: Fecha en que se procesó el lote
          example: '2019-07-05 16:03:21'
        status:
          type: string
          description: |
            Estado del lote de collect:
            - created (lote creado)
            - processing (lote en procesamiento)
            - processed (lote procesado)
        collectRows:
          type: array
          description: arreglo de resultados de los cargos (collect) generados
          items:
            $ref: '#/components/schemas/CollectStatus'

    CollectStatus:
      type: object
      properties:
        commerceOrder:
          type: string
          description: El número de la orden del comercio
          example: 'zc23456'
        type:
          type: integer
          description: |
            Tipo de cobro:
            - 1 Cobro automático
            - 2 Cobro normal (link de pago)
            - 3 Cobro por email
          example: '1'
        flowOrder:
          type: integer
          description: El número de la orden de Flow
          example: 9876476
        url:
          type: string
          description: |
            URL ha redireccionar. Los cargos automaticos no tienen url por ser síncronos. Para formar el link de pago a esta URL se debe concatenar el token de la siguiente manera:
              url + "?token=" + token
          example: 'https://www.flow.cl/web/pay.php'
        token:
          type: string
          description: token de la transacción
          example: "33373581FC32576FAF33C46FC6454B1FFEBD7E1H"
        status:
          type: string
          description: |
            Estado del registro de collect:
            - unprocessed (Fila no procesada)
            - collected (Cobro generado)
            - uncollected (Cobro no generado)
        errorCode:
          type: integer
          description: Código de error de la fila
          example: 105
        errorMsg:
          type: string
          description: Mensaje de error de la fila
          example: 12300 has been previously paid

    ReverseChargeResponse:
      type: object
      properties:
        status:
          type: string
          description: |
            Estado de la reversa:
            - 0 Reversa no efectuada
            - 1 Reversa efectuada
          example: '1'
        message:
          type: string
          description: Mensaje resultado de la reversa
          example: Reverse charge was successful

    Plan:
      type: object
      properties:
        planId:
          type: string
          description: Identificador del plan
          example: myPlan01
        name:
          type: string
          description: Nombre del plan
          example: Plan junior
        currency:
          type: string
          description: Moneda del plan
          example: CLP
        amount:
          type: number
          description: Monto del plan
          example: 20000
        interval:
          type: number
          description: |
            Define la frecuencia de cobro del plan:
            - 1 diaria
            - 2 semanal
            - 3 mesual
            - 4 anual
          example: 3
        interval_count:
          type: number
          description: |
            Número de intervalos de la frecuencia de cobro del plan, ejemplo:
            interal = 2 y interval_count = 2 significaría un plan quincenal.
          example: 1
        created:
          type: string
          format: 'yyyy-mm-dd hh:mm.ss'
          description: Fecha de creación del plan
          example: '2017-07-21 12:33:15'
        trial_period_days:
          type: number
          description: Número de días de Trial
          example: 15
        days_until_due:
          type: number
          description: Número de días pasados, después de generar un importe, para considerar el importe vencido.
          example: 3
        periods_number:
          type: number
          description: Número de períodos de duración del plan. Si el plan es de término indefinido el valor de periods_number sera 0 (cero)
          example: 12
        urlCallback:
          type: string
          format: uri
          description: URL donde Flow notificará al comercio los pagos efectuados por este plan.
          example: https://www.comercio.cl/flow/suscriptionResult.php
        charges_retries_number:
          type: number
          description: Número de reintentos de cargo, por omisión Flow utilizará 3 reintentos.
          example: 3
        currency_convert_option:
          type: number
          description: |
            Si hay conversión de moneda, en qué momento hará la conversión:
            - 1 al pago
            - 2 al importe (invoice)
        status:
          type: number
          description: |
            El estado del plan:
            - 1 activo
            - 0 eliminado
          example: 1
        public:
          type: number
          description: |
            Si el Plan es de visibilidad pública, es decir, expuestos a otras aplicaciones:
            - 0 privado
            - 1 público
          example: 1

    Subscription:
      type: object
      properties:
        subscriptionId:
          type: string
          description: Identificador de la suscripción
          example: "sus_azcyjj9ycd"
        planId:
          type: string
          description: Identificador del plan
          example: "MiPlanMensual"
        plan_name:
          type: string
          description: Nombre del plan
          example: "Plan mensual"
        customerId:
          type: string
          description: Identificador del cliente
          example: "cus_eblcbsua2g"
        created:
          type: string
          format: 'yyyy-mm-dd hh:mm.ss'
          description: Fecha de creación de la suscripción
          example: '2018-06-26 17:29:06'
        subscription_start:
          type: string
          format: 'yyyy-mm-dd hh:mm.ss'
          description: Fecha de inicio de la suscripción
          example: '2018-06-26 17:29:06'
        subscription_end:
          type: string
          format: 'yyyy-mm-dd hh:mm:ss'
          description: Fecha de término de la suscripción, si la suscripción no tiene término mostrará valor null.
          example: '2019-06-25 00:00:00'
        period_start:
          type: string
          format: 'yyyy-mm-dd hh:mm.ss'
          description: Fecha de inicio del período actual.
          example: '2018-06-26 00:00:00'
        period_end:
          type: string
          format: 'yyyy-mm-dd hh:mm.ss'
          description: Fecha de término del período actual.
          example: '2018-06-26 00:00:00'
        next_invoice_date:
          type: string
          format: 'yyyy-mm-dd hh:mm.ss'
          description: Fecha del siguiente cobro
          example: '2018-06-27 00:00:00'
        trial_period_days:
          type: number
          description: Número de días de Trial
          example: 1
        trial_start:
          type: string
          format: 'yyyy-mm-dd hh:mm.ss'
          description: Fecha de inicio del trial
          example: '2018-06-26 00:00:00'
        trial_end:
          type: string
          format: 'yyyy-mm-dd hh:mm.ss'
          description: Fecha de término del trial.
          example: '2018-06-26 00:00:00'
        cancel_at_period_end:
          type: number
          description: |
            Si la suscripción será cancelada automáticamente al finalizar el período actual:
            - 0 No
            - 1 Si
          example: 0
        cancel_at:
          type: string
          description: Fecha de cancelación de la suscripción
          example: null
        periods_number:
          type: number
          description: Número de períodos de vigencia de la suscripción
          example: 12
        days_until_due:
          type: number
          description: Número de días pasados, después de generar un importe, para considerar el importe vencido.
          example: 3
        status:
          type: number
          description: |
            Estado de la suscripción:
            - 0 Inactivo (no iniciada)
            - 1 Activa
            - 2 En período de trial
            - 4 Cancelada
          example: 1
        morose:
          type: number
          description: |
            Si la subscripción está morosa:
            - 0 si todos los invoices está pagados.
            - 1 si uno o más invoices están vencidos.
            - 2 si uno o más invoices están pendiente de pago, pero no vencidos.
          example: 0
        discount:
          $ref: '#/components/schemas/Discount'
        invoices:
          type: array
          description: Lista de los importe efectuados a la suscripción.
          items:
            $ref: '#/components/schemas/Invoice'

    Coupon:
      properties:
        id:
          type: number
          description: "El identificador del cupón"
          example: 166
        name:
          type: string
          description: "El nombre del cupón"
          example: 166
        percent_off:
          type: number
          description: "Si el cupón es del tipo porcentaje, en este campo indica el porcentaje de descuento, sino, muestra vacío."
          example: 10.00
        currency:
          type: string
          description: "Si el cupón es del tipo monto, aquí va la moneda, sino, muestra vacío"
          example: "CLP"
        amount:
          type: number
          description: "Si el cupón es del tipo monto, aquí va el monto de descuento, sino, muestra vacío"
          example: 2000.00
        created:
          type: string
          description: "La fecha de creación del cupón"
          example: "2018-07-13 09:57:53"
        duration:
          type: number
          description: "Si el cupón es de duración indefinida = 0, o es de duración definida = 1 "
          example: 1
        times:
          type: number
          description: "Si el cupón es de duración definida, en este campo va el número de veces de duración. Si el cupón es aplicado a un cliente, el número de duración equivale a meses, si el cupón es aplicado a una suscripción, el número de duración será los períodos del plan de suscripción"
          example: 1
        max_redemptions:
          type: number
          description: "Es el número de veces que puede ser aplicado este cupón, ya sea a clientes o a suscripciones. Una vez que se completa el número de veces, ya no queda disponible para ser aplicado."
          example: 50
        expires:
          type: string
          format: 'yyyy-mm-dd hh:mm.ss'
          description: "Si el cupón se creó con fecha de expiración aquí va la fecha."
          example: "2018-12-31 00:00:00"
        status:
          type: number
          description: "El estado del cupón, Activo = 1, Inactivo = 0"
          example: 1
        redemtions:
          type: number
          description: "El número de veces que se ha aplicado este cupón"
          example: 21


    Invoice:
      properties:
        id:
          type: number
          description: Identificador del importe
          example: 1034
        subscriptionId:
          type: string
          description: Identificador de la suscripción
          example: sus_azcyjj9ycd
        customerId:
          type: string
          description: Identificador del cliente
          example: cus_eblcbsua2g
        created:
          type: string
          format: 'yyyy-mm-dd hh:mm.ss'
          description: Fecha de creación del importe
          example: '2018-06-26 17:29:06'
        subject:
          type: string
          description: Descripción del importe
          example: PlanPesos - período 2018-06-27 / 2018-06-27
        currency:
          type: string
          description: Moneda del importe
          example: 'CLP'
        amount:
          type: number
          description: Monto del importe
          example: 20000
        period_start:
          type: string
          format: 'yyyy-mm-dd hh:mm.ss'
          description: Fecha de inicio del período del importe
          example: '2018-06-27 00:00:00'
        period_end:
          type: string
          format: 'yyyy-mm-dd hh:mm.ss'
          description: Fecha de término del período del importe
          example: '2018-07-26 00:00:00'
        attemp_count:
          type: integer
          description: Número de intentos de cobro del importe
          example: 0
        attemped:
          type: integer
          description: |
            Si este importe se cobrará:
            - 1 Se cobrará
            - 0 No se cobrará
          example: 1
        next_attemp_date:
          type: string
          format: 'yyyy-mm-dd hh:mm.ss'
          description: Fecha del siguiente intento de cobro
          example: '2018-07-27 00:00:00'
        due_date:
          type: string
          format: 'yyyy-mm-dd hh:mm.ss'
          description: Fecha en que este importe será considerado moroso
          example: '2018-06-30 00:00:00'
        status:
          type: integer
          description: |
            Estado del importe:
            - 0 impago
            - 1 pagado
            - 2 anulado
          example: 0
        error:
          type: integer
          description: |
            Si se produjo un error al intentar cobrar el invoice:
            - 0 Sin error
            - 1 Con error
          example: 0
        errorDate:
          type: string
          format: 'yyyy-mm-dd hh:mm.ss'
          description: Fecha en que se produjo el error o null si no hay error
          example: '2018-06-30 00:00:00'
        errorDescription:
          type: string
          description: Descripción de error o null si no hay error
          example: The minimum amount is 350 CLP
        items:
          type: array
          description: Items del invoice
          items:
            $ref: '#/components/schemas/InvoiceItem'
        payment:
          $ref: '#/components/schemas/PaymentStatus'
        outsidePayment:
          $ref: '#/components/schemas/OutsidePayment'
        paymentLink:
          type: string
          description: Link de pago. Cuando el invoice no esta pagado
          example: https://www.flow.cl/app/web/pay.php?token=7C18C35358FEF0E33C056C719E94956D4FC9BBEL
        chargeAttemps:
          type: array
          description: Intentos de cargo fallidos
          items:
            $ref: '#/components/schemas/ChargeAttemps'

    OutsidePayment:
      description: Objeto que muestra los datos de un pago por fuera
      type: object
      nullable: true
      properties:
        date:
          type: string
          description: Fecha del pago por fuera
          example: 2021-03-08 00:00:00
        comment:
          type: string
          description: descripción del pago por fuera
          example: Pago por caja

    InvoiceItem:
      type: object
      properties:
        id:
          type: number
          description: Identificador del InvoiceItem
          example: 567
        subject:
          type: string
          description: Descripción del InvoiceItem
          example: "PlanPesos - período 2018-06-27 / 2018-06-27"
        type:
         type: number
         description: |
          Tipo de item
          - 1 Cargo por plan
          - 2 Descuento
          - 3 Item pendiente
          - 9 Otros
         example: 1
        currency:
          type: string
          description: Moneda del item
          example: 'CLP'
        amount:
          type: number
          description: Monto del item
          example: 20000

    Error:
      type: object
      properties:
        code:
          type: number
          description: Código de error
          example: 401
        message:
          type: string
          description: Mensaje de error
          example: 'Bad Request'

    Discount:
      type: object
      description: Descuento aplicado a una Suscripción
      properties:
        id:
          type: number
          description: Identificador del descuento
          example: 181
        type:
          type: string
          description: |
            Tipo de descuento puede ser de 2 tipos
            - Subscription discount
            - Customer discount
          example: Subscription discount
        created:
          type: string
          description: Fecha de creación del descuento
          example: 2019-12-01 00:00:00
        start:
          type: string
          description: Fecha de inicio del descuento
          example: 2019-12-01 00:00:00
        end:
          type: string
          description: Fecha de término del descuento
          example: 2019-12-31 00:00:00
        deleted:
          type: string
          description: Fecha en que se eliminó el descuento o null si está vigente
          example: 2019-12-25 00:00:00
        status:
          type: number
          description: |
            Estado del descuento
            - 1 Activo
            - 0 Inactivo
          example: 1
        coupon:
          $ref: '#/components/schemas/Coupon'


    Settlement:
      type: object
      properties:
        id:
          type: number
          description: Identificador de la liquidación
          example: 1001
        date:
          type: string
          format: 'yyyy-mm-dd'
          description: fecha de la liquidación
          example: '2018-06-15'
        rut:
          type: string
          description: Rol único tributario RUT
          example: '9999999-9'
        name:
          type: string
          description: Nombre del usuario de la cuenta Flow
          example: "Francisco Castillo"
        email:
          type: string
          description: cuenta de email del usuario de Flow
          example: 'fcastillo@gmail.com'
        initialBalance:
          type: number
          description: Saldo inicial de la cuenta
          example: -1000
        transferred:
          type: number
          description: Monto a transferir a la cuenta bancaria del comercio.
          example: 120000
        billed:
          type: number
          description: Monto a facturar por Flow para esta liquidación.
          example: 2164
        finalBalance:
          type: number
          description: Saldo final de la liquidación. Un saldo final negativo significa que el comercio le adeuda dinero a Flow, en cambio, un saldo positivo significa que Flow le adeuda al comercio.
          example: 0
        transferredSummary:
          type: array
          description: Resumen de transferencia de fondos.
          items:
            $ref: '#/components/schemas/SettlementSummary'
        billedSummary:
          type: array
          description: Resumen de facturación
          items:
             $ref: '#/components/schemas/SettlementSummary'
        transfersDetail:
          type: array
          description: Detalle de las tranferencias bancarias
          items:
            $ref: '#/components/schemas/TransferDetail'
        paymentsDetail:
          type: array
          description: Detalle de pagos de la liquidación.
          items:
            $ref: '#/components/schemas/PaymentDetail'
        generalReturnsDetail:
          type: array
          description: Detalle de Devoluciones
          items:
            $ref: '#/components/schemas/GeneralDetail'
        refundReturnsDetail:
          type: array
          description: Detalle de reembolsos devueltos
          items:
            $ref: '#/components/schemas/RefundDetail'
        refundWithholdingDetail:
          type: array
          description: Detalle de reembolsos retenidos
          items:
            $ref: '#/components/schemas/RefundDetail'
        generalWithholdingDetail:
          type: array
          description: Detalle de retenciones efectuadas
          items:
            $ref: '#/components/schemas/GeneralDetail'
        refundBilledDetail:
          type: array
          description: Detalle de reembolsos facturados
          items:
            $ref: '#/components/schemas/RefundDetail'


    SettlementSummary:
      type: object
      description: Resumen de liquidación. Si los valores se muestran con signo negativo significa que se deducen ya sea de la transferencia bancaria o de la facturación.
      properties:
        item:
          type: string
          description: Concepto del detalle
          example: 'Comisión de pagos recibidos'
        amount:
          type: number
          description: Monto del detalle
          example: -1000
        taxes:
          type: number
          description: Monto del impuesto si es que aplica
          example: -190

    TransferDetail:
      type: object
      description: Detalle de transferencia bancaria
      properties:
        date:
          type: string
          format: 'yyyy-mm-dd'
          description: Fecha de la transferencia
          example: '2018-06-15'
        name:
          type: string
          description: Nombre asociado a la cuenta bancaria
          example: 'Francisco Castillo'
        bank:
          type: string
          description: Nombre del banco
          example: 'Banco de Chile - Edwards'
        account:
          type: string
          description: Número de la cuenta bancaria
          example: '001456700900'
        type:
          type: string
          description: Tipo de cuenta
          example: 'Cuenta corriente'
        rut:
          type: string
          description: Rol único tributario asociado a la cuenta bancaria
          example: '9999999-9'
        email:
          type: string
          description: cuenta de email asoaciada a la cuenta bancaria
          example: 'fcastillo@gmail.com'
        amount:
          type: number
          description: Monto de la transferencia bancaria
          example: 120000
        status:
          type: string
          description: Estado de la transferencia
          example: Transferida

    PaymentDetail:
      type: object
      description: Detalle de pagos de una liquidación
      properties:
        id:
          type: number
          description: Identificador Flow de la transacción
          example: 3879654
        date:
          type: string
          format: 'yyyy-mm-dd hh:mm.ss'
          description: Fecha del pago
          example: '2018-06-12 16:13:39'
        subject:
          type: string
          description: Concepto del pago
          example: 'Orden 13455 Castillo.cl'
        media:
          type: string
          description: Medio de pago
          example: Multicaja
        amount:
          type: number
          description: Monto del pago
          example: 53500
        rate:
          type: number
          description: Tasa de comision aplicada
          example: 3.35
        fee:
          type: number
          description: Monto de comisión aplicado
          example: 1960

    GeneralDetail:
      type: object
      description: Detalle de Retención o Devolución
      properties:
        id:
          type: number
          description: Identificador
          example: 101
        date:
          type: string
          format: 'yyyy-mm-dd hh:mm.ss'
          description: Fecha de la Retención o Devolución
          example: '2018-06-08 17:15:33'
        subject:
          type: string
          description: Concepto
          example: 'Dif IVA retenido/facturado fact 1345'
        amount:
          type: number
          description: Monto de la retención o devolución
          example: 100

    RefundDetail:
      type: object
      description: Detalle de Reembolsos en liquidación
      properties:
        id:
          type: number
          description: Identificador del reembolso
          example: 222
        date:
          type: string
          format: 'yyyy-mm-dd hh:mm.ss'
          description: Fecha del reembolso
          example: '2018-05-04 11:47:11'
        receiverEmail:
          type: string
          description: Email del receptor del reembolso
          example: 'fcastillo@gmail.com'
        paymentId:
          type: number
          description: Identificador del pago asociado al reembolso
          example: 3654771
        amount:
          type: number
          description: Monto del reembolso
          example: 2000
        fee:
          type: number
          description: Comisión del reembolso
          example: 202
    SettlementBaseV2:
      type: object
      properties:
        id:
          type: number
          description: Identificador de la liquidación
          example: 1001
        date:
          type: string
          format: 'yyyy-mm-dd'
          description: fecha de la liquidación
          example: '2018-06-15'
        taxId:
          type: string
          description: Identificador tributario
          example: '9999999-9'
        name:
          type: string
          description: Nombre del usuario de la cuenta Flow
          example: "John Doe"
        email:
          type: string
          description: cuenta de email del usuario de Flow
          example: 'johndoe@flow.cl'
        currency:
          type: string
          description: Moneda de liquidación
          example: CLP
        initial_balance:
          type: number
          description: Saldo inicial
          example: 0
        final_balance:
          type: number
          description: Saldo final
          example: 0
        transferred:
          type: number
          description: Total a depositar
          example: 0
        billed:
          type: number
          description: Monto neto a facturar
          example: 0
    SettlementV2:
      allOf:
        - $ref: '#/components/schemas/SettlementBaseV2'
        - type: object
          properties:
            summary:
              type: object
              properties:
                transferred:
                  type: array
                  description: Resumen de transferencia de fondos.
                  items:
                    $ref: '#/components/schemas/SettlementSummary'
                commission:
                  type: array
                  description: Resumen de comisiones
                  items:
                    $ref: '#/components/schemas/SettlementComissionSummary'
                payment:
                  type: array
                  description: Resumen de pagos recibidos
                  items:
                    $ref: '#/components/schemas/SettlementPaymentSummary'
                credit:
                  type: array
                  description: Resumen de devoluciones
                  items:
                    $ref: '#/components/schemas/SettlementCreditSummary'
                debit:
                  type: array
                  description: Resumen de retenciones
                  items:
                    $ref: '#/components/schemas/SettlementDebitSummary'
                billed:
                  type: array
                  description: Resumen de facturaciones
                  items:
                    $ref: '#/components/schemas/SettlementBilledSummary'
            detail:
              type: object
              properties:
                payment:
                  type: array
                  description: Detalle de pagos de la liquidación.
                  items:
                    $ref: '#/components/schemas/SettlementPaymentDetail'
                debit:
                  type: array
                  description: Detalle de devoluciones
                  items:
                    $ref: '#/components/schemas/SettlementGeneralDetail'
                credit:
                  type: array
                  description: Detalle de retenciones
                  items:
                    $ref: '#/components/schemas/SettlementGeneralDetail'
    SettlementGeneralSummary:
      type: object
      properties:
        amount:
          type: number
          description: Monto del detalle
          example: 1000
        commission:
          type: number
          description: Comision del detalle
          example: 10
          nullable: true
        taxes:
          type: number
          description: Monto del impuesto si es que aplica
          example: 190
        balance:
          type: number
          description: Total del item (monto - comision - taxes)
          example: 1200
    SettlementComissionSummary:
      type: object
      properties:
        type:
          type: string
          description: Tipo de detalle
          example: 'Comisión de pagos'
        amount:
          type: number
          description: Monto de comisión
          example: 1000
        taxes:
          type: number
          description: Monto del impuesto si es que aplica
          example: 190
        total:
          type: number
          description: Total del item (comision - taxes)
          example: 1200
    SettlementDebitSummary:
      allOf:
        - $ref: '#/components/schemas/SettlementGeneralSummary'
        - type: object
          properties:
            operations:
              type: number
              description: Cantidad de operaciones
              example: 100
            type:
              type: string
              description: Tipo de detalle
              example: 'Reembolsos'
    SettlementCreditSummary:
      allOf:
        - $ref: '#/components/schemas/SettlementGeneralSummary'
        - type: object
          properties:
            operations:
              type: number
              description: Cantidad de operaciones
              example: 100
            type:
              type: string
              description: Tipo de detalle
              example: 'Devolución Solicitada por el Comercio'
    SettlementBilledSummary:
      type: object
      properties:
        type:
            type: string
            description: Tipo de detalle
            example: 'Comisiones de pagos recibidos'
        amount:
          type: number
          description: Monto del detalle
          example: 1000
        taxes:
          type: number
          description: Monto del impuesto si es que aplica
          example: 190
        balance:
          type: number
          description: Total del item (monto - taxes)
          example: 1200
    SettlementPaymentSummary:
      type: object
      properties:
        paymentMethod:
          type: string
          description: Medio de pago
          example: Webpay
        brand:
          type: string
          description: Marca de tarjeta (aplica sólo para medios de pagto que aceptan tarjetas de débito, crédito o prepago)
          example: Visa
          nullable: true
        operations:
          type: number
          description: Cantidad de operaciones
          example: 100
        amount:
          type: number
          description: Monto del detalle
          example: 2000
        rate:
          type: number
          description: Tasa de comisión
          example: 4.19
        fixed:
          type: number
          description: Costo fijo por operaicón
          example: 100
        commission:
          type: number
          description: Comisión
          example: 83.8
        taxes:
          type: number
          description: Impuesto
          example: 15.9
        balance:
          type: number
          description: Saldo
          example: 1900.3
    SettlementPaymentDetail:
      type: object
      properties:
        trxId:
          type: number
          description: Número de la orden
          example: 100
        date:
          type: string
          format: yyyy-mm-dd h24:mi:ss
          description: Fecha/hora de pago
          example: "2020-12-01 23:01:56"
        concept:
          type: string
          description: Concepto de pago
          example: 1 unidad de producto A
        paymentMethod:
          type: string
          description: Medio de pago
          example: Webpay
        amount:
          type: number
          description: Monto del detalle
          example: 2000
        rate:
          type: number
          description: Tasa de comisión
          example: 4.19
        commission:
          type: number
          description: Comisión
          example: 83.8
        taxes:
          type: number
          description: Monto del impuesto si es que aplica
          example: 15.9
        balance:
          type: number
          description: Monto neto a abonar
          example: 1900.3
    SettlementGeneralDetail:
      type: object
      properties:
        id:
          type: number
          description: Identificador del detalle
          example: 100
        date:
          type: string
          format: yyyy-mm-dd h24:mi:ss
          description: Fecha del detalle
          example: "2020-12-01 23:01:56"
        concept:
          type: string
          description: Concepto del detalle
          example: Reembolso
        trxId:
          type: string
          description: Número de orden
          example: 123
          nullable: true
        amount:
          type: number
          description: Monto del detalle
          example: 2000
        commission:
          type: number
          description: Comisión
          example: 4.19
          nullable: true
        taxes:
          type: number
          description: Monto del impuesto si es que aplica
          example: 190
        balance:
          type: number
          description: Monto neto
          example: 83.80
    ChargeAttemps:
      type: object
      description: Intentos fallidos de cargos automáticos
      properties:
        id:
          type: number
          description: Identificador del intento
          example: 901
        date:
          type: string
          format: 'yyyy-mm-dd hh:mm.ss'
          description: fecha del intento
          example: "2018-12-06 15:03:33"
        customerId:
          type: string
          description: Identificador del Customer
          example: "cus_1uqfm95dch"
        invoiceId:
          type: number
          description: Identificador del Invoice, si el intento no corresponde a un Invoice este vendra vacío.
          example: 1234
        commerceOrder:
          type: string
          description: El número de la orden del comercio
          example: "1883"
        currency:
          type: string
          description: La moneda del intento de cargo
          example: "CLP"
        amount:
          type: number
          format: float
          description: El monto a cobrar especificado con 4 decimales
          example: 90000.0000
        errorCode:
          type: number
          description: El código del error que se produjo en el intento de cargo
          example: 1605
        errorDescription:
          type: string
          description: La descripción del error producido en el intento de cargo
          example: "This commerceOrder 1883 has been previously paid"
    Merchant:
      type: object
      description: Objeto de comercio asociado
      properties:
        id:
          type: string
          description: Id de comercio asociado
          example: NEG-A
        name:
          type: string
          description: Nombre de comercio asociado
          example: Negocio A
        url:
          type: string
          description: Url del comercio asociado
          example: https://flow.cl
        createdate:
          type: string
          description: Fecha de creación
          example: "02-04-2020 11:52"
        status:
          type: number
          description: "Estado del comercio. Valores posibles:\n\n0: Pendiente de aprobación\n\n1: Aprobado\n\n2: Rechazado"
          example: "0"
        verifydate:
          type: string
          nullable: true
          description: Fecha de aprobación/rechazo
          example: "02-04-2020 11:52"
    MerchantDeleteResponse:
      type: object
      description: Objeto de comercio asociado
      properties:
        status:
          type: string
          description: Estado de la operacion
          example: ok
        message:
          type: string
          description: Mensaje asociado a la operacion
          example: Merchant X deleted
```
