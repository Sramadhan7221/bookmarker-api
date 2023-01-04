template = {
   "swagger": "2.0",
   "info": {
      "title": "Bookmarks API",
      "description": "API for bookmarks",
      "contact": {
         "responsibleOrganization": "",
         "responsibleDeveloper": "",
         "email": "me@me.com",
         "url": "www.me.com",
      },
      "termsOfService": "http://me.com/terms",
      "version": "1.0"
   },
   "basePath": "/api/v1",  # base bash for blueprint registration
   "schemes": [
      "http",
      "https"
   ],
   "securityDefinitions": {
      "Bearer": {
         "type": "apiKey",
         "name": "Authorization",
         "in": "header",
         "description": "JWT Authorization header using Bearer scheme. Example: \"Authorization: Bearer {token}\""
      }
   },
   "operationId": "getmyData"
}

swagger_config = {
   "headers": [
   ],
   "specs": [
      {
         "endpoint": 'apispec',
         "route": '/apispec.json',
         "rule_filter": lambda rule: True,  # all in
         "model_filter": lambda tag: True,  # all in
      }
   ],
   "static_url_path": "/flasgger_static",
   # "static_folder": "static",  # must be set by user
   "swagger_ui": True,
   "specs_route": "/"
}
