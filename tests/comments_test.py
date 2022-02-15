import unittest
from app.models import User, Pitches, Comments


class CommentsTest(unittest.TestCase):
    def setUp(self):
        self.user_name = User(
            username='janey', password='12345', email='jwnjoroge4@gmail.com')
        self.new_pitch = Pitches(
            title='Pickup', content='Shady PLace', user_id=self.user_name.id)
        self.new_comment = Comments(
            comment='Be careful', pitch_id=self.new_pitch.id, user_id=self.user_name.id)

    def test_save_pitch(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comments.query.all()) > 0)

    def test_get_comment(self):
        self.new_comment.save_comment()
        comment = Comments.get_comment(self.new_pitch.id)
        self.assertTrue(len(comment) == 1)
