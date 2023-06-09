total_price_without_taxes = 0
special_customer = False

while True:
    command = input()

    if command == "regular" or command == "special":
        if command == "special":
            special_customer = True
        break

    given_price = float(command)

    if given_price < 0:
        print("Invalid price!")
    else:
        total_price_without_taxes += given_price

if total_price_without_taxes:
    taxes = total_price_without_taxes * 0.20
    total_price_with_taxes = total_price_without_taxes + taxes
    if special_customer:
        total_price_with_taxes *= 0.90
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price_without_taxes:.2f}$")
    print(f"Taxes: {taxes:.2f}$\n-----------")  # \n - new line
    print(f"Total price: {total_price_with_taxes:.2f}$")
else:
    print("Invalid order!")


# command = input()

# total_price_without_taxes = 0
# total_amount_of_taxes = 0
# total_price_with_taxes = 0

# while True:
#     if command == "special" or command == "regular":
#         if total_price_without_taxes <= 0:
#             print("Invalid order!")
#             break
#         if command == "special":
#             total_price_with_taxes -= total_price_with_taxes * 0.10
#         print(f"Congratulations you've just bought a new computer!\n"
#               f"Price without taxes: {total_price_without_taxes:.2f}$\n"
#               f"Taxes: {total_amount_of_taxes:.2f}$\n"
#               f"-----------\n"
#               f"Total price: {total_price_with_taxes:.2f}$")
#         break

#     given_price = float(command)
#     if given_price < 0:
#         print("Invalid price!")
#     elif given_price == 0:
#         print("Invalid order!")
#     else:
#         total_price_without_taxes += given_price
#         total_amount_of_taxes = total_price_without_taxes * 0.20
#         total_price_with_taxes = total_price_without_taxes + total_amount_of_taxes
#     command = input()
