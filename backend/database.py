from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

sql_database_url="mysql://root:Sqlrtpsswrd_NvD2022@localhost:3306/todoappdb"

print(sql_database_url)
engine=create_engine(sql_database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base=declarative_base()