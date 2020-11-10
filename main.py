def on_forever():
    if sonar.ping(DigitalPin.P8, DigitalPin.P12, PingUnit.CENTIMETERS) >= 0 and sonar.ping(DigitalPin.P8, DigitalPin.P12, PingUnit.CENTIMETERS) < 2:
        basic.show_number(1)
        control.wait_micros(1000)
    elif sonar.ping(DigitalPin.P8, DigitalPin.P12, PingUnit.CENTIMETERS) >= 2 and sonar.ping(DigitalPin.P8, DigitalPin.P12, PingUnit.CENTIMETERS) < 4:
        basic.show_number(5)
        control.wait_micros(1000)
    elif sonar.ping(DigitalPin.P8, DigitalPin.P12, PingUnit.CENTIMETERS) >= 4 and sonar.ping(DigitalPin.P8, DigitalPin.P12, PingUnit.CENTIMETERS) < 6:
        basic.show_number(10)
        control.wait_micros(1000)
    elif sonar.ping(DigitalPin.P8, DigitalPin.P12, PingUnit.CENTIMETERS) >= 6 and sonar.ping(DigitalPin.P8, DigitalPin.P12, PingUnit.CENTIMETERS) < 8:
        basic.show_number(2)
        control.wait_micros(1000)
basic.forever(on_forever)
