from tkinterClasses import *
from sendEmail import *
from patronCreator import *
from runGame import *
from wordsListCreator import *


os.environ["SDL_VIDEO_WINDOW_POS"] = "%d,%d" % (0, 0)

MenuApp = mainAppWin(MsgBox)
xResolution = MenuApp.xRes
yResolution = MenuApp.yRes

res = xResolution, yResolution
palabras_repetidas = []


def generaInfo(mails, palabras_repetidas):

    patron_generator = patronGen()
    patron_generator.create_figure()
    original_matrix = patron_generator.original_matrix

    enviaCorreo(mails) 
    remove(os.getcwd() + "/data/patron.png")
    palabras_juego = wordsList(palabras_repetidas)

    return original_matrix, palabras_juego


decision = MenuApp.decision
while decision:
    
    if len(MenuApp.mails) > 0:

        pygame.init()

        win = pygame.display.set_mode(res)
        pygame.key.set_mods(0) 
 
        icon = pygame.image.load(os.getcwd() + "/data/icon.png")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Código Secreto")

        Malla = malla(res)
        Cargando = cargando(res)
        Salir = salir(res)

        def redrawWin():
            win.fill((245,222,179))

            Salir.draw(win)
            if Salir.run:
                if not(Cargando.estado):
                    Cargando.estado = Salir.estado

                Cargando.draw(win)
                if not(Salir.reiniciar):
                    Matriz.posicion(win, Muerto, original_matrix)
                    Palabras.draw(win, Victoria, original_matrix, palabras_juego)
                    Malla.draw(win)
                    Muerto.draw(win, Victoria, Matriz, original_matrix)
                    Victoria.draw(win, Matriz, original_matrix, Muerto)
            Salir.draw(win)

            pygame.display.update()

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.display.iconify()

            redrawWin()

            if Salir.reiniciar and Cargando.estado:
                Salir.estado = False
                try:
                    info = generaInfo(MenuApp.mails, palabras_repetidas)

                    original_matrix = info[0]
                    palabras_juego = info[1]

                    palabras_repetidas += palabras_juego

                    if len(palabras_repetidas) >= 400:
                        palabras_repetidas = []

                    Palabras = palabras(res)
                    Matriz = ColoresMatriz(res)
                    Muerto = muerto(res)
                    Victoria = victoria(res)

                    Salir.reiniciar = False
                    
                except Exception:
                    Cargando.estado = False

            run = Salir.run

        pygame.quit()

        decision = Salir.decision

    else:
        decision = False
   

