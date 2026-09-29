# Run sheet: paste each prompt into ChatGPT / Gemini (fresh chat each), save output in the folder shown

Estimated 30-45 min. Note the time each answer takes for the Speed column.

## Ex01_GenAI_LLM_Fundamentals_Report
### q1_foundational_concepts.md  -> save to `Ex01_GenAI_LLM_Fundamentals_Report/outputs/<name>_chatgpt.md`, `_gemini.md`
# Prompt 1 — Foundational concepts of Generative AI
```
You are a university AI lecturer. Explain the foundational concepts of Generative AI for a third-year engineering student.
Cover: definition, discriminative vs generative models, key model families (GANs, VAEs, diffusion, autoregressive), training data, and 3 real applications.
Limit to 400 words. Use headings and one comparison table. Flag anything you are unsure about.
```

### q2_architectures_transformers.md  -> save to `Ex01_GenAI_LLM_Fundamentals_Report/outputs/<name>_chatgpt.md`, `_gemini.md`
# Prompt 2 — Generative AI architectures (transformers)
```
Explain Generative AI architectures with a focus on transformers.
Cover: self-attention (Q, K, V), multi-head attention, positional encoding, encoder vs decoder vs encoder-decoder, and why transformers replaced RNNs/LSTMs.
Include the scaled dot-product attention formula and a small numeric intuition. Max 450 words.
```

### q3_architecture_applications.md  -> save to `Ex01_GenAI_LLM_Fundamentals_Report/outputs/<name>_chatgpt.md`, `_gemini.md`
# Prompt 3 — Architectures and their applications
```
Map each Generative AI architecture (Transformer/LLM, GAN, VAE, Diffusion, Autoregressive audio/video models) to its best-fit applications.
Return a table: Architecture | Strengths | Weaknesses | Example products | Typical engineering use case.
Then give 3 sentences on how to choose an architecture for a new project.
```

### q4_scaling_impact.md  -> save to `Ex01_GenAI_LLM_Fundamentals_Report/outputs/<name>_chatgpt.md`, `_gemini.md`
# Prompt 4 — Impact of scaling in LLMs
```
Explain the impact of scaling on Large Language Models: parameters, data, and compute.
Cover scaling laws (Kaplan, Chinchilla), emergent abilities, diminishing returns, cost/energy, and inference-time scaling.
Cite the source paper names only if you are certain they exist; otherwise say "unsure". Max 400 words.
```

### q5_llm_how_built.md  -> save to `Ex01_GenAI_LLM_Fundamentals_Report/outputs/<name>_chatgpt.md`, `_gemini.md`
# Prompt 5 — What an LLM is and how it is built
```
Explain what a Large Language Model is and how it is built, end to end:
data collection & cleaning -> tokenization -> pre-training -> supervised fine-tuning -> RLHF/preference tuning -> evaluation -> deployment.
For each stage give one sentence on purpose and one on a typical tool or technique. Finish with a 5-line summary a beginner can remember.
```

## Ex02_Cross_Platform_Prompting
### 1_basic.md  -> save to `Ex02_Cross_Platform_Prompting/outputs/<name>_chatgpt.md`, `_gemini.md`
# Level 1 — Basic
```
Summarize this text.

<paste source_text.md>
```

### 2_role.md  -> save to `Ex02_Cross_Platform_Prompting/outputs/<name>_chatgpt.md`, `_gemini.md`
# Level 2 — Role
```
You are a technical editor for an engineering magazine. Summarize this text.

<paste source_text.md>
```

### 3_context.md  -> save to `Ex02_Cross_Platform_Prompting/outputs/<name>_chatgpt.md`, `_gemini.md`
# Level 3 — Context
```
You are a technical editor for an engineering magazine.
Context: the readers are final-year students who know basic ML but have not studied transformers. The summary will appear as a sidebar next to a longer article on LLMs.
Summarize this text.

<paste source_text.md>
```

### 4_constraint.md  -> save to `Ex02_Cross_Platform_Prompting/outputs/<name>_chatgpt.md`, `_gemini.md`
# Level 4 — Constraint
```
You are a technical editor for an engineering magazine.
Context: the readers are final-year students who know basic ML but have not studied transformers. The summary will appear as a sidebar next to a longer article on LLMs.
Constraints: max 60 words; neutral tone; no jargon without a 3-word explanation; do not mention company names; do not add facts that are not in the text.
Summarize this text.

<paste source_text.md>
```

### 5_output_format.md  -> save to `Ex02_Cross_Platform_Prompting/outputs/<name>_chatgpt.md`, `_gemini.md`
# Level 5 — Output format
```
You are a technical editor for an engineering magazine.
Context: the readers are final-year students who know basic ML but have not studied transformers. The summary will appear as a sidebar next to a longer article on LLMs.
Constraints: max 60 words in the summary; neutral tone; explain jargon in <=3 words; no company names; no facts outside the text.
Output format (JSON only):
{
  "headline": "<=8 words",
  "summary": "<=60 words",
  "key_terms": [{"term": "", "meaning": ""}],
  "limitations": ["", ""]
}
Summarize this text.

<paste source_text.md>
```

## Ex03_Prompt_Types_Chatbot
### 1_straightforward.md  -> save to `Ex03_Prompt_Types_Chatbot/outputs/<name>_chatgpt.md`, `_gemini.md`
# Straightforward
```
You are a friendly customer-support chatbot for an electronics store. A customer writes: "My wireless headphones won't connect to my phone." Give clear step-by-step troubleshooting in a conversational tone, max 120 words.
```
```
A customer asks: "Where is my order #48213?" You cannot access a database. Reply politely, explain what you need, and tell them how to track it.
```

### 2_tabular.md  -> save to `Ex03_Prompt_Types_Chatbot/outputs/<name>_chatgpt.md`, `_gemini.md`
# Tabular format
```
Act as a support chatbot. Return a table with columns: Issue category | Example customer message | Bot reply (max 25 words) | Escalate to human? (Y/N).
Rows: product troubleshooting (2), order tracking (2), general inquiry (2).
```

### 3_missing_word.md  -> save to `Ex03_Prompt_Types_Chatbot/outputs/<name>_chatgpt.md`, `_gemini.md`
# Missing word
```
Fill in every blank (___) to complete the support chatbot reply. Keep the sentence structure, friendly tone, return only the completed text.

"Hi ___! Thanks for contacting ___ support. I'm sorry your ___ is ___. Let's fix it: first, ___; if that doesn't work, ___. If the problem continues, I'll ___ so a specialist can help within ___."

Context: customer Priya, product SmartKettle X2, issue: won't heat.
```

### 4_preceding_question.md  -> save to `Ex03_Prompt_Types_Chatbot/outputs/<name>_chatgpt.md`, `_gemini.md`
# Preceding question
```
Before answering, work through these questions in order (show short answers):
Q1. What information is needed to help a customer whose order is late?
Q2. What are the three most likely reasons for a delay?
Q3. What tone reassures an upset customer?
Now, using Q1–Q3, reply to: "My order was due 3 days ago and nobody told me anything!"
```

## Ex04_Advanced_Prompting_Techniques
### 01_zero_shot.md  -> save to `Ex04_Advanced_Prompting_Techniques/outputs/<name>_chatgpt.md`, `_gemini.md`
# Zero-shot
**Smart Irrigation**
```
Design a rule for a smart irrigation controller that decides when to water using soil moisture (%), rain forecast (mm) and temperature (°C). Give the rule as pseudocode.
```
**Drone Navigation**
```
Describe how a quadcopter should navigate from point A to B while avoiding a moving obstacle, using only a camera and IMU.
```
**Robot Path Planning**
```
Choose a path-planning algorithm for a warehouse robot on a 20x20 grid with static shelves and explain the choice.
```

### 02_few_shot.md  -> save to `Ex04_Advanced_Prompting_Techniques/outputs/<name>_chatgpt.md`, `_gemini.md`
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

### 03_chain_of_thought.md  -> save to `Ex04_Advanced_Prompting_Techniques/outputs/<name>_chatgpt.md`, `_gemini.md`
# Chain of Thought
**Smart Irrigation**
```
A field of 2000 m² needs 4 mm of water/day. The pump delivers 30 L/min. Rain forecast is 1 mm. How many minutes must the pump run? Think step by step, show each calculation, then state the final answer.
```
**Drone Navigation**
```
A drone flies at 6 m/s toward an obstacle 30 m ahead and needs 2.5 s to stop with 4 m/s² braking after a 0.5 s detection delay. Will it stop in time? Reason step by step.
```
**Robot Path Planning**
```
Compare A* and Dijkstra on a 100x100 grid with 4-connectivity and uniform cost. Reason step by step about node expansions and the effect of the heuristic, then recommend one.
```

### 04_persona_pattern.md  -> save to `Ex04_Advanced_Prompting_Techniques/outputs/<name>_chatgpt.md`, `_gemini.md`
# Persona pattern
**Smart Irrigation**
```
Act as an agronomist with 20 years of drip-irrigation experience advising a small farmer with a limited budget. Recommend a sensor set and watering schedule for tomatoes. Speak plainly.
```
**Drone Navigation**
```
Act as a UAV flight-controller engineer at a safety-critical company. Review this plan: "Use GPS only for obstacle avoidance." List the failure modes and fixes.
```
**Robot Path Planning**
```
Act as a senior robotics professor grading a student's plan to use BFS for a weighted-cost warehouse. Give feedback and a corrected approach.
```

### 05_reverse_prompting.md  -> save to `Ex04_Advanced_Prompting_Techniques/outputs/<name>_chatgpt.md`, `_gemini.md`
# Reverse prompting (model asks / infers the prompt)
**Smart Irrigation**
```
I want a smart irrigation system for my farm. Do not answer yet. Ask me the 6 most important questions you need to design it, one list only.
```
**Drone Navigation**
```
Here is the output I got: "Use a PID controller with obstacle repulsive potential fields." Write the best prompt that would have produced exactly this kind of answer, and list what context the prompt must include.
```
**Robot Path Planning**
```
Given this final design document (paste), reconstruct the original requirements prompt that an engineer likely wrote.
```

### 06_graph_prompting.md  -> save to `Ex04_Advanced_Prompting_Techniques/outputs/<name>_chatgpt.md`, `_gemini.md`
# Graph prompting
**Smart Irrigation**
```
Represent the irrigation system as a graph: nodes = {soil sensor, weather API, controller, valve, pump, farmer app}; edges = data/control flows. Output the adjacency list, then explain the critical path and single points of failure.
```
**Drone Navigation**
```
Model the drone mission as a directed graph of states (Takeoff, Cruise, Avoid, Reroute, Land, Emergency) with transition conditions on edges. Output as Mermaid, then list unreachable/dead-end states.
```
**Robot Path Planning**
```
Given the weighted graph: A-B:4, A-C:2, B-C:1, B-D:5, C-D:8, C-E:10, D-E:2, D-F:6, E-F:3. Find the shortest path A->F with Dijkstra, showing the distance table at each step.
```

### 07_active_prompting.md  -> save to `Ex04_Advanced_Prompting_Techniques/outputs/<name>_chatgpt.md`, `_gemini.md`
# Active prompting (uncertainty-driven example selection)
Procedure: run the question 5 times, find the question with the most disagreement among answers, then have a human write a chain-of-thought exemplar for it and add it as a few-shot example.

**Step 1 – sample (run 5x)**
```
Should a drone with 20 min battery, carrying a 1 kg payload, 6 km from base and facing 8 m/s headwind, continue the mission or return? Answer CONTINUE or RETURN and give a one-line reason.
```
**Step 2 – exemplar (human-written)**
```
Q: <the most uncertain question>
Reasoning: <your step-by-step reasoning>
A: <correct answer>
```
**Step 3 – re-run with the exemplar prepended** and compare consistency across 5 runs.
Repeat for irrigation ("Skip watering if 3 mm rain is forecast but soil is at 12%?") and path planning ("Replan or continue when a new obstacle appears 1 cell ahead?").

