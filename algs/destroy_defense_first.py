from battle import commander
unit_client = commander.Client()

def search_target(data=None, **kawargs):
    towers = unit_client.ask_towers()
    if towers:
        tower_id = towers[0]["id"]
        unit_client.do_attack(tower_id)
        unit_client.when_item_destroyed(tower_id, search_target)
    else:
        attack_center()

def attack_center(data=None, **kawargs):
    center = unit_client.ask_center()
    unit_client.do_attack(center['id'])
search_target()
