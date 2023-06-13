from os import system
def welcome(dictionary):
    for item in dictionary:
        if item == "money":
            break
        if dictionary[item] < 150:
            num = dictionary[item]
            if item == "coffee":
                unity = "g"
            else:
                unity = "mL"
            print(f"There's just {num}{unity} of {item}!")   
    resposta = input("""
    What would you like?
    Espresso     $ 2.40 80 mL
    Latte        $ 3.45 300 mL
    Cappuccino   $ 2.80 100 mL
    """).title()
    return resposta
def not_enough(quantity, object):
    if object == "coffee":
        unity = "g"
    else:
        unity = "mL"
    vontade = input(f"Sorry, there is not enough {object}, only {quantity} {unity}. Type 'refill' to refill the {object}: ").lower()
    if vontade == "refill":
        colocado = input(f"How much {object} will you put on the machine? ").lower()
        new_colocado = "" 
        for char in colocado:
            if char != "m" and char !="l" and char != "g" and char != " ":
                new_colocado += char
        new_colocado = int(new_colocado)
        if "l" in colocado and ("m" not in colocado):
            new_colocado  = new_colocado * 1000
        quantity += new_colocado
    return quantity
            
def insert_cash(missing):
    if missing == 0:
        print("Please, insert the coins")
    else:
        print(f"Please, insert {missing} dollars")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    cash = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    cash = 12 * 0.25 + 4 * 0.10 + 1 * 0.05 + 0 * 0.01
    cash = float("%.2f" %(cash))
    return cash

def check(answer, conteudo):
    falta = 0
    continuar = True
    if answer == "Espresso" or answer == "Latte" or answer == "Cappuccino":
        for item in conteudo["drinks"][answer]["ingredients"]:
            if conteudo[item] < conteudo["drinks"][answer]["ingredients"][item]:
                conteudo[item] = not_enough(conteudo[item], item)
                continuar = False
                break
        if continuar == True:
            for item in conteudo["drinks"][answer]["ingredients"]:
                conteudo[item] -= conteudo["drinks"][answer]["ingredients"][item]
            money = insert_cash(falta)
            price = conteudo["drinks"][answer]["cost"]
            while money < price:              
                falta = price - money
                money += insert_cash(falta)
            conteudo["money"] += price
            if money == price:
                print(f"Here is your {answer}. Enjoy!☕")
            else:
                cash_back = money - price
                cash_back = "%.2f" %(cash_back)
                print(f"Here is your {cash_back} dollars in change and your {answer}. Enjoy!☕")
    elif answer == "Report":
        for item in conteudo:
            if item == "coffee":
                unidade = "g"
            elif item == "money":
                unidade = "$"
            elif item == "parar":
                break
            else:
                unidade = "mL"
            valor = conteudo[item]
            print(f"{item}: {valor} "+ unidade)
    elif answer == "Off":
        conteudo["parar"] = True
    return conteudo
        
content = {"milk": 500, "water": 500, "coffee": 700, "money": 0, "parar": False, 
"drinks": {
"Espresso": {"ingredients": {"water": 80, "coffee": 20,}, "cost": 2.4}, 
"Latte": {"ingredients": {"water": 100, "milk": 100, "coffee": 50,}, "cost": 3.45},
"Cappuccino": {"ingredients": {"water": 100, "milk": 20, "coffee": 20,}, "cost": 2.8}
}
}
while content["parar"] != True:
    content = check(welcome(content), content)
    input()
    system("cls")