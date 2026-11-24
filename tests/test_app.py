import app as a
import requests

def test_home():
    assert a.app.test_client().get('/').status_code == 200

def test_health():
    assert a.app.test_client().get('/api/health').json['records'] >= 30

def test_validation():
    c=a.app.test_client()
    assert c.post('/api/ask',json={'question':' '}).status_code==400
    assert c.post('/api/ask',data='{',content_type='application/json').status_code==400

def test_no_match():
    assert a.app.test_client().post('/api/ask',json={'question':'zxqv plutonium'}).json['mode']=='no_match'

def test_fallback(monkeypatch):
    def fail(*args): raise requests.ConnectionError('offline')
    monkeypatch.setattr(a,'generate',fail)
    d=a.app.test_client().post('/api/ask',json={'question':'What is Seva Sindhu?'}).json
    assert d['mode']=='retrieval_fallback' and d['sources']

def test_generation(monkeypatch):
    monkeypatch.setattr(a,'generate',lambda q,s:'Example mocked answer')
    assert a.app.test_client().post('/api/ask',json={'question':'What is UMANG?'}).json['mode']=='ollama_rag'

def test_feedback():
    assert a.app.test_client().post('/api/feedback',json={'helpful':True}).status_code==200
