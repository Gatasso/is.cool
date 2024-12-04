"""Cria Tabela de Aluno

Revision ID: 01ab21951e98
Revises: 46df5735e2a3
Create Date: 2024-12-03 19:30:39.342138

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '01ab21951e98'
down_revision = '46df5735e2a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('aluno',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('semester', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('professor', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=mysql.VARCHAR(length=255),
               type_=sa.String(length=100),
               existing_nullable=False)
        batch_op.drop_index('ix_professor_name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('professor', schema=None) as batch_op:
        batch_op.create_index('ix_professor_name', ['name'], unique=False)
        batch_op.alter_column('name',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(length=255),
               existing_nullable=False)

    op.drop_table('aluno')
    # ### end Alembic commands ###