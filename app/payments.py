import os, stripe
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

def create_checkout_session(customer_email):
    return stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{"price": os.getenv("STRIPE_PRICE_ID"), "quantity":1}],
        mode="subscription",
        customer_email=customer_email,
        success_url=os.getenv("APP_DOMAIN")+"/success",
        cancel_url=os.getenv("APP_DOMAIN")+"/cancel"
    ).url
