"""update model_peopleindb_grades_totaketuplelist

Revision ID: b09c7c821fff
Revises: 
Create Date: 2024-08-11 06:10:22.353047

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'b09c7c821fff'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('people', sa.Column('name', sa.String(), nullable=False))
    op.alter_column('people', 'role',
               existing_type=postgresql.ENUM('administrator', 'aide', 'guardian', 'parent', 'proctor', 'relative', 'student', 'teacher', name='role'),
               type_=sa.Enum('administrator', 'aide', 'guardian', 'parent', 'proctor', 'relative', 'student', 'teacher', name='roleenum'),
               existing_nullable=False)
    op.alter_column('people', 'AnonymizedStudentID',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=False)
    op.drop_index('ix_people_AnonymizedStudentID', table_name='people')
    op.drop_index('ix_people_Firstname', table_name='people')
    op.drop_index('ix_people_Lastname', table_name='people')
    op.create_index(op.f('ix_people_name'), 'people', ['name'], unique=False)
    op.drop_constraint('people_AnonymizedStudentID_fkey', 'people', type_='foreignkey')
    op.drop_column('people', 'Lastname')
    op.drop_column('people', 'Firstname')
    op.alter_column('students', 'anonymizedStudentID',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=False)
    op.alter_column('students', 'role',
               existing_type=postgresql.ENUM('administrator', 'aide', 'guardian', 'parent', 'proctor', 'relative', 'student', 'teacher', name='role'),
               type_=sa.Enum('administrator', 'aide', 'guardian', 'parent', 'proctor', 'relative', 'student', 'teacher', name='roleenum'),
               existing_nullable=False)
    op.drop_constraint('students_anonymizedStudentID_key', 'students', type_='unique')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('students_anonymizedStudentID_key', 'students', ['anonymizedStudentID'])
    op.alter_column('students', 'role',
               existing_type=sa.Enum('administrator', 'aide', 'guardian', 'parent', 'proctor', 'relative', 'student', 'teacher', name='roleenum'),
               type_=postgresql.ENUM('administrator', 'aide', 'guardian', 'parent', 'proctor', 'relative', 'student', 'teacher', name='role'),
               existing_nullable=False)
    op.alter_column('students', 'anonymizedStudentID',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    op.add_column('people', sa.Column('Firstname', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('people', sa.Column('Lastname', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.create_foreign_key('people_AnonymizedStudentID_fkey', 'people', 'students', ['AnonymizedStudentID'], ['anonymizedStudentID'])
    op.drop_index(op.f('ix_people_name'), table_name='people')
    op.create_index('ix_people_Lastname', 'people', ['Lastname'], unique=False)
    op.create_index('ix_people_Firstname', 'people', ['Firstname'], unique=False)
    op.create_index('ix_people_AnonymizedStudentID', 'people', ['AnonymizedStudentID'], unique=False)
    op.alter_column('people', 'AnonymizedStudentID',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    op.alter_column('people', 'role',
               existing_type=sa.Enum('administrator', 'aide', 'guardian', 'parent', 'proctor', 'relative', 'student', 'teacher', name='roleenum'),
               type_=postgresql.ENUM('administrator', 'aide', 'guardian', 'parent', 'proctor', 'relative', 'student', 'teacher', name='role'),
               existing_nullable=False)
    op.drop_column('people', 'name')
    # ### end Alembic commands ###
