import active_player
import product
import unittest
from track import Track
from unittest.mock import MagicMock

import tourney
from service_personnel import TicketSeller, Judge, Assistant


class TestTicket(unittest.TestCase):

    def test_ticket_number(self):
        ticket = product.Ticket(12345, "John Doe")
        self.assertEqual(ticket.get_ticket_number(), 12345)

    def test_ticket_name(self):
        ticket = product.Ticket(54321, "Jane Smith")
        self.assertEqual(ticket.get_ticket_name(), "Jane Smith")

class TestTournament(unittest.TestCase):

    def setUp(self):
        self.tournament = tourney.Tournament("Grand Tournament", 100)

    def test_register_participant(self):
        self.tournament.register_participant("Alice", "Thunder", 10)
        self.assertEqual(len(self.tournament.participants), 1)

    def test_register_ticket_seller(self):
        self.tournament.register_ticket_seller("Bob")
        self.assertIsNotNone(self.tournament.ticket_seller)

    def test_register_judge(self):
        self.tournament.register_judge("Charlie")
        self.assertIsNotNone(self.tournament.judge)

    def test_register_ticket(self):
        self.tournament.register_ticket(12345, "John Doe")
        self.assertEqual(len(self.tournament.tickets), 1)

    def test_register_track(self):
        self.tournament.register_track("Track1", 200)
        self.assertIsNotNone(self.tournament.track)

    def test_sell_ticket_with_seller_registered(self):
        ticket_seller = MagicMock()
        ticket_seller.sell_ticket = MagicMock()
        self.tournament.ticket_seller = ticket_seller

        self.tournament.sell_ticket()
        ticket_seller.sell_ticket.assert_called_once()

    def test_sell_ticket_without_seller_registered(self):
        with unittest.mock.patch('builtins.print') as mocked_print:
            self.tournament.sell_ticket()
            mocked_print.assert_called_with("Ticket seller is not registered.")

    def test_set_places_with_judge_registered(self):
        judge = MagicMock()
        judge.set_places = MagicMock()
        self.tournament.judge = judge

        self.tournament.set_places()
        judge.set_places.assert_called_once()

    def test_set_places_without_judge_registered(self):
        with unittest.mock.patch('builtins.print') as mocked_print:
            self.tournament.set_places()
            mocked_print.assert_called_with("Judge is not registered.")


class TestAssistant(unittest.TestCase):

    def test_get_assistant_name(self):
        assistant = Assistant("Alice")
        self.assertEqual(assistant.get_assistant_name(), "Alice")

    def test_get_assistant_name_empty(self):
        assistant = Assistant("")
        self.assertEqual(assistant.get_assistant_name(), "")

    def test_get_assistant_name_unicode(self):
        assistant = Assistant("Иван")
        self.assertEqual(assistant.get_assistant_name(), "Иван")


class TestJudge(unittest.TestCase):

    def test_is_have_horse_with_horses(self):
        judge = Judge("Alice")
        participants = [active_player.Participant("John", active_player.Horse("Thunder", 10)), active_player.Participant("Jane", active_player.Horse("Lightning", 12))]
        self.assertTrue(judge.is_have_horse(participants))

    def test_is_have_horse_without_horses(self):
        judge = Judge("Bob")
        participants = [active_player.Participant("Mike"), active_player.Participant("Sarah", active_player.Horse("Bolt", 11))]
        self.assertFalse(judge.is_have_horse(participants))

    def test_is_have_track_with_track(self):
        judge = Judge("Charlie")
        track = Track("Main Track", 1000)
        self.assertTrue(judge.is_have_track(track))

    def test_is_have_track_without_track(self):
        judge = Judge("David")
        track = Track()
        self.assertFalse(judge.is_have_track(track))


if __name__ == '__main__':
    unittest.defaultTestLoader.run()
