class Band():
    members = []

    def __init__(self, name):
        self.name = name

    @staticmethod
    def do_you_wanna_rock():
        print("Are you ready for some kick-ass solos?")
        return "Are you ready for some kick-ass solos?"

    def __repr__(self):
        return self.name

    @classmethod
    def play_solos(cls):
        for member in cls.members:
            print(f'{member} has an amazing {member.instrument} solo')

    @classmethod
    def create_from_data(cls, data):
        for musician in data:
          if musician['instrument'] == 'Guitar':
              cls.members.append(
                  Guitarist(musician['name'], musician['instrument']))

          elif musician['instrument'] == 'Bass':
              cls.members.append(Bassist(musician['name'], musician['instrument']))

          elif musician['instrument'] == 'Drums':
              cls.members.append(Drummer(musician['name'], musician['instrument']))

          elif musician['instrument'] == 'Vocals':
              cls.members.append(Singer(musician['name'], musician['instrument']))

    @classmethod
    def to_list(cls):
        return cls.members


class Musician(Band):
    musician_list = []

    def __init__(self, name):
        super().__init__(self)
        self.name = name
        self.__class__.musician_list.append(self)

    @classmethod
    def get_members(cls):
        return cls.musician_list


class Guitarist(Musician):
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument
        super().__init__(name)

    def play_solo(self):
        return 'plunk plunk twaaaaang'

    def get_instrument(self):
        return 'guitar'


class Bassist(Musician):
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument
        super().__init__(name)

    def play_solo(self):
        return 'bweee neeeeneer bwaaah'

    def get_instrument(self):
        return 'Bass'


class Drummer(Musician):
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument
        super().__init__(name)

    def play_solo(self):
        return 'pah rump pah pah pum'

    def get_instrument(self):
        return 'Drums'

class Singer(Musician):
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument
        super().__init__(name)

    def play_solo(self):
        return 'Ooooooh Lalalalalaaaaaahhh'

    def get_instrument(self):
        return 'Vocals'


data = [
    {'name': 'Dave',
     'instrument': 'Vocals'
     },
    {'name': 'Nate',
        'instrument': 'Bass'
     },
    {'name': 'Taylor',
        'instrument': 'Drums'
     },
    {'name': 'Chris',
     'instrument': 'Guitar'
     }
]


Band.do_you_wanna_rock()
Band.create_from_data(data)
Band.to_list()
Musician.play_solos()

