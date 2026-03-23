from fastapi import FastAPI


app = FastAPI(title="Vehicle Maintenance Tracker")


@app.get("/health")
def health_check():
    return {"status": "ok"}
