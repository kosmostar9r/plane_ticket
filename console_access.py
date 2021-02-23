# -*- coding: utf-8 -*-
import argparse
from ticket_maker import TicketMaker


class TicketManager:

    def __init__(self):
        self.ticket_parser = argparse.ArgumentParser(
            'Input your name(fio), departure place(from), arrival place(to) and date(date)')

    def add_arguments(self):
        self.ticket_parser.add_argument('-n', '--name', required=True, nargs=2,
                                        help='Your full name, example IVANOV A.A.')
        self.ticket_parser.add_argument('-f', '--departure', required=True, help='Departure place')
        self.ticket_parser.add_argument('-t', '--arrival', required=True, help='Arrival place')
        self.ticket_parser.add_argument('-d', '--date', required=True, help='Flight date (dd.mm.)')
        self.ticket_parser.add_argument('-s', '--save_to', required=False,
                                        help='File to save the ticket'
                                             ' (pls input full path to directory you want to save the ticket)')
        return self.ticket_parser.parse_args()

    def run(self):
        args = self.add_arguments()
        if args.save_to is None:
            tm = TicketMaker(name=' '.join(args.name), departure=args.departure, arrival=args.arrival, date=args.date)
        else:
            tm = TicketMaker(name=' '.join(args.name), departure=args.departure, arrival=args.arrival,
                             date=args.date, save_to=args.save_to)
        tm.make_ticket()
        tm.save_ticket()


manager = TicketManager()
manager.run()

# $ python3 console_access.py -n Surname N.N. -f City_from -t City_to -d dd.mm -s /full_file_path/ticket.png
