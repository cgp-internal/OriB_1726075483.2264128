from db import Base

class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    user = Column(String)
    note1 = Column(String)
    note2 = Column(String)
    image1 = Column(String)
    image2 = Column(String)
    image3 = Column(String)