"""init revision

Revision ID: 3cfce646762
Revises: 
Create Date: 2015-05-28 01:27:05.407436

"""

# revision identifiers, used by Alembic.
revision = '3cfce646762'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
import geoalchemy2


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('organization',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('address', geoalchemy2.types.Geography(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('organization', sa.Integer(), nullable=True),
    sa.Column('fb_first_name', sa.String(length=120), nullable=True),
    sa.Column('fb_last_name', sa.String(length=120), nullable=True),
    sa.Column('fb_id', sa.String(length=40), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('about_me', sa.String(length=120), nullable=True),
    sa.Column('is_superuser', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['organization'], ['organization.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('fb_id')
    )
    op.create_table('issue',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('reporter', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=120), nullable=True),
    sa.Column('coordinates', geoalchemy2.types.Geography(), nullable=True),
    sa.ForeignKeyConstraint(['reporter'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('issue_id', sa.Integer(), nullable=True),
    sa.Column('message', sa.String(length=400), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['issue_id'], ['issue.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment')
    op.drop_table('issue')
    op.drop_table('user')
    op.drop_table('organization')
    ### end Alembic commands ###
