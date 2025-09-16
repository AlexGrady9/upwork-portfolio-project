"""Run script for the application."""

import sys
import os

# Add src to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, 'src')
sys.path.insert(0, src_dir)

# Load environment variables
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

if __name__ == "__main__":
    import uvicorn
    
    print("🚀 Starting Upwork Portfolio Project...")
    print("📖 API Documentation: http://127.0.0.1:8000/docs")
    print("❤️ Health Check: http://127.0.0.1:8000/health") 
    print("🌐 Main Page: http://127.0.0.1:8000")
    print("\nPress Ctrl+C to stop the server")
    print("-" * 50)
    
    # Правильный способ запуска с reload
    uvicorn.run(
        "project_name.main:app",  # Передаем как строку!
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="info"
    )