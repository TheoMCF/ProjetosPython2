from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import firebase_admin
from firebase_admin import credentials, db
import time as t

cred = credentials.Certificate('C:/Users/axoga/Downloads/VsCode/Projetos-Python/App/credenciais_projeto.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://todorairai-default-rtdb.firebaseio.com/'
})

ref = db.reference('Tarefas')
GUI = Builder.load_file("gui.kv")
grid_de_tarefas = GUI.ids.gdt
lista_valores = list(ref.get().values())
lista_chaves = list(ref.get().keys())  

class Aplicativo(App):
    def build(self):
        return GUI

    def criar_tarefa(self):
        nova_tarefa = Label(text= f"{((GUI.ids.i0.text).strip()).capitalize()}", size_hint=(None, None))
        grid_de_tarefas.add_widget(nova_tarefa)
        id = sorted(ref.get().keys())
        numero_id = int((id[-1])[1]) + 1
        id_final = "t" + str(numero_id)
        nova_tarefa.id = id_final
        ref.update({id_final: nova_tarefa.text})
        GUI.ids.i0.text = ''
    
    def remover_tarefa(self):
        tarefa_para_remover = (GUI.ids.i1.text)
        print(lista_valores, lista_chaves, tarefa_para_remover)
        if tarefa_para_remover not in lista_valores:
            print('Tarefa não existente')
            GUI.ids.i1.text = ''
            GUI.ids.i1.hinttext = 'Tarefa não existente. Tente novamente'
            # GUI.ids.i1.hinttext
        else:
            pos_remover = lista_valores.index(tarefa_para_remover)
            id_remover = lista_chaves[pos_remover]
            for widget in grid_de_tarefas.children:
                if widget.text == tarefa_para_remover:
                    grid_de_tarefas.remove_widget(widget)
                    db.reference(f'Tarefas/{id_remover}').delete()
                    GUI.ids.i1.text = ''
                    break
    def on_start(self):
        # Carrega tarefas do banco de dados
        for item in lista_valores:
            nova_tarefa = Label(text=item, size_hint=(None, None))
            grid_de_tarefas.add_widget(nova_tarefa)

Aplicativo().run()