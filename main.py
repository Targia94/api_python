from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security.api_key import APIKeyHeader
from fastapi.openapi.docs import get_swagger_ui_html
import libraries.libraries as lib
from api.router import api_router
from starlette.middleware.cors import CORSMiddleware
from config import config

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
API_KEY = "A=j>tc[m{0$4o]"
API_KEY_NAME = "X-Access-Token"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


async def get_api_key(api_key_header: str = Depends(api_key_header)):
    if config.get('env') == 'development':
        return api_key_header
    # Altrimenti, verifica l'API key
    if api_key_header == API_KEY:
        return api_key_header
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="API Key non valida"
        )


@app.get("/api/swagger", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(openapi_url="/api/openapi.json", title="API Docs")


# Endpoint per generare l'OpenAPI JSON
@app.get("/api/openapi.json", include_in_schema=False)
async def get_openapi():
    return app.openapi()


app.include_router(api_router
                   , dependencies=[Depends(get_api_key)]
                   )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
