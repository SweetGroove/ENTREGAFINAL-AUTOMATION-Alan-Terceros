ENTREGA FINAL AUTOMATION TESTING QA 

Proyecto de automatización desarrollado utilizando python como lenguaje principal junto a pruebas UI (Selenium) aplicando el patron de diseño POM. 

Tecnologias utilizadas: 

    Python  ->  Lenguaje principal de desarrollo
    Pytest  ->  Framework para la ejecución, gestión de tests y asserts
    Selenium WebDriver  ->  Herramienta de automatización de interacciones con el navegador(UI)
    Requests    ->  Libreria para testear conexion HTTPS y API
    HTML Report ->  Generación de reportes
    POM ->  Patron de diseño implementado

    Para ejecutar: pytest -v

Para Testear API
   Ejecutar: pytest test_api_reqres.py   

El proyecto está estructurado de la siguiente manera:

    pages/: Clases del Page Object Model (Lógica de las páginas web).
    tests/: Scripts de prueba (UI y API).
    utils/: Herramientas comunes y cargadores de datos.
    data/: Archivos JSON con datos de prueba (Data Driven Testing).
    reports/: Resultados de las ejecuciones (HTML y Screenshots).