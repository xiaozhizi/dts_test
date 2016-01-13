"""updata bug model

Revision ID: 290128547a0
Revises: 214542d35112
Create Date: 2016-01-05 15:46:08.931000

"""

# revision identifiers, used by Alembic.
revision = '290128547a0'
down_revision = '214542d35112'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bugs', sa.Column('bug_last_update', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('bugs', 'bug_last_update')
    ### end Alembic commands ###