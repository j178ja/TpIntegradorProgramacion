import os

def limpiar_pantalla():
    """Limpia completamente la pantalla de la terminal"""
    # Windows usa 'cls', Linux/macOS usa 'clear'
    comando = 'cls' if os.name == 'nt' else 'clear'
    os.system(comando)
   
