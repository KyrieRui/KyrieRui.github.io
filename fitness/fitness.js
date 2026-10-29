(() => {
'use strict';
const M=FitnessModel;
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
let state={version:2,days:{},weights:{},templates:{}}, storageBroken=false;
const validate=v=>M.validate(v,plans,recipes.length);
try {
 const saved=localStorage.getItem(KEY);
 if(saved){const old=JSON.parse(saved);state=validate(old);if(old.version===1){localStorage.setItem(KEY+'-before-v2',saved);localStorage.setItem(KEY,JSON.stringify(state));$('save-status').textContent='旧记录已保留并升级，三餐记录从空白开始';}}
} catch(e){storageBroken=true;$('save-status').textContent='无法读取或迁移本地数据；不会覆盖原记录，请先恢复备份。';}
let selected=today();$('day').value=selected;
function record(){return state.days[selected]||(state.days[selected]=M.fresh(plans,selected,state.templates));}
function persist(){
 if(storageBroken){$('save-status').textContent='本地保存不可用，请导出本次记录备份。';return;}
 try{localStorage.setItem(KEY,JSON.stringify(state));$('save-status').textContent='已自动保存到当前浏览器';}catch(e){$('save-status').textContent='保存失败（存储空间或权限），请立即导出备份。';}
}
function el(tag,text,cls){const n=document.createElement(tag);if(text!==undefined)n.textContent=text;if(cls)n.className=cls;return n;}
function check(label,checked,onChange){const l=el('label',undefined,'check'),i=document.createElement('input');i.type='checkbox';i.checked=checked;i.addEventListener('change',()=>onChange(i.checked));l.append(i,el('span',label));return l;}
function monday(){return offset(selected,-((weekday(selected)+6)%7));}
function stats(){
 const start=monday();let required=0,optional=0,logged=0,foodDays=[];
 for(let i=0;i<7;i++){const d=offset(start,i),r=state.days[d];if(!r)continue;
  if(r.done){if([1,3,4,6].includes(weekday(d)))required++;if(weekday(d)===0)optional++;}
  const f=M.foodTotals(r);if(f.complete){logged++;foodDays.push(f.kcal);}
 }
 $('week-training').textContent=`${required} / 4${optional?' + 1 可选':''}`;$('week-diet').textContent=`${logged} / 7`;
 $('week-food-note').textContent=foodDays.length?`已完整记录日均 ${Math.round(foodDays.reduce((a,b)=>a+b,0)/foodDays.length)} kcal`:'仅统计三餐明确且确认记录完整的日期';
 const entries=Object.entries(state.weights).sort();if(entries.length){const [d,w]=entries.at(-1);$('latest').textContent=`${w.toFixed(2)} kg`;$('weight-change').textContent=`${d} · 较参考 ${(w-87.14)>=0?'+':''}${(w-87.14).toFixed(2)} kg`;}else{$('latest').textContent='—';$('weight-change').textContent='参考体重不计为实测记录';}
}
function button(text,fn){const b=el('button',text);b.type='button';b.onclick=fn;return b;}
function notice(text){$('save-status').textContent=text;}
function ask(text){return new Promise(resolve=>{const d=$('confirm-dialog');$('confirm-message').textContent=text;d.returnValue='cancel';d.addEventListener('close',()=>resolve(d.returnValue==='confirm'),{once:true});d.showModal();});}
function numberField(label,value,max,onChange,{min=0,step='any'}={}){
 const l=el('label',undefined,'field'),input=el('input');l.append(el('span',label),input);input.setAttribute('aria-label',label);input.type='number';input.min=min;input.max=max;input.step=step;input.inputMode='decimal';input.value=value??'';
 input.required=min>0;let lastValid=input.value;input.oninput=()=>{if(!input.validity.valid){notice(`请填写 ${min}–${max} 范围内的${label}，该数值尚未保存。`);return;}lastValid=input.value;const v=input.value===''?null:Number(input.value);onChange(v);};input.onblur=()=>{if(!input.validity.valid){input.value=lastValid;notice('无效数值已还原，请重新填写。');}};return l;
}
function selectField(label,value,options,onChange){const l=el('label',undefined,'field'),input=el('select');l.append(el('span',label),input);input.setAttribute('aria-label',label);options.forEach(([v,t])=>{const o=el('option',t);o.value=v;input.append(o);});input.value=value;input.onchange=()=>onChange(input.value);return l;}
function exercisePicker(value,onChange){const l=el('label',undefined,'field'),select=el('select');l.append(el('span','选择动作'),select);select.setAttribute('aria-label','选择动作');const blank=el('option','选择动作…');blank.value='';select.append(blank);const groups={};M.catalog.forEach(([name,group])=>{if(!groups[group]){groups[group]=el('optgroup');groups[group].label=group;select.append(groups[group]);}const o=el('option',name);o.value=name;groups[group].append(o);});if(value&&!M.catalog.some(x=>x[0]===value)){const o=el('option',value);o.value=value;select.append(o);}select.value=value;select.onchange=()=>{if(select.value)onChange(select.value);};return l;}
function trainingSummary(){const r=record(),sets=r.exercises.flatMap(e=>e.sets);$('exercise-count').textContent=sets.length?`${sets.filter(s=>s.done).length} / ${sets.length} 组`:'恢复日';$('training-done').checked=r.done;}
function renderEnergy(){const r=record(),e=M.energy(r,state.weights,selected);$('energy-total').textContent=e.kcal===null?'填写实际时长后显示估算':`本次总消耗约 ${e.kcal} kcal · 高于静息约 ${e.active} kcal`;$('energy-basis').textContent=`使用 ${e.kg.toFixed(2)}kg（${e.date||'初始参考体重'}），强度 ${r.met} MET。总消耗含同期静息消耗，不等于全天热量缺口，也不自动增加饮食额度。`;}
function renderTraining(){
 const r=record(),p=plans[weekday(selected)];$('workout-title').textContent=p[0];$('workout-note').textContent=p[2];$('exercises').replaceChildren();
 r.exercises.forEach((ex,i)=>{
  const card=el('article',undefined,'exercise-card'),head=el('div',undefined,'exercise-head');head.append(el('h3',`${i+1}. ${ex.name}`));
  const remove=button('移除动作',async()=>{if(await ask(`移除 ${ex.name} 及当天该动作记录？`)){r.exercises.splice(i,1);r.done=false;persist();renderTraining();stats();}});remove.setAttribute('aria-label',`移除动作 ${i+1}`);head.append(remove);card.append(head);
  const options=el('div',undefined,'edit-row');options.append(exercisePicker(ex.name,async name=>{if(await ask('替换动作会清空该动作当天的组记录，继续？')){r.exercises[i]=M.exercise(name);r.done=false;persist();renderTraining();stats();}else renderTraining();}),selectField('记录单位',ex.unit,[['次','次数'],['秒','秒数'],['分钟','分钟']],async v=>{if(ex.sets.some(s=>s.actual!==null||s.done)&&!await ask('切换单位会清空实际表现和完成勾选，保留目标数字供你调整，继续？')){renderTraining();return;}ex.unit=v;ex.sets.forEach(s=>{s.actual=null;s.done=false;});r.done=false;persist();renderTraining();stats();}));card.append(options);
  if(ex.hint)card.append(el('p',ex.hint,'fine'));card.append(el('p','重量填本组使用的重量；单侧哑铃按单手填写，自重动作可留空。目标数字可按当天状态调整。','fine'));
  ex.sets.forEach((set,j)=>{
   const row=el('div',undefined,'set-row'),status=el('span',undefined,'set-status');
   const updateStatus=()=>{status.textContent=set.actual===null?'未填实际表现':set.actual<set.target?`实际 ${set.actual}${ex.unit} / 目标 ${set.target}${ex.unit}`:`已达到目标 · ${set.actual}${ex.unit}`;status.className='set-status '+(set.actual!==null&&set.actual<set.target?'below':'');};updateStatus();
   const done=check(`第 ${j+1} 组`,set.done,v=>{set.done=v;if(!v)r.done=false;persist();trainingSummary();stats();});done.firstChild.setAttribute('aria-label',`${ex.name}第${j+1}组完成`);row.append(done);
   row.append(numberField(`目标（${ex.unit}）`,set.target,1000,v=>{if(v!==null&&v>0){set.target=v;persist();updateStatus();}},{min:1}),numberField('重量 kg',set.weight,1000,v=>{set.weight=v;persist();}),numberField(`实际（${ex.unit}）`,set.actual,1000,v=>{set.actual=v;persist();updateStatus();}));
   const del=button('删除组',async()=>{if((set.done||set.actual!==null)&&!await ask('删除本组实际记录？'))return;ex.sets.splice(j,1);r.done=false;persist();renderTraining();stats();});del.disabled=ex.sets.length===1;del.setAttribute('aria-label',`${ex.name}删除第${j+1}组`);row.append(del,status);card.append(row);
  });
  const add=button('+ 加一组',()=>{const last=ex.sets.at(-1);ex.sets.push(M.set(last.target,last.weight));r.done=false;persist();renderTraining();stats();});add.disabled=ex.sets.length>=30;add.setAttribute('aria-label',`${ex.name}加一组`);card.append(add);$('exercises').append(card);
 });
 trainingSummary();$('training-label').textContent=r.exercises.length?'今日训练已完成（可包含未达目标的组）':'今日已按计划休息 / 恢复';$('notes').value=r.notes;
 $('add-exercise-picker').replaceChildren(exercisePicker('',name=>{if(r.exercises.length>=30){notice('每天最多记录30个动作');return;}r.exercises.push(M.exercise(name));r.done=false;persist();renderTraining();stats();}));
 $('energy-inputs').replaceChildren(numberField('实际训练时长（分钟）',r.minutes,600,v=>{r.minutes=v;persist();renderEnergy();}),selectField('训练类型 / 强度',String(r.met),[['2.8','轻量核心 / 自重（2.8 MET）'],['3.5','常规多动作力量训练（3.5 MET）'],['6','高强度力量训练（6 MET）']],v=>{r.met=Number(v);persist();renderEnergy();}));renderEnergy();
}
const mealNames=['早餐','午餐','晚餐','额外加餐 / 饮料'],mealBudgets=[550,750,800,null];
function foodSummary(){const r=record(),f=M.foodTotals(r),container=$('food-summary');container.replaceChildren();
 container.append(el('strong',`${f.complete?'全天已记录':'当前已填小计'}：${Math.round(f.kcal)} kcal · ${f.proteinKnown?'蛋白质':'已填蛋白质'} ${Math.round(f.protein)}g`));
 let text=!f.caloriesKnown?'还有餐次未记录或未填热量，当前不是全天总摄入。':!r.foodComplete?'三餐已有记录；请确认零食、饮料等也已记完，再标记当天完整。':f.kcal>2200?`较初步目标上限多 ${Math.round(f.kcal-2200)} kcal。如实记录即可，下一餐按正常计划吃，不必通过漏餐或额外训练补偿。`:f.kcal<2000?`较初步目标下限少 ${Math.round(2000-f.kcal)} kcal。少吃一顿不等于达标，请同时关注蛋白质与营养。`:'当天摄入在初步热量目标范围内。';
 container.append(el('p',text),el('p',`${f.proteinKnown?'蛋白质已填写完整':'蛋白质尚有未填项'}；已填成本 NZ$${f.cost.toFixed(2)}${f.costKnown?'':'（部分成本未知）'}。${f.estimated?'包含估算值。':''}`,'fine'));
 $('food-complete').checked=r.foodComplete;stats();
}
function renderMeals(){const r=record();$('meal-log').replaceChildren();r.meals.forEach((meal,i)=>{
 const card=el('article',undefined,'meal-card');card.append(el('h3',mealNames[i]));if(mealBudgets[i])card.append(el('p',`可选分配参考约 ${mealBudgets[i]} kcal；重点看全天 2000–2200 kcal。`,'fine'));
 card.append(selectField(`${mealNames[i]}状态`,meal.status,[['unlogged','未记录（不当作零）'],['eaten','已吃'],['skipped',i===3?'没有额外摄入':'没吃这顿（计为零）']],v=>{meal.status=v;r.foodComplete=false;persist();renderMeals();}));
 if(meal.status==='eaten'){
  const l=el('label',undefined,'field'),note=el('textarea');note.rows=2;note.maxLength=2000;note.value=meal.text;note.placeholder='食物、份量、饮料、酱料；聚餐可先粗略记';l.append(el('span',`${mealNames[i]}吃了什么 / 份量`),note);note.oninput=()=>{meal.text=note.value;persist();};card.append(l);
  const fields=el('div',undefined,'meal-fields');fields.append(numberField(`${mealNames[i]}热量 kcal`,meal.kcal,20000,v=>{meal.kcal=v;r.foodComplete=false;persist();foodSummary();mealStatus();}),numberField(`${mealNames[i]}蛋白质 g`,meal.protein,1000,v=>{meal.protein=v;persist();foodSummary();}),numberField(`${mealNames[i]}费用 NZ$`,meal.cost,10000,v=>{meal.cost=v;persist();foodSummary();}));card.append(fields);
  card.append(check('外食 / 朋友聚餐',meal.social,v=>{meal.social=v;persist();}),check('营养数值是估算值',meal.estimated,v=>{meal.estimated=v;persist();foodSummary();}));
  const status=el('p',undefined,'fine');function mealStatus(){status.textContent=meal.kcal===null?'热量未知，先留空也可以；不会按零计算。':mealBudgets[i]&&meal.kcal>mealBudgets[i]?`比本餐参考多 ${Math.round(meal.kcal-mealBudgets[i])} kcal，查看全天合计即可。`:'';}mealStatus();card.append(status);
 }else card.append(el('p',meal.status==='skipped'?'本餐计为 0；之前填写的内容保留，切回“已吃”可恢复。':'尚未计入全天统计。','fine'));
 $('meal-log').append(card);
 });
 $('legacy-diet').hidden=!r.legacyDiet;if(r.legacyDiet)$('legacy-diet').textContent='旧版饮食打卡已保留：'+dietLabels.map((x,i)=>`${r.legacyDiet[i]?'✓':'—'} ${x}`).join('；')+'。旧打卡不会推算成三餐热量。';foodSummary();
}
function threeMeals(recipe){const m=recipe.meals;return [m[0],[m[1][0],m[1][1].concat(m[2][1].slice(1,2))],[m[3][0],m[3][1].concat(m[2][1].filter((_,i)=>i!==1))]];}
function renderRecipe(){const recipe=recipes[record().recipe],container=$('recipe');container.replaceChildren(el('h3',recipe.name));const totals=sum(recipe.meals.flatMap(m=>m[1]));const badges=el('div',undefined,'recipe-total');[`约 ${Math.round(totals[0])} kcal`,`蛋白质约 ${Math.round(totals[1])}g`,`约 NZ$${totals[2].toFixed(2)}`].forEach(t=>badges.append(el('span',t)));container.append(badges);
 threeMeals(recipe).forEach(([name,items],i)=>{const meal=el('div',undefined,'meal'),a=sum(items),description=items.map(([id,g])=>`${foods[id][0]} ${g}${id==='milk'?'ml':'g'}`).join(' + ');meal.append(el('strong',name),el('p',description),el('small',`约 ${Math.round(a[0])} kcal · ${Math.round(a[1])}g 蛋白质 · NZ$${a[2].toFixed(2)}`),button(`记入${mealNames[i]}`,async()=>{const r=record();if((r.meals[i].status!=='unlogged'||r.meals[i].text)&&!await ask(`用这份食谱替换${mealNames[i]}的记录？`))return;r.meals[i]={status:'eaten',text:description,kcal:Math.round(a[0]),protein:Math.round(a[1]*10)/10,cost:Math.round(a[2]*100)/100,social:false,estimated:true};r.foodComplete=false;persist();renderMeals();}));container.append(meal);});}
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
 $('day').value=selected;$('template-status').textContent='当天调整自动保存；模板只影响之后新建的日期。';const r=record();$('week').replaceChildren();for(let i=0;i<7;i++){const d=offset(monday(),i),b=el('button');b.type='button';b.setAttribute('aria-pressed',String(d===selected));b.setAttribute('aria-label',`${d} ${plans[weekday(d)][0]}`);b.append(el('span',['周一','周二','周三','周四','周五','周六','周日'][i]),el('strong',d.slice(5)),el('small',plans[weekday(d)][0].split(' / ')[0]));b.onclick=()=>{selected=d;render();};$('week').append(b);}renderTraining();renderMeals();renderRecipe();renderChart();stats();
}
$('day').onchange=()=>{if(dateOK($('day').value)){selected=$('day').value;render();}else $('day').value=selected;};$('today').onclick=()=>{selected=today();render();};
$('training-done').onchange=e=>{record().done=e.target.checked;persist();stats();};$('notes').oninput=e=>{record().notes=e.target.value;persist();};
$('food-complete').onchange=e=>{record().foodComplete=e.target.checked;persist();foodSummary();};
$('save-template').onclick=async()=>{if(await ask('将当天动作、组数、目标及重量保存为该星期几的模板？实际表现不会复制，已存在的日期记录不变。')){state.templates[weekday(selected)]=M.resetPerformance(record().exercises);persist();$('template-status').textContent='已保存：以后新建的同星期日期使用此模板。';}};
$('restore-plan').onclick=async()=>{if(await ask('恢复当天默认动作会清空当天逐组记录；备注、饮食和体重保留。继续？')){record().exercises=M.defaults(plans,weekday(selected));record().done=false;persist();renderTraining();stats();}};
$('reset-template').onclick=async()=>{if(await ask('清除此星期几的自定义模板？已记录日期不会改变。')){delete state.templates[weekday(selected)];persist();$('template-status').textContent='以后新建日期使用默认安排。';}};
$('add-custom').onclick=()=>{const name=$('custom-exercise').value.trim();if(!name||name.length>100)return;if(record().exercises.length>=30){notice('每天最多记录30个动作');return;}record().exercises.push(M.exercise(name));record().done=false;$('custom-exercise').value='';persist();renderTraining();stats();};
$('random-meal').onclick=()=>{const r=record();r.recipe=(r.recipe+1+Math.floor(Math.random()*(recipes.length-1)))%recipes.length;persist();renderRecipe();};
$('weight-form').onsubmit=e=>{e.preventDefault();if(!$('weight-form').reportValidity())return;const w=Number($('weight-input').value);if(!Number.isFinite(w)||w<30||w>300)return;state.weights[selected]=Math.round(w*100)/100;persist();renderChart();renderEnergy();stats();};
$('delete-weight').onclick=async()=>{if(await ask(`删除 ${selected} 的体重记录？`)){delete state.weights[selected];persist();renderChart();renderEnergy();stats();}};
$('export').onclick=()=>{const blob=new Blob([JSON.stringify(state,null,2)],{type:'application/json'}),url=URL.createObjectURL(blob),a=el('a');a.href=url;a.download=`fitness-backup-${today()}.json`;a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);};
$('import').onchange=async e=>{const file=e.target.files[0];if(!file)return;try{if(file.size>5*1024*1024)throw Error('文件超过 5MB');const incoming=validate(JSON.parse(await file.text()));const n=Object.keys(incoming.days).length,w=Object.keys(incoming.weights).length;if(!await ask(`导入 ${n} 天打卡和 ${w} 条体重记录？相同日期和星期模板将使用备份内容。`))return;state={version:2,days:{...state.days,...incoming.days},weights:{...state.weights,...incoming.weights},templates:{...state.templates,...incoming.templates}};storageBroken=false;persist();render();}catch(err){notice(`无法导入：${err.message}。原记录未改变。`);}finally{e.target.value='';}};
window.addEventListener('storage',e=>{if(e.key===KEY){try{state=e.newValue?validate(JSON.parse(e.newValue)):{version:2,days:{},weights:{},templates:{}};render();$('save-status').textContent='已更新同一浏览器其他标签页的记录';}catch(err){$('save-status').textContent='其他标签页的数据格式异常，请先导出备份。';}}});
render();
})();
