from fastapi import FastAPI
from fastapi import HTTPException
from database import User
from database import database as connection
from schemas import UserRequestModel
from schemas import UserResponseModel
import statsmodels
import uvicorn
from streamapi import *

app = FastAPI(title='Proof',
              description='Trying to elaborate a web page',
              version='1.0.1')


@app.on_event('startup')
def startup():
    if connection.is_closed():
        print("Connecting...")
        connection.connect()

    connection.create_tables([User])


@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        print("Closing")
        connection.close()


@app.get('/')
async def index():
    return 'This is a proof!'


@app.post('/users')
async def create_user(user_request: UserRequestModel):
    user = User.create(
        username=user_request.username,
        email=user_request.email
    )
    return user_request


@app.get('/users/{user_id}')
async def get_user(user_id):
    user = User.select().where(User.id == user_id).first()

    if user:
        return UserResponseModel(id=user.id,
                                 username=user.username,
                                 email=user.email)

    else:
        return HTTPException(404, 'User not found')


@app.delete('/users/{user_id}')
async def delete_user(user_id):
    user = User.select().where(User.id == user_id).first()

    if user:
        user.delete_instance()
        return True
    else:
        return HTTPException(404, 'User not found')


@app.get('/predict')
def predict(preg: str, plas: str, pres: str, skin: str,
            test: str, mass: str, pedi: str, age: str):
    model2 = pickle.load(open('C:/Users/Asus/Desktop/respaldo/Desktop/Proyectos/Proyecto API/model.pkl', 'rb'))
    makeprediction = model2.predict(
        [[preg, plas, pres, skin, test, mass, pedi, age]])
    output = makeprediction

    return model2#['Your health probability is: {}'.format(output)]


if __name__ == '__main__':
    uvicorn.run(app)
