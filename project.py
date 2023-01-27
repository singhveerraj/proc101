import random

response = "y"
while response == "y":
    
    number = random.randint(1,6)

    if number == 1:
        print("[-----]") 
        print("[     ]") 
        print("[  0  ]") 
        print("[     ]") 
        print("[-----]")
    if number == 2:
        print("[-----]") 
        print("[    0]") 
        print("[     ]") 
        print("[0    ]") 
        print("[-----]")
    if number == 3:
        print("[-----]") 
        print("[    0]") 
        print("[  0  ]") 
        print("[0    ]") 
        print("[-----]")
    if number == 4:
        print("[-----]") 
        print("[0   0]") 
        print("[     ]") 
        print("[0   0]") 
        print("[-----]")
    if number == 5:
        print("[-----]") 
        print("[0   0]") 
        print("[  0  ]") 
        print("[0   0]") 
        print("[-----]")
    elif number == 4:
        print("[-----]") 
        print("[0   0]") 
        print("[0   0]") 
        print("[0   0]") 
        print("[-----]")

    response=input("press y to roll again and n to exit:") 
    print("\n")
    if response == 'n':
        break