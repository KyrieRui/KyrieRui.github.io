import json,importlib.util,asyncio,re,sys
sys.path.insert(0,'site_src')
import grader
zh=json.load(open('ex_zh.json'))
EX={}
for i in range(1,6):
    spec=importlib.util.spec_from_file_location(f'ex{i}',f'tr/ex{i}.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);EX.update(m.EX)
out={};problems=0
for e in zh:
    k=f"{e['_lesson']}/{e['id']}";t=EX[k]
    sol=t['solution']
    stdout,err,g=asyncio.run(grader.run_code(sol))
    if err: print('ERR',k,err);problems+=1
    gr={}
    if 'requiredAst' in e['grading']: gr['requiredAst']=e['grading']['requiredAst']
    gr['stdoutEquals']=stdout
    if 'varsEqual' in e['grading']:
        gr['varsEqual']={n:grader._norm(g[n]) for n in e['grading']['varsEqual']}
    # same output for non-chinese originals?
    if not re.search(r'[一-鿿]',e['grading']['stdoutEquals']) and e['grading']['stdoutEquals']!=stdout:
        print('DIFF',k,repr(e['grading']['stdoutEquals']),repr(stdout));problems+=1
    # expected block in prompt
    blocks=[b for lang,b in re.findall(r'(?ms)^```(\w*)\n(.*?)^```',t['prompt']) if lang=='']
    if blocks and blocks[-1]!=stdout and k not in ('python12/01-detect-meta',):
        print('PROMPT-MISMATCH',k,repr(blocks[-1]),repr(stdout));problems+=1
    r=asyncio.run(grader.grade(sol,gr))
    if not r['ok']: print('FAIL',k,r);problems+=1
    r2=asyncio.run(grader.grade(t['starter'],gr))
    if r2['ok']: print('STARTER PASSES',k);problems+=1
    if re.search(r'[一-鿿]',json.dumps(t,ensure_ascii=False)): print('CHINESE',k);problems+=1
    out[k]=dict(id=e['id'],lesson=e['_lesson'],title=t['title'],prompt=t['prompt'],starterCode=t['starter'],solution=sol,grading=gr,hints=t['hints'])
json.dump(out,open('exercises_en.json','w'),ensure_ascii=False,indent=1)
print('problems',problems)
