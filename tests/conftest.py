import sys
import os

# Caminho da RAIZ do projeto (pai de 'src')
ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT_PATH not in sys.path:
    sys.path.insert(0, ROOT_PATH)
    print(f"[conftest] added project root: {ROOT_PATH}")
