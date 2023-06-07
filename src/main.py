import pyglet


window = pyglet.window.Window(fullscreen=True)


label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

#test github and vscode on windows

def update(dt):
    pass

@window.event
def on_draw():
    window.clear()
    label.draw()


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/60.0)
    pyglet.app.run()

