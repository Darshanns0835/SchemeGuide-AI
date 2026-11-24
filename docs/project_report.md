# SchemeGuide AI – University project report

## Abstract
A Flask application combines TF-IDF retrieval and a locally hosted Llama 3.2 model to explain introductory information about Indian public services. Official reference links and fallback responses support transparency.

## Problem and objectives
Government information is spread across portals. This project provides a single educational interface to discover relevant reference records, generate explanations, and navigate to official sources. It does not replace official applications or determine eligibility.

## Architecture and methodology
Browser → Flask validation → TF-IDF query vector → cosine similarity ranking → category filter and top three matches → Ollama prompt → answer and sources. If generation fails, retrieved text is returned. If retrieval fails, the system returns a no-match notice.

## Dataset
30 introductory records across discovery, education, agriculture, employment, housing, health, digital services, digital documents, Karnataka and public services. JSON is used at runtime; CSV is a duplicate for inspection. The records are not 30 distinct schemes and do not constitute a live government database.

## Modules
app.py handles endpoints, model integration and feedback. retrieval.py builds a TF-IDF matrix and ranks records. HTML/CSS/JS provide the frontend. Tests use Flask's test client and mocked generation.

## Evaluation and limitations
Tests cover validation, retrieval, filtering, mocked model success, model failure, no-match behavior and feedback. Real model quality needs separate manual testing. The dataset is small and may become stale; lexical matches may miss synonyms. Prompt constraints cannot guarantee factual accuracy. No sensitive information should be entered. Capture actual screenshots and test output on your computer for submission.

## Future scope
Expand verified scheme-specific records, add multilingual retrieval, source review dates and automated link checks, and evaluate answer accuracy against official documents.

## Conclusion
The prototype demonstrates retrieval-augmented generation and graceful degradation using a local model, without claiming official authority.

## References
See source_url in data/schemes.json for official references. Technical documentation: https://docs.ollama.com/ ; https://flask.palletsprojects.com/ ; https://scikit-learn.org/stable/ .
