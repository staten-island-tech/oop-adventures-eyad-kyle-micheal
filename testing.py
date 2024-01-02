from stuff import Player
Player.print_classes()
chosen = Player.better_choose_class()
if chosen:
    print(chosen.__dict__)