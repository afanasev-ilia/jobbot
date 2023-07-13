from fastapi import FastAPI

app = FastAPI(
    title='JobBot'
)


@app.get('/')
def hello():
    return 'Hello'
