from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

app = FastAPI(debug=True)

@app.get("/info")
async def test():
    return JSONResponse(status_code=status.HTTP_200_OK, 
                        content="Hello from backend")


