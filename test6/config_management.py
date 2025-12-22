from fastapi import FastAPI, Depends

app = FastAPI()

class Settings:
    def __init__(self):
        self.api_key = "supersecretapikey"
        self.debug = True

def get_settings():
    return Settings()

@app.get('/config')
def config(settings: Settings = Depends(get_settings)):
    return {
        "api_key": settings.api_key,
        "debug": settings.debug
    }