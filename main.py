from pyglet.window import mouse
from pyglet.window import key
from life import Life
import itertools
import pyglet

SIZE = 50

window = pyglet.window.Window(height=800, width=800)
game = Life()


@window.event
def on_draw():
    window.clear()
    batch = pyglet.graphics.Batch()
    batch_sprites = []
    for i, j in itertools.product(range(SIZE), repeat=2):
        if game.grid[i][j]:
            x, y = j*16, 784-i*16
            batch_sprites.append(pyglet.sprite.Sprite(pyglet.image.load('life16.png'), x, y, batch=batch))
    batch.draw()


@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        game.change_life(x // 16, SIZE - 1 - y // 16)


@window.event
def on_key_press(symbol, modifiers):
    global game
    if symbol == key.N:
        game = Life()


@window.event
def on_text(text):
    if text == ' ':
        game.iterate()


def main():
    pyglet.app.run()


if __name__ == '__main__':
    main()
