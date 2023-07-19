"""
Tic Tac Toe - Feld Analyse

Spieler X hat begonnen.

Gegeben ist eine 3x3 Matrix, die das Spielfeld repräsentiert.
Das Spielfeld ist gefüllt mit den zwei Farben der Spieler, also X und O sowie den leeren Feldern NONE.

Aufgabe:
-------------
Wir wollen in dieser Aufgabe einige Funktionen implementieren, die das Spielfeld überprüfen. 
Dazu gehört neben der fachlich richtigen Implementierung auch das Angeben der Datentypen (Type-Hints)

Wir gehen zu jeder Zeit von einem gültigen Spielfeld aus (zwei sieg-
reiche Spieler kann es zum Beispiel nicht geben)

0) Das Spielfeld:

board = [
        [X, X, O],
        [O, _, X],
        [O, X, _]
    ]

An den Feldern X und O haben die Spieler bereits gesetzt, die beiden _-Felder
sind noch ungenutzt.

Die Funktionen sollen ordentlich mit Type-Hints, Rückgabewerten und Doc-Strings beschrieben werden.

Folgende Funktionen sind zu implementieren:

------------------------------------------------------------------------------
1) player()

Welcher Spieler ist als nächstes am Zug? Wir gehen davon aus, dass
immer Spieler mit der Farbe X das Spiel begonnen hat. Implementiere diese
Funktion so, dass der aktuelle Spielstand erkannt und der nächste
Spieler berechnet wird.

Beispiel:

board = [
    [X, O, _],
    [_, _, _],
    [_, _, _]
]
Spieler X darf den nächsten Zug ausführen.


------------------------------------------------------------------------------
2) actions()
Erzeuge ein Set von allen freien Feldern der Matrix. in Form von Tupeln, die
Reihe und Spalte angegeben. Beispiel:

board = [
    [X, X, O],
    [O, _, _],
    [O, X, _]
]

Result: set{(1, 1), (1, 2), {2, 2}}

------------------------------------------------------------------------------

3) winner()

Prüft, ob es einen Gewinner gibt.
Gewinner ist die Farbe, der drei Steine in einer Reihe hat: Horizontal, Vertikal
oder diagonal

board = [
    [X, O, O],
    [X, _, _],
    [X, _, _]
]

X hat gewonnen. X wird zurückgegeben.

4) terminal()

Prüft, ob sich das Board im Endzustand befindet. Entweder,
winner() ist True
oder das Board voll belegt ist und keine Züge mehr möglich sind.

board = [
    [X, O, O],
    [X, _, _],
    [X, _, _]
]

Gibt true zurück, weil winner() True ist (X)

board = [
    [X, O, _],
    [_, _, _],
    [_, _, _]
]

gibt False zurück, weil weder winner() True noch Board voll.

"""

X = "X"
O = "O"
_ = None



def player(board: list) -> str:
    """
    Gibt die/den nächsten Spieler*in zurück 
    """
    el_count = 0
    for el in board:
        el_count += el.count(X)
        el_count += el.count(O)
    if el_count == 0:
        return X
    elif el_count % 2 == 0:
        return X  # gerade
    elif el_count % 2 != 0:
        return O  # ungerade


def actions(board: list) -> set:
    """
    Returned ein Set aller möglichen freien Felder in Form von Tupeln.
    Gibt ein leeres Set zurück, wenn keine freien Felder mehr existieren.
    """

    possible_actions = set()
    for row in range(len(board)):
        for column in range(len(board)):
            if not board[row][column]:
                possible_actions.add((row, column))
    return possible_actions

    # row = -1
    # for el in board:
    #     row += 1 
    #     #print("row:", row)
    #     column = -1
    #     for col in el:
    #         column += 1
    #         #print("col:", column, col)
    #         if col is None:
    #             possible_actions.add((row, column))


def winner(board: list) -> str:
    """
    Return winner, falls existiert. Prüft dazu alle Spalten, Reihen und die zwei
    Hauptdiagonalen. Ansonsten return None
    """

    board_new = board.copy()
    for el in actions(board_new):
        board_new[el[0]].insert(el[1], "Ersatz")
        board_new[el[0]].remove(None)
    
    boardT = [x for x in zip(*board_new)]
    board_diag = [row[i] for i, row in enumerate(board_new)]
    board_diag_alt = [row[i] for i, row in enumerate(reversed(board_new))]
    board_comb = board + [list(board_diag)] + [list(board_diag_alt)] + boardT

    for row in board_comb:
        if win_check(row) is not None:
            return win_check(row)


def win_check(row: list) -> str:
    if row.count(X) == 3:
        return X
    elif row.count(O) == 3:
        return O
    else:
        return None


def terminal(board: list) -> bool:
    """
    Gibt True zurück, wenn das Board voll ist oder ein Gewinner existiert.
    """
    if winner(board):
        return True
    elif not winner(board):
        el_count = 0
        for el in board:
            el_count += el.count(X)
            el_count += el.count(O)
        if el.count == 9:
            return True
    return False


if __name__ == "__main__":
    board = [
        [X, X, O],
        [O, _, X],
        [O, X, _]
    ]

    print("Nächsteer Zug: ", player(board))  # welcher Spiele ist als nächstes am Zug?
    print("Mögliche Züge: ", actions(board))  # gib mir eine Liste aller möglichen Spielzüge
    print("Gewinner: ", winner(board))  # gibt es einen Gewinner? Wer ist es?
    print("Spiel beendet?: ", terminal(board))  # ist das Spiel zu Ende, weil Gewinner oder alles voll?


# 1. Spieler ermitteln
# 2. Spielzüge ermitteln (tuple erzeugen von NONE werten in matrix)
# 3. Gewinner ermitteln: 
#       extra funktion die prüft ob row count(O o. X)0 == 3
#       transponierte und diagonale von Matrix check mit extra funktion
# 4. Boolsche werte in terminal erzeugen für Bedingungen des Spielendes
