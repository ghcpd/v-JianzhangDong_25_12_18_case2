import os

# Read API key from environment (recommended) with a safe default for CI/CD tests
API_KEY = os.environ.get("API_KEY", "VALID")

