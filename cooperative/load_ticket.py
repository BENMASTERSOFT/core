from .models import GeneralTicket


def get_ticket():
    ticket=GeneralTicket.objects.first()
    r_ticket=ticket.ticket
    ticket.ticket=int(r_ticket) + 1
    ticket.save()
    return r_ticket