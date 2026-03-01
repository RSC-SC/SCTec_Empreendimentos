from sqlalchemy import Column, Integer, String, Boolean, Date
from .database import Base

class Empreendimento(Base):
    __tablename__ = "empreendimentos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    responsavel = Column(String, nullable=False)
    municipio = Column(String, nullable=False)
    segmento = Column(String, nullable=False) 
    email = Column(String, nullable=False)
    status = Column(Boolean, default=True)
    cnpj = Column(String, nullable=True) 
    data_abertura = Column(Date, nullable=True)
    descricao = Column(String, nullable=True)