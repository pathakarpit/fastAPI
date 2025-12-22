from fastapi import FastAPI, Depends

app = FastAPI()

def get_db():
    db = {'connection': 'Database Connection Established'}
    try:
        yield db
    finally:
        db.close()
        pass


@app.get('/home')
def home(db=Depends(get_db)):
    return {'db_status': db['connection']}