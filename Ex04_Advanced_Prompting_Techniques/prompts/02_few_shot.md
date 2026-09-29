# Few-shot
**Smart Irrigation**
```
Classify irrigation decisions.
Input: moisture=15%, rain=0mm, temp=34C -> Decision: WATER (long)
Input: moisture=55%, rain=0mm, temp=25C -> Decision: SKIP
Input: moisture=30%, rain=8mm, temp=28C -> Decision: SKIP (rain expected)
Input: moisture=22%, rain=1mm, temp=31C -> Decision:
```
**Drone Navigation**
```
Choose the avoidance action.
Obstacle 5m ahead, static -> ACTION: yaw 30° and pass
Obstacle 3m ahead, moving toward drone -> ACTION: climb 2m and slow
Obstacle 2m left, moving away -> ACTION: continue
Obstacle 4m ahead, moving across path right-to-left -> ACTION:
```
**Robot Path Planning**
```
Pick algorithm.
Grid 10x10, static, single goal -> A*
Unknown map, exploring -> D* Lite
Continuous space, high-dimensional arm -> RRT*
Grid 50x50, dynamic obstacles, replanning needed -> 
```
