"""Initial database creation

Revision ID: c1eb1486bd41
Revises: 
Create Date: 2025-01-26 10:21:48.234615

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c1eb1486bd41'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('agent_logs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('agent_name', sa.String(length=100), nullable=False),
    sa.Column('ticker', sa.String(length=10), nullable=True),
    sa.Column('run_status', sa.String(length=50), nullable=False),
    sa.Column('message', sa.Text(), nullable=True),
    sa.Column('run_time', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stock_metadata',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ticker', sa.String(length=10), nullable=False),
    sa.Column('company_name', sa.String(length=255), nullable=False),
    sa.Column('market', sa.String(length=50), nullable=True),
    sa.Column('sector', sa.String(length=100), nullable=True),
    sa.Column('industry', sa.String(length=100), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('ticker')
    )
    op.create_table('stock_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ticker', sa.String(length=10), nullable=False),
    sa.Column('timestamp', sa.TIMESTAMP(), nullable=False),
    sa.Column('open', sa.Float(), nullable=False),
    sa.Column('high', sa.Float(), nullable=False),
    sa.Column('low', sa.Float(), nullable=False),
    sa.Column('close', sa.Float(), nullable=False),
    sa.Column('volume', sa.BigInteger(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['ticker'], ['stock_metadata.ticker'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('ticker', 'timestamp', name='uix_ticker_timestamp')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stock_data')
    op.drop_table('stock_metadata')
    op.drop_table('agent_logs')
    # ### end Alembic commands ###
