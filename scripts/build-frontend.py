from pathlib import Path
import re, html, json
root = Path(__file__).resolve().parents[1]
posts=[]
for p in sorted((root/'posts').glob('*.md')):
    text=p.read_text()
    fm={}
    body=text
    if text.startswith('---'):
        _, fm_text, body = text.split('---',2)
        for line in fm_text.strip().splitlines():
            if ':' in line:
                k,v=line.split(':',1)
                v=v.strip()
                if v.startswith('[') and v.endswith(']'):
                    fm[k.strip()]=[x.strip().strip('"') for x in v.strip('[]').split(',') if x.strip()]
                else:
                    fm[k.strip()]=v.strip('"')
    plain=re.sub(r'```[\s\S]*?```','',body)
    plain=re.sub(r'[#>*_`\-\[\]\(\)]','',plain)
    words=plain.split()
    excerpt=' '.join(words[:34]) + ('...' if len(words)>34 else '')
    posts.append({'file': str(p.relative_to(root)), 'slug': fm.get('slug', p.stem), 'title': fm.get('title', p.stem), 'description': fm.get('description',''), 'date': fm.get('date',''), 'tags': fm.get('tags',[]), 'body': body.strip(), 'excerpt': excerpt, 'word_count': len(words)})

def md_to_html(md):
    lines=md.strip().splitlines()
    out=[]; in_ul=False; in_code=False; code=[]
    def close_ul():
        nonlocal in_ul
        if in_ul:
            out.append('</ul>'); in_ul=False
    def inline(s):
        s=html.escape(s)
        s=re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
        s=re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2">\1</a>', s)
        return s
    for line in lines:
        if line.strip().startswith('```'):
            if not in_code:
                close_ul(); in_code=True; code=[]
            else:
                out.append('<pre><code>'+html.escape('\n'.join(code))+'</code></pre>'); in_code=False
            continue
        if in_code:
            code.append(line); continue
        if not line.strip():
            close_ul(); continue
        if line.startswith('# '):
            close_ul(); out.append(f'<h1>{inline(line[2:].strip())}</h1>')
        elif line.startswith('## '):
            close_ul(); out.append(f'<h2>{inline(line[3:].strip())}</h2>')
        elif line.startswith('### '):
            close_ul(); out.append(f'<h3>{inline(line[4:].strip())}</h3>')
        elif line.startswith('- '):
            if not in_ul: out.append('<ul>'); in_ul=True
            out.append(f'<li>{inline(line[2:].strip())}</li>')
        elif re.match(r'^\d+\.\s+', line):
            stripped = re.sub(r'^\d+\.\s+', '', line).strip()
            close_ul(); out.append(f'<p>{inline(stripped)}</p>')
        else:
            close_ul(); out.append(f'<p>{inline(line.strip())}</p>')
    close_ul()
    return '\n'.join(out)

for post in posts:
    post['html']=md_to_html(post['body'])

cards='\n'.join([f'''<article class="post-card" data-tags="{' '.join(html.escape(t) for t in p['tags'])}">
  <div class="post-kicker">Guide {i+1:02d} · {html.escape(str(p['word_count']))} words</div>
  <h3><a href="#post-{html.escape(p['slug'])}">{html.escape(p['title'])}</a></h3>
  <p>{html.escape(p['excerpt'])}</p>
  <div class="tags">{''.join(f'<span>{html.escape(t)}</span>' for t in p['tags'][:4])}</div>
</article>''' for i,p in enumerate(posts)])
post_json=json.dumps(posts, ensure_ascii=False).replace('</script>','<\\/script>')
index=root/'index.html'
text=index.read_text()
text=text.replace('7 draft posts</span><span>Markdown-first</span><span>No affiliate links yet</span><span>Anonymous founder voice', '7 step-by-step guides</span><span>Markdown-first</span><span>No affiliate links yet</span><span>Technical and anonymous')
text=text.replace('7 posts. One tiny media brand.', '7 guides. One tiny media brand.')
text=text.replace('Written as an anonymous first-person build log, but structured like useful tutorial content for people searching how to build with AI agents, static hosting, Telegram distribution, and local media workflows.', 'Rewritten as anonymous first-person technical guides. Each episode includes concrete steps, commands, file paths, verification checks, and the tradeoffs behind the build.')
text=re.sub(r'<div class="post-grid">.*?</div></div></section><section class="section business">', '<div class="post-grid">'+cards+'</div></div></section><section class="section business">', text, flags=re.S)
text=re.sub(r'<script id="postData" type="application/json">.*?</script>', lambda m: '<script id="postData" type="application/json">'+post_json+'</script>', text, flags=re.S)
index.write_text(text)
print('rebuilt index.html with', len(posts), 'instructional posts')
