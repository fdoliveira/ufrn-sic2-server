from ufrn import contato
from infosystem import database
from infosystem import system as infosystem


controllers = [contato.Controller()]


subsystems = {c.entity_cls.get_name(): c for c in controllers}
subsystems.update(infosystem.subsystems)


class API(object):
    """Class that represents system APIs."""
    pass


api = API()
for name, controller in subsystems.items():
    setattr(api, name, controller.manager)


# Dependency injection
for subsystem in subsystems.values():
    subsystem.manager.api = api