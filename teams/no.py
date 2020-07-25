from settings import *
from const import ACT
from teams.agent import Agent
from teams.team import Team

class NoTeam(Team):
    """A team with no players (XD)"""
    def set_players(self):
        self.players = []

    def move(self, state, reward):
        """ Moves the entire team """
        return []