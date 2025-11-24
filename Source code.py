def greet(name):
    print(f"Welcome to our reastaurant, {name}!")

def restaurant():
    menu = {
    'Coffee':80,
    'Pizza':120,
    'Pasta':130,
    'Burger':70,
    'Maggie':40
     }
    
    
    print("Here's the menu: ")
    print(" Burger 🍔 = Rs70 \n Coffee ☕ = Rs80 \n Maggie 🍜 = Rs40 \n Pasta 🍝= Rs130 \n Pizza 🍕= Rs120")
    total=0
    
    order=input("Please select your first item: ").title()
    if order in menu:
        print ("Great",order,"selected.✅ ")
        while True:
            try:
                quantity= int(input("please select the quantity of your item: "))
                if quantity>0:
                    break
                else:
                    print("Quantity must be a positive number.")
            except ValueError:
                print("Invalid input. Please enter a whole number for the quantity.")
        total += menu[order] * quantity
    else:
        print("Invalid choice!❌ ")
   
        
    while True:
        again=input("Do you want to order something else: (Yes/No)").title()
        if again != "Yes":
            break
        
        order = input("Please select your next item: ").title()
        if order in menu:
            print("Great", order, "selected.")
            quantity= int(input("please select the quantity of your item: "))
            total += menu[order] * quantity
        else:
            print("Choice not available")

    discount_amount = 0
    original_total = total
    valid_code = "CODE10" 
    discount_percentage = 0.10 
    
    discount_code = input("\nHave a discount code? Enter it here or press Enter to skip: ").upper()
    
    if discount_code == valid_code:
        discount_amount = total * discount_percentage
        total -= discount_amount # Apply the discount
        
        print(f"✅ Discount Code **{valid_code}** accepted! -Rs{discount_amount:.2f} applied.")
    elif discount_code: 

        print("❌ Invalid discount code. No discount applied.")
    

    # --- Final Bill Display ---
    print("\n--- 🧾 FINAL BILL 🧾 ---")
    
    # You can show the detailed receipt here!
    
    print("--------------------------")
    print(f"Subtotal: Rs{original_total:.2f}")

    if discount_amount > 0:
        print(f"Discount: -Rs{discount_amount:.2f}")
        print("--------------------------")

    print(f"**💰 FINAL AMOUNT DUE: Rs.{total:.2f}**")
    
    print("\n✨ Thank you for dining with us! ✨")
    print("We hope you enjoyed your meal 😋")
    print("Please visit again soon! 🍽️")
    print("💬 Got feedback? We'd love to hear from you.")
    print("⭐ Rate us from 1 to 5 stars before you go! ⭐")

user_name=input("Enter your name: ")
greet(user_name)
restaurant() 
