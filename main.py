from fastapi import FastAPI
from controller.faceController import router

app = FastAPI()
app.include_router(router)


'''
# Start project.
if __name__ == '__main__':
    app = FastAPI()
   

'''