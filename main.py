distance = 0

def on_forever():
    global distance
    distance = sonar.ping(DigitalPin.P0, DigitalPin.P1, PingUnit.CENTIMETERS)
    if distance < 0:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
    else:
        if distance < 2:
            basic.show_leds("""
                # . . . .
                                # . . . .
                                # . . . .
                                # . . . .
                                # . . . .
            """)
        else:
            if distance < 4:
                basic.show_leds("""
                    # # . . .
                                        # # . . .
                                        # # . . .
                                        # # . . .
                                        # # . . .
                """)
            if distance < 5:
                basic.show_leds("""
                    # # # . .
                                        # # # . .
                                        # # # . .
                                        # # # . .
                                        # # # . .
                """)
            else:
                if distance < 7:
                    basic.show_leds("""
                        # # # # .
                                                # # # # .
                                                # # # # .
                                                # # # # .
                                                # # # # .
                    """)
                if distance < 10:
                    basic.show_leds("""
                        # # # # #
                                                # # # # #
                                                # # # # #
                                                # # # # #
                                                # # # # #
                    """)
basic.forever(on_forever)
