import markdown,re
md=markdown.Markdown(extensions=['toc','tables','extra'])
body=md.convert(open('policy.md').read())
body=re.sub(r'<h1[^>]*>.*?</h1>','',body,count=1)
toc=''.join(f'<li><a href="#{t["id"]}">{t["name"]}</a></li>' for t in md.toc_tokens[0]['children'])
def page(title,main):
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="referrer" content="no-referrer"><title>{title}</title><link rel="stylesheet" href="style.css"></head>
<body><header><div class="wrap"><a class="brand" href="index.html">The Arnold Institute of Broscience</a>
<nav><a href="index.html">Home</a><a href="privacy.html">Privacy Policy</a></nav></div></header>
<main class="wrap">{main}</main>
<footer><div class="wrap">&copy; 2026 The Arnold Institute of Broscience &middot; <a href="privacy.html">Privacy Policy</a> &middot; <a href="mailto:arnoldinstitute@mail.grokbot.com">arnoldinstitute@mail.grokbot.com</a></div></footer>
</body></html>
'''
open('privacy.html','w').write(page('Privacy Policy — The Arnold Institute of Broscience',
 f'<h1>Privacy Policy</h1><nav class="toc" aria-label="Contents"><h2>Contents</h2><ol>{toc}</ol></nav><article>{body}</article>'))
open('index.html','w').write(page('The Arnold Institute of Broscience','''<h1>The Arnold Institute of Broscience</h1>
<p class="lead">A personal, non-commercial n-of-1 health research project. One subject, one variable at a time, and written results.</p>
<p>The Institute does not offer services to the public and does not provide medical advice.</p>
<h2 id="research">Research</h2>
<a class="card" href="research/the-way-back-to-the-table.html"><span class="card-kicker">Research Note</span>
<span class="card-title">The Way Back to the Table</span>
<span class="card-text">A 0–10 scale of how hard each food works your stomach, for easing back after a stomach bug, plus guidance on movement and the gut.</span></a>
<h2>About</h2>
<ul><li><a href="privacy.html">Privacy Policy</a></li>
<li>Contact: <a href="mailto:arnoldinstitute@mail.grokbot.com">arnoldinstitute@mail.grokbot.com</a></li></ul>'''))
