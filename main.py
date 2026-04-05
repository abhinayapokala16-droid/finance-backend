from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "API Working"}

@app.post("/transactions/")
def create(tx: schemas.TransactionCreate, db: Session = Depends(get_db)):
    return crud.create_transaction(db, tx)

@app.get("/transactions/")
def read(db: Session = Depends(get_db)):
    return crud.get_transactions(db)

@app.delete("/transactions/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    return crud.delete_transaction(db, id)