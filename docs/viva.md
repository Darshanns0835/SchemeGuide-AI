# Presentation and viva
Slides: title; problem; objectives; architecture; dataset; TF-IDF and cosine similarity; Ollama; live demonstration; testing and limitations; conclusion.

- What is RAG? Retrieve relevant records and provide them as context to a language model before generation.
- What is TF-IDF? Term frequency–inverse document frequency, a lexical weighting method.
- What is cosine similarity? Normalized dot product of two vectors.
- Why top three? Limit context size while providing multiple candidate records.
- What does a score mean? Text similarity, not eligibility probability.
- Why Ollama? Local model runtime with HTTP API.
- Why Flask? Lightweight web framework for pages and JSON endpoints.
- What happens offline? Retrieved text is returned without the model.
- Is the data live? No, a curated static educational dataset.
- How is eligibility decided? By the relevant official authority, not this application.
- Can the LLM hallucinate? Yes; grounding reduces but cannot eliminate this risk.
