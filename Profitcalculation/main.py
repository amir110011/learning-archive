# Calculate the final profit by considering the leverage
print("If you want to give the market profit and leverage to calculate the final profit, press 1.")
print("If you want to calculate your final profit based on risk rewerd, press 2.")

menu = int(input("coice a item: "))
if(menu == 1):
    l = float(input("enter a levrage: "))
    m = float(input("market changes: "))

    profit = m*l
    print("your final profit is " + str(profit))

elif(menu == 2):
    price = float(input("enter your entry price: "))
    target = float(input("enter your target: "))
    stoploss = float(input("enter your stop loss: "))
    levrage = float(input("enter a levrage: "))

    print("you are import this data: entry price= {0} , target= {1},\n stoploss= {2}, levrage= {3}\n".format(
        price, target, stoploss, levrage))

    risk = price - stoploss
    rewerd = price - target
    rr = round(((risk/rewerd) * 100), 2)

    def profitrate(a):
        b = ((price - a)/price)*100
        return b*levrage
    finaltarget = profitrate(target)
    finalstoploss = profitrate(stoploss)

    print("your risk is {} and your rewerd {} and \n risk/rewerd rate is {} %".format(risk, rewerd, rr))
    print("your target with levrage is {} % and your stop loss with levrage {} %".format(
        finaltarget, finalstoploss))


input("ernter any key...")
