SAY_HI = "Say hi."
DONT_SAY_HI = "Don't say hi."
RUN_FOR_IT = "Run for it."
KEEP_WALKING = "Keep walking."
ADDRESS_WITH_NICKNAME = "Address the person using an amusing nickname such as 'Sarge', 'Slugger', or 'Master Blaster.'"
HELLO_DOCTOR = "Hello, doctor. What are my test results?"

remember_name = bool(input('Do you remember the person\'s name?'))

if remember_name:
    is_Ex = bool(input('Is it an ex?'))
    if is_Ex:
        are_Drunk = bool(input('Are you drunk?'))
        if are_Drunk:
            rekindle = bool(input('Do you want to rekindle and/or give \'em what for?'))
            output = SAY_HI if rekindle else DONT_SAY_HI
        else:
            in_Convertible = bool(input('Are you in a convertible with Brad Pitt and/or Rihanna?'))
            output = SAY_HI if in_Convertible else DONT_SAY_HI
    else:
        friends_Ex = bool(input('A friend\'s ex?'))
        if friends_Ex:
            output = DONT_SAY_HI
        else:
            enemy_or_Frenemy = bool(input('An enemy or frenemy?'))
            if enemy_or_Frenemy:
                in_Convertible = bool(input('Are you in a convertible with Brad Pitt and/or Rihanna?'))
                output = SAY_HI if in_Convertible else DONT_SAY_HI
            else:
                robbing_Bank = bool(input('Are you robbing a bank?'))
                if robbing_Bank:
                    output = DONT_SAY_HI
                else:
                    wearing_Bathrobe = bool(input('Are you in a bathrobe?'))
                    output = DONT_SAY_HI if wearing_Bathrobe else SAY_HI
else:
    time_to_Flee = bool(input('Is there time to flee?'))
    if time_to_Flee:
        output = RUN_FOR_IT
    else:
        pretend_Call = bool(input('Could you pretend to get a call on your cell?'))
        if pretend_Call:
            output = HELLO_DOCTOR
        else:
            wearing_Sunglasses = bool(input('Are you wearing sunglasses?'))
            if wearing_Sunglasses:
                output = KEEP_WALKING
            else:
                output = ADDRESS_WITH_NICKNAME