"""init

Revision ID: 095e818f3f18
Revises: 
Create Date: 2024-11-02 14:50:35.613242

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '095e818f3f18'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # creating a uuid-ossp extension if not extists
    op.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')

    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hashtag',
    sa.Column('id', sa.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('name', sa.String(length=140), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.CheckConstraint("name LIKE '#%'", name='check_hashtag_format'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('media',
    sa.Column('id', sa.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('content_type', sa.String(length=50), nullable=False),
    sa.Column('media_type', sa.Enum('IMAGE', 'VIDEO', name='mediatype'), nullable=False),
    sa.Column('url', sa.String(), nullable=False),
    sa.Column('thumbnail_url', sa.String(), nullable=True),
    sa.Column('width', sa.Integer(), nullable=True),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('size', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.Column('full_name', sa.String(length=512), nullable=False),
    sa.Column('phone_number', sa.String(length=16), nullable=True),
    sa.Column('bio', sa.String(length=1024), nullable=True),
    sa.Column('avatar', sa.String(), nullable=True),
    sa.Column('birth_date', sa.Date(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('deleted_at', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('uni_user_email', 'user', ['email'], unique=True, postgresql_where=False)
    op.create_index('uni_username', 'user', ['username'], unique=True, postgresql_where=False)
    op.create_table('friendship',
    sa.Column('id', sa.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('requester_id', sa.UUID(), nullable=False),
    sa.Column('addressee_id', sa.UUID(), nullable=False),
    sa.Column('status', sa.String(length=10), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.CheckConstraint("status IN ('pending', 'accepted', 'rejected')", name='check_friendship_status'),
    sa.CheckConstraint('requester_id != addressee_id', name='check_self_friendship'),
    sa.ForeignKeyConstraint(['addressee_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['requester_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('requester_id', 'addressee_id', name='uq_friendship')
    )
    op.create_table('like',
    sa.Column('id', sa.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('content_id', sa.UUID(), nullable=False),
    sa.Column('content_type', sa.String(length=10), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.CheckConstraint("content_type IN ('post', 'comment')", name='check_content_type'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id', 'content_id', 'content_type', name='uq_user_content_like')
    )
    op.create_table('message',
    sa.Column('id', sa.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('sender_id', sa.UUID(), nullable=False),
    sa.Column('receiver_id', sa.UUID(), nullable=False),
    sa.Column('content', sa.String(length=1024), nullable=False),
    sa.Column('is_read', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('deleted_at', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.CheckConstraint('sender_id != receiver_id', name='check_self_message'),
    sa.ForeignKeyConstraint(['receiver_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['sender_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('notification',
    sa.Column('id', sa.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('action_user_id', sa.UUID(), nullable=False),
    sa.Column('type', sa.String(length=20), nullable=False),
    sa.Column('content_id', sa.UUID(), nullable=False),
    sa.Column('content_type', sa.String(length=10), nullable=False),
    sa.Column('is_read', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.CheckConstraint("content_type IN ('post', 'comment', 'friendship', 'message')", name='check_content_type'),
    sa.CheckConstraint("type IN ('like', 'comment', 'follow', 'message')", name='check_notification_type'),
    sa.ForeignKeyConstraint(['action_user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post',
    sa.Column('id', sa.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=True),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('content', sa.String(length=1024), nullable=False),
    sa.Column('visibility', sa.String(length=16), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.Column('deleted_at', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post_hashtag',
    sa.Column('id', sa.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('post_id', sa.UUID(), nullable=False),
    sa.Column('hashtag_id', sa.UUID(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['hashtag_id'], ['hashtag.id'], ),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('post_id', 'hashtag_id', name='uq_post_hashtag')
    )
    op.create_table('post_media',
    sa.Column('id', sa.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('post_id', sa.UUID(), nullable=True),
    sa.Column('media_id', sa.UUID(), nullable=True),
    sa.Column('position', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.CheckConstraint('position >= 0 AND position < 4', name='check_position_range'),
    sa.ForeignKeyConstraint(['media_id'], ['media.id'], ),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('post_id', 'position', name='uq_post_media_position')
    )
    op.create_table('post_share',
    sa.Column('id', sa.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('post_id', sa.UUID(), nullable=False),
    sa.Column('comment', sa.String(length=280), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('deleted_at', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post_share')
    op.drop_table('post_media')
    op.drop_table('post_hashtag')
    op.drop_table('post')
    op.drop_table('notification')
    op.drop_table('message')
    op.drop_table('like')
    op.drop_table('friendship')
    op.drop_index('uni_username', table_name='user', postgresql_where=False)
    op.drop_index('uni_user_email', table_name='user', postgresql_where=False)
    op.drop_table('user')
    op.drop_table('media')
    op.drop_table('hashtag')
    # ### end Alembic commands ###
