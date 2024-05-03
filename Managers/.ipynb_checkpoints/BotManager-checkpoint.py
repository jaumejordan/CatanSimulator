from Bots import RandomBot, AlexPastorBot
from Classes.DevelopmentCards import DevelopmentCardsHand
from Classes.Hand import Hand


class BotManager:
    """
    Clase que se encarga de los bots. De momento solo los carga en la partida, sin embargo, cabe la posibilidad de que
    sea el bot manager el que se encargue de darle paso a los bots a hacer sus turnos
    """
    actual_player = 0
    first_bot_class = ''
    second_bot_class = ''
    third_bot_class = ''
    fourth_bot_class = ''

    players = []

    def __init__(self, for_test=False):
        if not for_test:
            self.first_bot_class = self.import_bot_class_from_input('first')
            self.second_bot_class = self.import_bot_class_from_input('second')
            self.third_bot_class = self.import_bot_class_from_input('third')
            self.fourth_bot_class = self.import_bot_class_from_input('fourth')
        elif for_test == 'test_específico':
            self.first_bot_class = AlexPastorBot.AlexPastorBot
            self.second_bot_class = AlexPastorBot.AlexPastorBot
            self.third_bot_class = AlexPastorBot.AlexPastorBot
            self.fourth_bot_class = AlexPastorBot.AlexPastorBot
        else:
            self.first_bot_class = RandomBot.RandomBot
            self.second_bot_class = RandomBot.RandomBot
            self.third_bot_class = RandomBot.RandomBot
            self.fourth_bot_class = RandomBot.RandomBot

        self.reset_game_values()
        return

    def set_actual_player(self, player_id=0):
        """
        :param player_id: int
        :return: None
        """
        self.actual_player = player_id
        return

    def reset_game_values(self):
        self.players = [
            {
                'id': 0,
                'victory_points': 0,
                'hidden_victory_points': 0,
                'player': self.first_bot_class(0),
                'resources': Hand(),
                'development_cards': DevelopmentCardsHand(),
                'knights': 0,
                'already_played_development_card': 0,
                'largest_army': 0,
                'longest_road': 0,
            },
            {
                'id': 1,
                'victory_points': 0,
                'hidden_victory_points': 0,
                'player': self.second_bot_class(1),
                'resources': Hand(),
                'development_cards': DevelopmentCardsHand(),
                'knights': 0,
                'already_played_development_card': 0,
                'largest_army': 0,
                'longest_road': 0,
            },
            {
                'id': 2,
                'victory_points': 0,
                'hidden_victory_points': 0,
                'player': self.third_bot_class(2),
                'resources': Hand(),
                'development_cards': DevelopmentCardsHand(),
                'knights': 0,
                'already_played_development_card': 0,
                'largest_army': 0,
                'longest_road': 0,
            },
            {
                'id': 3,
                'victory_points': 0,
                'hidden_victory_points': 0,
                'player': self.fourth_bot_class(3),
                'resources': Hand(),
                'development_cards': DevelopmentCardsHand(),
                'knights': 0,
                'already_played_development_card': 0,
                'largest_army': 0,
                'longest_road': 0,
            }
        ]
        return

    def import_bot_class_from_input(self, name=''):
        module_class = input(
            'Module and class of the ' + name + ' bot located in the folder Bots/ (e.g. mymodule.myclass) (leave blank to use the default): ')
        if module_class == '':
            klass = RandomBot.RandomBot
        else:
            components = module_class.split('.')
            module = __import__('Bots.' + components[0], fromlist=[components[1]])
            klass = getattr(module, components[1])

        return klass
