# coding: utf-8

import numpy
import pygame

import buttons


# CONSTANTS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (109, 196, 255)

BUTTON_SIZE = 30
BLOCKSIZE = 30

class CellsGrid:
    def __init__(self, resolution):
        self.cells = numpy.zeros(resolution, dtype=bool)
        self.res = resolution
    def change_cell(self, pos):
        self.cells[pos[0], pos[1]] = not self.cells[pos[0], pos[1]]

    def __getitem__(self, k):
        return self.cells[k]




class ConwaysLife:
    def do_play(self):
        self.play = True
        self.stop = False

    def do_pause(self):
        self.play = False
        self.stop = False

    def do_stop(self):
        self.play = False
        self.stop = True
        pygame.quit()

    def __init__(self, resolution=(720, 480)):
        super().__init__()

        self.resolution = resolution

        self.play = False
        self.stop = False

        self.cells = CellsGrid((self.resolution[0] // BLOCKSIZE, self.resolution[1] // BLOCKSIZE))


    def mainloop(self):

        pygame.init()
        self.screen = pygame.display.set_mode(self.resolution)

        self.labelFont = pygame.font.SysFont('Arial', 16)


        main_button = buttons.MainButton(
            (0, self.resolution[1] - BUTTON_SIZE), [
                buttons.PlayPauseButton((0, self.resolution[1] - BUTTON_SIZE * 2), self, (BUTTON_SIZE, BUTTON_SIZE)),
            ], (BUTTON_SIZE, BUTTON_SIZE)
        )

        move_camera = False
        fps_clock = pygame.time.Clock()

        self.do_play()
        while not self.stop:
            self.screen.fill(BLACK)
            # events captures
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.do_stop()
                    exit(0)

                if event.type == pygame.KEYDOWN:
                    # check for pause key
                    if event.key == pygame.K_SPACE:
                        if self.play:
                            self.do_pause()
                        else:
                            self.do_play()


                    # check for exit/stop key
                    if event.key == pygame.K_ESCAPE:
                        self.do_stop()
                        return


                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if not main_button.check_hold(event.pos):
                            self.cells.change_cell((event.pos[0] // BLOCKSIZE, event.pos[1] // BLOCKSIZE))



                if event.type == pygame.MOUSEBUTTONUP:
                    main_button.check_release()


            if self.play:
                pass
            else:
                pass

            blockSize = 20 #Set the size of the grid block
            for x in range(self.cells.res[0]):
                for y in range(self.cells.res[1]):
                    rect = pygame.Rect(x*BLOCKSIZE, y*BLOCKSIZE, BLOCKSIZE, BLOCKSIZE)
                    pygame.draw.rect(self.screen, WHITE, rect, (not self.cells[x][y]))

            main_button.update(self.screen)

            pygame.display.flip()
            fps_clock.tick()


if __name__=="__main__":
    app = ConwaysLife()
    app.mainloop()