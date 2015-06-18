# Initialize database.
from sqlalchemy import update
from cit import create_app
from cit.db import db
from mixer.backend.sqlalchemy import Mixer
from mixer.backend.flask import mixer
from cit.auth.models import User
from cit.organizations.models import Organization
from cit.issues.models import Issue, Photo
from cit.comments.models import Comment
from random import randint
import sys
import argparse

app = create_app()

class MyOwnMixer(Mixer):
    def populate_target(self, values):
        target = self.__scheme(**values)
        return target


mixer = MyOwnMixer()


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--make-admin', action='store', default='')
    args = parser.parse_args()

    return parser


def generate_test_data():
    with app.app_context():
        organization = mixer.blend(Organization,
                                   name=mixer.RANDOM,
                                   address='POINT(49.831900 23.997740)')
        db.session.add(organization)
        db.session.commit()
        user = mixer.blend(User,
                           fb_first_name=mixer.RANDOM,
                           fb_last_name=mixer.RANDOM,
                           fb_id=mixer.RANDOM,
                           email=mixer.RANDOM,
                           about_me=mixer.RANDOM)
        db.session.add(user)
        db.session.commit()
        issue = mixer.blend(Issue,
                            reporter='1',
                            description=mixer.RANDOM,
                            coordinates='POINT(49.832868 24.001136)'
                            )
        db.session.add(issue)
        comment = mixer.blend(Comment,
                              author=user,
                              issue=issue,
                              message=mixer.RANDOM)
        db.session.add(comment)
        photo = mixer.blend(Photo,
                            issue=issue,
                            file_path='1.jpg')
        db.session.add(photo)
        db.session.commit()


def make_user_as_admin(user_id):
    with app.app_context():
        db.session.query(User).filter(User.fb_id == user_id).update({"is_superuser": True})
        db.session.commit()


if __name__ == "__main__":
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    if namespace.make_admin:
        make_user_as_admin(namespace.make_admin)
    else:
        generate_test_data()
        
