import webbrowser

"""Módulo para abrir un video tutorial en YouTube"""
def ver_video():
    """Abre un video tutorial de YouTube en el navegador"""
    url = "https://www.youtube.com/watch?v=ArKbAx1K-2U"  
    print("\nAbriendo video tutorial en el navegador...")
    webbrowser.open(url)

