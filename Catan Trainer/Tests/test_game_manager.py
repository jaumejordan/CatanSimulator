from Classes.Materials import Materials
from Managers.GameManager import GameManager
from Classes.TradeOffer import TradeOffer
from Classes.Constants import MaterialConstants


class TestGameManager:
    game_manager = GameManager(for_test=True)

    def test_reset_values(self):
        self.game_manager.already_played_development_card = True
        self.game_manager.last_dice_roll = 4
        self.game_manager.largest_army = 5
        self.game_manager.largest_army_player = {"name": "<NAME>"}
        self.game_manager.longest_road = {"name": "<NAME>"}
        self.game_manager.board.build_town(0, 0)
        self.game_manager.board.build_city(0, 0)
        self.game_manager.board.build_town(2, 7)
        self.game_manager.development_cards_deck.draw_card()
        self.game_manager.set_turn(2)
        self.game_manager.set_whose_turn_is_it(3)
        self.game_manager.set_phase(1)
        self.game_manager.set_round(10)
        self.game_manager.bot_manager.players[0]['victory_points'] = 5

        self.game_manager.reset_game_values()

        assert self.game_manager.already_played_development_card is False
        assert self.game_manager.last_dice_roll == 0
        assert self.game_manager.largest_army_player == {} and self.game_manager.largest_army == 2
        assert self.game_manager.longest_road == {'longest_road': 4, 'player': -1}
        assert (self.game_manager.board.nodes[0]['player'] == -1 and
                self.game_manager.board.nodes[0]['has_city'] is False)
        assert (self.game_manager.board.nodes[0]['player'] == -1 and
                self.game_manager.board.nodes[0]['has_city'] is False)
        assert (self.game_manager.board.nodes[2]['player'] == -1 and
                self.game_manager.board.nodes[7]['has_city'] is False)
        assert (self.game_manager.development_cards_deck.deck != [] and
                self.game_manager.development_cards_deck.current_index == 0)
        assert (self.game_manager.turn_manager.turn == 0 and self.game_manager.turn_manager.whose_turn_is_it == 0 and
                self.game_manager.turn_manager.phase == 0 and self.game_manager.turn_manager.round == 0)
        assert self.game_manager.bot_manager.players[0]['victory_points'] == 0

    def test_give_resources(self):
        self.game_manager.reset_game_values()

        self.game_manager.last_dice_roll = 11
        # Añadimos pueblos al J0
        self.game_manager.board.nodes[20]['player'] = 0  # Un pueblo adyacente
        self.game_manager.board.nodes[13]['player'] = 0  # Un pueblo no adyacente
        self.game_manager.board.nodes[33]['player'] = 0
        self.game_manager.board.build_city(0, 33)  # Una ciudad adyacente

        # Añadimos pueblos al J2
        self.game_manager.board.nodes[10]['player'] = 2  # Un pueblo adyacente
        self.game_manager.board.nodes[39]['player'] = 2  # Un pueblo no adyacente
        self.game_manager.board.nodes[0]['player'] = 2
        self.game_manager.board.build_city(2, 0)  # Una ciudad adyacente

        self.game_manager.give_resources()

        # Comprobamos los del J0
        assert self.game_manager.bot_manager.players[0]['player'].hand.resources.get_cereal() == 3
        assert self.game_manager.bot_manager.players[0]['resources'].resources.get_cereal() == 3

        assert self.game_manager.bot_manager.players[0]['player'].hand.resources.get_mineral() == 0
        assert self.game_manager.bot_manager.players[0]['resources'].resources.get_mineral() == 0

        assert self.game_manager.bot_manager.players[0]['player'].hand.resources.get_clay() == 0
        assert self.game_manager.bot_manager.players[0]['resources'].resources.get_clay() == 0

        assert self.game_manager.bot_manager.players[0]['player'].hand.resources.get_wood() == 0
        assert self.game_manager.bot_manager.players[0]['resources'].resources.get_wood() == 0

        assert self.game_manager.bot_manager.players[0]['player'].hand.resources.get_wool() == 0
        assert self.game_manager.bot_manager.players[0]['resources'].resources.get_wool() == 0

        # Comprobamos los del J2
        assert self.game_manager.bot_manager.players[2]['player'].hand.resources.get_cereal() == 0
        assert self.game_manager.bot_manager.players[2]['resources'].resources.get_cereal() == 0

        assert self.game_manager.bot_manager.players[2]['player'].hand.resources.get_mineral() == 0
        assert self.game_manager.bot_manager.players[2]['resources'].resources.get_mineral() == 0

        assert self.game_manager.bot_manager.players[2]['player'].hand.resources.get_clay() == 0
        assert self.game_manager.bot_manager.players[2]['resources'].resources.get_clay() == 0

        assert self.game_manager.bot_manager.players[2]['player'].hand.resources.get_wood() == 3
        assert self.game_manager.bot_manager.players[2]['resources'].resources.get_wood() == 3

        assert self.game_manager.bot_manager.players[2]['player'].hand.resources.get_wool() == 0
        assert self.game_manager.bot_manager.players[2]['resources'].resources.get_wool() == 0

    def test_send_trade_to_everyone(self):
        trade = TradeOffer(Materials(1, 0, 0, 0, 0), Materials(0, 0, 1, 0, 1))

        assert type(self.game_manager.send_trade_to_everyone(trade)) is list

    def test_build_town(self):
        self.game_manager.reset_game_values()

        # No tenemos materiales suficientes así que no hará nada
        assert self.game_manager.build_town(0, 0)['response'] is False

        self.game_manager.bot_manager.players[0]['resources'].add_material([MaterialConstants.CEREAL,
                                                                            MaterialConstants.CLAY,
                                                                            MaterialConstants.WOOD,
                                                                            MaterialConstants.WOOL
                                                                            ], 1)
        # No tenemos carretera así que no hará nada
        assert self.game_manager.build_town(0, 0)['response'] is False

        self.game_manager.board.nodes[0]['roads'].append({'player_id': 0, 'node_id': 1})

        assert self.game_manager.build_town(0, 0)['response'] is True
        assert self.game_manager.bot_manager.players[0]['resources'].get_total() == 0

    def test_build_city(self):
        self.game_manager.reset_game_values()

        # No tenemos materiales suficientes así que no hará nada
        assert self.game_manager.build_city(0, 0)['response'] is False

        self.game_manager.bot_manager.players[0]['resources'].add_material([MaterialConstants.CEREAL,
                                                                            MaterialConstants.MINERAL
                                                                            ], 3)
        # No tenemos poblado así que no hará nada
        assert self.game_manager.build_city(0, 0)['response'] is False

        self.game_manager.board.nodes[0]['player'] = 0

        assert self.game_manager.build_city(0, 0)['response'] is True
        assert self.game_manager.bot_manager.players[0]['resources'].get_total() == 1

    def test_build_road(self):
        self.game_manager.reset_game_values()

        # No tenemos materiales suficientes así que no hará nada
        assert self.game_manager.build_road(0, 0, 1)['response'] is False

        self.game_manager.bot_manager.players[0]['resources'].add_material([MaterialConstants.CLAY,
                                                                            MaterialConstants.WOOD
                                                                            ], 1)
        # No tenemos poblado así que no hará nada
        assert self.game_manager.build_road(0, 0, 1)['response'] is False

        self.game_manager.board.nodes[0]['player'] = 0

        assert self.game_manager.build_road(0, 0, 1)['response'] is True
        assert self.game_manager.bot_manager.players[0]['resources'].get_total() == 0

    def test_build_development_card(self):
        self.game_manager.reset_game_values()

        # No tenemos materiales suficientes así que no hará nada
        assert self.game_manager.build_development_card(0)['response'] is False

        self.game_manager.bot_manager.players[0]['resources'].add_material([MaterialConstants.CEREAL,
                                                                            MaterialConstants.MINERAL,
                                                                            MaterialConstants.WOOL
                                                                            ], 1)

        assert self.game_manager.build_development_card(0)['response'] is True
        assert self.game_manager.bot_manager.players[0]['resources'].get_total() == 0

        self.game_manager.development_cards_deck.current_index = 25
        # No quedan más cartas que robar
        assert self.game_manager.build_development_card(0)['response'] is False


if __name__ == '__main__':
    test = TestGameManager()
    # test.test_reset_values()
    # test.test_give_resources()
    # test.test_send_trade_to_everyone()
    # test.test_build_town()
    # test.test_build_city()
    # test.test_build_road()
    test.test_build_development_card()
    