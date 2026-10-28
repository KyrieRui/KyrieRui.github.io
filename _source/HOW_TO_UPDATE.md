# How to update the tutorial site

The website at the repo root is generated from this `_source` folder with MkDocs Material.

1. Edit the Markdown files in `_source/Article/`.
2. Rebuild:

   ```bash
   cd _source
   pip install -r requirements.txt
   mkdocs build -d /tmp/site_build
   ```

3. Copy everything in `/tmp/site_build/` to the repo root (overwriting the old pages), keep `.nojekyll`, `survivor/` and `_source/`, then commit and push.
