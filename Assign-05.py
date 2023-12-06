# importing from constants
import constants


def sales(check_out):
    # purchasing something in Prince Edward Island
    subtotal = check_out
    tax = constants.HST_PEI_TAX * subtotal
    total = round(subtotal + tax, 2)
    # printing total
    print(f"Prince Edward Island: {total}")

    # purchasing something in Ontario
    subtotal = check_out
    tax = constants.HST_ONTARIO_TAX * subtotal
    total = round(subtotal + tax, 2)
    # printing total
    print(f"Ontario: {total}")

    # purchasing something in Alberta
    subtotal = check_out
    tax = constants.GST_ALBERTA_TAX * subtotal
    total = round(subtotal + tax, 2)
    # printing total
    print(f"Alberta: {total}")

    # purchasing something in British Columbia
    subtotal = check_out
    tax = (constants.GST_BC_TAX + constants.PST_BC_TAX) * subtotal
    total = round(subtotal + tax, 2)
    # printing total
    print(f"British Columbia: {total}")

    # purchasing something in Manitoba
    subtotal = check_out
    tax = (constants.GST_MANITOBA_TAX + constants.PST_MANITOBA_TAX) * subtotal
    total = round(subtotal + tax, 2)
    # printing total
    print(f"Manitoba: {total}")

    # purchasing something in New Brunswick
    subtotal = check_out
    tax = constants.HST_NB_TAX * subtotal
    total = round(subtotal + tax, 2)
    # printing total
    print(f"New Brunswick: {total}")

    # purchasing something in NewFoundland and Labrador
    subtotal = check_out
    tax = constants.HST_NL_TAX * subtotal
    total = round(subtotal + tax, 2)
    # printing total
    print(f"NewFoundLand and Labrador: {total}")

    # purchasing something in NorthWest Territories
    subtotal = check_out
    tax = constants.GST_NWT_TAX * subtotal
    total = round(subtotal + tax, 2)
    # printing total
    print(f"Northwest Territories: {total}")

    # purchasing something in Nova Scotia
    subtotal = check_out
    tax = constants.HST_NS_TAX * subtotal
    total = round(subtotal + tax, 2)
    # printing total
    print(f"Nova Scotia: {total}")

    # purchasing something in Nunavut
    subtotal = check_out
    tax = constants.GST_NVT_TAX * subtotal
    total = round(subtotal + tax, 2)
    # printing total
    print(f"Nunavut: {total}")

    # purchasing something in Quebec
    subtotal = check_out
    tax = (constants.GST_QUEBEC_TAX + constants.QST_QUEBEC_TAX) * subtotal
    total = round(subtotal + tax, 2)
    # printing total
    print(f"Quebec: {total}")

    # purchasing something in Saskatchewan
    subtotal = check_out
    tax = (constants.GST_SASK_TAX + constants.PST_SASK_TAX) * subtotal
    total = round(subtotal + tax, 2)
    # printing total
    print(f"Saskatchewan: {total}")

    # purchasing something in Yukon
    subtotal = check_out
    tax = constants.GST_YK_TAX * subtotal
    total = round(subtotal + tax, 2)
    # printing total
    print(f"Yukon: {total}")


def main():
    # telling you what the code is going to do
    print("What are the prices of subtotal in all 13 provinces and territories ")

    # ask price for item
    check_out_str = input("item price: ")

    try:
        # casting to float
        check_out = float(check_out_str)
    except ValueError:
        # if can't cast to float
        print(f"{check_out_str} is an in correct input")
    else:
        # check_out is less than or equal to 0 this will print
        if not check_out >= 0:
            print("STOP try to steal from here")
            print("That price is not real please enter a real price")
        else:
            # calling function
            sales(check_out)


if __name__ == "__main__":
    main()
