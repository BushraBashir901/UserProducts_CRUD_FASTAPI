from database import SessionLocal

#dependency for db connection   
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()