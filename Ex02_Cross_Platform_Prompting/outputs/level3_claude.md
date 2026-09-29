# Level 3 (Context) - Claude output

**Sidebar: Why transformers changed language AI**

Older language models, called recurrent networks, read text one word-piece (token) at a time. Transformers, introduced in 2017, instead use "self-attention": every token is compared with every other token at once. This parallel approach trains much faster on GPUs and links words that sit far apart in a text.

Training transformers on huge text collections produced Large Language Models (LLMs), such as GPT, Claude and Gemini. First they learn to predict the next token; then human feedback fine-tunes them to follow instructions.

They are not perfect. LLMs can hallucinate (state false things confidently), cost a lot to train and run, and absorb biases from their data. Researchers are working on efficiency, retrieval-augmented generation (looking up documents while answering), longer context windows and more reliable reasoning.
