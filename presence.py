import pypresence

previous_id = None
RPC = None

def update_presence(app_id, values):
    global RPC
    global previous_id

    if app_id != previous_id:
        if isinstance(RPC, pypresence.Presence):
            RPC.close()
        
        RPC = pypresence.Presence(app_id)
        RPC.connect()
        previous_id = app_id
    
    party_size = None
    if values['party_size'] is not None and values['party_max'] is not None:
        party_size = [values['party_size'], values['party_max']]
    
    RPC.update(
        state=values['state'],
        details=values['details'],
        start=values['start'],
        end=values['end'],
        large_image=values['large_image_key'],
        large_text=values['large_image_text'],
        small_image=values['small_image_text'],
        small_text=values['small_image_text'],
        party_size=party_size
    )