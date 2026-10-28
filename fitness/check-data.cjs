// Verify menu arithmetic and backup validation using the app's own data definitions.
const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict');
const src=fs.readFileSync(__dirname+'/fitness.js','utf8');
const pre=src.slice(src.indexOf("const KEY="),src.indexOf('try{const saved='));
const ctx={document:{getElementById(){return {}}},Date};vm.createContext(ctx);
vm.runInContext(pre+';this.api={recipes,sum,validate,dateOK,offset,plans};',ctx);
const {recipes,sum,validate,dateOK,offset,plans}=ctx.api;
for(const r of recipes){const [k,p,c]=sum(r.meals.flatMap(m=>m[1]));assert(k>=2000&&k<=2200,r.name+' energy');assert(p>=140&&p<=160,r.name+' protein');assert(c>=10&&c<=15,r.name+' cost');console.log(r.name,Math.round(k)+' kcal',p.toFixed(1)+'g','NZ$'+c.toFixed(2));}
assert(!dateOK('2026-02-30'));assert(dateOK('2028-02-29'));assert.equal(offset('2026-12-31',1),'2027-01-01');
const valid={version:1,days:{'2026-10-28':{sets:plans[3][1].map(e=>Array(e[1]).fill(false)),diet:[true,false,true,false],done:false,notes:'test',recipe:1}},weights:{'2026-10-28':87.14}};
assert.equal(validate(valid).weights['2026-10-28'],87.14);
for(const bad of [null,{}, {...valid,version:2},{...valid,weights:{'2026-10-28':null}},{...valid,weights:{'2026-02-30':80}},{...valid,weights:{'2026-10-28':'80'}}])assert.throws(()=>validate(bad));
console.log('Menu targets, date boundaries and backup validation passed.');
