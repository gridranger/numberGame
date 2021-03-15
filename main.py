from typing import List, Sequence

from pygame import init, KEYDOWN, K_F4, K_LALT, K_RALT
from pygame.display import flip, set_mode, set_caption
from pygame.event import Event, get as get_events
from pygame.key import get_pressed
from pygame.locals import QUIT
from pygame.time import Clock

from settings import fps, screen_height, screen_width
from ui import TitleScene


class Main:
    title = "Számjáték"
    version = "0.1"

    def __init__(self):
        init()
        self.screen = set_mode((screen_width, screen_height))
        set_caption(f"{Main.title} v{Main.version}")
        self.clock = Clock()
        self.active_scene = TitleScene(self.screen)

    def _clean_events(self, pressed_keys: Sequence[bool]) -> List[Event]:
        result = []
        for current_event in get_events():
            quit_attempt = False
            if current_event.type == QUIT:
                quit_attempt = True
            elif current_event.type == KEYDOWN:
                alt_pressed = pressed_keys[K_LALT] or pressed_keys[K_RALT]
                if current_event.key == K_F4 and alt_pressed:
                    quit_attempt = True
            if quit_attempt:
                self.active_scene.terminate()
            else:
                result.append(current_event)
        return result

    def run_game(self):
        while self.active_scene:
            pressed_keys = get_pressed()
            events = self._clean_events(pressed_keys)
            self.active_scene.process_input(events, pressed_keys)
            self.active_scene.update()
            self.active_scene.render()
            self.active_scene = self.active_scene.next_scene
            flip()
            self.clock.tick(fps)


if __name__ == "__main__":
    Main().run_game()  # pragma: no cover
