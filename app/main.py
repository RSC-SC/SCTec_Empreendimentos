from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from . import models, schemas, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="SCTec Empreendedorismo SC - API")

@app.post("/empreendimentos/", response_model=schemas.EmpreendimentoResponse)
def criar_empreendimento(obj: schemas.EmpreendimentoCreate, db: Session = Depends(database.get_db)):
    dados_dict = obj.model_dump() if hasattr(obj, "model_dump") else obj.dict()
    novo_item = models.Empreendimento(**dados_dict)
    db.add(novo_item)
    db.commit()
    db.refresh(novo_item)
    return novo_item

@app.get("/empreendimentos/", response_model=List[schemas.EmpreendimentoResponse])
def listar_empreendimentos(
    segmento: Optional[str] = None, 
    municipio: Optional[str] = None, 
    db: Session = Depends(database.get_db)
):
    query = db.query(models.Empreendimento)
    
    if segmento:
        # Filtra ignorando maiúsculas/minúsculas
        query = query.filter(models.Empreendimento.segmento.ilike(f"%{segmento}%"))
    
    if municipio:
        query = query.filter(models.Empreendimento.municipio.ilike(f"%{municipio}%"))
        
    return query.all()

@app.put("/empreendimentos/{id}", response_model=schemas.EmpreendimentoResponse)
def atualizar_empreendimento(id: int, obj_atualizado: schemas.EmpreendimentoCreate, db: Session = Depends(database.get_db)):
    db_item = db.query(models.Empreendimento).filter(models.Empreendimento.id == id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Empreendimento não encontrado")
    
    dados_novos = obj_atualizado.model_dump() if hasattr(obj_atualizado, "model_dump") else obj_atualizado.dict()
    
    for key, value in dados_novos.items():
        setattr(db_item, key, value)
    
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/empreendimentos/{id}")
def remover_empreendimento(id: int, db: Session = Depends(database.get_db)):
    db_item = db.query(models.Empreendimento).filter(models.Empreendimento.id == id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Empreendimento não encontrado")
    
    db.delete(db_item)
    db.commit()
    return {"message": f"Empreendimento {id} removido com sucesso"}