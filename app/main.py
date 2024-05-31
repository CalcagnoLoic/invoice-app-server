from typing import List
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database.db import engine, SessionLocal
from models.models import Base
from controllers.controllers import read_all_invoices, read_invoice_by_id
from schemas.schemas import Invoice

app = FastAPI()

origins = [
    "http://localhost:8000/invoices",
    "http://localhost:8000",
    "http://localhost:5173",
    "http://localhost:5173/invoice-app-web/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/invoices/", status_code=200, response_model=List[Invoice])
async def get_all_invoice(db: Session = Depends(get_db)):
    invoices = read_all_invoices(db)
    return invoices


@app.get("/invoices/{invoice_id}", status_code=200, response_model=List[Invoice])
async def get_invoice(invoice_id: str, db: Session = Depends(get_db)):
    invoice = read_invoice_by_id(db, invoice_id)
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return invoice


@app.post("/create-new-invoice/", status_code=201)
async def create_new_invoice(db: Session = Depends(get_db)):
    pass


@app.put("/edit-invoice/{invoice_id}")
async def edit_invoice(db: Session = Depends(get_db)):
    pass


@app.delete("/invoices/{invoice_id}")
async def delete_invoice(db: Session = Depends(get_db)):
    pass
