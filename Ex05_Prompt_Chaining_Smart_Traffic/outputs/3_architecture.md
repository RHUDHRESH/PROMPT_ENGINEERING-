# Step 3 - Architecture

*Chained from `2_requirements.md` (FR1-FR8, NFR1-NFR5).*

## Components
| Component | Responsibility | Requirements |
|---|---|---|
| Sensors (loop detectors or camera + vehicle counter) | Report queue length per approach every cycle | FR1 |
| Emergency-vehicle detector (siren/RF preemption receiver) | Report which approach an emergency vehicle is on | FR4 |
| Edge controller (roadside unit) | Runs the decision engine locally; owns the safety fallback | NFR1, NFR2 |
| Decision engine (`TrafficController`) | `next_phase(queues, emergency)` and `green_time(queue_len)` | FR2-FR7 |
| Signal actuators | Convert the chosen direction and green time into signal states with safe amber/all-red intervals | FR2, NFR2 |
| Cloud dashboard | Stores metrics, shows queues, waits, emergency events | FR8 |

## Data flows
1. Sensors -> edge controller: `{N,E,S,W}` queue counts each cycle.
2. Emergency detector -> edge controller: optional direction (bypasses normal polling).
3. Edge controller -> decision engine: queues plus emergency flag; returns direction, then `green_time(queue[direction])`.
4. Edge controller -> actuators: (direction, seconds).
5. Edge controller -> cloud (asynchronous, batched): decisions, skipped counters, emergencies.

Priority inside the decision engine mirrors the requirements: **emergency > starved > longest queue**.

## Technology choices
- Edge: single-board computer running Python 3 (stdlib-only core, NFR3).
- Messaging: MQTT over TLS to the cloud (NFR5); local wired serial or GPIO to the signal controller.
- Cloud: time-series store plus a web dashboard.
- Watchdog timer on the edge box triggers the fixed-time fallback if no decision arrives in time (NFR2).
