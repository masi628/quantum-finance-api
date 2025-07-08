from fastapi import FastAPI, Request
from quantum_robo_advisor import generate_portfolio
from payments import create_checkout_session
from ai_scaler import calculate_price

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Quantum Finance API running"}

@app.get("/price")
def dynamic_price():
    return {"price": calculate_price()}

@app.post("/subscribe")
def subscribe(user: dict):
    return {"checkout_url": create_checkout_session(customer_email=user["email"])}

@app.post("/generate")
def generate(user: dict):
    return generate_portfolio(user)
