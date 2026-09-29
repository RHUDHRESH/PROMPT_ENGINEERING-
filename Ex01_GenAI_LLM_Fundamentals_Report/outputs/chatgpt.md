# ChatGPT responses

Tool: ChatGPT in the current Codex session. Exact model version was not exposed. Date: 2026-09-29. Completion times were not measured. Each section answers the corresponding prompt in `prompts/`.

## Q1 — Foundational concepts

Generative AI refers to models that learn patterns in examples and use them to create new content, such as text, images, audio, video or code. A generative model estimates a data distribution such as p(x), or a conditional distribution such as p(x|y), and samples from it. A discriminative model instead estimates a label or decision boundary, often p(y|x).

| Model family | How it generates | Example uses |
|---|---|---|
| Autoregressive | Predicts the next element repeatedly | Text, code, audio tokens |
| GAN | A generator competes with a discriminator | Image synthesis, augmentation |
| VAE | Encodes data into a latent distribution and decodes samples | Representation learning, controlled generation |
| Diffusion | Learns to remove noise over repeated steps | Images, audio and video |

Training examples shape what a model can represent. Data filtering, licensing, coverage and bias affect the result; generated output is not guaranteed to be true or original. Applications include drafting and translation, image design, and engineering assistance such as code suggestions. The system still needs human review for factual, safety or rights-sensitive use.

## Q2 — Generative AI architectures, focusing on transformers

A transformer splits input into tokens and maps each token to a vector. Self-attention lets each token combine information from other tokens. For queries Q, keys K and values V, scaled dot-product attention is `Attention(Q,K,V) = softmax(QKᵀ / √d_k)V`. The scale √d_k keeps dot products from growing too large as vector width increases. A query matches keys; the resulting weights blend the values. For example, weights 0.7 and 0.3 produce a context vector that is 70% of one value and 30% of another.

Multi-head attention runs several learned attention operations in parallel, allowing different heads to capture different relationships. Positional information is added because attention alone does not encode word order. Encoder-only models build contextual representations; decoder-only models predict the next token with a causal mask; encoder-decoder models encode an input and generate a conditioned output, useful for translation.

Transformers train efficiently on parallel hardware because they process a sequence together during training, unlike recurrent networks that step through tokens in order. Attention also creates shorter paths between distant tokens. The trade-off is attention cost that grows roughly quadratically with sequence length in the basic implementation; long-context models use optimisations to reduce memory or computation.

## Q3 — Architectures and applications

| Architecture | Strengths | Weaknesses | Example product or system | Engineering use |
|---|---|---|---|---|
| Transformer / LLM | Flexible language and code generation; instruction following | Can invent facts; high compute and context costs | ChatGPT, Gemini, Claude | Documentation drafts, code assistance, retrieval-based technical Q&A |
| GAN | Fast image sampling after training; sharp outputs | Training can be unstable; mode collapse | StyleGAN-family research systems | Synthetic inspection images for augmentation, with validation |
| VAE | Smooth latent space; useful probabilistic representation | Samples may look blurrier than GAN or diffusion outputs | VAE-based image and anomaly-detection systems | Compact sensor representation and anomaly exploration |
| Diffusion | High-quality, diverse image generation; controllable denoising | Iterative sampling can be compute-intensive | DALL·E and Stable Diffusion systems | Concept imagery, synthetic visual data and design exploration |
| Autoregressive audio/video | Models temporal order and can condition on prior frames or tokens | Long sequences increase latency; temporal consistency remains difficult | Speech-generation and text-to-video systems | Voice interfaces, simulation assets and visualisation |

Choose based on output type, quality and latency needs, available data and compute, and the cost of errors. Prototype with a baseline, measure task-specific quality, and add human review wherever mistakes could cause harm.

## Q4 — Impact of scaling in LLMs

Scaling changes model parameters, training data and compute together. Kaplan et al. (2020) reported empirical power-law trends between language-model loss and scale. Hoffmann et al. (2022), in *Training Compute-Optimal Large Language Models*, showed that some large models were undertrained for their parameter count and argued for allocating more tokens per parameter at fixed compute. These findings guide planning; they do not guarantee a particular capability or product outcome.

More scale often improves average predictive performance, but each gain costs more data, accelerator time, energy and money. Diminishing returns appear when added compute yields smaller improvements on the target task. Claims of “emergent abilities” depend on the metric and evaluation scale; apparent jumps can arise when continuous improvements cross a threshold-based score.

Inference-time scaling spends more computation while answering, for example by sampling or checking multiple candidate solutions. It can improve selected reasoning tasks, but raises latency and cost and does not remove hallucinations. A practical choice balances measured task quality against training and serving cost, including smaller models, retrieval, caching and human checks.

## Q5 — What an LLM is and how it is built

| Stage | Purpose | Typical technique or tool |
|---|---|---|
| Data collection and filtering | Assemble relevant, permitted examples and remove poor-quality or sensitive records | Deduplication, policy filters, data documentation |
| Tokenization | Convert text into integer token IDs | Subword tokenizers such as BPE or SentencePiece |
| Pre-training | Learn broad language patterns by predicting tokens | Transformer training with next-token loss and distributed GPU/TPU jobs |
| Supervised fine-tuning | Teach the model to follow example instructions | Curated prompt-response examples and supervised optimization |
| Preference tuning | Align response choices with human preferences | Preference comparisons; RLHF or direct preference optimization |
| Evaluation | Measure capability, robustness, safety and regressions | Held-out benchmarks, red-team tests and human review |
| Deployment | Serve responses with limits, monitoring and updates | Model serving, rate limits, logging controls and evaluation gates |

Remember: collect responsibly, turn text into tokens, train to predict, tune to follow instructions, test carefully, then serve with monitoring.
