import requests
import pytest

# URL base para la API JSONPlaceholder
BASE_URL = "https://jsonplaceholder.typicode.com"

# --- CASO DE PRUEBA 1: GET (Éxito) ---
def test_get_all_posts_success():
    """
    Verifica el método GET (Obtener todos los posts).
    - Espera código 200 (OK).
    - Valida la estructura JSON y que la lista no esté vacía.
    """
    endpoint = f"{BASE_URL}/posts"
    response = requests.get(endpoint)

    # 1. Assertion del Código de Estado (Éxito)
    assert response.status_code == 200
    
    # 2. Validar Estructura y Contenido
    data = response.json()
    
    # Verifica que sea una lista y contenga elementos
    assert isinstance(data, list)
    assert len(data) > 0, "La lista de posts no debe estar vacía."
    
    # Verifica la estructura de un elemento individual (el primero)
    first_post = data[0]
    assert "userId" in first_post
    assert "id" in first_post
    assert isinstance(first_post["title"], str)

# --- CASO DE PRUEBA 2: POST (Creación) ---
def test_post_create_post_success():
    """
    Verifica el método POST (Crear un nuevo post).
    - Espera código 201 (Created).
    - Valida que los datos enviados sean reflejados en la respuesta.
    """
    endpoint = f"{BASE_URL}/posts"
    payload = {
        "title": "Mi Nuevo Post Automatizado",
        "body": "Contenido de prueba para el testing de la API.",
        "userId": 1
    }
    
    response = requests.post(endpoint, json=payload)

    # 1. Assertion del Código de Estado (Creación Exitosa)
    assert response.status_code == 201
    
    # 2. Validar Contenido de la Respuesta
    data = response.json()
    
    # Verifica que los datos enviados coincidan con la respuesta
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    
    # Verifica que se haya generado un ID
    assert "id" in data
    assert data["id"] is not None

# --- CASO DE PRUEBA 3: DELETE (Eliminación) ---
def test_delete_post_success():
    """
    Verifica el método DELETE (Eliminar un post).
    - Espera código 200 (OK) en JSONPlaceholder, o 204 (No Content) en otras APIs.
    - Valida que el cuerpo de la respuesta esté vacío.
    """
    # Usamos el ID 1 para simular la eliminación
    endpoint = f"{BASE_URL}/posts/1"
    
    response = requests.delete(endpoint)

    # 1. Assertion del Código de Estado 
    # JSONPlaceholder retorna 200 para DELETE, a diferencia de 204 en otras APIs.
    assert response.status_code == 200 
    
    # 2. Validar que la Respuesta esté Vacía (o un objeto vacío)
    assert response.text == "{}" or response.text == ""

# --- CASO DE PRUEBA 4: GET (Error) ---
def test_get_single_post_not_found():
    """
    Verifica el manejo de errores (GET de recurso inexistente).
    - Espera código 404 (Not Found).
    """
    # Intentamos obtener un post con un ID muy alto que no existe
    endpoint = f"{BASE_URL}/posts/99999"
    response = requests.get(endpoint)

    # 1. Assertion del Código de Estado (Error)
    assert response.status_code == 404

    # 2. Validar que la Respuesta esté vacía o sea un objeto vacío
    # JSONPlaceholder retorna un objeto vacío {} para 404
    assert response.text == "{}"