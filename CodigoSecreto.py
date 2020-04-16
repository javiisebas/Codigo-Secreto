from tkinterClasses import *
from sendEmail import *
from patronCreator import *
from runGame import *
from wordsListCreator import *


os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (0, 0)

DameCorreos = mainAppWin()
xResolution = DameCorreos.xRes
yResolution = DameCorreos.yRes

res = xResolution, yResolution


decision = True
while decision:

    patron_generator = patronGen()
    patron_generator.create_figure()
    original_matrix = patron_generator.original_matrix
    
    if len(DameCorreos.mails) > 0:

        enviaCorreo(DameCorreos.mails, ) 
        remove('patron.png')
        palabras_juego = wordsList()  


        pygame.init()

        win = pygame.display.set_mode(res)
        pygame.key.set_mods(0) 
 
        icon = pygame.image.load('icon/icon.png')
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Código Secreto")

        Malla = malla(res)
        Palabras = palabras(res)
        Matriz = ColoresMatriz(res)
        Muerto = muerto(res)
        Victoria = victoria(res)
        Salir = salir(res)


        def redrawWin():
            win.fill((245,222,179))

            Salir.draw(win)
            if Salir.run:
                Matriz.posicion(win, Muerto, original_matrix)
                Palabras.draw(win, Victoria, original_matrix, palabras_juego)
                Malla.draw(win)
                Muerto.draw(win, Victoria, Matriz, original_matrix)
                Victoria.draw(win, Matriz, original_matrix)
            Salir.draw(win)

            pygame.display.update()

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            redrawWin()
            run = Salir.run

        pygame.quit()

        Pregunta = preguntar()
        decision = Pregunta.decision

    else:
        remove('patron.png')
        decision = False
   

