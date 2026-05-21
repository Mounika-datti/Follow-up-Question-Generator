from sqlalchemy import Column, Integer, String, Float
from database.db import Base

class InterviewResponse(Base):

    __tablename__ = "responses"

    id = Column(Integer, primary_key=True, index=True)

    question = Column(String)

    answer = Column(String)

    followup_question = Column(String)

    confidence = Column(Float)