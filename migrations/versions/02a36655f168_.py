"""empty message

Revision ID: 02a36655f168
Revises: 100952249cee
Create Date: 2021-08-21 18:07:16.329201

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02a36655f168'
down_revision = '100952249cee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
