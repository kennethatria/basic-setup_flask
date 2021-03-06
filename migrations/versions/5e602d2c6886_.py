"""empty message

Revision ID: 5e602d2c6886
Revises: 8955a292b8fc
Create Date: 2019-04-08 20:40:21.430781

"""

# revision identifiers, used by Alembic.
revision = '5e602d2c6886'
down_revision = '8955a292b8fc'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('incident', sa.Column('incident_location', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('incident', 'incident_location')
    # ### end Alembic commands ###
