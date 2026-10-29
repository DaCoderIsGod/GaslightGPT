from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from chat import chatbot
from fastapi.responses import JSONResponse

app = FastAPI()
origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)
chat_history = []
@app.get('/chat/{model}')
def chat(input: str, model: str):
    try:
        output, _ = chatbot(input, "therapist", history=[])
        return output
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

