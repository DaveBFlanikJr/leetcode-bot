from modles.db import Base, engine
from modles.workspace import Workspace


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Tables created.")
