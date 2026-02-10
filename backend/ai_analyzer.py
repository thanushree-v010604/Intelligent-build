def analyze_error(error_message: str):
    error_message = error_message.lower()

    if "modulenotfounderror" in error_message:
        return {
            "issue": "Missing Python module",
            "solution": "Install required package using pip install <package-name>"
        }

    if "syntaxerror" in error_message:
        return {
            "issue": "Syntax error in code",
            "solution": "Check brackets, colons, and indentation"
        }

    if "connection refused" in error_message:
        return {
            "issue": "Service not running",
            "solution": "Ensure backend or database is running"
        }

    return {
        "issue": "Unknown error",
        "solution": "Check logs and debug manually"
    }
