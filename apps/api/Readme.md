# AI Financial Intelligence Platform

An AI-powered stock analysis platform that combines:

- Real-time stock market data
- Financial news aggregation
- FinBERT sentiment analysis
- Price intelligence metrics
- Gemini-powered market summaries

## Run in the monorepo

Install the Python dependencies for the backend:

```powershell
cd apps/api/backend
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

Start the API on its own:

```powershell
cd apps/api
pnpm dev
```

Or activate the backend venv once and start everything from the repo root:

```powershell
cd apps/api/backend
.\.venv\Scripts\activate
cd ..\..
pnpm dev
```

The API will run at `http://localhost:8000` and the root health route is `/`.

## Tech Stack

- FastAPI
- Python
- YFinance
- FinBERT
- Google Gemini API

## Features

- Stock Fundamentals
- News Analysis
- Sentiment Scoring
- Price Intelligence Layer
- AI-generated Market Insights