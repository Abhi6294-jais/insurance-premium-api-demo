Insurance Premium Category Predictor

This repo contains:
- `app.py` - FastAPI app exposing a `/predict` endpoint using `model.pkl`.
- `main.py` - Patient management API.
- `frontend.py` - Streamlit frontend that calls the `/predict` endpoint.
- `fastapi_ml_model.ipynb` - Notebook used to train and save `model.pkl`.
- `requirements.txt` - Python dependencies.

Notes before pushing
- `model.pkl` is ignored by default; if you want the model in the repo use Git LFS or upload the model elsewhere and update `app.py` to download it at runtime.
- `meyenv` (virtualenv) is ignored. Recreate environment locally with `python -m venv meyenv` and `pip install -r requirements.txt`.

How to push this project to GitHub (create repo on GitHub first)

1. Initialize and commit locally (already done for you):

   git init
   git add .
   git commit -m "Initial commit"

2. Create a GitHub repository in your account (via GitHub UI).
3. Add remote and push (replace `<your-github-repo-url>`):

   git remote add origin <your-github-repo-url>
   git branch -M main
   git push -u origin main

Deploy frontend to Streamlit Cloud (after pushing):
- Go to https://share.streamlit.io/ and click "New app" → connect your GitHub repo and choose `frontend.py`.
- Update `API_URL` in `frontend.py` to your deployed FastAPI public URL (or the hosted server IP).

Run locally

1. Activate venv and start FastAPI:

```powershell
.\meyenv\Scripts\Activate.ps1
.\meyenv\Scripts\python -m uvicorn app:app --reload
```

2. Run Streamlit frontend locally:

```powershell
streamlit run frontend.py
```

If you want, I can add a GitHub remote and push — tell me the repo URL or I can open a browser to create the repo for you.