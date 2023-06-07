"""added openAI blacklist

Revision ID: 951a5ce4741b
Revises: b3cb0f9f62c3
Create Date: 2023-05-19 17:36:04.741819

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "951a5ce4741b"
down_revision = "b3cb0f9f62c3"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "openai_bans",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name=op.f("fk_openai_bans_user_id_users")
        ),
        sa.PrimaryKeyConstraint("user_id", name=op.f("pk_openai_bans")),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("openai_bans")
    # ### end Alembic commands ###