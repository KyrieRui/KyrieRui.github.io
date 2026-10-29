/* Data model shared by the browser and offline regression checks. */
(function(root){
'use strict';
const clone=x=>JSON.parse(JSON.stringify(x));
const catalog=[
 ['高位下拉','背',10],['坐姿划船','背',10],['单臂哑铃划船','背',10],['辅助引体向上','背',8],['胸托划船','背',10],
 ['哑铃弯举','二头',10],['锤式弯举','二头',10],['绳索弯举','二头',12],
 ['杠铃卧推','胸',8,40],['上斜哑铃卧推','胸',10,10],['蝴蝶机夹胸','胸',12,29],['器械推胸','胸',10],['俯卧撑','胸',10],
 ['三头下压','三头',12],['绳索过头臂屈伸','三头',12],
 ['腿举','腿',10],['高脚杯深蹲','腿',10],['罗马尼亚硬拉','腿',10],['腿弯举','腿',12],['腿屈伸','腿',12],['提踵','腿',15],['保加利亚分腿蹲','腿',8],
 ['坐姿哑铃推肩','肩',10],['哑铃侧平举','肩',15],['反向飞鸟','肩',15],['绳索面拉','肩',15],
 ['平板支撑','核心',30,null,'秒'],['死虫','核心',10],['绳索卷腹','核心',12],['侧平板支撑','核心',20,null,'秒'],
 ['轻松步行 / 骑车','有氧',25,null,'分钟']
];
const validDate=s=>typeof s==='string'&&/^\d{4}-\d{2}-\d{2}$/.test(s)&&Number.isFinite(Date.parse(s+'T12:00:00Z'))&&new Date(s+'T12:00:00Z').toISOString().slice(0,10)===s;
const dayOf=s=>new Date(s+'T12:00:00').getDay();
const set=(target=10,weight=null)=>({target,weight,actual:null,done:false});
function exercise(name,count=3,hint=''){const c=catalog.find(x=>x[0]===name);return {name,unit:c?.[4]||'次',hint,sets:Array.from({length:count},()=>set(c?.[2]||10,c?.[3]??null))};}
function defaults(plans,w){return plans[w][1].map(([name,n,hint])=>exercise(name==='腿举 / 深蹲（二选一）'?'腿举':name,n,hint));}
function resetPerformance(list){return clone(list).map(e=>({...e,sets:e.sets.map(s=>({...s,actual:null,done:false}))}));}
const meal=()=>({status:'unlogged',text:'',kcal:null,protein:null,cost:null,social:false,estimated:true});
function fresh(plans,d,templates={}){return {exercises:resetPerformance(templates[dayOf(d)]||defaults(plans,dayOf(d))),done:false,notes:'',recipe:0,minutes:null,met:3.5,meals:[meal(),meal(),meal(),{...meal(),status:'skipped'}],foodComplete:false,legacyDiet:null};}
function foodTotals(r){
 const eaten=r.meals.filter(m=>m.status==='eaten');
 const total=k=>eaten.reduce((s,m)=>s+(m[k]??0),0);
 const caloriesKnown=r.meals.every(m=>m.status==='skipped'||(m.status==='eaten'&&m.kcal!==null));
 const proteinKnown=r.meals.every(m=>m.status==='skipped'||(m.status==='eaten'&&m.protein!==null));
 return {kcal:total('kcal'),protein:total('protein'),cost:total('cost'),caloriesKnown,proteinKnown,costKnown:r.meals.every(m=>m.status==='skipped'||(m.status==='eaten'&&m.cost!==null)),complete:r.foodComplete&&caloriesKnown,estimated:eaten.some(m=>m.estimated)};
}
function energy(r,weights,date){const latest=Object.keys(weights).filter(d=>d<=date).sort().at(-1);const kg=latest?weights[latest]:87.14;return {kg,date:latest||null,kcal:r.minutes===null?null:Math.round(r.met*3.5*kg/200*r.minutes),active:r.minutes===null?null:Math.round((r.met-1)*3.5*kg/200*r.minutes)};}
function validate(input,plans,recipeCount){
 const obj=x=>x&&typeof x==='object'&&!Array.isArray(x);
 const fail=()=>{throw Error('备份内容或数值格式不正确');};
 const str=(x,max)=>typeof x==='string'&&x.length<=max;
 const num=(x,max,nullable=true)=>nullable&&x===null||typeof x==='number'&&Number.isFinite(x)&&x>=0&&x<=max;
 if(!obj(input)||![1,2].includes(input.version)||!obj(input.days)||!obj(input.weights)||Object.keys(input.days).length>20000||Object.keys(input.weights).length>20000)fail();
 const v={version:2,days:{},weights:{},templates:{}};
 function exercises(list){if(!Array.isArray(list)||list.length>30)fail();return list.map(e=>{if(!obj(e)||!str(e.name,100)||!e.name.trim()||!['次','秒','分钟'].includes(e.unit)||!str(e.hint,300)||!Array.isArray(e.sets)||e.sets.length<1||e.sets.length>30)fail();return {name:e.name,unit:e.unit,hint:e.hint,sets:e.sets.map(s=>{if(!obj(s)||!num(s.target,1000,false)||s.target<=0||!num(s.weight,1000)||!num(s.actual,1000)||typeof s.done!=='boolean')fail();return {target:s.target,weight:s.weight,actual:s.actual,done:s.done};})};});}
 for(const [d,w] of Object.entries(input.weights)){if(!validDate(d)||!num(w,300,false)||w<30)fail();v.weights[d]=w;}
 if(input.version===2){if(!obj(input.templates))fail();for(const [day,list] of Object.entries(input.templates)){if(!/^[0-6]$/.test(day))fail();v.templates[day]=resetPerformance(exercises(list));}}
 for(const [d,raw] of Object.entries(input.days)){
  if(!validDate(d)||!obj(raw)||typeof raw.done!=='boolean'||!str(raw.notes,2000)||!Number.isInteger(raw.recipe)||raw.recipe<0||raw.recipe>=recipeCount)fail();
  if(input.version===1){
   const expected=plans[dayOf(d)][1];if(!Array.isArray(raw.sets)||raw.sets.length!==expected.length||raw.sets.some((a,i)=>!Array.isArray(a)||a.length!==expected[i][1]||a.some(b=>typeof b!=='boolean'))||!Array.isArray(raw.diet)||raw.diet.length!==4||raw.diet.some(b=>typeof b!=='boolean'))fail();
   const r=fresh(plans,d);r.exercises.forEach((e,i)=>e.sets.forEach((s,j)=>s.done=raw.sets[i][j]));Object.assign(r,{done:raw.done,notes:raw.notes,recipe:raw.recipe,legacyDiet:raw.diet.slice()});v.days[d]=r;
  }else{
   if(!num(raw.minutes,600)||![2.8,3.5,6].includes(raw.met)||typeof raw.foodComplete!=='boolean'||!Array.isArray(raw.meals)||raw.meals.length!==4||!(raw.legacyDiet===null||Array.isArray(raw.legacyDiet)&&raw.legacyDiet.length===4&&raw.legacyDiet.every(x=>typeof x==='boolean')))fail();
   const meals=raw.meals.map(m=>{if(!obj(m)||!['unlogged','eaten','skipped'].includes(m.status)||!str(m.text,2000)||!num(m.kcal,20000)||!num(m.protein,1000)||!num(m.cost,10000)||typeof m.social!=='boolean'||typeof m.estimated!=='boolean')fail();return {status:m.status,text:m.text,kcal:m.kcal,protein:m.protein,cost:m.cost,social:m.social,estimated:m.estimated};});
   v.days[d]={exercises:exercises(raw.exercises),done:raw.done,notes:raw.notes,recipe:raw.recipe,minutes:raw.minutes,met:raw.met,meals,foodComplete:raw.foodComplete,legacyDiet:raw.legacyDiet};
  }
 }
 return v;
}
const api={catalog,clone,set,exercise,defaults,resetPerformance,fresh,foodTotals,energy,validate};
if(typeof module!=='undefined'&&module.exports)module.exports=api;else root.FitnessModel=api;
})(typeof window==='undefined'?{}:window);
