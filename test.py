import re


class Band():
    members = []

    def __init__(self, name):
        self.name = name
        self.__class__.members.append(self)

    @staticmethod
    def making_da_band():
        return "It's time to make the band"

    def __repr__(self):
        return f'{self.name}'

    @classmethod()
    def play_solos(cls):
        for member in cls.members:
            print(f'Super {member.instrument} solo from {member}')

    @staticmethod
    def create_from_data(data):
        split_data = re.findall(r"\S.*", data)
        print(split_data)

    title = split_data[0]
    members = []
    for i in range(1, len(split_data)):
        current_member = split_data[i].split(',')

        if current_member[1] == 'Guitar':
            members.append(Guitarist(current_member[0]))
        elif current_member[1] == 'Bass':
            members.append(Bassist(current_member[0]))
        elif current_member[1] == 'Drums':
            members.append(Drummer(current_member[0]))
        else:
            members.append(Musician(current_member[0]))

            return Band(title, members)

    @classmethod
    def to_list(cls):
        output = ''
        for current_band in cls.all_bands:
            output += current_band.__str__() + '\n\n'
    return output

    if __name__ == "__main__":

        band_one = """
        Foofighters
        Chris Shiflett,Guitar
        Taylor Hawkins,Drums
        Nate Mendel,Bass
        Dave Grohl, Guitar/Vocals
    """

        print(Band.create_from_data(data))


@classmethod
def to_list(cls):
    print(cls.members)
    return cls.members


class Musician(Band):
    # musician_list = []

    def __init__(self, name):
        super().__init__(self)
        self.name = name
        # self.__class__.musician_list.append(self)

    # @classmethod
    # def get_members(cls):
    #     return cls.musician_list


class Guitarist(Musician):
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument
        super().__init__(name)

    def play_solo(self):
        return '*loud guitar noises*'

    def get_instrument(self):
        return 'guitar'


class Bassist(Musician):
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument
        super().__init__(name)

    def play_solo(self):
        return 'basssssssssss'

    def get_instrument(self):
        return 'Bass'


class Drummer(Musician):
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument
        super().__init__(name)

    def play_solo(self):
        return 'badum badum ch badum ch'

    def get_instrument(self):
        return 'Drums'


# guitar_boy = Guitarist('Jimmy', 'guitar')
# bass_boy = Bassist('Michael', 'bass')
# drummer_boy = Drummer('Lisa', 'drums')


# data = [
#     {'name': 'Jimmy',
#      'instrument': 'Guitar'
#      },

#     {'name': 'Michael',
#         'instrument': 'Bass'
#      },
#     {'name': 'Lisa',
#         'instrument': 'Drums'
#      }
# ]


# Band.create_from_data(data)
Band.play_solos()
# Band.to_list()
