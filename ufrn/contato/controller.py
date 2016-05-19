from ufrn.contato import entity
from infosystem.common.subsystem import controller


class Controller(controller.Controller):

    def __init__(self):
        super(Controller, self).__init__(entity.Contato)
