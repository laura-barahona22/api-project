#Cuando las queries que se hacen a la API son erroneas o los datos no existen en nuestra DB
from flask import request

class APIError(Exception):
    statusCode = 500

class Error404(APIError)
    statusCode = 400

def checkvalidParams(valid_params):
    params=[request.args.keys()]
    for p in params:
        if p not in valid_params:
            raise APIError(f'{p} is not a valid query parametrer.Valid params:{valid_params}')

def errorHelper(validQueryParams=[]):
    def decorator(fn):
        def wrapper(*args,*kwargs)
            try:
                checkvalidParams(validqueryParams)
                return fn(+args,*kwargs)
            except APIError as e:
                return {"status":"api-error",
                        "message":str(e)
                },e.statusCode
            except Exception as e:
                return {"status":"error"
                        "message":str(e)
                },500
        wrapper.__name__=fn.__name__
        return wrapper
    return decorator