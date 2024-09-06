from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import httpx

app = FastAPI()

# Replace with the actual E-Courts API endpoint
E_COURTS_API_URL = 'https://apis.akshit.me/eciapi/16'

@app.get("/get_court_data")
async def get_court_data(case_number: str):
    if not case_number:
        raise HTTPException(status_code=400, detail="Case number is required")
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f'{E_COURTS_API_URL}', params={'case_number': case_number})
            response.raise_for_status()  # Raise an exception for bad status codes
        
        # Assuming the API returns JSON data
        data = response.json()
        return JSONResponse(content=data)
    
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Error fetching court data: {str(e)}")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)