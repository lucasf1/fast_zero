"""create columns created_at and updated_at for table todos

Revision ID: b05cf7ec05a2
Revises: 64e1e5e682ea
Create Date: 2025-06-19 15:38:13.646662

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b05cf7ec05a2'
down_revision: Union[str, None] = '64e1e5e682ea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table('users', schema=None) as batch_op:  

        batch_op.add_column(   
            sa.Column(
                'updated_at',
                sa.DateTime(),
                server_default=sa.text('(CURRENT_TIMESTAMP)'),
                nullable=False,
            )
        )


def downgrade() -> None:
    with op.batch_alter_table('users', schema=None) as batch_op:  
        batch_op.drop_column('updated_at') 
