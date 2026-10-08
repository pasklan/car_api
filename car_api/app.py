from fastapi import FastAPI, status

from car_api.routers import user


app = FastAPI()

app.include_router(
    router=user.router,
    prefix='/api/v1/users',
    tags=['users'],
)

@app.get('/health_check', status_code=status.HTTP_200_OK)
def health_check():
    return {'status': 'Ok'}

