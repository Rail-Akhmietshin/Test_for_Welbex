"""DB creation

Revision ID: 7a8e25ca3d97
Revises: 
Create Date: 2023-06-04 10:46:50.722220

"""
from alembic import op
import sqlalchemy as sa



# revision identifiers, used by Alembic.
revision = '7a8e25ca3d97'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('app_transportation_location',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('city', sa.String(), nullable=False),
    sa.Column('state', sa.String(), nullable=False),
    sa.Column('zip_code', sa.Integer(), nullable=False),
    sa.Column('lat', sa.Float(), nullable=False),
    sa.Column('lon', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('zip_code')
    )
    op.create_table('app_transportation_car',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('unique_id', sa.String(), nullable=False),
    sa.Column('current_location', sa.Integer(), nullable=False),
    sa.Column('load_capacity', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['current_location'], ['app_transportation_location.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('unique_id')
    )
    op.create_table('app_transportation_cargo',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('pick_up', sa.Integer(), nullable=False),
    sa.Column('delivery', sa.Integer(), nullable=False),
    sa.Column('weight', sa.Float(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['delivery'], ['app_transportation_location.id'], ),
    sa.ForeignKeyConstraint(['pick_up'], ['app_transportation_location.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('app_transportation_cargo')
    op.drop_table('app_transportation_car')
    op.drop_table('app_transportation_location')
    # ### end Alembic commands ###
