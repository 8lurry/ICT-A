def electricity_bill(unit):
    """
    # Returns electricity bill for different unit consumption range.
    # 
    # consumed = unit*1.5+25 if unit <= 100
    # consumed = 100*1.5+(unit-100)*2.5+50 if 100 < unit <=200
    # consumed = 100*1.5+100*2.5+(unit-200)*4+75 if 200 < unit <=300
    # consumed = 100*1.5+100*2.5+100*4+(unit-300)*5+100 if 300 < unit <=350
    # consumed = 1500 if unit > 350
    """
    unit = unit
    if unit <= 100:
        return unit * 1.5 + 25
    elif unit <= 200:
        return 100 * 1.5 + (unit - 100) * 2.5 + 50
    elif unit <= 300:
        return 100 * 1.5 + 100 * 2.5 + (unit - 200) * 4 + 75
    elif unit <= 350:
        return 100 * 1.5 + 100 * 2.5 + 100 * 4 + (unit - 300) * 5 + 100
    else:
        return 1500

if __name__=="__main__":
    import sys
    if len(sys.argv) == 2:
        try:
            unit = int(sys.argv[1])
            print(electricity_bill(unit))
        except:
            pass
    else:
        unit = int(input("How many units have the user consumed? (int value): "))
        print(electricity_bill(unit))
