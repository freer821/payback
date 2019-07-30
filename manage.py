import os
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from main import create_app, db
from config import config_by_name

app = create_app(config_by_name[os.environ.get('ENV', 'dev')])
app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db, render_as_batch=True )
manager.add_command('db', MigrateCommand)

from main.models import user, shop

@manager.command
def run():
    app.run(host='0.0.0.0')

if __name__ == "__main__":
    manager.run()