# 1 task
def calculate_paying_off_credit_card_debt(balance, monthly_payment_rate, interest_rate):
    minimum_monthly_payment = balance * monthly_payment_rate
    interest_paid = interest_rate / 12.0 * balance

    principal_paid = minimum_monthly_payment - interest_paid
    remaining_balance = balance - principal_paid

    return minimum_monthly_payment, remaining_balance, principal_paid


def main_first_task():
    balance = int(input("Balance: "))
    monthly_payment_rate = float(input("Monthly payment rate: "))
    interest_rate = float(input("Interest rate: "))

    remaining_balance = balance
    total_amount_paid = 0

    for i in range(1, 13):
        minimum_monthly_payment, remaining_balance, principal_paid = \
            calculate_paying_off_credit_card_debt(remaining_balance, monthly_payment_rate, interest_rate)

        minimum_monthly_payment = round(minimum_monthly_payment, 2)
        remaining_balance = round(remaining_balance, 2)
        principal_paid = round(principal_paid, 2)

        total_amount_paid += minimum_monthly_payment

        print("\nMonth: ", i)
        print("Minimum monthly payment: ", minimum_monthly_payment)
        print("Remaining balance: ", remaining_balance)
        print("Principal paid: ", principal_paid)

    print("\nRESULT")
    print("Total amount paid: ", round(total_amount_paid, 2))


# 2 task
def paying_debt_off_in_a_year(balance, interest_rate):
    monthly_interest_rate = interest_rate / 12.0

    approx_payment = balance / 12
    remainder = approx_payment % 10
    monthly_payment = approx_payment - remainder

    quantity_of_month = 1
    updated_balance = balance

    # while True:
    #
    #
    #     while quantity_of_month <= 12:
    #
    #         quantity_of_month += 1
    #
    # monthly_payment += 10
    #
    #     updated_balance = updated_balance * (1 + monthly_interest_rate) - monthly_payment
    #
    #     updated_balance -= monthly_payment

    # while quantity_of_month <= 12:
    #     updated_balance = updated_balance * (1 + monthly_interest_rate)
    #
    #     if minimum_monthly_payment * quantity_of_month - updated_balance >= 0:
    #         break
    #     else:
    #
    #
    #     updated_balance = updated_balance * (1 + monthly_interest_rate) - minimum_monthly_payment
    #
    #     quantity_of_month += 1
    #
    #
    # print(updated_balance)
    # print(quantity_of_month)


def main_second_task():
    balance_on_the_credit_card = int(input("Balance on the credit card: "))
    interest_rate = float(input("Interest rate: "))

    paying_debt_off_in_a_year(balance_on_the_credit_card, interest_rate)


def main():
    # main_first_task()
    main_second_task()


if __name__ == "__main__":
    main()
