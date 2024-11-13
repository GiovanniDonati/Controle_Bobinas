from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title='Controle de Bobinas'
)

def __init__():
    uvicorn.run('backend.app.main:app', port='8001', host='0.0.0.0', reload=True, log_level='info')
    
if __name__ == '__main__':
    __init__()