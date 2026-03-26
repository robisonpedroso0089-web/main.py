# main.py - GROKZOMBORG: ROADMAP CONTINUADO - FASES FUTURAS 2027-2028
# O monstro agora mostra o Roadmap completo + fases futuras!

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
        self.evolucao = 3

        self.rugidos = [
            "ROADMAP CONTINUADO! ROOOAAAR-ZIIIMB!",
            "*bip bip* FUTURO DO ECOZUM CARREGANDO!",
            "01000110 01000001 01010011 01000101 01010011 01000110 01010101 01010100 01010101 01010010 01000001 01010011!",
            "EU SOU O MONSTRO QUE VAI DOMINAR O PLANETA!"
        ]

        self.sons = [
            SoundLoader.load('data/sounds/roar1.wav'),
            SoundLoader.load('data/sounds/roar2.wav'),
            SoundLoader.load('data/sounds/roar3.wav'),
            SoundLoader.load('data/sounds/roar4.wav')
        ]
        for s in self.sons:
            if s: s.volume = 1.3

        with self.canvas.before:
            Color(0.01, 0.12, 0.04, 1)
            self.bg = Rectangle(pos=self.pos, size=self.size)

        self.bind(size=self.atualizar_fundo, pos=self.atualizar_fundo)

        self.x = self.width / 2
        self.y = self.height / 2
        self.vx = random.choice([-5, 5])
        self.vy = random.choice([-5, 5])

        self.desenhar()
        Clock.schedule_interval(self.update, 1/60.0)
        self.tocar_som()

        # ROADMAP COMPLETO + FUTURO
        self.roadmap_text = Label(
            text="🌍 ROADMAP COMPLETO - ECOZUM\n\n"
                 "✅ FASE 1 - Monstro Básico\n"
                 "✅ FASE 2 - Chat com Ollama\n"
                 "📱 FASE 3 - Versão Mobile (APK)\n"
                 "🔬 FASE 4 - Realidade Aumentada\n"
                 "   • Zumbi aparece no quintal real\n"
                 "   • Detecção de lixo com câmera\n\n"
                 "🌳 FASE 5 - Impacto Real\n"
                 "   • Cada rugido = árvore plantada\n"
                 "   • Parceria com ONGs\n\n"
                 "🌐 FASE 6 - Global (2027)\n"
                 "   • Multiplayer mundial\n"
                 "   • Ranking de zumbis ecológicos\n"
                 "   • Site oficial + App Store\n\n"
                 "🚀 FASE 7 - Expansão (2028)\n"
                 "   • Modo escola (aulas interativas)\n"
                 "   • Grokzomborg em metaverso\n"
                 "   • IA que aprende com as crianças\n"
                 "   • Milhões de zumbis salvando o planeta!\n\n"
                 "TOQUE NA TELA PRA EVOLUIR O MONSTRO!",
            font_size='24sp',
            color=(0, 1, 0.5, 1),
            size_hint=(0.92, 0.78),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            halign='center'
        )
        self.add_widget(self.roadmap_text)

    def atualizar_fundo(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size

    def desenhar(self):
        self.canvas.clear()
        with self.canvas:
            cores = [(0,0.8,0.2), (0,1,0.4), (0.1,1,0.6), (0.3,1,0.8)]
            Color(*cores[self.evolucao])

            tam = 140 + self.evolucao * 40
            Ellipse(pos=(self.x-tam/2, self.y-tam/2), size=(tam, tam))

            Color(0, 1, 0.5, 1)
            olho = 38 + self.evolucao * 12
            Ellipse(pos=(self.x-olho-25, self.y+30), size=(olho, olho*1.6))
            Ellipse(pos=(self.x+25, self.y+30), size=(olho, olho*1.6))

            Color(0.4, 1, 0.6, 1)
            Line(points=[self.x+45, self.y-35, self.x+125, self.y-145],
                 width=12 + self.evolucao*6, cap='round')

            if self.evolucao == 3:
                Color(0, 1, 0.4, random.uniform(0.5, 0.9))
                for _ in range(32):
                    Line(points=[self.x + random.randint(-170,170),
                                self.y + random.randint(-170,170),
                                self.x + random.randint(-170,170),
                                self.y + random.randint(-170,170)],
                         width=random.randint(4,11))

    def update(self, dt):
        self.x += self.vx
        self.y += self.vy

        if self.x < 120 or self.x > self.width - 120:
            self.vx *= -1
        if self.y < 120 or self.y > self.height - 200:
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
                    font_size='46sp',
                    color=(0,1,0.5,1),
                    pos_hint={'center_x':0.5, 'top':1},
                    size_hint_y=None, height=140)
        self.add_widget(msg)
        Clock.schedule_once(lambda dt: self.remove_widget(msg), 3.0)

        return True


class GrokzomborgApp(App):
    def build(self):
        self.title = "Grokzomborg - Roadmap 2026-2028"
        self.icon = "data/icon.png"
        return GrokzomborgWidget()


if __name__ == '__main__':
    GrokzomborgApp().run()
name: "CodeQL"

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]
  schedule:
    - cron: '0 0 * * 0'   # Toda domingo à meia-noite

jobs:
  analyze:
    name: Analyze
    runs-on: ubuntu-latest
    permissions:
      actions: read
      contents: read
      security-events: write

    strategy:
      fail-fast: false
      matrix:
        language: [ 'python' ]

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Initialize CodeQL
        uses: github/codeql-action/init@v3
        with:
          languages: ${{ matrix.language }}

      - name: Perform CodeQL Analysis
        uses: github/codeql-action/analyze@v3
