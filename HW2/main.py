from ps2_newton import evaluate_poly, compute_deriv


def main():
    # # 1 task
    # poly = (0.0, 0.0, 5.0, 9.3, 7.0)
    # x = int(input("x: "))
    #
    # poly_answer = evaluate_poly(poly, x)
    # print(poly_answer)

    # 2 task
    poly = (-2.0, -2.0, 17.5, 4.0, 1.0, -5.0)

    deriv_answer = compute_deriv(poly)
    print(deriv_answer)


if __name__ == "__main__":
    main()
