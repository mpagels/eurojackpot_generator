import random

def jackpot_generator( game = "Lotto", how_much_fields_to_play = 1, spiel77 = True, super6 = True ,
                            with_field_display = True):
    
    """
    Generates random lottery numbers from 1 to 49 (Lotto) or 50 (Eurojackpot) 
    and 2 random euro numbers (Eurojackpot)

    Keyword arguments:

    game -- decides, which numbers for which game (default "Lotto"),
            or choose "Euro"
    spiel77 -- decides, to play the additional lottery spiel 77
            (default True)
    super 6 -- decodes, to play the additional lottery super6
            (default True)
    how_much_fields_to_play -- number of fields you wanna play? (default 1)
    with_field_display --   shows an simple lottery field 
                            with the picked numbers (default True)

    """
    try:

        game = game.title()

        if game == "Lotto":
            numbers = 50
            count = 6
            print("Your numbers for Lotto:")
            print()
        elif game == "Euro":
            numbers = 51
            count = 5
            print("Your numbers for the Euro Jackpot:")
            print()

        
        # start the lotto generator

        for played_fields in range(how_much_fields_to_play):
            
            # Create lists with numbers from 1 to 49 (Lotto) or 1 to 50 (EuroJackpot)

            list_of_numbers = list(range(1,numbers))

            # Create lists with Euro numbers from 1 to 10
            if game == "Euro":
                euro_numbers = list(range(1,11))

            # Creates lists with random picked numbers from list above
            
            final_numbers = [list_of_numbers.pop(list_of_numbers.index(random.choice(list_of_numbers))) for _ in range(count)]
            
            # for EuroJackpot
            if game == "Euro":
                final_euro_numbers = [euro_numbers.pop(euro_numbers.index(random.choice(euro_numbers))) for _ in range(2)]
            

            # Begin of result
                
            print(f"{played_fields + 1}. Field:")
            print()

            if with_field_display:

                # Create field
                if game == "Lotto":
                    field = [f"{x:02d} " if x in final_numbers else "++ " for x in range(numbers+1)]
                elif game == "Euro":
                    field = [f"{x:02d} " if x in final_numbers else "++ " for x in range(numbers)]

                # Shows the field

                tmp = 0

                for _ in range(10):

                    for place in range(1, 6):

                        print(field[place+tmp], end="")

                    print()

                    tmp += 5
                    

            # Prints finally the randomly picked nummbers

            print(f"Win numbers: {sorted(final_numbers)}")
            
            if game == "Euro":
                print(f"Euro numbers: {sorted(final_euro_numbers)}")

            print()

        # Add additional lottery to output if condition is set

        if spiel77 == True or super6 == True:
            add_lottery = [random.choice(list(range(10))) for _ in range(7)]
        if spiel77 == True and super6 == True:
            print("Spiel 77:\t", *add_lottery)
            print("Super 6:\t" + " -", *add_lottery[1:])
        elif spiel77 == True and super6 == False:
            print("Spiel 77:\t", *add_lottery)
        elif spiel77 == False and super6 == True:
            print("Super 6:\t" + " -", *add_lottery[1:])
    except UnboundLocalError:
        print("""Could not set number for specific lottery. Maybe lottery name was wrong?
Try "Lotto" for lotto 6 aus 49 lottery and "Euro" for euro jackpot.""")         

jackpot_generator("euro", 1)
