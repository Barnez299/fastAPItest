from fastapi import FastAPI
import databases
import sqlalchemy


app = FastAPI()


''' DATABASE CONNECTION '''
DATABASE_URL = "postgresql://postgres:123456789@localhost/posts"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(
    DATABASE_URL
)


# ''' APP EVENT SETTING'''
# @app.on_event("startup")
# async def startup():
#     await database.connect()


# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()