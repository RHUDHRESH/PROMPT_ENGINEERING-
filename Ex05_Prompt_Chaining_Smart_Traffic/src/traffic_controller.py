"""Adaptive traffic-signal controller for a 4-way intersection (reference implementation)."""
from typing import Dict, Optional

DIRECTIONS = ("N", "E", "S", "W")


class TrafficController:
    def __init__(self, min_green: int = 10, max_green: int = 60,
                 seconds_per_vehicle: float = 2.0, max_wait_cycles: int = 3):
        if min_green <= 0 or max_green < min_green:
            raise ValueError("invalid green-time bounds")
        self.min_green = min_green
        self.max_green = max_green
        self.seconds_per_vehicle = seconds_per_vehicle
        self.max_wait_cycles = max_wait_cycles
        self._skipped = {d: 0 for d in DIRECTIONS}

    def green_time(self, queue_len: int) -> int:
        """Green seconds proportional to queue length, clamped to [min, max]."""
        if queue_len < 0:
            raise ValueError("queue length cannot be negative")
        return int(max(self.min_green, min(self.max_green, queue_len * self.seconds_per_vehicle)))

    def next_phase(self, queues: Dict[str, int], emergency: Optional[str] = None) -> str:
        """Pick the direction to serve next. Emergency > starved > longest queue."""
        if set(queues) != set(DIRECTIONS):
            raise ValueError("queues must have keys N, E, S, W")
        if emergency is not None:
            if emergency not in DIRECTIONS:
                raise ValueError("unknown emergency direction")
            return self._serve(emergency)
        starved = [d for d in DIRECTIONS if self._skipped[d] >= self.max_wait_cycles and queues[d] > 0]
        if starved:
            return self._serve(max(starved, key=lambda d: queues[d]))
        return self._serve(max(DIRECTIONS, key=lambda d: queues[d]))

    def _serve(self, direction: str) -> str:
        for d in DIRECTIONS:
            self._skipped[d] = 0 if d == direction else self._skipped[d] + 1
        return direction


if __name__ == "__main__":
    c = TrafficController()
    q = {"N": 12, "E": 3, "S": 8, "W": 1}
    d = c.next_phase(q)
    print(d, c.green_time(q[d]), "s")
