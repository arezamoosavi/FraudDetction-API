from starlette.applications import Starlette
from starlette.responses import PlainTextResponse, JSONResponse
from starlette.routing import Route, WebSocketRoute


def homepage(request):
    return PlainTextResponse('Hello, world!')

def uname(request):
    user = request.path_params['user']
    return JSONResponse({'You': user})

def startup():
    print('Ready to go')


routes = [
    Route('/', homepage),
    Route("/{user}", uname)
]

app = Starlette(debug=True, routes=routes, on_startup=[startup])


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5000)