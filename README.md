# 📚 Library Management – Módulo para Odoo 18

Este repositorio contiene elmódulo Library Management desarrollado como prueba técnica para implementar la gestión de una biblioteca en Odoo 18.0: permite registrar miembros, libros, préstamos, devoluciones y expone un endpoint REST para consultar información de libros por ISBN.

## ✅ Funcionalidades implementadas

- Registro de miembros con generación automática de código.
- Registro de libros (validación de ISBN, cálculo de años desde publicación, disponibilidad).
- Registro de préstamos:
  - Bloqueo si el miembro tiene más de 5 préstamos activos.
  - Control manual de devolución (campo y botón `returned`).
- Menús y vistas para gestionar libros, miembros y préstamos desde el backend.
- Endpoint REST:
  ```
  GET /api/library/book/<isbn>
  ```
  Devuelve en JSON los datos completos del libro.

---

## ⚙️ Requisitos previos

- Docker Desktop (Instalable desde página oficial: https://docs.docker.com/desktop/setup/install/windows-install/)
- Docker Compose (archivo "docker-compose.yml" incluido en el repostorio).
- Odoo 18.0 (al levantarse el contenedor se levanta desde la configuración en archivo yml).

---

## 🐳 Levantar el entorno (Docker)

1. Clona el repositorio:

```bash
git clone https://github.com/ronaaldleonpro/odoo_library.git
cd odoo_library
```

2. Levanta los contenedores:

- Abre Docker Desktop
- Abre un terminal en la raíz del proyecto y ejecuta:

```bash
docker compose up -d
```

3. Accede a Odoo:

- URL: [http://localhost:8069](http://localhost:8069)
- Usuario inicial: crea uno en la pantalla de configuración.

> **Nota:** Si es la primera vez, crea una base de datos desde `http://localhost:8069/web/database/manager` si no, restaura la previamente creada.

---

## 📦 Instalar y actualizar el módulo

1. Entra a Odoo ([http://localhost:8069](http://localhost:8069)).

2. Activa el modo **Desarrollador**:

   - Haz clic en tu Settings -> Developer Tools -> `Activar modo desarrollador`.

3. Actualiza la lista de aplicaciones:

   - Menú superior izquierda `Apps` → Botón `Actualizar lista de aplicaciones`.

4. Busca `Library Management` y haz clic en `Instalar`.

5. Para aplicar cambios futuros:

   - Menú `Apps` → Busca `Library Management` → Botón `Actualizar (Upgrade)`.

---

## 📖 Cómo usar el módulo

- En el menú superior izquierda aparecerá: **Library Management**.
- Desde ahí tendrás acceso a:
  - **Books**: gestionar libros.
  - **Members**: gestionar miembros.
  - **Loans**: gestionar préstamos y devoluciones.
- En la vista de préstamos, puedes registrar devoluciones accionando el botón `Return`.

---

## 🌐 Endpoint REST

**Consultar información de un libro por ISBN**:

```
GET http://localhost:8069/api/library/book/<isbn>
```

Ejemplo usando `curl`:

```bash
curl http://localhost:8069/api/library/book/978-12345-6-789-0
```

Respuesta esperada (JSON):

```json
{
  "book_id": 1,
  "title": "Sample Book",
  "author": "John Doe",
  "isbn": "978-12345-6-789-0",
  "available": true,
  "available_display": "Available",
  "publication_year": 2020,
  "active_loans": 1
}
```

---

## 🛠️ Estructura del módulo

```
odoo-library/
   ├── addons/
   │   └── library_management/
   │         ├── controllers/
   │         │   ├── __init__.py
   │         │  └── library_api.py
   │         ├── models/
   │         │  ├── __init__.py
   │         │  ├── library_book.py
   │         │  ├── library_loan.py
   │         │  └── library_member.py
   │         ├── security/
   │         │   ├── ir.model.access.csv
   │         ├── views/
   │         │   ├── __init__.py
   │         │   ├── book_views.xml
   │         │   ├── loan_views.xml
   │         │   ├── member_views.xml
   │         │   └── menu_views.xml
   │         ├── static/
   │         │   └── description/
   │         │       └── icon.png
   │         ├── __init__.py
   │         └── __manifest__.py
   ├── .gitignore
   ├── docker-compose.yml
   └── README.md
```

---

---

## ✏️ Notas finales

- Tras seguir estas instrucciones, tendrás todas las funcionalidades de la prueba técnica funcionando en local.
- Si tienes dudas, revisa el código en cada carpeta (`models`, `controllers`, `views`).

---

# 🧠 Aprendizaje

- Referencia para formato de creación del ISBN
- https://www.isbn-international.org/es/agencies
- https://agenciaisbnelsalvador.blogspot.com/2015/04/estructura-del-isbn.html

## 🚀 Autor

Ronald León
