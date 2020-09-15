import pprint as pp


class Flight:
    def __init__(self, number, aircraft):
        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}'")
        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code '{number}'")
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f'Invalid Route number: {number}')

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()

    def allocate_seat(self, seat, passenger):
        """Allocation of seat to a passenger
        Args:
            seat : a seat designator such as '12a'.
            passenger : Passenger name e.g. 'Jim Lahey'.

            Raises:
                ValueError: Error raised if seat already taken
        """
        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError(f'Seat {seat} is already occupied')

        self._seating[row][letter] = passenger

    def _parse_seat(self, seat):
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError(f'Invalid seat letter {letter}')

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f'Invalid seat row {row_text}')

        if row not in rows:
            raise ValueError(f'Invalid row number {row}')

        return row, letter

    def relocate_passenger(self, from_seat, to_seat):
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError(f'No passenger to relocate in {from_seat}')

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError(f'seat is already occupied')

        self._seating[to_row][to_letter] = self._seating[from_row][to_letter]
        self._seating[from_row][to_letter] = None

    def available_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self._seating
                   if row is not None)

    def boarding_pass(self, card_printer):
        for passenger, seat in sorted(self.passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())

    def passenger_seats(self):
        """Searches all seats for occupants"""
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, f"{row}{letter}")


class Aircraft:
    def __init__(self, reg, model, num_rows, num_seats):
        self._reg = reg
        self._model = model
        self._num_rows = num_rows
        self._num_seats = num_seats

    def reg(self):
        return self._reg

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self._num_rows + 1),
                "ABCDEFGHJK"[:self._num_seats])


def create_flight():
    plane = Aircraft('2020-D-12', 'Boeing227', num_rows=22, num_seats=6)
    a = Flight('GB2277', plane)
    a.allocate_seat('21B', 'John')
    a.allocate_seat('11A', 'Henry')
    a.relocate_passenger('21B', '11B')
    a.boarding_pass(card_printer)


def card_printer(passenger, seat, flight_number, aircraft):
    output = f" | Passenger - {passenger}" \
             f" | Seat - {seat}" \
             f" | Flight - {flight_number}" \
             f" | Aircraft - {aircraft}"
    banner = "+" + "-" * (len(output) - 2) + "+"
    border = "|" + "-" * (len(output) - 2) + "|"
    lines = [banner, border, output, border, banner]
    card = "\n".join(lines)
    print(card)
    print()

