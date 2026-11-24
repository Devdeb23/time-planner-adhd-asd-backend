from fastapi import FastAPI
app = FastAPI(title="Time Planner")

@app.get("/")


def home():
    return {"messaggio": "Ciao"}