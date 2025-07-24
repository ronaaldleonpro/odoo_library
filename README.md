📚 Library Management - Módulo para Odoo 18

✅ Descripción
Este repositorio contiene el módulo Library Management desarrollado como prueba técnica para la gestión de biblioteca en Odoo 18. Incluye:

-Registro de socios con código único
-Catálogo de libros mostrando años de antigüedad
-Préstamo y devolución de libros (máx. 5 activos por socio)
-Servicio REST para consultar información de libros por ISBN

🐳 Levantar el entorno (Docker)

Requisitos previos

-Tener instalado Docker y Docker Compose (incluido en Docker Desktop en Windows/Mac).

Pasos:
git clone https://github.com/ronaaldleonpro/odoo_library.git
cd odoo-library
docker compose up

-Accede a: http://localhost:8069

⚙️ Crear o restaurar base de datos limpia de Odoo 18

Crea una base nueva desde el selector: http://localhost:8069/web/database/manager

Nombre sugerido: library_db
Usuario: admin
Passwor: @admin

Restauara base de datos: library_db
docker cp odoo18.dump odoo-library-db-1:/odoo18.dump
docker exec -it odoo-library-db-1 bash
pg_restore -U odoo -d postgres /odoo18.dump

📦 Instalar el módulo

-Dentro de Odoo → Apps → Update Apps List
-Busca Library Management → Activar

Tras instalarlo podrás:
-Registrar nuevos socios (con código generado automáticamente)
-Gestionar catálogo de libros y ver antigüedad
-Registrar préstamos y devoluciones
-Probar el endpoint REST

🌐 Endpoint REST (Integración externa)

URL: /library/book/<isbn>
Método: GET (retorna JSON)
Ejemplo de respuesta:
{
"isbn": "1234567890",
"status": "pending"
}

🛠 Estructura del proyecto
odoo-library/
├── docker-compose.yml
├── README.md
├── .gitignore
└── addons/
   └── library_management/
      ├── **manifest**.py
      ├── models/
      │   ├── **init**.py
      │   ├── member.py
      │   ├── book.py
      │   └── loan.py
      ├── controllers/
      │   ├── **init**.py
      │   └── api.py
      └── views/
          ├── member_views.xml
          ├── book_views.xml
          └── loan_views.xml
