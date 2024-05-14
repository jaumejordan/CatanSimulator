import math
import random

from Classes.Constants import DevelopmentCardConstants as Dcc


# Debido a como funciona el juego, en caso de querer lanzar una carta de desarrollo debería de lanzarse siempre que
# un jugador devuelva una carta como parte de su on_... Si devuelve una carta, el GameManager resuelve su efecto y
# cuenta cualquier otra carta que intente lanzar como un paso de fase.
class DevelopmentDeck:
    # Puedes construir cualquier cantidad de cartas de desarrollo PERO solo puedes jugar una.
    # Puedes jugar cualquier cantidad de cartas de desarrollo que otorguen puntos de victoria.
    # Las cartas que dan puntos de victoria (idealmente) se mantienen en secreto hasta que se pueda ganar con ellas
    # NO se puede jugar una carta que se acaba de comprar SALVO que sea una que te lleve a 10 puntos de victoria
    # Se pueden jugar en cualquier momento de una ronda, incluso antes de tirar el dado (en cualquier on_... del bot)

    deck = []  # Deck es un array de objetos carta
    current_index = 0  # La carta que se va a robar si alguien construye una

    def __init__(self):
        # Se vacía primero por completo el deck para evitar que se dupliquen las cartas
        self.deck.clear()
        # Genera el array de cartas de desarrollo y lo baraja
        # Hay 14 soldados
        # 6 cartas de progreso (2 de cada)
        # 5 de puntos de victoria
        for i in range(0, 14):
            self.deck.append(DevelopmentCard(i, Dcc.KNIGHT, Dcc.KNIGHT_EFFECT))
        for i in range(14, 19):
            self.deck.append(DevelopmentCard(i, Dcc.VICTORY_POINT, Dcc.VICTORY_POINT_EFFECT))
        for i in range(19, 21):
            self.deck.append(DevelopmentCard(i, Dcc.PROGRESS_CARD, Dcc.ROAD_BUILDING_EFFECT))
        for i in range(21, 23):
            self.deck.append(DevelopmentCard(i, Dcc.PROGRESS_CARD, Dcc.YEAR_OF_PLENTY_EFFECT))
        for i in range(23, 25):
            self.deck.append(DevelopmentCard(i, Dcc.PROGRESS_CARD, Dcc.MONOPOLY_EFFECT))
        return

    def shuffle_deck(self):
        # Se barajan las cartas de desarrollo
        current_index, random_index = len(self.deck), 0
        while current_index != 0:
            random_index = math.floor(random.random() * current_index)
            current_index -= 1
            (self.deck[current_index], self.deck[random_index]) = (self.deck[random_index], self.deck[current_index])
        return

    def draw_card(self):
        if self.current_index != len(self.deck):  # No quedan cartas que robar
            card = self.deck[self.current_index]
            self.current_index += 1
            return card
        return

    def __str__(self):
        string = '[ \n'
        for card in self.deck:
            string += card.__str__()
            string += ', \n'
        string += ']'

        return string


class DevelopmentCard:
    """
    Carta de desarrollo
    :param id: Número que identifica la carta.
    :param type: Punto de victoria, soldado, o carta de progreso (monopolio, año de la cosecha,
    construir 2 carreteras gratis).
    :param effect: En función del número que tiene, hace una cosa u otra.
    """

    def __init__(self, id=0, type='', effect=0):
        self.id = id
        self.type = type
        self.effect = effect
        return

    def __str__(self):
        return "{'id': " + str(self.id) + ", 'type': " + str(self.type) + ", 'effect': " + str(self.effect) + "}"

    def __to_object__(self):
        return {'id': self.id, 'type': self.type, 'effect': self.effect}


class DevelopmentCardsHand:
    """
    Clase que interactúa con la mano del jugador. Cada jugador solo puede ver su propia mano salvo que se use una carta,
    en cuyo caso los demás jugadores saben la carta usada.
    """
    hand = []  # Cartas que posee en mano

    def __init__(self):
        self.hand = []
        return

    def add_card(self, card):
        if isinstance(card, DevelopmentCard):
            self.hand.append(card)
        else:
            return

    def check_hand(self):
        """
        Devuelve la mano que tiene el jugador, por si quiere por su cuenta comprobar qué cartas posee para gastar.
        :return: [{'id': int, 'type': string, 'effect': int}...]
        """
        hand_array = []
        for card in self.hand:
            card_obj = {'id': card.id, 'type': card.type, 'effect': card.effect}
            hand_array.append(card_obj)

        return hand_array

    def select_card_by_array_index(self, index):
        """
        Al usar esta función indicas que quieres jugar esta carta pasando el índice de la carta en el array,
        lo que se la pasa al gameManager, la juega y la borra de la mano.
        :param index:
        :return: {'id': int, 'type': string, 'effect': int}
        """
        if len(self.hand):
            card_obj = self.hand[index]
            return card_obj
        return

    def select_card_by_id(self, id):
        """
        Seleccionas la carta con el ID que se le pase, la pasa al gameManager, la juega y la borra de la mano.
        :param id: (int) Número indicativo de la carta.
        """
        for card in self.hand:
            if card.id == id:
                card_obj = card
                return card_obj

        return

    def delete_card(self, id):
        """
        Borra la carta con la ID que se le pase.
        :param id: (int) Número indicativo de la carta.
        """
        rest_of_hand = []
        for card in self.hand:
            if card.id != id:
                rest_of_hand.append(card)
        self.hand = rest_of_hand
        return
