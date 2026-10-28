(() => {
'use strict';
const KEY='ray-fitness-v1', $=id=>document.getElementById(id);
const today=()=>{const d=new Date();return `${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,'0')}-${String(d.getDate()).padStart(2,'0')}`;};
const dateOK=s=>typeof s==='string' && /^\d{4}-\d{2}-\d{2}$/.test(s) && Number.isFinite(Date.parse(s+'T12:00:00Z')) && new Date(s+'T12:00:00Z').toISOString().slice(0,10)===s;
const offset=(s,n)=>{const d=new Date(s+'T12:00:00');d.setDate(d.getDate()+n);return `${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,'0')}-${String(d.getDate()).padStart(2,'0')}`;};
const weekday=s=>new Date(s+'T12:00:00').getDay();
const plans=[
 ['可选训练',[['轻量全身练习',2,'选择熟悉动作，按恢复情况调整'],['轻松步行 / 骑车',1,'20–30 分钟，可跳过']], '周日不计入四次必选训练；疲劳时休息即可。'],
 ['背 + 二头',[['高位下拉',3,'8–10 次 · 自选可控重量'],['坐姿划船',3,'8–10 次'],['单臂哑铃划船',2,'每侧 8–10 次'],['哑铃弯举',3,'8–10 次']], '先热身，正式组间充分休息。'],
 ['休息 / 恢复',[], '今天不安排力量训练，可轻松散步或做舒适的活动。'],
 ['胸 + 三头',[['杠铃卧推',3,'6–8 次 · 参考 40kg × 7'],['上斜哑铃卧推',3,'8–10 次 · 单手参考 10kg'],['蝴蝶机夹胸',3,'8–12 次 · 参考 23–29kg'],['三头下压',3,'8–12 次 · 按当天状态选重量']], '卧推先做低疲劳热身；上斜卧推组间参考休息 2–3 分钟。'],
 ['腿',[['腿举 / 深蹲（二选一）',3,'6–10 次 · 先掌握动作'],['罗马尼亚硬拉',3,'8–10 次 · 自选可控重量'],['腿弯举',3,'10–12 次'],['提踵',3,'12–15 次']], '保持动作可控，热身后再进入正式组。'],
 ['休息 / 恢复',[], '给肌肉恢复时间，今天无需补做力量训练。'],
 ['肩 + 核心',[['坐姿哑铃推肩',3,'8–10 次'],['哑铃侧平举',3,'10–15 次'],['反向飞鸟',3,'10–15 次'],['平板支撑',3,'20–45 秒 · 保持可控姿势']], '根据恢复情况调整重量与时长。']
];
const dietLabels=['热量约 2000–2200 kcal','蛋白质约 140–160g','饮食成本控制在 NZ$10–15 / 天','按免烹饪计划吃饭，并包含蔬果'];
// Generic estimates per 100g (milk per 100ml): kcal, protein grams, NZD.
const foods={oats:['燕麦',380,13,.4],milk:['低脂牛奶',50,3.6,.23],banana:['香蕉（可食部分）',89,1.1,.35],apple:['苹果',52,.3,.4],bread:['全麦面包',250,10,.55],chicken:['熟鸡肉（去骨可食部分）',165,31,1.8],veg:['即食沙拉 / 黄瓜小番茄',25,1,.6],cottage:['Cottage Cheese',85,12,1.5],pb:['花生酱',600,25,1],yogurt:['高蛋白原味酸奶',65,10,1.2],tuna:['水浸金枪鱼（沥干）',110,25,2]};
const recipes=[
 {name:'熟鸡三明治日',meals:[['早餐 · 冷泡燕麦',[['oats',100],['milk',300],['banana',120]]],['午餐 · 鸡肉沙拉三明治',[['bread',100],['chicken',180],['veg',150]]],['加餐 · 酸奶水果',[['yogurt',150],['apple',180],['milk',200]]],['晚餐 · 奶酪开放三明治',[['bread',100],['cottage',150],['pb',25],['veg',150]]]]},
 {name:'金枪鱼 + 熟鸡双拼日',meals:[['早餐 · 冷泡燕麦',[['oats',100],['milk',300],['banana',120]]],['午餐 · 金枪鱼奶酪三明治',[['bread',100],['tuna',100],['cottage',100],['veg',150]]],['加餐 · 酸奶水果',[['yogurt',150],['apple',180],['milk',200]]],['晚餐 · 鸡肉沙拉配面包',[['bread',120],['chicken',120],['pb',30],['veg',150]]]]},
 {name:'酸奶碗 + 熟鸡日',meals:[['早餐 · 冷泡燕麦酸奶碗',[['oats',100],['milk',250],['yogurt',200],['apple',180]]],['午餐 · 鸡肉三明治',[['bread',100],['chicken',180],['veg',150]]],['加餐 · 香蕉牛奶',[['milk',250],['banana',150],['pb',25]]],['晚餐 · 奶酪面包沙拉',[['bread',100],['cottage',150],['veg',150]]]]}
];
const sum=items=>items.reduce((a,[id,g])=>a.map((v,i)=>v+foods[id][i+1]*g/100),[0,0,0]);
let state={version:1,days:{},weights:{}}, storageBroken=false;
function validate(v){
 if(!v || v.version!==1 || !v.days || !v.weights || Array.isArray(v.days)||Array.isArray(v.weights))throw Error('格式不正确');
 const clean={version:1,days:{},weights:{}};
 if(Object.keys(v.days).length>20000||Object.keys(v.weights).length>20000)throw Error('记录过多');
 for(const [d,r] of Object.entries(v.days)){
  if(!dateOK(d)||!r||typeof r!=='object'||!Array.isArray(r.sets)||!Array.isArray(r.diet)||r.diet.length!==4||r.diet.some(x=>typeof x!=='boolean')||typeof r.done!=='boolean'||typeof r.notes!=='string'||r.notes.length>2000||!Number.isInteger(r.recipe)||r.recipe<0||r.recipe>=recipes.length)throw Error('每日记录格式不正确');
  const exercises=plans[weekday(d)][1];
  if(r.sets.length!==exercises.length||r.sets.some((a,i)=>!Array.isArray(a)||a.length!==exercises[i][1]||a.some(x=>typeof x!=='boolean')))throw Error('训练记录格式不正确');
  clean.days[d]={sets:r.sets.map(a=>a.slice()),diet:r.diet.slice(),done:r.done,notes:r.notes,recipe:r.recipe};
 }
 for(const [d,w] of Object.entries(v.weights)){if(!dateOK(d)||typeof w!=='number'||!Number.isFinite(w)||w<30||w>300)throw Error('体重记录格式不正确');clean.weights[d]=w;}
 return clean;
}
try{const saved=localStorage.getItem(KEY);if(saved)state=validate(JSON.parse(saved));}catch(e){storageBroken=true;$('save-status').textContent='无法读取本地数据；请先导出或恢复备份，当前修改不会覆盖原数据。';}
let selected=today();$('day').value=selected;
function record(){return state.days[selected]||(state.days[selected]={sets:plans[weekday(selected)][1].map(e=>Array(e[1]).fill(false)),diet:[false,false,false,false],done:false,notes:'',recipe:0});}
function persist(){
 if(storageBroken){$('save-status').textContent='本地保存不可用，请导出本次记录备份。';return;}
 try{localStorage.setItem(KEY,JSON.stringify(state));$('save-status').textContent='已自动保存到当前浏览器';}catch(e){$('save-status').textContent='保存失败（存储空间或权限），请立即导出备份。';}
}
function el(tag,text,cls){const n=document.createElement(tag);if(text!==undefined)n.textContent=text;if(cls)n.className=cls;return n;}
function check(label,checked,onChange){const l=el('label',undefined,'check'),i=document.createElement('input');i.type='checkbox';i.checked=checked;i.addEventListener('change',()=>onChange(i.checked));l.append(i,el('span',label));return l;}
function monday(){return offset(selected,-((weekday(selected)+6)%7));}
function stats(){const start=monday();let required=0,optional=0,diet=0;for(let i=0;i<7;i++){const d=offset(start,i),r=state.days[d];if(r?.done){if([1,3,4,6].includes(weekday(d)))required++;if(weekday(d)===0)optional++;}if(r?.diet.every(Boolean))diet++;}$('week-training').textContent=`${required} / 4${optional?' + 1 可选':''}`;$('week-diet').textContent=`${diet} / 7`;const entries=Object.entries(state.weights).sort();if(entries.length){const [d,w]=entries.at(-1);$('latest').textContent=`${w.toFixed(2)} kg`;$('weight-change').textContent=`${d} · 较参考 ${(w-87.14)>=0?'+':''}${(w-87.14).toFixed(2)} kg`;}else{$('latest').textContent='—';$('weight-change').textContent='参考体重不计为实测记录';}}
function renderTraining(){
 const r=record(),p=plans[weekday(selected)];$('workout-title').textContent=p[0];$('workout-note').textContent=p[2];$('exercises').replaceChildren();
 p[1].forEach(([name,n,hint],i)=>{
  const row=el('div',undefined,'exercise');const label=check('',r.sets[i].every(Boolean),v=>{r.sets[i].fill(v);if(!v)r.done=false;persist();renderTraining();stats();});label.lastChild.append(el('strong',name),el('small',`${n} 组 · ${hint}`));label.firstChild.setAttribute('aria-label',`${name}全部完成`);row.append(label);
  const sets=el('div',undefined,'sets');for(let j=0;j<n;j++){const l=check(`第${j+1}组`,r.sets[i][j],v=>{r.sets[i][j]=v;if(!v)r.done=false;persist();renderTraining();stats();});l.firstChild.setAttribute('aria-label',`${name}第${j+1}组`);sets.append(l);}row.append(sets);$('exercises').append(row);
 });
 const total=r.sets.flat();$('exercise-count').textContent=total.length?`${total.filter(Boolean).length} / ${total.length} 组`:'恢复日';$('training-label').textContent=p[1].length?'今日训练已完成':'今日已按计划休息 / 恢复';$('training-done').checked=r.done;$('notes').value=r.notes;
}
function renderRecipe(){const r=recipes[record().recipe],container=$('recipe');container.replaceChildren(el('h3',r.name));const totals=sum(r.meals.flatMap(m=>m[1]));const badges=el('div',undefined,'recipe-total');[`约 ${Math.round(totals[0])} kcal`,`蛋白质约 ${Math.round(totals[1])}g`,`约 NZ$${totals[2].toFixed(2)}`].forEach(t=>badges.append(el('span',t)));container.append(badges);r.meals.forEach(([name,items])=>{const meal=el('div',undefined,'meal'),a=sum(items);meal.append(el('strong',name),el('p',items.map(([id,g])=>`${foods[id][0]} ${g}${id==='milk'?'ml':'g'}`).join(' + ')),el('small',`约 ${Math.round(a[0])} kcal · ${Math.round(a[1])}g 蛋白质 · NZ$${a[2].toFixed(2)}`));container.append(meal);});}
function renderChart(){
 const entries=Object.entries(state.weights).sort();$('weight-history').replaceChildren();entries.slice().reverse().forEach(([d,w])=>{const row=el('div',undefined,'history-row');row.append(el('span',d),el('span',`${w.toFixed(2)} kg`));$('weight-history').append(row);});
 $('weight-input').value=state.weights[selected]??'';$('delete-weight').disabled=state.weights[selected]===undefined;
 if(!entries.length){$('chart').replaceChildren(el('div','保存第一次体重，开始绘制你的趋势。参考值 87.14kg 不会自动写入称重记录。','chart-empty'));return;}
 const ns='http://www.w3.org/2000/svg',svg=document.createElementNS(ns,'svg');svg.setAttribute('viewBox','0 0 800 260');svg.setAttribute('role','img');svg.setAttribute('aria-label',`体重趋势：${entries.length} 条记录，从 ${entries[0][1]}kg 到 ${entries.at(-1)[1]}kg。下方可查看全部记录。`);
 const values=entries.map(e=>e[1]),lo=Math.min(...values,87.14)-.7,hi=Math.max(...values,87.14)+.7,t0=Date.parse(entries[0][0]),t1=Date.parse(entries.at(-1)[0]),x=d=>t1===t0?420:70+(Date.parse(d)-t0)/(t1-t0)*680,y=w=>210-(w-lo)/(hi-lo)*180;
 function shape(tag,attrs,text){const n=document.createElementNS(ns,tag);Object.entries(attrs).forEach(([k,v])=>n.setAttribute(k,v));if(text)n.textContent=text;svg.append(n);return n;}
 for(let i=0;i<4;i++){const v=lo+(hi-lo)*i/3;shape('line',{x1:65,x2:760,y1:y(v),y2:y(v),stroke:'var(--line-strong)'});shape('text',{x:8,y:y(v)+4,fill:'var(--fg-subtle)','font-size':12},v.toFixed(1));}
 shape('line',{x1:65,x2:760,y1:y(87.14),y2:y(87.14),stroke:'var(--fg-subtle)','stroke-dasharray':'5 5'});shape('text',{x:70,y:y(87.14)-7,fill:'var(--fg-subtle)','font-size':11},'参考 87.14kg');
 shape('polyline',{points:entries.map(([d,w])=>`${x(d)},${y(w)}`).join(' '),fill:'none',stroke:'var(--accent)','stroke-width':3});
 entries.forEach(([d,w])=>{const c=shape('circle',{cx:x(d),cy:y(w),r:4,fill:'var(--accent)'});const t=document.createElementNS(ns,'title');t.textContent=`${d}: ${w.toFixed(2)}kg`;c.append(t);});
 shape('text',{x:70,y:245,fill:'var(--fg-subtle)','font-size':12},entries[0][0]);if(entries.length>1)shape('text',{x:750,y:245,fill:'var(--fg-subtle)','font-size':12,'text-anchor':'end'},entries.at(-1)[0]);$('chart').replaceChildren(svg);
}
function render(){
 $('day').value=selected;const r=record();$('week').replaceChildren();for(let i=0;i<7;i++){const d=offset(monday(),i),b=el('button');b.type='button';b.setAttribute('aria-pressed',String(d===selected));b.setAttribute('aria-label',`${d} ${plans[weekday(d)][0]}`);b.append(el('span',['周一','周二','周三','周四','周五','周六','周日'][i]),el('strong',d.slice(5)),el('small',plans[weekday(d)][0].split(' / ')[0]));b.onclick=()=>{selected=d;render();};$('week').append(b);}renderTraining();$('diet-checks').replaceChildren();dietLabels.forEach((t,i)=>$('diet-checks').append(check(t,r.diet[i],v=>{r.diet[i]=v;persist();stats();})));renderRecipe();renderChart();stats();
}
$('day').onchange=()=>{if(dateOK($('day').value)){selected=$('day').value;render();}else $('day').value=selected;};$('today').onclick=()=>{selected=today();render();};
$('training-done').onchange=e=>{record().done=e.target.checked;persist();stats();};$('notes').oninput=e=>{record().notes=e.target.value;persist();};
$('random-meal').onclick=()=>{const r=record();r.recipe=(r.recipe+1+Math.floor(Math.random()*(recipes.length-1)))%recipes.length;persist();renderRecipe();};
$('weight-form').onsubmit=e=>{e.preventDefault();if(!$('weight-form').reportValidity())return;const w=Number($('weight-input').value);if(!Number.isFinite(w)||w<30||w>300)return;state.weights[selected]=Math.round(w*100)/100;persist();renderChart();stats();};
$('delete-weight').onclick=()=>{if(confirm(`删除 ${selected} 的体重记录？`)){delete state.weights[selected];persist();renderChart();stats();}};
$('export').onclick=()=>{const blob=new Blob([JSON.stringify(state,null,2)],{type:'application/json'}),url=URL.createObjectURL(blob),a=el('a');a.href=url;a.download=`fitness-backup-${today()}.json`;a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);};
$('import').onchange=async e=>{const file=e.target.files[0];if(!file)return;try{if(file.size>5*1024*1024)throw Error('文件超过 5MB');const incoming=validate(JSON.parse(await file.text()));const n=Object.keys(incoming.days).length,w=Object.keys(incoming.weights).length;if(!confirm(`导入 ${n} 天打卡和 ${w} 条体重记录？相同日期将使用备份内容。`))return;state={version:1,days:{...state.days,...incoming.days},weights:{...state.weights,...incoming.weights}};storageBroken=false;persist();render();}catch(err){alert(`无法导入：${err.message}。原记录未改变。`);}finally{e.target.value='';}};
window.addEventListener('storage',e=>{if(e.key===KEY){try{state=e.newValue?validate(JSON.parse(e.newValue)):{version:1,days:{},weights:{}};render();$('save-status').textContent='已更新同一浏览器其他标签页的记录';}catch(err){$('save-status').textContent='其他标签页的数据格式异常，请先导出备份。';}}});
render();
})();
