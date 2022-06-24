import pygame
import pygame_gui

money_per_second = 1
money = 0
cost = 10
cost_factory = 100
cost_prestige = 1000000

pygame.init()

pygame.display.set_caption('Money Maker')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((800, 600))

current_money = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((100, 100), (300, 200)),
                                            text="Current money: "+str(money), manager=manager)
printer_cost = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((100, 100), (300, 300)),
                                            text="Printer cost: "+str(cost), manager=manager)
factory_cost = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((100, 00), (300, 300)),
                                            text="Factory cost: "+str(cost_factory), manager=manager)
mps = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((100, 100), (300, 400)),
                                            text="Money per second: "+str(money_per_second), manager=manager)
prestige_cost = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((100, 200), (300, 300)),
                                            text="Prestige cost: "+str(cost_prestige), manager=manager)

earn_money = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((600, 500), (150, 50)),
                                            text='Earn Money',
                                            manager=manager)
buy_printer = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((400, 500), (150, 50)),
                                            text='Buy Printer',
                                            manager=manager)
buy_prestige = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 500), (150, 50)),
                                            text='Prestige',
                                            manager=manager)
buy_factory = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((00, 500), (150, 50)),
                                            text='Buy Factory',
                                            manager=manager)
clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    money += money_per_second
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == earn_money:
                money += 10
            if event.ui_element == buy_printer:
                if money >= cost:
                    money_per_second *= 1.5
                    cost *= 2
            if event.ui_element == buy_factory:
                if money >= cost_factory:
                    money_per_second *= 15
                    cost_factory *= 5
            if event.ui_element == buy_prestige:
                if money >= cost_prestige:
                    money_per_second *= 1500
                    cost_prestige *= 1000

        manager.process_events(event)

    manager.update(time_delta)

    current_money.set_text("Current money: "+"{:.2f}".format(money))
    printer_cost.set_text('Buy Printer Cost: '+str(cost))
    mps.set_text('Money per second: '+"{:.2f}".format(money_per_second))
    factory_cost.set_text('Buy Factory Cost: '+str(cost_factory))
    prestige_cost.set_text('Prestige Cost: '+str(cost_prestige))

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)
    pygame.display.update()