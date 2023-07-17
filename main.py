from typing import Optional
import fastapi
import uvicorn

api = fastapi.FastAPI()

@api.get('/')
def index():
    body="<html>" \
    "<body style='padding: 10px;'>" \
    "<h1>Welcome</h1>" \
    "</body>" \
    "</html>" 

    return fastapi.responses.HTMLResponse(content=body)


@api.get('/api/calculate')
def calculate( x :int ,y:int ,z:Optional[int] = None ):
    if z==0:
        return fastapi.responses.JSONResponse(content={"error":"z can't be 0"}, status_code=400)


    value = (x+y)*z
    return {
        'value': value
    }
    

uvicorn.run(api, port=8000)