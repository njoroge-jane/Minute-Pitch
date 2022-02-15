import unittest
from app.models import Pitches, User


class PitchesTest(unittest.TestCase):
    def setUp(self):
        self.user_name = User(
            username='janey', password='12345', email='jwnjoroge4@gmail.com')
        self.new_pitch = Pitches(
            title='Pickup', content='Shady PLace', user_id=self.user_name.id)

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitches.query.all()) > 0)

    def test_get_pitch(self):
        self.new_pitch.save_pitch()
        pitch = Pitches.get_pitch(self.user_name.id)
        self.assertTrue(len(pitch) == 1)
