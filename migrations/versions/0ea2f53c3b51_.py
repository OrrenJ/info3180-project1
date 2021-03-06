"""empty message

Revision ID: 0ea2f53c3b51
Revises: ef900b3de057
Create Date: 2017-03-12 16:06:09.253748

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ea2f53c3b51'
down_revision = 'ef900b3de057'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_profile',
    sa.Column('userid', sa.String(length=13), nullable=False),
    sa.Column('firstname', sa.String(length=80), nullable=True),
    sa.Column('lastname', sa.String(length=80), nullable=True),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('gender', sa.String(length=1), nullable=True),
    sa.Column('biography', sa.String(length=127), nullable=True),
    sa.Column('created_on', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('userid'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_profile')
    # ### end Alembic commands ###
