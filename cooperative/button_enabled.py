  member=MemberShipTerminationRequest.objects.get(id=pk)
    button_enabled=False
    if maturity_date <= current_date:
        button_enabled=True
    else:  
        if member.lock_status.title == 'OPEN':
            button_enabled=True
