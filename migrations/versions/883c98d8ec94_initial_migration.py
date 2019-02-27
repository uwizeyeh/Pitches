"""Initial Migration

Revision ID: 883c98d8ec94
Revises: 
Create Date: 2019-02-26 18:52:50.857377

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '883c98d8ec94'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('pitche_id', sa.Integer(), nullable=True))
    op.add_column('comments', sa.Column('users_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comments', 'pitche', ['pitche_id'], ['id'])
    op.create_foreign_key(None, 'comments', 'users', ['users_id'], ['id'])
    op.add_column('pitche', sa.Column('users_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'pitche', 'users', ['users_id'], ['id'])
    op.drop_constraint('users_comment_id_fkey', 'users', type_='foreignkey')
    op.drop_column('users', 'comment_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('comment_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('users_comment_id_fkey', 'users', 'comments', ['comment_id'], ['id'])
    op.drop_constraint(None, 'pitche', type_='foreignkey')
    op.drop_column('pitche', 'users_id')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'users_id')
    op.drop_column('comments', 'pitche_id')
    # ### end Alembic commands ###
