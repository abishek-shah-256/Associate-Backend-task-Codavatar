"""CallLog-Added destination_phone_number

Revision ID: 64f1b2db81ea
Revises: 870ef05370f3
Create Date: 2024-12-07 21:53:14.572650

"""
from collections.abc import Sequence

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "64f1b2db81ea"
down_revision: str | None = "870ef05370f3"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "call_logs", sa.Column("destination_phone_number", sa.String(), nullable=False)
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("call_logs", "destination_phone_number")
    # ### end Alembic commands ###
