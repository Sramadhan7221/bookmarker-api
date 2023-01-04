HTTP_200_OK=200
HTTP_201_CREATED=201
HTTP_202_ACCEPTED=202
HTTP_203_NON_AUTHORITATIVE_INFORMATION=203
HTTP_204_NO_CONTENT=204
HTTP_205_RESET_CONTENT=205
HTTP_206_PARTIAL_CONTENT=206
HTTP_207_MULTI_STATUS=207
HTTP_208_ALREADY_REPORTED=208
HTTP_226_IM_USED=226
HTTP_300_MULTIPLE_CHOICES=300
HTTP_301_MOVED_PERMANENTLY=301
HTTP_302_FOUND=302
HTTP_303_SEE_OTHER=303
HTTP_304_NOT_MODIFIED=304
HTTP_305_USE_PROXY=305
HTTP_306_RESERVED=306
HTTP_307_TEMPORARY_REDIRECT=307
HTTP_308_PERMANENT_REDIRECT=308
HTTP_400_BAD_REQUEST=400
HTTP_401_UNAUTHORIZED=401
HTTP_402_PAYMENT_REQUIRED=402
HTTP_403_FORBIDDEN=403
HTTP_404_NOT_FOUND=404
HTTP_405_METHOD_NOT_ALLOWED=405
HTTP_406_NOT_ACEPTABLE=406
HTTP_407_PROXY_AUTH_REQUIRED=407
HTTP_408_REQUEST_TIMEOUT=408
HTTP_409_CONFLICT=409
HTTP_410_GONE=410
HTTP_411_LENGTH_REQUIRED=411
HTTP_412_PRECONDITION_FAILED=412
HTTP_413_REQUEST_ENTITY_TOO_LARGE=413
HTTP_414_REQUEST_URI_TOO_LONG=414
HTTP_414_UNSUPORTED_MEDIA_TYPE=415
HTTP_500_INTERNAL_SERVER_ERROR=500

def is_informational(status):
   #1xx
   pass

def is_success(status):
   #2xx
   pass

def is_redirect(status):
   #3xx
   pass

def is_client_err(status):
   #4xx
   pass

def is_server_err(status):
   #5xx
   pass