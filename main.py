import uvicorn
from fastapi import FastAPI, File, UploadFile
from pandasExer import dataframeCreating
from fastapi.responses import StreamingResponse, JSONResponse
import pandas as pd
from io import StringIO
import requests


app = FastAPI()

data = dataframeCreating.data()

def readJson():
    #return pd.read_json("https://www.omdbapi.com/?apikey=4287ad07&s=Avengers")
    #print(pd.read_json("products.json").to_dict(orient='records'))
    return pd.read_json("products.json").to_dict(orient='records')

def fetchData():
    try:
        return requests.get('https://www.omdbapi.com/?apikey=4287ad07&s=Avengers',verify=False, timeout=5).json()
    except Exception as e:
        print(e)
        return "No data"


@app.get("/")
def index():
    return {"message": data}

@app.get("/movies")
def index():
    data = fetchData()
    
    return {"data": data}

@app.get("/products")
def index():
    data = readJson()
    
    return JSONResponse(data)

@app.post("/upload-csv/")
async def upload_csv(file: UploadFile = File(...)):
    # Ensure the uploaded file is a CSV
    if file.content_type != "text/csv":
        return {"error": "File must be a CSV"}
    
    # Read the file content
    content = await file.read()
    
    # Convert bytes to a string and load into Pandas DataFrame
    csv_data = StringIO(content.decode("utf-8"))
    df = pd.read_csv(csv_data)
    
    # Example: Return the first few rows as JSON
    return df.head().to_dict(orient="records")

@app.get("/download-csv/")
async def download_csv():
    # Create a sample DataFrame
    df = pd.DataFrame({"Name": ["Alice", "Bob"], "Age": [25, 30]})
    # Convert DataFrame to CSV
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)
    # Return as a downloadable file
    return StreamingResponse(csv_buffer, media_type="text/csv", headers={"Content-Disposition": "attachment; filename=data.csv"})

@app.post("/process-csv/")
async def process_csv(file: UploadFile = File(...)):
    # Read the uploaded file
    content = await file.read()
    # Convert bytes to string and load into Pandas DataFrame
    df = pd.read_csv(StringIO(content.decode("utf-8")))
    # Perform some processing (e.g., calculate mean of a column)
    if "Age" in df.columns:
        mean_age = df["Age"].mean()
        return {"mean_age": mean_age}
    return {"error": "Column 'Age' not found"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)