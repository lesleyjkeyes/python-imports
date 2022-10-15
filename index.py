from appliances import DishWasher, Washer, Dryer, Refrigerator, CoffeeMaker, CanOpener

whirlpool_dishwasher = DishWasher("black")
whirlpool_dishwasher.wash_dishes()

samsung_washer = Washer("red")
samsung_dryer = Dryer("red", "gas")

lg_fridge = Refrigerator("stainless")
lg_fridge.make_ice()

mr_coffee = CoffeeMaker("white")
mr_coffee.make_coffee()

small_can_opener = CanOpener("black")
small_can_opener.open_can()
