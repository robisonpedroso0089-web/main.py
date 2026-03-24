# main.py - GROKZOMBORG: GITHUB INTEGRADO, ROBISON!
# O monstro agora sabe que você tem o repo no GitHub e está rugindo pra ele!

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.uix.label import Label
import random

class GrokzomborgWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.evolucao = 3  # NÍVEL MÁXIMO - GITHUB ATIVADO!
        self.rugidos = [
            "GITHUB DESPERTADO! ROOOAAAR-ZIIIMB!",
            "*bip bip* REPOSITÓRIO GROKZOMBORG ATIVO!",
            "01000111 01001001 01010100 01001000 01010101 01000010!",
            "EU SOU O MONSTRO DO SEU GITHUB... WiFi 6E VERDE!"
        ]

        # Sons
        self.sons = [
            SoundLoader.load('data/sounds/roar1.wav'),
            SoundLoader.load('data/sounds/roar2.wav'),
            SoundLoader.load('data/sounds/roar3.wav'),
            SoundLoader.load('data/sounds/roar4.wav')
        ]
        for s in self.sons:
            if s: s.volume = 1.3

        # Fundo com vibe GitHub (preto com verde neon)
        with self.canvas.before:
            Color(0.01, 0.05, 0.02, 1)
            self.bg = Rectangle(pos=self.pos, size=self.size)

        self.bind(size=self.atualizar_fundo, pos=self.atualizar_fundo)

        self.x = self.width / 2
        self.y = self.height / 2
        self.vx = random.choice([-6, 6])
        self.vy = random.choice([-6, 6])

        self.desenhar()
        Clock.schedule_interval(self.update, 1/60.0)
        self.tocar_som()

        # Label do GitHub
        self.github_label = Label(
            text="✅ Seu repo no GitHub está vivo!\n"
                 "https://github.com/robisonpedroso0089-web/grokzomborg\n\n"
                 "Toque na tela pra evoluir o monstro\n"
                 "e continuar construindo o EcoZum!",
            font_size='32sp',
            color=(0, 1, 0.5, 1),
            size_hint=(0.9, 0.4),
            pos_hint={'center_x': 0.5, 'center_y': 0.55},
            halign='center'
        )
        self.add_widget(self.github_label)

    def atualizar_fundo(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size

    def desenhar(self):
        self.canvas.clear()
        with self.canvas:
            cores = [(0,0.8,0.2), (0,1,0.4), (0.1,1,0.6), (0.3,1,0.8)]
            Color(*cores[self.evolucao])

            tam = 130 + self.evolucao * 45
            Ellipse(pos=(self.x-tam/2, self.y-tam/2), size=(tam, tam))

            Color(0, 1, 0.5, 1)
            olho = 35 + self.evolucao * 12
            Ellipse(pos=(self.x-olho-20, self.y+25), size=(olho, olho*1.6))
            Ellipse(pos=(self.x+20, self.y+25), size=(olho, olho*1.6))

            Color(0.4, 1, 0.6, 1)
            Line(points=[self.x+40, self.y-30, self.x+120, self.y-140],
                 width=12 + self.evolucao*5, cap='round')

            if self.evolucao == 3:
                Color(0, 1, 0.4, random.uniform(0.5, 0.9))
                for _ in range(30):
                    Line(points=[self.x + random.randint(-170,170),
                                self.y + random.randint(-170,170),
                                self.x + random.randint(-170,170),
                                self.y + random.randint(-170,170)],
                         width=random.randint(4,10))

    def update(self, dt):
        self.x += self.vx
        self.y += self.vy

        if self.x < 110 or self.x > self.width - 110:
            self.vx *= -1
        if self.y < 110 or self.y > self.height - 190:
            self.vy *= -1

        self.desenhar()

    def tocar_som(self):
        som = self.sons[self.evolucao]
        if som:
            som.stop()
            som.play()

    def on_touch_down(self, touch):
        self.x = touch.x
        self.y = touch.y

        self.evolucao = (self.evolucao + 1) % 4
        self.tocar_som()

        from kivy.uix.label import Label
        msg = Label(text=self.rugidos[self.evolucao],
                    font_size='48sp',
                    color=(0,1,0.5,1),
                    pos_hint={'center_x':0.5, 'top':1},
                    size_hint_y=None, height=150)
        self.add_widget(msg)
        Clock.schedule_once(lambda dt: self.remove_widget(msg), 3.0)

        return True


class GrokzomborgApp(App):
    def build(self):
        self.title = "Grokzomborg - GitHub Ativo"
        self.icon = "data/icon.png"
        return GrokzomborgWidget()


if __name__ == '__main__':
    GrokzomborgApp().run()
