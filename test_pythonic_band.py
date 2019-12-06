import pytest

from pythonic_band import Band, Musician, Guitarist, Bassist, Drummer, Singer


def do_you_wanna_rock():
    assert "Are you ready for some kick-ass solos?" == Band.do_you_wanna_rock()


def test_Dave_is_instance_of_correct_class(Dave):
    assert isinstance(Dave, Singer)


def test_Dave_is_instance_of_parent_class(Dave):
    assert isinstance(Dave, Musician)


def test_jimmy_name(Dave):
    assert Dave.name == 'Dave'


def test_Dave_instrument(Dave):
    assert Dave.instrument == 'Vocals'


def test_to_list():
    Dave = Singer('Dave', 'Vocals')
    Chris = Guitarist('Chris', 'guitar')
    Nate = Bassist('Nate', 'bass')
    Taylor = Drummer('Taylor', 'drums')
    expected = [Dave, Chris, Nate, Taylor]
    actual = Band.to_list()
    assert actual == expected

def test_create_band_from_data(Dave):
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

    Band.create_from_data(data)

    assert Band.members[0] == Dave


@pytest.fixture()
def Dave():
    return Singer('Dave', 'vocals')



@pytest.fixture(autouse=True)
def clean():
    Band.members = []
