import pytz

from datetime import datetime

from .. import db

eat_timezone = pytz.timezone('Africa/Nairobi')


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    done = db.Column(db.Boolean, default=False)
    modified_at = db.Column(db.DateTime, default=datetime.now(eat_timezone), onupdate=datetime.now(eat_timezone))
    created_at = db.Column(db.DateTime, default=datetime.now(eat_timezone))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<Todo %r>' % self.name

    def __str__(self):
        return '{0}'.format(self.name)
