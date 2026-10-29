const key='aspaen-secret-code-v1';
export function read(){try{const x=JSON.parse(localStorage.getItem(key));return x&&x.version===1&&x.games&&x.settings?x:null;}catch{return null;}}
export function save(data){try{localStorage.setItem(key,JSON.stringify(data));return true;}catch{return false;}}
export function erase(){localStorage.removeItem(key);}
