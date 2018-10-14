import subprocess

from libqtile.widget import volume


class UsefulVolumeWidget(volume.Volume):
    def __init__(
            self, *,
            button_up=volume.BUTTON_UP,
            button_down=volume.BUTTON_DOWN,
            button_mute=volume.BUTTON_MUTE,
            button_right=volume.BUTTON_RIGHT,
            **kwargs):
        super().__init__(**kwargs)

        self.button_up = button_up
        self.button_down = button_down
        self.button_mute = button_mute
        self.button_right = button_right

    def button_press(self, x, y, button):
        if button == self.button_down:
            if self.volume_down_command is not None:
                subprocess.call(self.volume_down_command)
            else:
                subprocess.call(self.create_amixer_command('-q',
                                                           'sset',
                                                           self.channel,
                                                           '%d%%-' % self.step))
        elif button == self.button_up:
            if self.volume_up_command is not None:
                subprocess.call(self.volume_up_command)
            else:
                subprocess.call(self.create_amixer_command('-q',
                                                           'sset',
                                                           self.channel,
                                                           '%d%%+' % self.step))
        elif button == self.button_mute:
            if self.mute_command is not None:
                subprocess.call(self.mute_command)
            else:
                subprocess.call(self.create_amixer_command('-q',
                                                           'sset',
                                                           self.channel,
                                                           'toggle'))
        elif button == self.button_right:
            if self.volume_app is not None:
                subprocess.Popen(self.volume_app)

        self.draw()

    def cmd_increase_vol(self):
        # Emulate button press.
        self.button_press(0, 0, self.button_up)

    def cmd_decrease_vol(self):
        # Emulate button press.
        self.button_press(0, 0, self.button_down)

    def cmd_mute(self):
        # Emulate button press.
        self.button_press(0, 0, self.button_mute)

    def cmd_run_app(self):
        # Emulate button press.
        self.button_press(0, 0, self.button_right)
