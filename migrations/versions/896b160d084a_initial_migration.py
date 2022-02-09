"""Initial Migration

Revision ID: 896b160d084a
Revises: 
Create Date: 2022-02-09 08:49:08.044215

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '896b160d084a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
