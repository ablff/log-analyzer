from fastapi import FastAPI
from main import analyze_logs
from blocklist_generator import generate_blocklist
from viewer import viewer_web

app = FastAPI(
    title="Security Log Analyzer API",
    description="REST API for threat monitoring and log analysis",
    version="1.0.0"
)

@app.get("/analyze")

def trigger_analysis():
    analysis_result = analyze_logs()
    return analysis_result 

@app.get("/generate-blocklist")

def trigger_blocklist():
    blocklist_result = generate_blocklist()
    return blocklist_result

@app.get("/viewer")

def trigger_viewer():
    viewer_result = viewer_web()
    return viewer_result