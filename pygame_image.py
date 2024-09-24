import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    bg_img2 = pg.transform.flip(bg_img, True, False)
    kk_rct = kk_img.get_rect() #8-1
    kk_rct.center = 300, 200 #8-2

    tmr = 0
    while True:
        mx = 0
        my = 0
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()
        if key_lst:
            #kk_rct.move_ip((-1, 0))
            mx = -1
            #my = 0
        if key_lst[pg.K_UP]:
            #mx = 0          # こうかとんの縦座標を―1する
            my = -1
        if key_lst[pg.K_DOWN]:
            #mx = 0
            my = +1
        if key_lst[pg.K_LEFT]:
            mx = -2
            #my = 0
        if key_lst[pg.K_RIGHT]:
            mx = 2
            #my = 0
        
        kk_rct.move_ip((mx, my))

        #for i in [pg.K_UP,pg.K_DOWN,pg.K_LEFT,pg.K_RIGHT]:
        #if key_lst[]:
        
            
        x = -(tmr%3200)
        screen.blit(bg_img, [x, 0])
        screen.blit(bg_img2, [x+1600, 0])
        screen.blit(bg_img, [x+3200, 0])
        screen.blit(bg_img2, [x+4800, 0])
        screen.blit(kk_img, kk_rct) #4  #8-5
        pg.display.update()
        tmr += 1        
        clock.tick(200) #5


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()