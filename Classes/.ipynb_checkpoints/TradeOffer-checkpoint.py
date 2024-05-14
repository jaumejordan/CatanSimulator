from Classes.Materials import Materials


class TradeOffer:
    """
    Clase que representa los intercambios entre jugadores.
    """
    def __init__(self, gives=Materials(), receives=Materials()):
        self.gives = gives
        self.receives = receives
        return

    def __str__(self):
        return 'TradeOffer( ' + str(self.gives) + ' | ' + str(self.receives) + ' )'

    def __to_object__(self):
        return {'gives': self.gives.__to_object__(), 'receives': self.receives.__to_object__()}
