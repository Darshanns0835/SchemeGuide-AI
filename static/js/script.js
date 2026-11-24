const $ = id => document.getElementById(id);
async function post(url, body) {
  const res = await fetch(url, {method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
  const data = await res.json();
  if (!res.ok) throw new Error(data.error || 'Request failed');
  return data;
}
$('form').addEventListener('submit', async e => {
  e.preventDefault(); if ($('ask').disabled) return;
  $('ask').disabled=true; $('status').textContent='Searching knowledge base…'; $('answer').textContent=''; $('sources').replaceChildren(); $('feedback').hidden=true; $('thanks').textContent='';
  try {
    const data=await post('/api/ask',{question:$('question').value,category:$('category').value});
    $('answer').textContent=data.answer;
    $('status').textContent='Response mode: '+data.mode;
    if(data.sources.length){const h=document.createElement('h3');h.textContent='Retrieved sources';$('sources').append(h);}
    for(const s of data.sources){
      const item=document.createElement('article');item.className='source';
      const title=document.createElement('strong');title.textContent=s.scheme+' · Similarity '+(s.score*100).toFixed(1)+'%';
      const para=document.createElement('p');para.textContent=s.answer;
      const link=document.createElement('a');link.href=s.source_url;link.textContent='Open official reference ↗';link.target='_blank';link.rel='noopener noreferrer';
      item.append(title,para,link);$('sources').append(item);
    }
    $('feedback').hidden=false;
  }catch(err){$('status').textContent=err.message;}finally{$('ask').disabled=false;}
});
document.querySelectorAll('.example').forEach(b=>b.onclick=()=>{$('question').value=b.textContent;$('category').value='All';$('question').focus();});
document.querySelectorAll('[data-value]').forEach(b=>b.onclick=async()=>{try{const d=await post('/api/feedback',{helpful:b.dataset.value==='true'});$('thanks').textContent=d.message;}catch(e){$('thanks').textContent=e.message;}});
