def analyze_error(error_text: str):
    """
    Simple AI-style error analysis (rule-based)
    """

    error_text = error_text.lower()

    if "assert" in error_text:
        return {
            "reason": "A test assertion failed",
            "suggestion": "Check expected vs actual values in your test"
        }

    if "none" in error_text:
        return {
            "reason": "Function returned None",
            "suggestion": "Ensure your function returns a value"
        }

    if "syntaxerror" in error_text:
        return {
            "reason": "Python syntax error",
            "suggestion": "Check brackets, colons, or indentation"
        }

    if "modulenotfounderror" in error_text:
        return {
            "reason": "Missing module or wrong import",
            "suggestion": "Check file name and import path"
        }

    return {
        "reason": "Unknown error",
        "suggestion": "Check logs manually"
    }
