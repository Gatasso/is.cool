from typing import Optional
import sqlalchemy as alchemy
import sqlalchemy.orm as orm
from app import db
from datetime import datetime, timezone

class Professor(db.Model):
    __tablename__ = "professor"
    id: orm.Mapped[int] = orm.mapped_column(primary_key = True)
    name: orm.Mapped[Optional[str]] = orm.mapped_column(alchemy.String(100), nullable= False)
    password: orm.Mapped[str] = orm.mapped_column(alchemy.String(255), nullable = False)

    test: orm.WriteOnlyMapped['Prova'] = orm.relationship(back_populates='professor')

    def __repr__(self):
        return '<Professor {}>'.format(self.name)

class Aluno(db.Model):
    __tablename__ = "aluno"
    id: orm.Mapped[int] = orm.mapped_column(primary_key = True)
    name: orm.Mapped[str] = orm.mapped_column(alchemy.String(100), nullable = False)
    password:orm.Mapped[str] = orm.mapped_column(alchemy.String(255), nullable = False)
    semester: orm.Mapped[int] = orm.mapped_column(nullable = False)

    def __repr__(self):
        return '<Aluno {}>'.format(self.name)

class Prova(db.Model):
    __tablename__ = "prova"
    id: orm.Mapped[int] = orm.mapped_column(primary_key = True)
    semestre: orm.Mapped[Optional[int]] = orm.mapped_column(nullable = True)
    status: orm.Mapped[Optional[str]] = orm.mapped_column(alchemy.String(15),nullable = True)
    nota: orm.Mapped[Optional[int]] = orm.mapped_column(nullable = True)
    data_hora_inicio: orm.Mapped[Optional[datetime]] = orm.mapped_column(default=lambda: datetime.now(timezone.utc), index= True, nullable = True)
    data_hora_fim: orm.Mapped[Optional[datetime]] = orm.mapped_column(default=lambda: datetime.now(timezone.utc), index= True,nullable = True)
    idProf: orm.Mapped[int] = orm.mapped_column(alchemy.ForeignKey(Professor.id))

    professor: orm.Mapped[Professor] = orm.relationship(back_populates = 'test')
    questions: orm.WriteOnlyMapped['Questao'] = orm.relationship(back_populates='test')


    def __repr__(self):
        return '<Prova {}>'.format(self.id)


class Questao(db.Model):
    __tablename__ = "questao"
    id: orm.Mapped[int] = orm.mapped_column(primary_key = True)
    tipo: orm.Mapped[str] = orm.mapped_column(alchemy.String(15), index = True)
    enunciado: orm.Mapped[str] = orm.mapped_column(alchemy.Text)
    idProva: orm.Mapped[Optional[int]] = orm.mapped_column(alchemy.ForeignKey(Prova.id))
    idProf: orm.Mapped[int] = orm.mapped_column(alchemy.ForeignKey(Professor.id))
    
    test: orm.Mapped[Professor] = orm.relationship(back_populates = 'questions')

    def __repr__(self):
        return '<Id {}>'.format(self.id)