from .ai_analyzer import analyze_error

def run_pipeline():
    try:
        # Simulated build step
        print("Running build...")
        return {
            "status": "success",
            "message": "Build completed successfully"
        }

    except Exception as e:
        analysis = analyze_error(str(e))
        return {
            "status": "failed",
            "error": str(e),
            "analysis": analysis
        }
