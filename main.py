from app.screen import available_screens
from settings import screen

screen = available_screens.get(screen.get('driver'))

screen().show_text('HO HO HO!')
