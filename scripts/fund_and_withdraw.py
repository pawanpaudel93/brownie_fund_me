from brownie import FundMe
from .helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print("The current entrance fee is:", entrance_fee)
    print("Funding the contract with", entrance_fee, "Wei")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    print("Withdrawing the contract")
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
