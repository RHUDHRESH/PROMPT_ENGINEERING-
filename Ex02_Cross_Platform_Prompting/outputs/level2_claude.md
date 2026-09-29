# Level 2 (Role) - Claude output

**Transformers and the rise of LLMs**

Since the 2017 paper "Attention Is All You Need", transformers have displaced recurrent networks as the standard architecture for sequence modelling. Rather than reading tokens one by one, they use self-attention to link every token with every other in parallel. This makes GPU training much faster and captures long-range dependencies.

Scaling transformers on large text corpora gave rise to Large Language Models such as GPT, Claude and Gemini. These are pre-trained to predict the next token, then fine-tuned with human feedback so they follow instructions.

The caveats: they can hallucinate facts, are expensive to train and run, and inherit biases from their training data. Active research areas are efficiency, retrieval-augmented generation, longer context windows and dependable reasoning.
