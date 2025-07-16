from fastapi import FastAPI
from pydantic import BaseModel
from .quantum_robo_advisor import generate_portfolio
from .payments import create_checkout_session
from .ai_scaler import calculate_price
from .email_sender import send_email

app = FastAPI(
    title="Quantum Finance API",
    description="API per ottimizzazione di portafogli e derivati tramite algoritmi quantistici",
    version="1.0.0"
)

class UserInput(BaseModel):
    email: str
    risk: str = "medium"
    budget: float = 2.0

@app.get("/")
def root():
    return {"status": "Quantum Finance API running 🚀"}

@app.get("/price")
def dynamic_price():
    return {"price": calculate_price()}

@app.post("/subscribe")
def subscribe(user: UserInput):
    url = create_checkout_session(customer_email=user.email)
    send_email(user.email, "Benvenuto su Quantum Finance", "Grazie per esserti iscritto!")
    return {"checkout_url": url}

@app.post("/generate")
def generate(user: UserInput):
    return generate_portfolio(user.dict())
