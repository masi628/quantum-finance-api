import os
import stripe

stripe.api_key = os.environ.get("STRIPE_API_KEY")

def create_checkout_session(customer_email):
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[{
                "price": os.environ.get("STRIPE_PRICE_ID"),
                "quantity": 1,
            }],
            mode="subscription",
            customer_email=customer_email,
            success_url=f"{os.environ.get('APP_DOMAIN')}/success",
            cancel_url=f"{os.environ.get('APP_DOMAIN')}/cancel",
        )
        return session.url
    except Exception as e:
        return {"error": str(e)}
