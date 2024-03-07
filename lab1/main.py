import tourney

tourney = tourney.Tournament("Flemington Racecours", 20)
tourney.register_participant("Petr", "Krya", 14)
tourney.register_participant("Dima", "Porsh", 19)
tourney.register_participant("Sasha", "Lada", 23)
tourney.register_participant("Beastyqt", "HRE", 20)
tourney.register_ticket_seller("Pasha")
tourney.register_judge("Zheka")
tourney.register_track("Churchill Downs", 122)
tourney.register_ticket(1, "Mall")
tourney.sell_ticket()
tourney.sell_ticket()
tourney.set_places()
