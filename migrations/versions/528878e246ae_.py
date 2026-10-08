"""empty message

Revision ID: 528878e246ae
Revises: 637cd96f8a79
Create Date: 2026-05-13 19:54:14.024733

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '528878e246ae'
down_revision: Union[str, Sequence[str], None] = '637cd96f8a79'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
