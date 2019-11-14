import random

def eurojackpot_generator(how_much_field_to_play = 1, 
                            with_field_display = "yes"):
    
    """
    Generates 5 random lottery numbers from 1 to 50 
    and 2 random euro numbers

    Keyword arguments:

    how_much_field_to_play -- number of fields you wanna play? (default 1)
    with_field_display --   shows an simple lottery field 
                            with the picked numbers (default "yes")

    """

    for played_fields in range(how_much_field_to_play):
        
        # Create lists with numbers from 1 to 50 and 1 to 10

        numbers_to_50 = list(range(1,51))
        euro_numbers = list(range(1,11))

        # Creates lists with random picked numbers from list above

        final_numbers = [numbers_to_50.pop(numbers_to_50.index(random.choice(numbers_to_50))) for _ in range(5)]
        final_euro_numbers = [euro_numbers.pop(euro_numbers.index(random.choice(euro_numbers))) for _ in range(2)]
        

        # Begin of result
               
        print(f"{played_fields + 1}. Field:")
        print()

        if with_field_display == "yes":

            # Create field

            field = [f"{x:02d} " if x in final_numbers else "++ " for x in range(51)]

            # Shows the field

            tmp = 0

            for _ in range(10):

                for place in range(1, 6):

                    print(field[place+tmp], end="")

                print()

                tmp += 5

        # Prints finally the randomly picked nummbers

        print(f"Win numbers: {sorted(final_numbers)}")
        print(f"Euro numbers: {sorted(final_euro_numbers)}")

        print()

eurojackpot_generator(8)