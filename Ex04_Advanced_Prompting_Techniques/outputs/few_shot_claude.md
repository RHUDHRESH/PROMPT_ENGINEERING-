# Few-shot - Claude outputs (3 case studies)
Tool: Claude, answered directly. Token counts below are approximate word counts (prompt + output).

## Case 1: Smart Irrigation
Approx. words (prompt + output): about 110

Input: moisture=22%, rain=1mm, temp=31C -> Decision: **WATER (short)**

Reason: moisture is low-ish and it is hot, while 1 mm of rain is negligible. It is not as dry as the 15% example (long), and the rain is far below the 8 mm example (skip). The exact label "short" extrapolates between the examples; it is a judgement call.

## Case 2: Drone Navigation
Approx. words (prompt + output): about 120

Obstacle 4m ahead, moving across path right-to-left -> ACTION: **yaw 30° right, slow, pass behind the obstacle's trailing side, then resume heading**

Reason: the obstacle is leaving the path toward the left, so passing on the right moves away from where it is heading. It is not moving toward the drone, so a climb is unnecessary. Speed is reduced because it is only 4 m away.

## Case 3: Robot Path Planning
Approx. words (prompt + output): about 90

Grid 50x50, dynamic obstacles, replanning needed -> **D\* Lite**

Reason: the grid is known but changes, and D\* Lite repairs the previous search incrementally instead of replanning from scratch (unlike A\*), following the pattern of the "unknown map" example.
