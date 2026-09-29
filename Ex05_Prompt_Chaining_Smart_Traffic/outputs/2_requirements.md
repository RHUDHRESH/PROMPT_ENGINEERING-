# Step 2 - Requirements

*Chained from `1_problem.md` (its goals and metrics become the requirements below).*

| ID | Requirement | Priority (MoSCoW) | Test method |
|---|---|---|---|
| FR1 | The system shall read the queue length of each of the four approaches (N, E, S, W). | Must | Unit test with a dict of four queue counts; reject other key sets |
| FR2 | Green time shall be proportional to queue length (seconds-per-vehicle factor). | Must | Unit test: green_time(15) = 30 s with factor 2 |
| FR3 | Green time shall be clamped to [min_green, max_green]. | Must | Unit test at 0, 100 vehicles |
| FR4 | An emergency vehicle on an approach shall pre-empt normal selection and receive the next green. | Must | Unit test: emergency="W" beats N with 50 queued |
| FR5 | An approach with waiting vehicles skipped max_wait_cycles times shall be served before the longest-queue rule applies (emergency still wins). | Must | Unit test: run 5 cycles, small queue is served |
| FR6 | Otherwise the approach with the longest queue shall be served. | Must | Unit test |
| FR7 | Invalid input (missing directions, negative queue, unknown emergency direction, bad bounds) shall raise an error. | Must | Unit tests expecting ValueError |
| FR8 | A dashboard shall show queues, waits and emergency events. | Should | Manual demo / integration test |
| NFR1 | A decision shall be computed in under 50 ms on edge hardware. | Must | Timing benchmark |
| NFR2 | Fail-safe: on sensor or controller failure, fall back to a fixed-time plan. | Must | Fault-injection test |
| NFR3 | Controller core shall use only the Python standard library. | Should | Dependency check |
| NFR4 | Decision logic shall be deterministic (ties resolved in a fixed order). | Should | Repeat-run test |
| NFR5 | Sensor and cloud links shall be authenticated and encrypted. | Should | Security review |
| FR9 | Machine-learning demand forecasting. | Could | Offline evaluation |
| FR10 | Pedestrian phases and multi-intersection coordination. | Won't (this release) | n/a |
