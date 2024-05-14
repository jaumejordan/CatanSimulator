class Materials:
    """
    Clase que representa los materiales. Se usa tanto en la mano de los jugadores como en las ofertas
    """

    def __init__(self, cereal=0, mineral=0, clay=0, wood=0, wool=0):
        self.cereal = cereal
        self.mineral = mineral
        self.clay = clay
        self.wood = wood
        self.wool = wool
        self.array_ids = [cereal, mineral, clay, wood, wool]
        return

    def get_from_id(self, material_constant):
        self.array_ids = [self.cereal, self.mineral, self.clay, self.wood, self.wool]
        return self.array_ids[material_constant]

    # adders #####
    def add_cereal(self, amount):
        self.cereal = self.cereal + amount
        return None

    def add_mineral(self, amount):
        self.mineral = self.mineral + amount
        return None

    def add_clay(self, amount):
        self.clay = self.clay + amount
        return None

    def add_wood(self, amount):
        self.wood = self.wood + amount
        return None

    def add_wool(self, amount):
        self.wool = self.wool + amount
        return None

    def has_this_more_materials(self, materials):
        """
        Si le llega otra clase Materials() comprobará si hay más o igual materiales que los que hay en el parámetro y
        si le llega un string con lo que se quiere construir comprobará si tiene suficiente material para hacerlo.
        :param materials: (str o Materials()) Nombre de lo que se quiere construir o materiales.
        :return: bool
        """
        if isinstance(materials, str):
            if materials == 'town':
                materials = Materials(1, 0, 1, 1, 1)
            elif materials == 'city':
                materials = Materials(2, 3, 0, 0, 0)
            elif materials == 'road':
                materials = Materials(0, 0, 1, 1, 0)
            elif materials == 'card':
                materials = Materials(1, 1, 0, 0, 1)
            else:
                return False

        if isinstance(materials, Materials):
            if (0 <= materials.cereal <= self.cereal and 0 <= materials.mineral <= self.mineral and
                    0 <= materials.clay <= self.clay and 0 <= materials.wood <= self.wood and
                    0 <= materials.wool <= self.wool):

                return True

            return False
        else:
            return False

    def __str__(self):
        return 'Materials( Cereal: ' + str(self.cereal) + ', Mineral:' + str(self.mineral) + ', Clay:' + str(
            self.clay) + ', Wood:' + str(self.wood) + ', Wool:' + str(self.wool) + ' )'

    def __to_object__(self):
        return {'cereal': str(self.cereal), 'mineral': str(self.mineral), 'clay': str(self.clay),
                'wood': str(self.wood), 'wool': str(self.wool)}

    def __repr__(self):
        return 'Materials()'
