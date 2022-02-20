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
    monthly_payment = balance / 12
    if monthly_payment % 10 != 0:
        monthly_payment -= monthly_payment % 10

    updated_balance = balance
    while updated_balance >= 0:
        updated_balance = balance
        months_needed = 0
        monthly_payment += 10

        while months_needed < 12:
            months_needed += 1

            monthly_interest_rate_payment = updated_balance * (interest_rate / 12)
            updated_balance += monthly_interest_rate_payment - monthly_payment

            if updated_balance <= 0:
                break

    return monthly_payment, months_needed, updated_balance


def main_second_task():
    balance_on_the_credit_card = int(input("Balance on the credit card: "))
    interest_rate = float(input("Interest rate: "))

    minimum_monthly_payment, months_needed, updated_balance = \
        paying_debt_off_in_a_year(balance_on_the_credit_card, interest_rate)

    print("RESULT")
    print("Monthly payment to pay off debt in 1 year: ", minimum_monthly_payment)
    print("Number of months needed: ", months_needed)
    print("Balance: ", round(updated_balance, 2))


def main():
    # main_first_task()
    main_second_task()


if __name__ == "__main__":
    main()
