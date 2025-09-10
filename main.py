from fastapi import FastAPI



app = FastAPI()



@app.get("/")
def index():
    return {"message": "hello world"}

if __name__ == "__main__":
    app.run()