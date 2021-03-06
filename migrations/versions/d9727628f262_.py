"""empty message

Revision ID: d9727628f262
Revises: 9cf171d2a7a9
Create Date: 2019-03-19 08:33:22.120233

"""

# revision identifiers, used by Alembic.
revision = 'd9727628f262'
down_revision = '9cf171d2a7a9'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('feedback',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(), nullable=True),
    sa.Column('rating', sa.String(), nullable=True),
    sa.Column('service_id', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('feedback')
    # ### end Alembic commands ###
