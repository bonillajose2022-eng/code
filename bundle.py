"""Emit a standalone entrypoint: no modules, fetches or external assets at runtime."""
from pathlib import Path
import base64,re,json
root=Path(__file__).resolve().parents[1]
d=root/'dist' if (root/'dist').is_dir() else root
assets={p.name:'data:image/svg+xml;base64,'+base64.b64encode(p.read_bytes()).decode() for p in (d/'assets/images').glob('*.svg')}
source=[]
for f in ['data/missions.js','utils/engine.js','utils/storage.js','utils/reports.js','script.js']:
 s=(d/f).read_text()
 s=re.sub(r'^import .*?;\n','',s,flags=re.M)
 s=re.sub(r'^export ','',s,flags=re.M)
 source.append(s)
js='\n'.join(source)
js='const embeddedImages='+json.dumps(assets)+';\n'+js
js=js.replace('src="assets/images/agency.svg"','src="${embeddedImages[\'agency.svg\']}"')
js=js.replace('src="assets/images/mission-${selected*4+current+1}.svg"','src="${embeddedImages[`mission-${selected*4+current+1}.svg`]}"')
html=(root/'tools/index.template.html').read_text()
html=html.replace('href="assets/images/agency.svg"',f'href="{assets["agency.svg"]}"')
html=html.replace('src="assets/images/agency.svg"',f'src="{assets["agency.svg"]}"')
html=html.replace('<link rel="stylesheet" href="styles.css">','<style>'+ (d/'styles.css').read_text()+'</style>')
fallback='<p class="eyebrow">ASPAEN NEIVA / ENGLISH ESCAPE ROOM</p><h1>THE SECRET CODE</h1><p>The operation is loading. If it does not start, enable JavaScript in your browser and reopen this file.</p><noscript>JavaScript is required to play.</noscript>'
html=html.replace('<main id="app"></main>','<main id="app">'+fallback+'</main>')
boot="""window.addEventListener('error',function(event){var panel=document.getElementById('app');if(panel&&!document.getElementById('start')){var p=document.createElement('p');p.textContent='The game could not start. Please reopen the downloaded index.html in an up-to-date browser. Error: '+event.message;panel.appendChild(p);}});"""
html=html.replace('<script type="module" src="script.js"></script>','<script>'+boot+'\n(function(){\n'+js.replace('</script','<\\/script')+'\n})();</script>')
(d/'index.html').write_text(html)
(root/'tests/standalone-bundle.js').write_text('(function(){\n'+js+'\n})();')
print('Standalone HTML:',len(html.encode()),'bytes;',len(assets),'embedded SVGs')
