from typing import Optional
from pydantic import BaseModel, EmailStr, field_validator
from datetime import date, datetime
import re

SEGMENTOS_PERMITIDOS = [
    "Tecnologia", "Comércio", "Indústria", "Serviços", "Agronegócio"
]

class EmpreendimentoBase(BaseModel):
    nome: str
    responsavel: str
    municipio: str
    segmento: str
    email: EmailStr
    status: bool = True
    cnpj: Optional[str] = None
    data_abertura: Optional[date] = None
    descricao: Optional[str] = None

    @field_validator('data_abertura', mode='before')
    @classmethod
    def formatar_data_br(cls, v):
        if isinstance(v, str):
            try:
                return datetime.strptime(v, "%d/%m/%Y").date()
            except ValueError:
                raise ValueError('Formato de data inválido. Use DD/MM/AAAA')
        return v
    
    @field_validator('data_abertura')
    @classmethod
    def validar_data_abertura(cls, v):
        if v > date.today():
            raise ValueError('A data de abertura não pode ser uma data futura')
        return v

    @field_validator('cnpj')
    @classmethod
    def validar_cnpj(cls, v):
        # Remove caracteres não numéricos
        cnpj = re.sub(r'\D', '', v)
        if len(cnpj) != 14:
            raise ValueError('CNPJ deve ter 14 dígitos')
        
        # Validação básica de dígitos repetidos
        if cnpj == cnpj[0] * 14:
            raise ValueError('CNPJ inválido')
        return cnpj
    
    @field_validator('segmento')
    @classmethod
    def validar_segmento(cls, v: str) -> str:
        v_formatado = v.strip().capitalize()
        if v_formatado not in SEGMENTOS_PERMITIDOS:
            raise ValueError(f"Segmento inválido. Escolha entre: {', '.join(SEGMENTOS_PERMITIDOS)}")
        return v_formatado

class EmpreendimentoCreate(EmpreendimentoBase):
    pass

class EmpreendimentoResponse(EmpreendimentoBase):
    id: int

    class Config:
        from_attributes = True