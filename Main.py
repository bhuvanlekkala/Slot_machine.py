import random

MAX_NUMBER_OF_LINES = 3
MAX_BET = 100
MIN_BET = 1

Rows = 3
Columns = 3

symbol_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8,
}

symbol_value = {
    "A":5,
    "B":4,
    "C":3,
    "D":2,
}

def check_winnings(columns, lines,bet, values):
    total_winnings = 0
    for line in range(lines):
        symbol=columns[line][0]
        for column in columns[line]:
            if column != symbol:
                break
        else:
            total_winnings += bet * values[symbol]
    return total_winnings

def check_line(columns, line, bet, values):
    symbol = columns[line[0]][0]
    for column_index, row_index in line:
        if columns[column_index][row_index] != symbol:
            return 0
    return bet * values[symbol]

def get_slot_machine_spin(rows, Columns, symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns=[]
    for _ in range(Columns):
        column=[]
        current_symbols=all_symbols[:]
        for _ in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine_spin(columns):
    for row  in range(len(columns[0])):
                for i, column in enumerate(columns):
                    if i != len(columns) - 1:
                        print(column[row], end=" | ")
                    else:
                        print(column[row], end=" ")      
                
                print()

def deposit():
    while True:
        amount = input("How much amount would you like to deposit? $ ")
        try:
            amount = float(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        except ValueError:
            print("Please enter a valid amount.")
    return amount

def get_number_of_lines():
    while True:
        number_of_lines = input(
            "How many lines would you like to play(1-" + str(MAX_NUMBER_OF_LINES) + ")?")
        try:
            number_of_lines = int(number_of_lines)
            if number_of_lines > 0 and number_of_lines <= MAX_NUMBER_OF_LINES:
                break
            else:
                print("Number of lines must be between 1 and " + str(MAX_NUMBER_OF_LINES) + ".")
        except ValueError:
            print("Please enter a valid number.")
    return number_of_lines

def get_bet():
    while True:
        amount = input("How much would you like to bet? $")
        try:
            amount = float(amount)
            if MIN_BET<= amount <= MAX_BET:
                break
            else:
                print(f"Bet amount must be between ${MIN_BET} - ${MAX_BET}.")
        except ValueError:
            print("Please enter a valid number.")
    return amount

def spin(balance):
    number_of_lines= get_number_of_lines()
    while True:
        bet_amount = get_bet()
        total_bet_amount = number_of_lines * bet_amount
        if total_bet_amount > balance:
            print(f"You don't have enough balance to place this bet. Your balance is ${balance}.")  
        else:
            break
    print(f"you are betting ${bet_amount} on {number_of_lines} lines.Total bet amount is ${total_bet_amount}.")

    slots= get_slot_machine_spin(Rows, Columns, symbol_count)
    print_slot_machine_spin(slots)
    winnings = check_winnings(slots, number_of_lines, bet_amount, symbol_value)
    print(f"You won ${winnings}.")
    balance += winnings - total_bet_amount
    print(f"Your balance is ${balance}.")
    return balance


def main():
    balance = deposit()
    while True:
        balance = spin(balance)
        if balance <= 0:
            print("You don't have enough balance to play.")
            break
        play_again = input("Would you like to play again? (y/n) ")
        if play_again.lower() != 'y':
            break
    print(f"Your final balance is ${balance}.")
    print("Thanks for playing!")

    
    
main()
