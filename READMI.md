# Quantum Finance API 🚀

API FastAPI per ottimizzazione portafogli e pricing derivati con Qiskit, integrata con Stripe per pagamenti automatici.

## 📦 Struttura

- `/app` → codice Python
- `Dockerfile` → immagine Docker per deployment
- `.env.example` → variabili ambiente da configurare
- `requirements.txt` → dipendenze Python

## 🚀 Deploy su DigitalOcean

### App Platform
1. Spingi la repo su GitHub.
2. Crea un nuovo progetto su DigitalOcean App Platform, seleziona Docker.
3. Aggiungi variables da `.env.example`.
4. Deploy automatico da GitHub.

### Droplet
```bash
git clone https://github.com/TUO/quantum-finance-api.git
cd quantum-finance-api
cp .env.example .env  # inserisci le tue variabili
docker build -t qf-api .
docker run -d -p 8000:8000 --env-file .env qf-api
