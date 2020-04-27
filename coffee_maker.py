class CoffeeMaker:
  supplies = {"water" : 400, "milk" : 540, "coffee" : 120, "cups" : 9, "money" : 550}
  espresso = {"water" : 250, "milk" : 0, "coffee" : 16, "cups" : 1, "money" : 0}
  latte = {"water" : 350, "milk" : 75, "coffee" : 20, "cups" : 1, "money" : 0}
  cappuccino = {"water" : 200, "milk" : 100, "coffee" : 12, "cups" : 1, "money" : 0}
    
  def __init__(self, answer):
    self.answer = answer

  def remaining(self):
    water = self.supplies["water"]
    milk = self.supplies["milk"]
    coffee = self.supplies["coffee"]
    cups = self.supplies["cups"]
    money = self.supplies["money"]
    message_1 = "The coffee machine has:\n{} of water\n{} of milk\n{} of coffee beans\n{} of disposable cups \n{} of money".format(water,milk,coffee,cups,money)
    print(message_1)




  def fill(self):
    print("Write how many ml of water do you want to add:")
    add_water = input()
    print("Write how many ml of milk do you want to add:")
    add_milk = input()
    print("Write how many grams of coffee beans do you want to add:")
    add_beans = input()
    print("Write how many disposable cups of coffee do you want to add:")
    add_cups = input()
    self.supplies["water"] += int(add_water)
    self.supplies["milk"] += int(add_milk)
    self.supplies["coffee"] += int(add_beans)
    self.supplies["cups"] += int(add_cups)

    
  def take(self):
    print("I gave you {}".format(self.supplies["money"]))
    self.supplies["money"] = 0


  def buy(self):
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    user_buy = input()
    if user_buy == "back":
      return None
    elif user_buy == "1":
      for supply in self.supplies.keys():
        if self.supplies[supply] < self.espresso[supply]:
          print("Sorry, not enough {}".format(supply))
          break
      else:
        print("I have enough resources, making you a coffee!")
        self.supplies["water"] -= self.espresso["water"]
        self.supplies["milk"] -= self.espresso["milk"]
        self.supplies["coffee"] -= self.espresso["coffee"]
        self.supplies["cups"] -= self.espresso["cups"]
        self.supplies["money"] += 4
    elif user_buy == "2":
      for supply in self.supplies.keys():
        if self.supplies[supply] < self.latte[supply]:
          print("Sorry, not enough {}".format(supply))
          break
      else:
        print("I have enough resources, making you a coffee!")
        self.supplies["water"] -= self.latte["water"]
        self.supplies["milk"] -= self.latte["milk"]
        self.supplies["coffee"] -= self.latte["coffee"]
        self.supplies["cups"] -= self.latte["cups"]
        self.supplies["money"] += 7
    elif user_buy == "3":
      for supply in self.supplies.keys():
        if self.supplies[supply] < self.cappuccino[supply]:
          print("Sorry, not enough {}".format(supply))
          break
      else:
        print("I have enough resources, making you a coffee!")
        self.supplies["water"] -= self.cappuccino["water"]
        self.supplies["milk"] -= self.cappuccino["milk"]
        self.supplies["coffee"] -= self.cappuccino["coffee"]
        self.supplies["cups"] -= self.cappuccino["cups"]
        self.supplies["money"] += 6

while True:
  print("Write action (buy, fill, take, remaining, exit):")
  user_input = input()
  user = CoffeeMaker(user_input)
  if user_input == "exit":
    break
  if user_input == "remaining":
    print()        
    user.remaining()
    print()
  elif user_input == "fill":
    print()
    user.fill()
    print()
  elif user_input == "take":
    print()
    user.take()
    print()
  elif user_input == "buy":
    print()
    user.buy()
    print()
