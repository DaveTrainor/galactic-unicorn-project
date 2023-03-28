def load_screen(driver):
    available_screens = {
        'pico_unicorn': 'PicoUnicornScreen',
        'galactic_unicorn': 'PicoGalacticUnicornScreen',
    }
    driver = available_screens.get(driver)
    screen_module = __import__(f'app.screen.{driver}')
    screen_module = getattr(screen_module.screen, driver)
    return getattr(screen_module, driver)
