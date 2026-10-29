from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get('/chat/{model}')
def chatbot(input: str, model: str):
    if model == 'therapist':
        return input + 'hello'
    else:
        return input + ' huhuh'

