# Fitness tracker

Buildless static tracker at `/fitness/`, using the existing site theme. Edit `index.html`, `fitness.css`, `model.js` and `fitness.js`. The tutorial generator preserves this directory. Category links remain hidden per the user's preference.

## Training

The weekly default split is back/biceps Monday, chest/triceps Wednesday, legs Thursday, shoulders/core Saturday, optional Sunday. The catalog includes 31 choices plus custom names. Each dated exercise snapshot stores its own set list, target, working weight, actual result, unit (reps/seconds/minutes) and completion. Blank actual results stay unknown; completion does not claim the target was achieved.

Adding/deleting sets and replacing exercises changes only the selected date. Saving a weekly template strips actual results/completions and affects only dates created afterward. Existing dated records are never regenerated from templates. Resetting the template does not reset past records. Destructive edits have an accessible modal confirmation.

## Energy estimate

Total kcal = MET × 3.5 × kg / 200 × minutes. Active kcal above rest uses MET − 1. MET choices: light core/bodyweight 2.8, multiple-exercise resistance 3.5, vigorous resistance 6.0, based on https://pacompendium.com/conditioning-exercise/ (2024 Adult Compendium). The latest dated weight on/before the workout is used, or the explicitly marked 87.14kg reference. Duration is actual session time including normal rests, excluding long unrelated breaks. No estimate without duration. This is not a daily deficit calculation, does not infer energy from repetitions, and does not raise the food allowance.

## Three-meal diary

Breakfast/lunch/dinner plus an optional extras/drinks bucket. States: unlogged, eaten, skipped. Skipped counts as zero; unlogged or missing kcal prevents claiming a complete total. Meal values are aggregate intake for that meal, with food/portion notes, kcal, protein, cost, social-meal flag and estimate flag. Switching to skipped retains existing details for later recovery but excludes them from totals. Weekly averages include only days explicitly marked complete with all kcal accounted for. Unknown protein/cost remain marked partial. Three recipe menus retain the original daily food totals and allow individually copying a meal into the diary after overwrite confirmation.

## Persistence / migration

localStorage key remains `ray-fitness-v1`; stored schema is version 2 with `days`, `weights`, `templates`. Keeping the original key ensures existing users are found. Version 1 is validated and migrated, original serialized data is backed up under `ray-fitness-v1-before-v2` before writing v2. Legacy checkmarks, completion, notes, recipe and weights are preserved. Legacy diet checkmarks remain visible but cannot imply fabricated food calories. Migration/storage failures show a warning and do not overwrite original data.

JSON backups accept versions 1 and 2, validate fully before mutation, then merge dates/weights/templates after confirmation. Data never uploads to the repository or a backend. Cross-device transfer uses export/import; automatic synchronization requires an authenticated service.

## Checks

`node --check fitness/fitness.js`, `node --check fitness/model.js`, `node fitness/check-data.cjs`.
Regression checks cover v1 migration, v2 backup round-trip, editable set preservation, template isolation, unknown/skipped/social meal totals, date boundaries, invalid backup data and historical-weight energy estimates. Browser checks cover add/remove/replace actions, low actual reps, refresh persistence, selecting dates, weekly templates, recipe-to-meal logging, export/import, and 390px/1280px layouts. Browser QA uses localhost data only.
