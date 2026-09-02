from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Jenkins Demo App"}

@app.get("/health")
def health_check():
    return {"status": "ok"}


# test1

// trigger test 2
// webhook test
// confirm auto-trigger works
