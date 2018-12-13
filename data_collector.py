from board import GameBoardData
from input_parser import InputParser
import farmer_agents
import landlord_agents
from constants import *
import random


class DataCollector(object):

    @staticmethod
    def start_game(farmer_agent, landlord_agent, farmer_policy, landlord_policy, f, landlord_depth=None, farmer_depth=None):
        print('***GAME START***')
        board_state = GameBoardData()
        LandlordAgents = getattr(landlord_agents, landlord_agent)
        FarmerAgents = getattr(farmer_agents, farmer_agent)
        if landlord_agent == MCT_AGENT:
            landlord = LandlordAgents(LANDLORD, landlord_policy)
        else:
            landlord = LandlordAgents(LANDLORD, landlord_policy, depth=landlord_depth)
        if farmer_agent == MCT_AGENT:
            farmer_one = FarmerAgents(FARMER_ONE, farmer_policy)
            farmer_two = FarmerAgents(FARMER_TWO, farmer_policy)
        else:
            farmer_one = FarmerAgents(FARMER_ONE, farmer_policy, depth=farmer_depth)
            farmer_two = FarmerAgents(FARMER_TWO, farmer_policy, depth=farmer_depth)
        while not board_state.is_terminal:
            turn = board_state.turn
            action = None
            if turn == FARMER_ONE:
                action = farmer_one.get_action(board_state)
                print('farmer1 plays {0}'.format(action))
            if turn == FARMER_TWO:
                action = farmer_two.get_action(board_state)
                print('farmer2 plays {0}'.format(action))
            if turn == LANDLORD:
                action = landlord.get_action(board_state)
                print('landlord plays {0}'.format(action))
            board_state = board_state.next_state(action)
        print('*** GAME OVER, {0} WIN ***'.format(board_state.winner))
        winner = 'landlord'
        if board_state.winner in [FARMER_ONE, FARMER_TWO]:
            winner = 'farmer'
        f.write('[landlord]{0}-{1}-{2}::[farmer]{3}-{4}-{5}::[winner]{6}||\n'.format(landlord_agent,
                                                                                landlord_policy,
                                                                                landlord_depth,
                                                                                farmer_agent,
                                                                                farmer_policy,
                                                                                farmer_depth,
                                                                                winner))


if __name__ == '__main__':
    f = open('minimax_depth.txt', 'a')
    # for i in range(0, 100):
    #     DataCollector.start_game(ALPHA_BETA_AGENT, ALPHA_BETA_AGENT, EVALUATION, EVALUATION, f, landlord_depth=2,
    #                              farmer_depth=2)
    # for i in range(0, 100):
    #     DataCollector.start_game(ALPHA_BETA_AGENT, ALPHA_BETA_AGENT, EVALUATION, EVALUATION, f, landlord_depth=3,
    #                              farmer_depth=3)
    for i in range(0, 10):
        DataCollector.start_game(ALPHA_BETA_AGENT, ALPHA_BETA_AGENT, EVALUATION, EVALUATION, f, landlord_depth=2,
                                 farmer_depth=3)
    for i in range(0, 10):
        DataCollector.start_game(ALPHA_BETA_AGENT, ALPHA_BETA_AGENT, EVALUATION, EVALUATION, f, landlord_depth=3,
                                 farmer_depth=2)
    f.close()
    print ('minimax depth done')
    f1 = open('minimax_evaluation.txt', 'a')
    for i in range(0, 100):
        DataCollector.start_game(ALPHA_BETA_AGENT, ALPHA_BETA_AGENT, EVALUATION, LONGEST_COMBO, f1, landlord_depth=3,
                                farmer_depth=3)
    for i in range(0, 100):
        DataCollector.start_game(ALPHA_BETA_AGENT, ALPHA_BETA_AGENT, LONGEST_COMBO, EVALUATION, f1, landlord_depth=3,
                                farmer_depth=3)
    for i in range(0, 100):
        DataCollector.start_game(ALPHA_BETA_AGENT, ALPHA_BETA_AGENT, EVALUATION, CARD_VALUE, f1, landlord_depth=3,
                                farmer_depth=3)
    for i in range(0, 100):
        DataCollector.start_game(ALPHA_BETA_AGENT, ALPHA_BETA_AGENT, CARD_VALUE, EVALUATION, f1, landlord_depth=3,
                                farmer_depth=3)
    for i in range(0, 100):
        DataCollector.start_game(ALPHA_BETA_AGENT, ALPHA_BETA_AGENT, LONGEST_COMBO, CARD_VALUE, f1, landlord_depth=3,
                                farmer_depth=3)
    for i in range(0, 100):
        DataCollector.start_game(ALPHA_BETA_AGENT, ALPHA_BETA_AGENT, CARD_VALUE, LONGEST_COMBO, f1, landlord_depth=3,
                                farmer_depth=3)
    f1.close()
    print ('minimax evaluation done')

    f2 = open('minimax_mcts.txt', 'a')
    for i in range(0, 100):
        DataCollector.start_game(MCT_AGENT, ALPHA_BETA_AGENT, RANDOM, EVALUATION, f2, landlord_depth=3)
    for i in range(0, 100):
        DataCollector.start_game(ALPHA_BETA_AGENT, MCT_AGENT, EVALUATION, RANDOM, f2, farmer_depth=3)
    for i in range(0, 100):
        DataCollector.start_game(MCT_AGENT, ALPHA_BETA_AGENT, RANDOM, LONGEST_COMBO, f2, landlord_depth=3)
    for i in range(0, 100):
        DataCollector.start_game(ALPHA_BETA_AGENT, MCT_AGENT, LONGEST_COMBO, RANDOM, f2, farmer_depth=3)
    for i in range(0, 100):
        DataCollector.start_game(MCT_AGENT, ALPHA_BETA_AGENT, RANDOM, CARD_VALUE, f2, landlord_depth=3)
    for i in range(0, 100):
        DataCollector.start_game(ALPHA_BETA_AGENT, MCT_AGENT, CARD_VALUE, RANDOM, f2, farmer_depth=3)
    f2.close()
