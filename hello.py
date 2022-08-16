from sanic import Sanic
from sanic.response import json

app = Sanic("welcome")

@app.route('/')
async def test(request):
    return json({'hello': 'api again'})

if __name__ == '__main__':
    app.run()