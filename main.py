from app.screen import load_screen
from settings import screen

screen = load_screen(screen.get('driver'))

screen().show_sprite()
