import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from .config import BACKEND_URL
from .main import main
from .bobina_create import page_bobina_creator
from .bobina_remove import page_bobina_remover
from .bobina_move import page_bobina_mover
from .bobina_move_production import page_bobina_mover_producao
from .bobina_history import page_bobina_historico
from .bobina_stock import page_bobina_estoque