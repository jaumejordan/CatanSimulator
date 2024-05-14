from Classes.Board import Board
from Classes.DevelopmentCards import *
from Classes.Hand import Hand
from Classes.TradeOffer import TradeOffer


class BotInterface:
    """
    Interfaz que implementa a un bot
    """

    def __init__(self, bot_id):
        self.hand = Hand()
        self.board = Board()
        self.development_cards_hand = DevelopmentCardsHand()
        self.id = bot_id

    # Los triggers son llamados por el GameDirector las veces que sean necesarias hasta que devuelvan null
    #  o el GameDirector le niegue continuar el trigger
    def on_trade_offer(self, incoming_trade_offer=TradeOffer()):
        """
        Trigger para cuando llega una oferta. Devuelve si la acepta, la niega o envía una contraoferta
        :param incoming_trade_offer: Oferta de comercio que le llega al bot
        :return: true, TradeOffer, false
        """
        return False

    def on_turn_start(self):
        """
        Trigger para cuando empieza el turno. Termina cuando hace un return. Se hace antes que tirar dados. Sirve para jugar cartas de desarrollo
        :return: DevelopmentCard, None
        """
        return None

    def on_having_more_than_7_materials_when_thief_is_called(self):
        """
        Trigger que se llama cuando se debe descartar materiales. Si no los descarta el bot, los descartará
        el GameDirector aleatoriamente.
        :return: Hand()
        """
        return self.hand

    def on_moving_thief(self):
        """
        Trigger para cuando sale un 7 en el dado o se usa una carta de soldado. Esto obliga a mover al ladrón.
        Si no se hace el GameDirector lo hará de manera aleatoria. Incluyendo robar 1 recurso de cualquier
        jugador adyacente a la ficha de terreno seleccionada
        :return: {terrain, player}
        """
        terrain_id = 0
        for terrain in self.board.terrain:
            if terrain['has_thief']:
                terrain_id = terrain['id']
                break

        return {'terrain': terrain_id, 'player': -1}

    def on_turn_end(self):
        """
        Trigger para cuando acaba el turno. Termina cuando hace un return. Sirve para jugar cartas de desarrollo
        :return: DevelopmentCard, None
        """
        return None

    def on_commerce_phase(self):
        """
        Trigger para cuando empieza la fase de comercio. Devuelve una oferta
        :return: TradeOffer, dict{'gives': int, 'receives': int}, None
        """
        return None

    def on_build_phase(self, board_instance):
        """
        Trigger para cuando empieza la fase de construcción. Devuelve un string indicando qué quiere construir
        :return: dict{'building': str, 'node_id': int, 'road_to': int/None}, None
        """
        return None

    def on_game_start(self, board_instance):
        """
        Se llama únicamente al inicio de la partida y sirve para colocar 1 pueblo y una carretera adyacente en el mapa
        :return: int, int
        """
        self.board = board_instance

        node_id = random.randint(0, 53)
        possible_roads = self.board.nodes[node_id]['adjacent']

        return node_id, possible_roads[random.randint(0, len(possible_roads) - 1)]

    def on_monopoly_card_use(self):
        """
        Se elige un material. El resto de jugadores te entregan dicho material
        0: Cereal
        1: Mineral
        2: Clay
        3: Wood
        4: Wool
        :return: int, representa el material elegido
        """
        return None

    def on_road_building_card_use(self):
        """
        Se eligen 2 lugares válidos donde construir carreteras. Si no son válidos, el programa pondrá aleatorios
        :return: {'node_id': int, 'road_to': int, 'node_id_2': int, 'road_to_2': int}
        """
        return None

    def on_year_of_plenty_card_use(self):
        """
        Se eligen dos materiales (puede elegirse el mismo 2 veces). Te llevas una carta de ese material
        :return: {'material': int, 'material_2': int}
        """
        return None
