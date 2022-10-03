from itertools import groupby
from ascii import logo


def all_equal(iterable):
    """Returns True if all the elements are equal to each other"""
    g = groupby(iterable)
    return next(g, True) and not next(g, False)


def valid_inputs(cell_no, cell_value):
    if cell_no not in ("A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"):
        print("\nInvalid Cell Number")
        return False
    elif cells[cell_no.lower()] in ["X", "O"]:
        print("\nCell already has a value")
        return False
    elif cell_value not in ("X", "O"):
        print("\nInvalid Input, Value must be X or O")
        return False
    else:
        return True


def check_cells():
    r1 = [cells["a1"], cells["a2"], cells["a3"]]
    r2 = [cells["b1"], cells["b2"], cells["b3"]]
    r3 = [cells["c1"], cells["c2"], cells["c3"]]
    c1 = [cells["a1"], cells["b1"], cells["c1"]]
    c2 = [cells["a2"], cells["b2"], cells["c2"]]
    c3 = [cells["a3"], cells["b3"], cells["c3"]]
    d1 = [cells["a1"], cells["b2"], cells["c3"]]
    d2 = [cells["c1"], cells["b2"], cells["a3"]]

    items_list = [r1, r2, r3, c1, c2, c3, d1, d2]

    for items in items_list:
        if all_equal(items) and " " not in items:
            print(f"\n {items[0][0]} wins!🔥")
            return True


def cells_not_filled():
    for key in cells:
        if cells[key] not in ("X", "O"):
            return True


def tic_tac_toe():
    print(f"""              
    {cells["a1"]} | {cells["a2"]} | {cells["a3"]}
   -----------
    {cells["b1"]} | {cells["b2"]} | {cells["b3"]}
   ------------
    {cells["c1"]} | {cells["c2"]} | {cells["c3"]}    
        
        """
    )


def start_game():
    game_is_on = True
    print("""
    Cells Guide
    
    A1 | A2 | A3
   -------------
    B1 | B2 | B3
   -------------
    C1 | C2 | C3  
    
    """)
    while game_is_on:

        tic_tac_toe()
        try:
            user_input = input("Enter the name of the cell and value e.g A1=X: ").replace(" ", "").split("=")
            cell = user_input[0].upper()
            value = user_input[1].upper()
        except IndexError:
            print("Wrong Input")
        else:
            if valid_inputs(cell, value):
                cells[cell.lower()] = value
                if check_cells():
                    tic_tac_toe()
                    game_is_on = False
                elif not cells_not_filled():
                    game_is_on = False
                    print(tic_tac_toe)
                    print(f"Draw! 🤝")


cells = {
    "a1": " ",
    "a2": " ",
    "a3": " ",
    "b1": " ",
    "b2": " ",
    "b3": " ",
    "c1": " ",
    "c2": " ",
    "c3": " ",
}

print(logo)
start_game()

