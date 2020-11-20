import datetime

from ..base import db


class Match(db.Model):
    id = db.Column(db.Integer(), primary_key=True)

    _red_user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)
    # red_user = db.relationship('User')

    _blue_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # blue_user = db.relationship('User')

    _start_time = db.Column(db.DateTime(), nullable=False)
    _end_time = db.Column(db.Integer, nullable=True)

    _max_time = db.Column(db.DateTime(), nullable=False)
    _ranked = db.Column(db.Boolean(), nullable=False)

    def __init__(self, red_user_id, blue_user_id, ranked, max_time, **kwargs):
        super(Match, self).__init__(**kwargs)
        self._red_user_id = red_user_id
        self._blue_user_id = blue_user_id
        self._ranked = ranked
        self._max_time = max_time

    @property
    def start_time(self):
        return self._start_time

    @property
    def end_time(self):
        return self._end_time

    @property
    def red_user_id(self):
        return self._red_user_id

    @property
    def blue_user_id(self):
        return self._blue_user_id

    def begin(self):
        self._start_time = datetime.datetime.now()

    def end(self):
        self._end_time = datetime.datetime.now()
