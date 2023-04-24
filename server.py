import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "social_network")
import uvicorn
from social_network.asgi import application

if __name__ == "__main__":
    # Inicia o servidor WSGI do Uvicorn
    uvicorn.run(application, host="0.0.0.0", port=8000, workers=4, reload=True)
