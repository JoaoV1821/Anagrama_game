import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED
from Anagrama import Anagrama


class Sistema_anagrama:
    def __init__(self):
        self.__anagrama = Anagrama()


    def __janela_principal(self):
        sg.theme('Reds') 

        layout = [
            [sg.Text('Palavra embaralhada:', justification='left'), sg.Text(f'{self.__anagrama.palavra_embaralhada}')],
            [sg.Text('Palpite:', justification='left'), sg.Input(key='palpite')],
            [sg.Button('Enviar'), sg.Button('Cancelar')]
        ]

        return sg.Window(title='Anagrama', layout=layout)
    

    def window_init(self):
       
            window = self.__janela_principal()
            sg.popup('Olá este é o Anagrama Game, aqui você tentará adivinhar o nome de uma das sete maravilhas do mundo antigo. Você terá direito a cinco tentativas. Boa sorte!')

            while True:
                try:
                    event, values = window.read()

                    if event == 'Cancelar' or event == WINDOW_CLOSED:
                        break

                    elif event == 'Enviar':

                        if values['palpite'] == self.__anagrama.palavra_normal:
                            sg.popup('Você acertou!')
                            break

                        else:
                            sg.popup('Palpite errado')
                            self.__anagrama.tentativas -= 1
                        
                        if self.__anagrama.tentativas == 0:
                            sg.popup(f'Acabaram as tentativas. A palavra era {self.__anagrama.palavra_normal}')
                            break

                except Exception as E:
                    sg.popup(E)
                    continue
       
if __name__ == '__main__':
    sistema = Sistema_anagrama()
    sistema.window_init()
