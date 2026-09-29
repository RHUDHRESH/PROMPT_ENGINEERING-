# Claude outputs
Model/version used: Claude (Sonnet 5.5, answered directly in a Claude Code session; not a fresh web chat)   Date: 2026-09-29

| Prompt | Time to complete (s) |
|---|---|
| Q1 | not measured |
| Q2 | not measured |
| Q3 | not measured |
| Q4 | not measured |
| Q5 | not measured |

## Q1

### Definition
Generative AI refers to models that learn the probability distribution of training data, p(x), and can sample new data (text, images, audio, code) resembling it.

### Discriminative vs generative
| Aspect | Discriminative | Generative |
|---|---|---|
| Learns | p(y given x), a decision boundary | p(x) or p(x, y), the data distribution |
| Output | Label or number | New samples |
| Examples | Logistic regression, CNN classifier | GPT-style LLMs, GANs, diffusion |
| Typical use | Spam detection, diagnosis | Writing, image synthesis |

### Key model families
- **GANs:** a generator and a discriminator train adversarially. Samples are sharp, but training is unstable and can suffer mode collapse.
- **VAEs:** an encoder maps data to a latent distribution and a decoder reconstructs it. Training is stable and the latent space is smooth, but outputs tend to be blurrier.
- **Diffusion models:** learn to reverse a gradual noising process, generating by iterative denoising. Quality is high, but sampling is slow.
- **Autoregressive models:** factor p(x) as a product of next-token probabilities. This is the basis of LLMs.

### Training data
Models need large, diverse data: web text and code for LLMs, image-caption pairs for text-to-image systems. Data quality, duplication, licensing and bias directly shape model behaviour. Most training is self-supervised, so no manual labels are required.

### Three applications
1. Code assistants that complete and explain code.
2. Text-to-image tools for design and prototyping.
3. Synthetic data generation, for example to augment scarce medical or driving datasets.

### Uncertainty
The four-family split is a teaching simplification. Modern systems mix them (latent diffusion uses a VAE plus a transformer or U-Net), and diffusion can also be viewed as a hierarchical latent-variable model.

## Q2

### Overview
A transformer is a neural architecture built on attention rather than recurrence. It was introduced in "Attention Is All You Need" (Vaswani et al., 2017).

### Self-attention (Q, K, V)
Each token embedding is projected into a query Q (what I am looking for), a key K (what I offer) and a value V (what I carry). Similarity between queries and keys decides how much of each value is mixed into the output.

**Attention(Q, K, V) = softmax(Q Kᵀ / √d_k) V**

Dividing by √d_k keeps dot products from growing with dimension, which would push softmax into regions with tiny gradients.

### Numeric intuition
Take d_k = 2, query q = [1, 0], keys k1 = [1, 0] and k2 = [0, 1], values v1 = [10, 0] and v2 = [0, 10].
Scores = [1, 0] / √2 = [0.707, 0]. Softmax gives weights of about [0.67, 0.33]. Output = 0.67·v1 + 0.33·v2 ≈ [6.7, 3.3]. The token attends mostly, but not exclusively, to the more similar key.

### Multi-head attention
Several attention operations run in parallel with different learned projections. Each head can specialise (for instance in syntax or coreference). Outputs are concatenated and linearly projected.

### Positional encoding
Attention alone ignores order, so position information is added to the embeddings. The original paper used fixed sinusoids. Many modern models use learned or rotary (RoPE) encodings.

### Encoder vs decoder vs encoder-decoder
- **Encoder-only** (BERT-style): bidirectional context, suited to classification and embeddings.
- **Decoder-only** (GPT-style): causal masking, so each token sees only earlier tokens. Suited to generation and now dominant for LLMs.
- **Encoder-decoder** (T5, original Transformer): the encoder reads the input and the decoder attends to it via cross-attention. Suited to translation and summarisation.

### Why transformers replaced RNNs/LSTMs
1. RNNs process tokens sequentially, so they cannot be parallelised across a sequence. Transformers train much faster on GPUs.
2. Any two tokens are connected in one step, so long-range dependencies are easier to learn. In RNNs, signals must pass through many steps and gradients vanish.
3. They scale predictably with data and compute.

Trade-off: attention cost grows quadratically with sequence length, which motivates efficient-attention research.

## Q3

| Architecture | Strengths | Weaknesses | Example products | Typical engineering use case |
|---|---|---|---|---|
| Transformer / LLM | Flexible, strong language and reasoning, few-shot learning, scales well | Hallucination, high compute cost, quadratic attention | ChatGPT, Claude, Gemini, GitHub Copilot | Chatbots, code assistance, document Q&A with retrieval |
| GAN | Fast single-pass sampling, sharp images | Unstable training, mode collapse, weak coverage of the distribution | StyleGAN-based face generators, some super-resolution tools | Real-time image enhancement, style transfer, data augmentation |
| VAE | Stable training, smooth latent space, useful for compression | Blurrier outputs, posterior collapse | Often a component inside latent diffusion systems | Anomaly detection, representation learning, latent compression |
| Diffusion | Very high fidelity, diverse, controllable via conditioning | Slow iterative sampling, heavy compute | Stable Diffusion, DALL-E, Midjourney (architecture details for some are not public) | Image, video and design generation, inpainting |
| Autoregressive audio/video models | Coherent long sequences, conditioning on text | Slow token-by-token generation, high cost for video; some leading systems are proprietary, so exact architectures are uncertain | WaveNet-lineage speech models, text-to-speech and music tools, text-to-video systems (mix of diffusion and transformers) | Speech synthesis, music and sound design, video prototyping |

**Choosing an architecture:** start from the output modality and the latency budget: text or code points to an LLM, images or video to diffusion, and real-time or on-device generation to a GAN or a distilled model. Then weigh data availability and cost, and prefer a pre-trained model you can prompt, fine-tune or ground with retrieval before training from scratch. Finally, prototype on a small evaluation set that measures the failure mode you fear most, such as hallucination, artifacts or latency, before committing.

## Q4

### Parameters, data, compute
Scaling means increasing model parameters (N), training tokens (D) and training compute (C). Loss falls smoothly and predictably as each grows.

### Scaling laws
- **Kaplan et al., 2020, "Scaling Laws for Neural Language Models"** (I am confident this exists). It found power-law loss trends in N, D and C, and suggested that for a fixed budget, model size should grow faster than data.
- **Hoffmann et al., 2022, "Training Compute-Optimal Large Language Models"**, known as Chinchilla (confident it exists). It re-examined this and concluded that parameters and tokens should scale roughly equally, at around 20 tokens per parameter. Many earlier models were therefore undertrained. Treat "20:1" as an approximate rule of thumb.

Practice has since moved on: because inference cost is paid on every query, teams often train smaller models on far more tokens than Chinchilla-optimal.

### Emergent abilities
Some skills, such as multi-step arithmetic or in-context learning, appear to show up abruptly beyond a certain scale. A paper by Wei et al. (2022) on emergent abilities exists, though I am not certain of its exact title. Later work argued that some apparent emergence is an artifact of discontinuous metrics. The debate is unresolved.

### Diminishing returns
Power laws mean each constant improvement in loss needs multiplicatively more compute. Good-quality text data is also finite, so data availability may become a bottleneck, and lower loss does not automatically mean better real-world usefulness.

### Cost and energy
Frontier training runs use thousands of accelerators for weeks, and are estimated to cost tens of millions of dollars or more. Exact figures and energy use are often undisclosed, so I would treat public estimates as uncertain. Inference at scale can exceed training in total energy.

### Inference-time scaling
Spending more compute at answer time, through longer chain-of-thought, sampling several answers and voting, or search with verifiers, improves reasoning on hard tasks. It offers a second axis to trade cost against quality, though gains vary by task.

## Q5

| Stage | Purpose | Typical tool or technique |
|---|---|---|
| 1. Data collection and cleaning | Gather a large, diverse and clean corpus so the model learns language and knowledge. | Web crawls, licensed and code datasets, deduplication (for example MinHash), quality and toxicity filters. |
| 2. Tokenization | Convert text into integer tokens the model can process. | Subword methods such as byte-pair encoding (BPE) or SentencePiece. |
| 3. Pre-training | Learn general language patterns by predicting the next token over trillions of tokens. | Decoder-only transformer, cross-entropy loss, AdamW, distributed training with PyTorch, DeepSpeed or Megatron-style parallelism on GPU/TPU clusters. |
| 4. Supervised fine-tuning (SFT) | Teach the base model to follow instructions using example prompt-response pairs. | Curated human-written demonstrations, full fine-tuning or LoRA. |
| 5. RLHF / preference tuning | Align outputs with human preferences for helpfulness and safety. | Reward model plus PPO (as in InstructGPT), or simpler methods like DPO; some labs also use AI feedback. |
| 6. Evaluation | Measure capability, safety and regressions before release. | Benchmarks such as MMLU, human preference tests, red-teaming, task-specific test sets. |
| 7. Deployment | Serve the model reliably, cheaply and safely to users. | Quantization, KV caching, batching in serving engines such as vLLM, plus guardrails, monitoring and retrieval or tool integration. |

Exact recipes differ by lab and are often not public, so the techniques above are typical rather than universal.

### 5-line summary
1. An LLM is a huge neural network trained to predict the next token.
2. Clean data and tokenization decide what it can learn.
3. Pre-training builds broad knowledge; fine-tuning teaches it to follow instructions.
4. Preference tuning makes answers more helpful and safer, but not perfectly truthful.
5. It still needs evaluation, guardrails and monitoring, because it can hallucinate.
