import os
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

# Dossier de l'app (fiable aussi sur Android)
BASE = os.path.dirname(os.path.abspath(__file__))

NOM = "𝐂𝚯𝐃𝚵 𝛅፝֟፝͜𝒟 𝐊𝚫𝐑𝚫—͟͟͞͞𓆪"
FOND = os.path.join(BASE, "fond.png")
FONT_PATH = os.path.join(BASE, "font.ttf")
FONT = FONT_PATH if os.path.exists(FONT_PATH) else "Roboto"

BANNI = (
    "𝑻𝒖 𝒂𝒖𝒓𝒂𝒊𝒔 𝒅𝒖̂ 𝒕'𝒂𝒈𝒆𝒏𝒐𝒖𝒊𝒍𝒍𝒆𝒓 𝒒𝒖𝒂𝒏𝒅 𝒕𝒖 𝒆𝒏 𝒂𝒗𝒂𝒊𝒔 𝒍'𝒐𝒄𝒄𝒂𝒔𝒊𝒐𝒏. "
    "𝑯𝒆́𝒍𝒂𝒔, 𝒕𝒐𝒏 𝒂̂𝒎𝒆 𝒎'𝒂𝒑𝒑𝒂𝒓𝒕𝒊𝒆𝒏𝒕 𝒎𝒂𝒊𝒏𝒕𝒆𝒏𝒂𝒏𝒕.\n\n"
    "𝑻𝒖 𝒑𝒆𝒏𝒔𝒂𝒊𝒔 𝒎𝒆 𝒅𝒆́𝒇𝒊𝒍𝒆𝒓 ? 𝑵𝒐𝒏, 𝒕𝒖 𝒆𝒔 𝒋𝒖𝒔𝒕𝒆 𝒗𝒆𝒏𝒖 𝒎𝒆 𝒄𝒐𝒏𝒇𝒊𝒓𝒎𝒆𝒓 "
    "𝒒𝒖𝒆 𝒑𝒆𝒓𝒔𝒐𝒏𝒏𝒆 𝒏𝒆 𝒑𝒆𝒖𝒕 𝒎𝒆 𝒕𝒐𝒖𝒄𝒉𝒆𝒓.\n\n"
    "𝑷𝒆𝒓𝒔𝒐𝒏𝒏𝒆 𝒏𝒆 𝒎𝒆 𝒅𝒊𝒕 𝒏𝒐𝒏 𝒅𝒆𝒖𝒙 𝒇𝒐𝒊𝒔. 𝑴𝒆𝒓𝒄𝒊 𝒑𝒐𝒖𝒓 𝒍'𝒆́𝒄𝒉𝒂𝒖𝒇𝒇𝒆𝒎𝒆𝒏𝒕, "
    "𝒆𝒕 𝒒𝒖𝒆 𝒕𝒂 𝒅𝒊𝒔𝒑𝒂𝒓𝒊𝒕𝒊𝒐𝒏 𝒔𝒆𝒓𝒗𝒆 𝒅'𝒆𝒙𝒆𝒎𝒑𝒍𝒆 𝒂𝒖𝒙 𝒂𝒖𝒕𝒓𝒆𝒔 𝒊𝒏𝒔𝒆𝒄𝒕𝒆𝒔 "
    "𝒒𝒖𝒊 𝒐𝒏𝒕 𝒍'𝒊𝒅𝒆́𝒆 𝒅𝒆 𝒔𝒆 𝒅𝒓𝒆𝒔𝒔𝒆𝒓 𝒄𝒐𝒏𝒕𝒓𝒆 𝒎𝒐𝒊.\n\n"
    "🇨🇭 𝑭𝒖𝒄𝒌𝒆𝒅 𝒃𝒚 🇨🇭\n"
    "𝐂𝚯𝐃𝚵 𝛅፝֟፝͜𝒟 𝐊𝚫𝐑𝚫—͟͟͞͞𓆪"
)
NON_BANNI = (
    "𝑶̂ 𝒈𝒓𝒂𝒏𝒅 𝒄𝒉𝒂𝒏𝒄𝒆𝒍𝒊𝒆𝒓 𝒅𝒆 𝒍'𝒐𝒓𝒅𝒓𝒆 𝒑𝒖𝒓𝒈𝒂𝒕𝒐𝒊𝒓𝒆.\n\n"
    "𝑽𝒐̂𝒕𝒓𝒆 𝒄𝒊𝒃𝒍𝒆 𝒄𝒊𝒓𝒄𝒖𝒍𝒆 𝒆𝒏𝒄𝒐𝒓𝒆 𝒅𝒂𝒏𝒔 𝒍𝒂 𝒏𝒂𝒕𝒖𝒓𝒆 ⚰️"
)


class CheckerApp(App):
    def build(self):
        self.title = NOM
        # Évite que le clavier cache le champ de saisie
        Window.softinput_mode = "below_target"

        root = FloatLayout()
        if os.path.exists(FOND):
            root.add_widget(Image(source=FOND, fit_mode="fill"))

        box = BoxLayout(orientation="vertical", padding=20, spacing=12)
        box.add_widget(Label(text=NOM, font_name=FONT, font_size="20sp",
                             size_hint_y=None, height=80))
        box.add_widget(Label(text="Entrez le pseudo à vérifier :",
                             size_hint_y=None, height=40))

        self.champ = TextInput(multiline=False, size_hint_y=None, height=48)
        box.add_widget(self.champ)

        btn = Button(text="Lancer le Ban Checker", size_hint_y=None, height=52,
                     background_color=(0.83, 0.69, 0.22, 1), color=(0, 0, 0, 1))
        btn.bind(on_press=self.verifier)
        box.add_widget(btn)

        scroll = ScrollView()
        self.res = Label(text="", font_name=FONT, size_hint_y=None,
                         halign="left", valign="top")
        self.res.bind(
            width=lambda w, v: setattr(w, "text_size", (v, None)),
            texture_size=lambda w, v: setattr(w, "height", v[1]),
        )
        scroll.add_widget(self.res)
        box.add_widget(scroll)

        root.add_widget(box)
        return root

    def verifier(self, *args):
        pseudo = self.champ.text.strip()
        if not pseudo:
            self.res.text = "Veuillez entrer un pseudo."
            self.res.color = (1, 1, 0, 1)
        elif "ban" in pseudo.lower():
            self.res.text = BANNI
            self.res.color = (1, 0.3, 0.3, 1)
        else:
            self.res.text = NON_BANNI
            self.res.color = (0.3, 0.65, 1, 1)


if __name__ == "__main__":
    CheckerApp().run()
