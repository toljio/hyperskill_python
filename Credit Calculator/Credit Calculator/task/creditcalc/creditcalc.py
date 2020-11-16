from math import ceil, log, pow
import argparse


def nominal_rate(r):
    return r / (12 * 100)


def annuity_payment(p, r, n):
    i = nominal_rate(r)
    return ceil(p * (i * pow(1 + i, n) / (pow(1 + i, n) - 1)))


def credit_principal(a, r, n):
    i = nominal_rate(r)
    return ceil(a / (i * pow(1 + i, n) / (pow(1 + i, n) - 1)))


def period_count(a, r, p):
    i = nominal_rate(r)
    return ceil(log(a / (a - i * p), 1 + i))


def print_months(m):
    y = m // 12
    m %= 12
    if m and y:
        print(f'You need {y} years and {m} months to repay this credit!')
    elif m:
        print(f'You need {m} months to repay this credit!')
    elif y:
        print(f'You need {y} years to repay this credit!')


def diff_payment(p, n, r, m):
    i = nominal_rate(r)
    return ceil(p / n + i * (p - p * (m - 1) / n))


def print_overpayment(a, n, p):
    o = a * n - p
    print("Overpayment =", o)


parser = argparse.ArgumentParser()
parser.add_argument("--type", help="type of payments (annuity or diff)", choices=["annuity", "diff"])
parser.add_argument("--payment", type=float, help="monthly payment")
parser.add_argument("--principal", type=float, help="used for calculations of both types of payment.")
parser.add_argument("--periods", type=float, help="the number of months")
parser.add_argument("--interest", type=float, help="interest payment")
args = parser.parse_args()
if args.type == "diff" and args.periods and args.interest and args.principal:
    overpayment = 0
    for j in range(1, int(args.periods) + 1):
        d = diff_payment(args.principal, args.periods, args.interest, j)
        print(f'Month {j}: paid out {d}')
        overpayment += d
    overpayment -= args.principal
    print("Overpayment =", overpayment)
elif args.type == "annuity":
    if args.periods and args.interest and args.principal:
        a = annuity_payment(args.principal, args.interest, args.periods)
        print(f'Your annuity payment {a}!')
        print_overpayment(a, args.periods, args.principal)
    elif args.periods and args.interest and args.payment:
        p = credit_principal(args.payment, args.interest, args.periods)
        print(f'Your credit principal {p}!')
        print_overpayment(args.payment, args.periods, p)
    elif args.principal and args.interest and args.payment:
        n = period_count(args.payment, args.interest, args.principal)
        print_months(n)
        print_overpayment(args.payment, n, args.principal)
    else:
        print("Incorrect parameters")
else:
    print("Incorrect parameters")
