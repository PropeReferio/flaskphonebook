"""empty message

Revision ID: 14a2cbc4e1ff
Revises: 
Create Date: 2020-01-08 17:33:30.031059

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14a2cbc4e1ff'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('entry',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('avenger', sa.String(length=30), nullable=False),
    sa.Column('address', sa.String(length=150), nullable=False),
    sa.Column('phone', sa.String(length=12), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('address')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('entry')
    # ### end Alembic commands ###