import subprocess
from .ai_analyzer import analyze_error

def run_pipeline():
    try:
        result = subprocess.run(
            ["python", "-m", "pytest"],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            return {
                "status": "SUCCESS",
                "message": "Build & Tests passed successfully ✅"
            }
        else:
            ai_result = analyze_error(result.stderr)

            return {
                "status": "FAILED",
                "error_log": result.stderr,
                "ai_analysis": ai_result
            }

    except Exception as e:
        return {
            "status": "ERROR",
            "message": str(e)
        }
