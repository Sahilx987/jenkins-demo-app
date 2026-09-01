form fastapi import FASTAPI

app = FASTAPI()

@app.get("/")
def read_root()
    return {"message": "Hello from Jenkins Demo App"}

@app.get("/health")
def health_check():
    return {"status" : ok}
