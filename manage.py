import os
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from main import create_app, db
from config import config_by_name
app = create_app(config_by_name[os.environ.get('ENV', 'dev')])
app.app_context().push()

from main.models import user

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run()

if __name__ == "__main__":
    manager.run()