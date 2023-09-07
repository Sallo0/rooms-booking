"""test

Revision ID: 934f48b2b0ff
Revises: d7d115b756c9
Create Date: 2023-08-30 21:24:42.941444

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '934f48b2b0ff'
down_revision: Union[str, None] = 'd7d115b756c9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('hotels', 'rooms_quantity')
    op.drop_column('rooms', 'quantity')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rooms', sa.Column('quantity', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('hotels', sa.Column('rooms_quantity', sa.INTEGER(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
