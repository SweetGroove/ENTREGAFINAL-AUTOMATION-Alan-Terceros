Pre entrega QA - Constancia de avances en el curso

Tecnologias utilizadas: python - pytest - selenium web driver - git

Los test son los siguientes:

    1.  Automatización de login
    2.  Verificación del título de la página de inventario sea el correcto
        Comprobación de existencia de productos visibles en la página
    3.  Prueba de que hay items cargados en el carrito

    Para ejecutar: pytest -v

 Para Testear API
   Ejecutar: pytest test_api_reqres.py   

El proyecto está estructurado de la siguiente manera:

    pages/: Clases del Page Object Model (Lógica de las páginas web).
    tests/: Scripts de prueba (UI y API).
    utils/: Herramientas comunes y cargadores de datos.
    data/: Archivos JSON con datos de prueba (Data Driven Testing).
    reports/: Resultados de las ejecuciones (HTML y Screenshots).