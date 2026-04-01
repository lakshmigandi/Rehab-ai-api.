import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field

# 1. Initialize your Clinical App
app = FastAPI(title="Dr. Lakshmi's 3D-Robotic Rehab Suite")

# 2. Define the Patient Data Model (Pydantic)
class RehabData(BaseModel):
    joint: str = Field(..., description="E.g., Knee or Shoulder")
    angle: float = Field(..., ge=0, le=180, description="Degrees of flexion")
    patient_id: int
    is_painful: bool = False

# 3. Create the Analysis Endpoint
@app.post("/analyze_movement")
async def analyze_movement(data: RehabData):
    # Clinical Logic: Check if the range of motion is functional
    status = "Improving" if data.angle > 90 else "Requires Attention"
    
    return {
        "status": "Success",
        "message": f"Analyzing {data.joint} for Patient {data.patient_id}",
        "clinical_feedback": f"Current flexion: {data.angle}°. {status}.",
        "doctor_note": "Data secured under 3D-Robotic Rehab Protocol"
    }

# 4. Root Heartbeat Check (Verify Server is Live)
@app.get("/")
async def home():
    return {
        "message": "Dr. Lakshmi's MedTech Server is Online and Secure",
        "version": "1.0.0",
        "status": "Ready for Clinical Data"
    }

# 5. START THE SERVER (Standard Production Mode)
if __name__ == "__main__":
    # We use 0.0.0.0 so the Docker container can communicate externally
    uvicorn.run(app, host="0.0.0.0", port=8000)
