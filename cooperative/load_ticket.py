from .models import GeneralTicket 


def get_ticket():
    ticket=GeneralTicket.objects.first()

    if not ticket:
        return 'a'
    else:
        r_ticket=str(ticket.ticket).zfill(5)
        ticket.ticket=int(r_ticket) + 1
        ticket.save()
        return r_ticket