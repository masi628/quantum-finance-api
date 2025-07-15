from fastapi import FastAPI
from pydantic import BaseModel
from quantum_robo_advisor import generate_portfolio
from payments import create_checkout_session
from ai_scaler import calculate_price

app = FastAPI()

# 🔐 Modello utente con validazione tramite Pydantic
class UserInput(BaseModel):
    email: str
    risk: str = "medium"
    budget: float = 2.0

@app.get("/")
def root():
    return {"status": "Quantum Finance API running"}

@app.get("/price")
def dynamic_price():
    return {"price": calculate_price()}

@app.post("/subscribe")
def subscribe(user: UserInput):
    return {
        "checkout_url": create_checkout_session(customer_email=user.email)
    }

@app.post("/generate")
def generate(user: UserInput):
    return generate_portfolio(user.dict())
