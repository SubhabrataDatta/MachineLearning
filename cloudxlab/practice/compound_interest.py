def compound_interest(principle, rate, years):
    x=principle
    if years==0:
        comp_interest=0
    else:
        for time in range(1,years+1):
            interest=(principle*rate*1)/100
            principle=principle+interest
            comp_interest=principle-x
    return comp_interest

print(compound_interest(100,5,2))