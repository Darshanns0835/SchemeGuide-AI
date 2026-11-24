from retrieval import Retriever

def test_rank():
    results=Retriever().search('What is Seva Sindhu Karnataka?')
    assert 1<=len(results)<=3
    assert results[0]['scheme']=='Seva Sindhu'
    assert all(0<=r['score']<=1 for r in results)

def test_filter():
    assert all(r['category']=='Karnataka' for r in Retriever().search('Seva Sindhu','Karnataka'))
