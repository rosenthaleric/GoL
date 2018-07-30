import pyglet
import math
from gol import GoL


class Window(pyglet.window.Window):

    def __init__(self):
        super().__init__(500, 500)
        self.res = 10
        self.gol = GoL(self.get_size()[0], self.get_size()[1], self.res)
        pyglet.clock.schedule_interval(self.update, 1.0 / 60.0)
        self.label = pyglet.text.Label(font_name='Lucida Sans',
                                       font_size=15,
                                       bold=True,
                                       x = 5, y = 30,
                                       width = self.width / 2, multiline=True,)

    def on_draw(self):
        self.clear()
        self.gol.draw()
        self.label.draw()

    def update(self, t):
        self.gol.next_gen()
        self.label.text = 'Cells alive: ' + str(self.gol.total) \
                          + "\nAverage age: " + '{0:.2f}'.format(self.gol.av_age)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        self.gol.populate(math.floor(x / self.res), math.floor(y / self.res))


window = Window()
pyglet.app.run()