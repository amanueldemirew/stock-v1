import click
import os
from alembic import command
from alembic.config import Config

# Get the absolute path to the alembic.ini file in the app/database directory
alembic_cfg = Config(os.path.join(os.path.dirname(__file__), "app", "database", "alembic.ini"))

@click.group()
def cli():
    """Database management commands"""
    pass

@click.command()
@click.option('--message', '-m', required=True, help='Migration message')
def migrate(message):
    """Generate new migration"""
    # Set the script_location to the correct migrations directory
    alembic_cfg.set_main_option('script_location', os.path.join(os.path.dirname(__file__), "app", "database", "migrations"))
    command.revision(alembic_cfg, message=message, autogenerate=True)
    click.echo("✅ Migration created")

@click.command()
def upgrade():
    """Upgrade to latest migration"""
    alembic_cfg.set_main_option('script_location', os.path.join(os.path.dirname(__file__), "app", "database", "migrations"))
    command.upgrade(alembic_cfg, "head")
    click.echo("✅ Database upgraded")

@click.command()
def downgrade():
    """Downgrade by one migration"""
    alembic_cfg.set_main_option('script_location', os.path.join(os.path.dirname(__file__), "app", "database", "migrations"))
    command.downgrade(alembic_cfg, "-1")
    click.echo("⬇️ Database downgraded")

@click.command()
def current():
    """Show current migration"""
    alembic_cfg.set_main_option('script_location', os.path.join(os.path.dirname(__file__), "app", "database", "migrations"))
    command.current(alembic_cfg)

@click.command()
def history():
    """Show migration history"""
    alembic_cfg.set_main_option('script_location', os.path.join(os.path.dirname(__file__), "app", "database", "migrations"))
    command.history(alembic_cfg)

# Add commands to the CLI group
cli.add_command(migrate)
cli.add_command(upgrade)
cli.add_command(downgrade)
cli.add_command(current)
cli.add_command(history)

if __name__ == '__main__':
    cli()