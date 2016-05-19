from ufrn.common import cpf
from infosystem.common.subsystem import entity
from infosystem.database import db 


class Contato(entity.Entity, db.Model):

    attributes = ['id', 'nome', 'cpf']
    nome = db.Column(db.String(80), nullable=False)
    cpf = db.Column(db.String(11), nullable=False, unique=True)

    def __init__(self, id, nome, cpf):
        super(Profissional, self).__init__(id)
        self.nome = nome
        self.cpf = cpf

    def is_stable(self):
        is_stable = cpf.is_valid(self.cpf)

        if not is_stable:
            raise Exception('is_stable validation error')