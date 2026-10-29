export const fresh = (minutes=17)=>({agency:'',completed:0,current:0,answers:[[],[],[],[]],attempts:[0,0,0,0],hints:[0,0,0,0],digits:[],remaining:minutes*60,duration:minutes*60,running:false,deadline:null,won:false,date:new Date().toISOString(),elapsed:0});
export function remaining(s,now=Date.now()){return s.running?Math.max(0,Math.ceil((s.deadline-now)/1000)):s.remaining;}
export function pause(s,now=Date.now()){const r=remaining(s,now);if(s.running)s.elapsed+=Math.max(0,s.remaining-r);s.remaining=r;s.running=false;s.deadline=null;}
export function start(s,now=Date.now()){if(!s.running&&s.remaining>0&&!s.won){s.running=true;s.deadline=now+s.remaining*1000;}}
export function score(s){return s.won?100:Math.max(25,Math.min(75,s.completed*25));}
export function canOpen(s,index){return Number.isInteger(index)&&index>=0&&index<4&&index<=s.completed;}
export function verify(s,index,value,correct,{teacherMode=false,approved=false}={}){if(remaining(s)<=0)return 'expired';if(s.won||index!==s.completed||index>3)return 'locked';if(!/^\d$/.test(value))return 'invalid';if(!approved)s.attempts[index]++;if(Number(value)!==correct)return 'wrong';if(teacherMode&&!approved)return 'approval';s.digits.push(value);s.completed++;s.current=Math.min(3,s.completed);return 'correct';}
export function unlockVault(s,code,expected){if(remaining(s)<=0)return 'expired';if(s.completed!==4)return 'locked';if(!/^\d{4}$/.test(code)||code!==expected)return 'wrong';pause(s);s.won=true;return 'correct';}
