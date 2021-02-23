# -*- coding: utf-8 -*-
import os

from PIL import Image, ImageFont, ImageDraw, ImageColor

TICKET_TEMPLATE = Image.open('files/ticket_template.png')
FONT = os.path.join('files', 'Tengri.ttf')
TICKET_FONT = ImageFont.truetype(FONT, size=14)


class TicketMaker:

    def __init__(self, name, departure, arrival, date, save_to=None):
        self.name = name.split(' ')
        self.departure = departure
        self.arrival = arrival
        self.date = date
        self.save_to = save_to
        self.ticket = ImageDraw.Draw(TICKET_TEMPLATE)

    def make_ticket(self):
        name_x, name_y = 47, 128
        name_message = f'{self.name[0].upper()} {self.name[1].upper()}'
        self.ticket.text(xy=(name_x, name_y), text=name_message, font=TICKET_FONT, fill=ImageColor.colormap['black'])

        from_y = 197
        from_message = self.departure.upper()
        self.ticket.text(xy=(name_x, from_y), text=from_message, font=TICKET_FONT, fill=ImageColor.colormap['black'])

        to_y = 263
        to_message = self.arrival.upper()
        self.ticket.text(xy=(name_x, to_y), text=to_message, font=TICKET_FONT, fill=ImageColor.colormap['black'])

        date_x = 286
        date_message = self.date
        self.ticket.text(xy=(date_x, to_y), text=date_message, font=TICKET_FONT, fill=ImageColor.colormap['black'])

    def save_ticket(self):
        save_to = self.save_to if self.save_to else 'ticket_named.png'
        save_to = os.path.normpath(save_to)
        TICKET_TEMPLATE.save(save_to)
        print(f'Ticket saved at {save_to}')


if __name__ == '__main__':
    tm = TicketMaker(name='KONOVALOV A.V.', departure='MOSCOW', arrival='BERLIN', date='25.12')
    tm.make_ticket()
    tm.save_ticket()
