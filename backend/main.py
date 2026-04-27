from pathlib import Path
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

import cache
import ai
import weather

app = FastAPI()

# Mount the frontend directory so we can serve the index file safely
frontend_dir = Path(__file__).parent.parent / "frontend"
if frontend_dir.exists():
    app.mount("/static", StaticFiles(directory=str(frontend_dir)), name="static")

@app.get("/")
async def read_index():
    index_file = frontend_dir / "index.html"
    if index_file.exists():
        return FileResponse(str(index_file))
    return JSONResponse(status_code=404, content={"message": "Frontend not found"})

@app.post("/analyze")
async def analyze_crop(file: UploadFile = File(...)):
    try:
        # 1. Read image
        image_bytes = await file.read()
        
        # 2. Hash it
        img_hash = cache.get_image_hash(image_bytes)
        
        # 3. Check cache
        cached_res = cache.get_cached_result(img_hash)
        
        # 4. If cached -> return instantly
        if cached_res:
            return JSONResponse(content=cached_res)
            
        # 5. Else: Run AI + weather
        ai_result = ai.analyze_crop_image(image_bytes)
        weather_advice = weather.get_weather_advice()
        
        # Combine results
        final_result = {
            "disease": ai_result.get("disease", ""),
            "action": ai_result.get("action", ""),
            "warning": ai_result.get("warning", ""),
            "weather_advice": weather_advice
        }
        
        # Store in cache
        cache.set_cached_result(img_hash, final_result)
        
        # Return
        return JSONResponse(content=final_result)
        
    except Exception as e:
        print(f"DEBUG: Endpoint Error - {e}")
        # NEVER crash backend
        return JSONResponse(content={
            "disease": "Fallback: Possible crop issue.",
            "action": "Monitor closely.",
            "warning": "System error.",
            "weather_advice": "Check conditions before action"
        })
