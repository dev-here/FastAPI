from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {"data": {"name":"fast api"}}

@app.get('/abouts')
def about():
    return { "data": "about us "}