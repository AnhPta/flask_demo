"""empty message

Revision ID: fe531ae57a2d
Revises: 
Create Date: 2018-12-15 05:06:54.230288

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe531ae57a2d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('branch',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('phone', sa.String(length=120), nullable=True),
    sa.Column('tax_number', sa.String(length=120), nullable=True),
    sa.Column('website', sa.String(length=120), nullable=True),
    sa.Column('description', sa.String(length=155), nullable=True),
    sa.Column('bank', sa.String(length=120), nullable=True),
    sa.Column('city_id', sa.Integer(), nullable=True),
    sa.Column('district_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_branch_bank'), 'branch', ['bank'], unique=False)
    op.create_index(op.f('ix_branch_city_id'), 'branch', ['city_id'], unique=False)
    op.create_index(op.f('ix_branch_description'), 'branch', ['description'], unique=False)
    op.create_index(op.f('ix_branch_district_id'), 'branch', ['district_id'], unique=False)
    op.create_index(op.f('ix_branch_email'), 'branch', ['email'], unique=True)
    op.create_index(op.f('ix_branch_name'), 'branch', ['name'], unique=True)
    op.create_index(op.f('ix_branch_phone'), 'branch', ['phone'], unique=True)
    op.create_index(op.f('ix_branch_status'), 'branch', ['status'], unique=False)
    op.create_index(op.f('ix_branch_tax_number'), 'branch', ['tax_number'], unique=True)
    op.create_index(op.f('ix_branch_website'), 'branch', ['website'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_branch_website'), table_name='branch')
    op.drop_index(op.f('ix_branch_tax_number'), table_name='branch')
    op.drop_index(op.f('ix_branch_status'), table_name='branch')
    op.drop_index(op.f('ix_branch_phone'), table_name='branch')
    op.drop_index(op.f('ix_branch_name'), table_name='branch')
    op.drop_index(op.f('ix_branch_email'), table_name='branch')
    op.drop_index(op.f('ix_branch_district_id'), table_name='branch')
    op.drop_index(op.f('ix_branch_description'), table_name='branch')
    op.drop_index(op.f('ix_branch_city_id'), table_name='branch')
    op.drop_index(op.f('ix_branch_bank'), table_name='branch')
    op.drop_table('branch')
    # ### end Alembic commands ###
