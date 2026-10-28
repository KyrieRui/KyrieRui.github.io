# Fitness tracker

Static, buildless tracker at `/fitness/`. Uses the existing site CSS variables and theme script. Edit `index.html`, `fitness.css` and `fitness.js` directly. The tutorial generator copies this directory to its output; its shared navigation template and source CSS/JS also include the categories.

## Data

`ray-fitness-v1` in localStorage: `{version:1, days:{"YYYY-MM-DD":{sets:boolean[][],diet:boolean[4],done:boolean,notes:string,recipe:number}},weights:{"YYYY-MM-DD":number}}`.
Dates use the device's local calendar. Weeks begin Monday. Four required training days and optional Sunday are counted separately. Rest-day confirmation does not count as a training session. Daily completion is a separate confirmation to allow modified sessions. Unchecking an exercise clears daily completion. Reference weight 87.14kg is not a fabricated dated measurement.

JSON export/import transfers data manually. Import validates all entries before merging; imported dates replace matching dates after confirmation. Data stays in the browser and is never committed or sent to a server. A separate authenticated backend would be needed for automatic device synchronization.

## Meal estimates

Three whole-day menus, randomized without immediately repeating the current selection. Nutrients and cost are summed from the per-100g food estimates in `fitness.js` (milk per 100ml). Costs are consumed-portion estimates using budget/private-label or promotional products, not live quotes or whole-package shopping costs. All menus are within 2000–2200 kcal, 140–160g protein and NZ$10–15 under those assumptions. Use actual product labels and local prices. Oats need refrigerated soaking and chicken must be fully cooked/ready to eat.

## Verification

Run `node --check fitness/fitness.js` and `node fitness/check-data.cjs` from the repo root. Serve the repo root and check date isolation, exercise/group toggles, reload persistence, daily diet, weight add/update/delete, random menus, mobile widths, light/dark themes, and JSON backup round-trip. All browser QA records belong to localhost only.
