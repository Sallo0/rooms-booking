"""hotels name location gin index

Revision ID: 46d25b2dba87
Revises: e0af3de70e95
Create Date: 2023-09-08 19:44:17.854461

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "46d25b2dba87"
down_revision: Union[str, None] = "e0af3de70e95"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_index(
        op.f("ix_hotels_location"),
        "hotels",
        [sa.text("to_tsvector('russian', name || ' ' || location)")],
        postgresql_using="gin",
    )


def downgrade() -> None:
    op.drop_index(op.f("ix_hotels_location"), table_name="hotels")
