"""User-Remove mobile from User table

Revision ID: ff3690ac781a
Revises: 64f1b2db81ea
Create Date: 2024-12-08 03:21:36.310725

"""
from collections.abc import Sequence

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "ff3690ac781a"
down_revision: str | None = "64f1b2db81ea"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("users_mobile_key", "users", type_="unique")
    op.drop_column("users", "mobile")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users", sa.Column("mobile", sa.VARCHAR(), autoincrement=False, nullable=True)
    )
    op.create_unique_constraint("users_mobile_key", "users", ["mobile"])
    # ### end Alembic commands ###
