"""empty message

Revision ID: 56b63fff9feb
Revises: 
Create Date: 2017-03-12 12:51:10.547059

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56b63fff9feb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profile', sa.Column('gender', sa.String(length=1), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profile', 'gender')
    # ### end Alembic commands ###