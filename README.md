# Proyecto de Automatización de Pruebas - Urban Grocers App

## Descripción del Proyecto
Este proyecto automatiza pruebas de API para validar el campo `name` al crear kits de productos en la aplicación 
Urban Grocers. Las pruebas verifican respuestas correctas para entradas válidas y respuestas de error para entradas inválidas.

## Estructura del Proyecto
- **create_kit_name_kit_test.py**: Contiene las pruebas automatizadas del campo `name`.
- **sender_stand_request.py**: Define los métodos de solicitud a la API.
- **configuration.py** y **data.py**: Archivos de configuración y datos para las pruebas.

## Resumen de Resultados de Pruebas
En la última ejecución:
- **5 pruebas pasaron** exitosamente.
- **4 pruebas fallaron** debido a diferencias entre el código de estado esperado y el recibido. Estos errores indican
- que la API acepta valores inválidos para el campo `name` (como campos vacíos, largos excesivos, tipos de datos incorrectos, 
- y ausencia de campo), y devuelve un código de éxito (201) en lugar de errores esperados (400 o 500).

### Próximos Pasos
Se sugiere revisar la validación de entradas en la API para garantizar que los valores inválidos generen respuestas de error adecuadas.

## Instrucciones para Ejecutar las Pruebas
Ejecuta las pruebas con el siguiente comando en el directorio raíz del proyecto:

pytest create_kit_name_kit_test.py
