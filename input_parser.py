import argparse


class InputParser:
    def __init__(self):
        self._parser = argparse.ArgumentParser(description='Input parser')
        self._input_args = None

    @property
    def landlord_agent(self):
        return self._input_args.landlord

    @property
    def farmer_agent(self):
        return self._input_args.farmer

    @property
    def player_agent(self):
        return self._input_args.player

    @property
    def is_manual_mode(self):
        return self._input_args.manual

    @property
    def evaluation(self):
        return self._input_args.evaluation

    @property
    def is_debug_mode(self):
        return self._input_args.debug

    def _set_landlord_agent(self):
        self._parser.add_argument('-l', '--landlord',
                                  help='Agent used for landlord',
                                  required=False,
                                  default='ReflexAgent')

    def _set_farmer_agent(self):
        self._parser.add_argument('-f', '--farmer',
                                  help='Agent used for farmer',
                                  required=False,
                                  default='ReflexAgent')

    def _set_player_agent(self):
        self._parser.add_argument('-p', '--player',
                                  help='Agent used for player(yourself)',
                                  required=False,
                                  default='ReflexAgent')

    def _set_evaluation(self):
        self._parser.add_argument('-e', '--evaluation',
                                  help='Evaluation or rollout policy used for agent',
                                  required=False,
                                  default='random')

    def _set_manual(self):
        self._parser.add_argument('-m', '--manual',
                                  help='For manual play',
                                  action='store_true')

    def _set_debug_mod(self):
        self._parser.add_argument('-d', '--debug',
                                  help='Debug mode',
                                  type=bool,
                                  required=False,
                                  default=False)

    def parse_input(self):
        self._set_farmer_agent()
        self._set_landlord_agent()
        self._set_player_agent()
        self._set_evaluation()
        self._set_manual()
        self._set_debug_mod()
        self._input_args = self._parser.parse_args()