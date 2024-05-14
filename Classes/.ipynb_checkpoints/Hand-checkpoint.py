from Classes.Materials import Materials


class Hand:
    """
    Clase que representa la mano de los jugadores
    """

    def __init__(self):
        self.resources = Materials()
        return

    def add_material(self, resource, amount):
        """
        Suma amount al material seleccionado (si es negativo lo resta de la cantidad actual).
        Si se le pasa una lista se convierte en una función recusiva de sí misma.
        :param resource: (int o list) tipo de recurso a añadir.
        :param amount: (int) cantidad del recurso a añadir.
        :return: None
        """
        if isinstance(resource, list):
            for material in resource:
                self.add_material(material, amount)

        else:
            if resource == 0:
                self.resources.add_cereal(amount)
            elif resource == 1:
                self.resources.add_mineral(amount)
            elif resource == 2:
                self.resources.add_clay(amount)
            elif resource == 3:
                self.resources.add_wood(amount)
            elif resource == 4:
                self.resources.add_wool(amount)

        return

    def remove_material(self, resource, amount):
        """
        Resta amount al material seleccionado (si es negativo lo suma de la cantidad actual).
        Si se le pasa una lista se convierte en una función recusiva de sí misma.
        :param resource: (int o list) tipo de recurso a quitar.
        :param amount: (int)cantidad del recurso a quitar.
        :return: None
        """
        if isinstance(resource, list):
            for material in resource:
                self.remove_material(material, amount)
        else:
            if self.get_from_id(resource) >= amount:
                self.add_material(resource, (amount * -1))
        return

    def get_from_id(self, material_id):
        return self.resources.get_from_id(material_id)

    def get_total(self):
        return (self.resources.cereal + self.resources.mineral + self.resources.clay
                + self.resources.wood + self.resources.wool)

    def __str__(self):
        return 'Hand(' + str(self.resources) + ')'
