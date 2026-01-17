from enum import Enum


class SoccerPlayer:
    # The position a player can play on the pitch.
    position = Enum("position", ["GK",  # Goalkeeper
                                 "DF",  # Defender
                                 "MF",  # Midfield
                                 "FW"  # Forward
                                 ])

    def __init__(self, first_name, last_name, age, position):
        """
        SoccerPlayer constructor.

        :param first_name: the first name of the player
        :param last_name: the last name of the player
        :param age: the player's age
        :param position: the position on the pitch
        """
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.position = position

    def __lt__(self, other):
        """
        Compare two SoccerPlayer objects based on their names.

        :param other: the other SoccerPlayer object to compare
        :return: True if their names are equal, False otherwise
        """
        return self.get_name().casefold() == other.get_name().casefold()

    def __eq__(self, other):
        """
        Check if two SoccerPlayer objects are equal.

        :param other: the other object to compare
        :return: True if self is equal to other, False otherwise
        """
        if self is other:
            return True
        if not isinstance(other, SoccerPlayer):
            return False
        return (
                self.age == other.age and
                self.first_name == other.first_name and
                self.last_name == other.last_name and
                self.position == other.position
        )

    def get_age(self):
        """
        Get the age of the player.

        :return: the age
        """
        return self.age

    def get_name(self):
        """
        Get the full name of the player.

        :return: the full name
        """
        return f'{self.first_name} {self.last_name}'

    def get_position(self):
        """
        Get the position of the player.

        :return: the position
        """
        return self.position

    def __hash__(self):
        """
        Compute the hash value of the SoccerPlayer object.

        :return: the hash value
        """
        return hash((self.age, self.first_name, self.last_name, self.position))

    def __str__(self):
        return self.get_name()


class SoccerTeam:
    def __init__(self, name: str):
        self.name = name
        self.size = 0
        self.pl = []

    def add_player(self, player: SoccerPlayer):
        if (player not in self.pl) and len(self.pl) < 11:
            self.pl.append(player)
            return True
        return False

    def get_average_age(self):
        if len(self.pl) == 0:
            return 0.0
        ml = []
        for e in self.pl:
            ml.append(e.get_age())
        return float(sum(ml) / len(ml))

    def get_formation(self):
        posl = self.get_posl()
        return f'{posl.count('position.DF')}-{posl.count('position.MF')}-{posl.count('position.FW')}'

    def get_name(self):
        return self.name

    def get_players(self):
        return self.pl + (11 - len(self.pl)) * [None]

    def get_posl(self):
        posl = []
        for e in self.pl:
            posl.append(str(e.position))
        return posl

    def get_players_at(self, position: SoccerPlayer.position):
        rl = []
        for pl in self.pl:
            if pl.position == position:
                rl.append(pl)
        return rl

    def substitute(self, player_out: SoccerPlayer, player_in: SoccerPlayer):
        if (player_out in self.pl) and (player_in not in self.pl):
            if (str(player_out.position) == 'position.GK' and str(player_in.position) == 'position.GK') or (
                    str(player_out.position) != 'position.GK' and str(player_in.position) != 'position.GK'):
                self.pl.remove(player_out)
                self.pl.append(player_in)
                return True
        return False