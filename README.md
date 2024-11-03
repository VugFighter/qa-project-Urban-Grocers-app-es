# Urban Grocers - Pruebas de Automatización para Creación de Kit de Productos

## Descripción del Proyecto

Este proyecto contiene pruebas automatizadas para validar el comportamiento del campo `name` al crear un kit de productos 
en la aplicación Urban Grocers. Las pruebas se diseñaron para verificar que el servidor responda adecuadamente a diferentes 
tipos de entradas en este campo y cumpla con las validaciones esperadas. La implementación utiliza `pytest` para la ejecución 
de pruebas automatizadas y está estructurada para ejecutar aserciones positivas y negativas en diferentes casos de entrada.

## Estructura del Proyecto

- **create_kit_name_kit_test.py**: Archivo principal de pruebas que incluye los casos de prueba para diferentes valores del campo `name`.
- **sender_stand_request.py**: Archivo que maneja las solicitudes POST al servidor.
- **configuration.py**: Contiene la configuración base para las URL del servicio y los endpoints.
- **data.py**: Contiene los datos de prueba predefinidos.

## Ejecución de las Pruebas

Para ejecutar las pruebas, asegúrate de tener configurado `pytest` y usa el siguiente comando desde el directorio principal del proyecto:

```bash
pytest create_kit_name_kit_test.py
```

## Resultados Esperados y Observados

Cada prueba está diseñada con un valor específico para el campo `name` y realiza una aserción basada en el estado de respuesta esperado. 
Los resultados actuales indican que:

- **Pruebas Exitosas (PASSED)**:
  - **1 letra** (`test_1_1_letter_name`): Retorna un estado 200 como se esperaba.
  - **511 letras** (`test_2_511_letter_name`): Retorna un estado 200, confirmando que el límite es aceptado.
  - **Espacio entre letras** (`test_6_space_bt_letters_name`): Retorna un estado 200, permitiendo espacios en el nombre.
  - **Nombre numérico en string** (`test_7_string_number_name`): Retorna un estado 200, aceptando números en formato string.

- **Pruebas Fallidas (FAILED)**:
  - **0 letras** (`test_3_0_letter_name`): Se esperaba un código 400, pero se recibió un 201, indicando que el servidor no manejó la falta de contenido como error.
  - **512 letras** (`test_4_512_letter_name`): Se esperaba un código 400, pero se recibió un 201, sugiriendo que el servidor no reconoce el límite de caracteres.
  - **Caracteres especiales** (`test_5_special_car_name`): Se esperaba un código 400, pero el servidor aceptó caracteres especiales, retornando un 201.
  - **Sin campo 'name'** (`test_8_no_name`): Se esperaba un 400; sin embargo, el servidor respondió con un 500, indicando una violación de la restricción NOT NULL.
  - **Número entero como nombre** (`test_9_integer_name`): Se esperaba un 400, pero el servidor respondió con un 201, aceptando el número entero como un valor válido.

### Resumen

Las pruebas indican que el servidor permite algunos valores no válidos en el campo `name`, tales como campos vacíos, entradas con caracteres especiales, 
y valores numéricos enteros. Estos resultados sugieren que se deben revisar las validaciones en el backend para asegurar que los datos del campo `name` 
cumplan con los requisitos definidos.
>>>>> Las mejoras y sugerencias son bienvenidas para continuar optimizando la automatización de las pruebas.