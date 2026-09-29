# Report: Fundamentals of Generative AI and Large Language Models

## 1. Foundational concepts of Generative AI
Generative AI covers models that learn the distribution of their training data and can sample new, similar content: text, images, audio, code or video. This differs from discriminative models, which learn p(y | x) and output a label or score, such as a spam classifier. A generative model instead learns p(x), or p(x, y), and can therefore create examples.

Four families are usually taught. Generative Adversarial Networks (GANs, Goodfellow et al., 2014) pit a generator against a discriminator. They produce sharp samples quickly but are hard to train and prone to mode collapse. Variational Autoencoders (VAEs, Kingma and Welling, 2013) learn a smooth latent space through an encoder and decoder. They are stable but tend to produce blurrier output. Diffusion models (for example DDPM, Ho et al., 2020) generate by iteratively denoising random noise, giving high quality at the price of slow sampling. Autoregressive models factor the data distribution into next-element predictions, which underlies today's large language models. This split is a simplification, since real systems combine them (latent diffusion uses a VAE-style encoder).

Training data is mostly self-supervised: web text, code, image-caption pairs. Its quality, licensing and bias strongly shape behaviour. Common applications are code assistants, image generation for design, and synthetic data for domains where real data is scarce.

## 2. Generative AI architectures (Transformers)
The transformer (Vaswani et al., 2017) replaced recurrence with attention. Each token is projected to a query, key and value, and the output is

Attention(Q, K, V) = softmax(Q Kᵀ / √d_k) V.

The √d_k scaling stops large dot products from saturating the softmax. Small example: with d_k = 2, query [1, 0], keys [1, 0] and [0, 1], the scores are [0.71, 0], the softmax weights are about [0.67, 0.33], and the output is that weighted mix of the two value vectors. Multi-head attention runs several such operations in parallel so different heads can capture different relations. Because attention ignores order, positional encodings (sinusoidal in the original paper, often rotary today) are added.

Encoder-only models (BERT-style) suit understanding tasks, decoder-only models (GPT-style, with causal masking) suit generation, and encoder-decoder models suit translation and summarisation. Transformers displaced RNNs and LSTMs because they parallelise across the sequence, connect distant tokens in one step, and scale well with data and compute. The main cost is attention that grows quadratically with sequence length.

## 3. Architectures and applications
Each architecture has a natural niche. Transformers and LLMs are the most flexible tool for language, code and reasoning, with weaknesses in hallucination and cost. GANs give fast single-pass generation, useful for real-time image enhancement, but are unstable to train. VAEs suit representation learning, anomaly detection and latent compression. Diffusion models lead in image and increasingly video quality and are controllable through conditioning, though sampling is slow. Autoregressive audio and video models offer coherent long sequences for speech and music, at high generation cost; exact designs of several commercial systems are not public, so claims about them should be treated cautiously.

To choose, start from the modality and latency budget, then consider data and cost. Prefer adapting a pre-trained model (prompting, fine-tuning, retrieval) over training from scratch, and test on a small evaluation set that targets your worst failure mode.

## 4. Impact of scaling in LLMs
Loss on language modelling improves predictably, following power laws, as parameters, data and compute increase (Kaplan et al., 2020). Hoffmann et al. (2022, "Chinchilla") argued that for a fixed compute budget, parameters and training tokens should grow together, roughly 20 tokens per parameter, meaning many earlier models were undertrained. In practice, because inference cost recurs on every query, developers often train smaller models on much more data.

Some abilities appear to emerge suddenly at scale, though later analyses suggest part of this depends on how performance is measured, so the topic is contested. Returns diminish: each fixed gain in loss needs multiplicatively more compute, and high-quality text is finite. Training and serving are expensive and energy-hungry; precise figures are often undisclosed and should be treated as estimates. A newer axis is inference-time scaling, where extra computation at answer time (longer reasoning, multiple samples, verification) improves results on hard tasks.

## 5. What an LLM is and how it is built
An LLM is a very large neural network, usually a decoder-only transformer, trained to predict the next token. Construction proceeds in stages. Data is collected, deduplicated and filtered. Text is tokenized into subwords (for example byte-pair encoding). Pre-training on trillions of tokens builds general knowledge. Supervised fine-tuning on instruction-response examples teaches the model to follow instructions. Preference tuning, such as RLHF (Ouyang et al., 2022, InstructGPT) or simpler methods like DPO, aligns behaviour with human preferences. Evaluation uses benchmarks, human preference tests and red-teaming. Deployment relies on quantization, caching, batching and guardrails. Exact recipes differ between organisations and are often not disclosed, so this pipeline describes the typical case rather than any specific model.

## 6. Tool comparison summary (see `comparison.md`)
The repository contains Claude answers saved earlier and ChatGPT answers produced in the current Codex session. Both were reviewed against the same five topics. The provisional desk-review scores are tied at 19/25 with speed omitted because it was not measured. The Claude scores were initially self-assessed by the model that supplied those answers; neither column is an independent human evaluation. Fresh, timed runs and blind human scoring would make the comparison stronger.

## 7. Conclusion
Generative AI has moved from specialised models such as GANs and VAEs to transformer-based LLMs and diffusion models, whose quality comes largely from scale and from careful post-training. Understanding the mechanics (attention, next-token prediction, fine-tuning, preference tuning) helps engineers pick the right architecture, set realistic expectations and design safeguards. The main risks remain hallucination, cost, bias and limited transparency. Comparing tools on identical prompts is useful, but conclusions should wait until every tool has actually been run and the claims verified.

## References
1. Vaswani, A., et al. (2017). [Attention Is All You Need](https://arxiv.org/abs/1706.03762). NeurIPS 2017.
2. Kaplan, J., et al. (2020). [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361).
3. Hoffmann, J., et al. (2022). [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556) (Chinchilla).
4. Ouyang, L., et al. (2022). [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155) (InstructGPT). NeurIPS 2022.
5. Goodfellow, I., et al. (2014). [Generative Adversarial Nets](https://arxiv.org/abs/1406.2661). NeurIPS 2014.
6. Kingma, D. P., and Welling, M. (2013). [Auto-Encoding Variational Bayes](https://arxiv.org/abs/1312.6114).
7. Ho, J., Jain, A., and Abbeel, P. (2020). [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239). NeurIPS 2020.
