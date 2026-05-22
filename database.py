from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql+psycopg2://vimekrestomart:cjgP8llip6gRWIVDvAmdRv6jkmf2ZvtF@dpg-d889ereq1p3s73bs2pa0-a.oregon-postgres.render.com/vimekrestomart"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()