import os, stripe
from fastapi import FastAPI, Request, HTTPException

app = FastAPI()
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
endpoint_secret = os.getenv("STRIPE_WEBHOOK_SECRET")

@app.post("/webhook")
async def stripe_webhook(request: Request):
    payload, sig = await request.body(), request.headers.get("stripe-signature")
    try:
        event = stripe.Webhook.construct_event(payload, sig, endpoint_secret)
    except:
        raise HTTPException(400, "Invalid webhook signature")
    if event["type"]=="checkout.session.completed":
        sess = event["data"]["object"]
        print("✅ Subscribed:", sess.get("customer_email"))
    return {"status":"success"}
