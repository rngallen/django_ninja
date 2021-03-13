# django_ninja

Create API with django ninja

**Easy**: Designed to be easy to use and intuitive.
**FAST execution**: Very high performance thanks to Pydantic and async support.
**Fast to code**: Type hints and automatic docs lets you focus only on business logic.
**Standards-based**: Based on the open standards for APIs: **OpenAPI** (previously known as Swagger) and **JSON Schema**.
**Django friendly**: (obviously) has good integration with the Django core and ORM.
**Production ready**: Used by multiple companies on live projects.


Configure and .env file with the following variables
```
DJANGO_SETTINGS_MODULE=apidemo.settings.development
```
SECRET_KEY=your_secret_key
ENGINE=db_backends
DB_NAME=database_name
DB_USER=database_user
DB_PASSWORD=database_password
DB_HOST=host_name
PORT=database_type_default_port
EMAIL_HOST=email_host_server
EMAIL_HOST_USER=email_account
EMAIL_HOST_PASSWORD=email_password
EMAIL_PORT=email_default_port
EMAIL_USE_SSL=depends_on_email_server
DEFAULT_FROM_EMAIL=default_from_email
#EMAIL_USE_TLS=depends_on_email_server