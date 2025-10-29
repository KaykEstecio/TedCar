from importlib import util
from pathlib import Path
import sys

APP_PATH = Path(__file__).resolve().parents[1] / 'app.py'

spec = util.spec_from_file_location('app', str(APP_PATH))
mod = util.module_from_spec(spec)
# Garantir que o diretório do app esteja em sys.path para imports relativos funcionarem
app_dir = str(APP_PATH.parent)
if app_dir not in sys.path:
    sys.path.insert(0, app_dir)

spec.loader.exec_module(mod)

app = mod.app

with app.test_client() as c:
    resp = c.get('/cars')
    print('STATUS', resp.status_code)
    print('BODY')
    print(resp.data.decode())
