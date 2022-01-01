"""new table

Revision ID: 0e0a997e261c
Revises: 
Create Date: 2021-03-12 21:03:17.136630

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0e0a997e261c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('video_tracking')
    op.drop_table('posts')
    op.drop_table('movies')
    op.drop_table('pages')
    op.alter_column('video', 'CreatedAt',
               existing_type=mysql.DATETIME(),
               nullable=True)
    op.alter_column('video', 'Description',
               existing_type=mysql.TEXT(),
               nullable=True)
    op.alter_column('video', 'KeyWords',
               existing_type=mysql.TEXT(),
               nullable=True)
    op.alter_column('video', 'OrderCol',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True,
               existing_server_default=sa.text('0'))
    op.alter_column('video', 'OverAllCol',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True,
               existing_server_default=sa.text('0'))
    op.alter_column('video', 'VideoImage',
               existing_type=mysql.VARCHAR(length=500),
               nullable=True,
               existing_server_default=sa.text("''"))
    op.alter_column('video', 'VideoLink',
               existing_type=mysql.VARCHAR(length=500),
               nullable=True,
               existing_server_default=sa.text("''"))
    op.alter_column('video', 'VideoLink2',
               existing_type=mysql.VARCHAR(length=500),
               nullable=True,
               existing_server_default=sa.text("''"))
    op.alter_column('video', 'VideoPage',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('video', 'VideoTitle',
               existing_type=mysql.VARCHAR(length=500),
               nullable=True,
               existing_server_default=sa.text("''"))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('video', 'VideoTitle',
               existing_type=mysql.VARCHAR(length=500),
               nullable=False,
               existing_server_default=sa.text("''"))
    op.alter_column('video', 'VideoPage',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('video', 'VideoLink2',
               existing_type=mysql.VARCHAR(length=500),
               nullable=False,
               existing_server_default=sa.text("''"))
    op.alter_column('video', 'VideoLink',
               existing_type=mysql.VARCHAR(length=500),
               nullable=False,
               existing_server_default=sa.text("''"))
    op.alter_column('video', 'VideoImage',
               existing_type=mysql.VARCHAR(length=500),
               nullable=False,
               existing_server_default=sa.text("''"))
    op.alter_column('video', 'OverAllCol',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False,
               existing_server_default=sa.text('0'))
    op.alter_column('video', 'OrderCol',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False,
               existing_server_default=sa.text('0'))
    op.alter_column('video', 'KeyWords',
               existing_type=mysql.TEXT(),
               nullable=False)
    op.alter_column('video', 'Description',
               existing_type=mysql.TEXT(),
               nullable=False)
    op.alter_column('video', 'CreatedAt',
               existing_type=mysql.DATETIME(),
               nullable=False)
    op.create_table('pages',
    sa.Column('Id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('OrderCol', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('PageName', mysql.VARCHAR(length=500), server_default=sa.text("''"), nullable=False),
    sa.Column('PageImage', mysql.VARCHAR(length=500), server_default=sa.text("''"), nullable=False),
    sa.Column('CreatedAt', mysql.DATETIME(), nullable=False),
    sa.PrimaryKeyConstraint('Id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('movies',
    sa.Column('Id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('OrderCol', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('OverAllCol', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('MovieTitle', mysql.VARCHAR(length=500), server_default=sa.text("''"), nullable=False),
    sa.Column('MovieLink', mysql.VARCHAR(length=500), server_default=sa.text("''"), nullable=False),
    sa.Column('MovieImage', mysql.VARCHAR(length=500), server_default=sa.text("''"), nullable=False),
    sa.Column('DirectLink', mysql.TEXT(), nullable=False),
    sa.Column('TorrentLink', mysql.TEXT(), nullable=False),
    sa.Column('Description', mysql.TEXT(), nullable=False),
    sa.Column('MovieDescription', mysql.TEXT(), nullable=False),
    sa.Column('KeyWords', mysql.TEXT(), nullable=False),
    sa.Column('CreatedAt', mysql.DATETIME(), nullable=False),
    sa.PrimaryKeyConstraint('Id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('posts',
    sa.Column('Id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('OrderCol', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('OverAllCol', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('Title', mysql.VARCHAR(length=500), server_default=sa.text("''"), nullable=False),
    sa.Column('Image', mysql.VARCHAR(length=500), server_default=sa.text("''"), nullable=False),
    sa.Column('PostData', mysql.TEXT(), nullable=False),
    sa.Column('Description', mysql.TEXT(), nullable=False),
    sa.Column('KeyWords', mysql.TEXT(), nullable=False),
    sa.Column('CreatedAt', mysql.DATETIME(), nullable=False),
    sa.PrimaryKeyConstraint('Id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('video_tracking',
    sa.Column('Id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('VideoId', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('Ip', mysql.VARCHAR(length=25), server_default=sa.text("''"), nullable=False),
    sa.Column('CreatedAt', mysql.DATETIME(), nullable=False),
    sa.PrimaryKeyConstraint('Id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
