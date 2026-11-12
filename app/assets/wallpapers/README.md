# Launcher wallpapers

The fifteen entries in `SOURCES.json` each have a background JPEG, a thumbnail and a small blurred panel backdrop. Four registered material JPEGs per image live in `../materials/`. All derived images retain the source photograph's terms.

Oliver's fork can add four more locally — JFK at the diner, Mustang at the villa, Superbird in the desert and Petty #43 — with `python3 scripts/apply-oliver-assets.py`. Those photos are his own and are never committed: the prepared files live in the gitignored `.local/oliver-wallpapers/` folder and the copied files are covered by `.gitignore`. The same script also installs the three transparent device photos (Apple TV 4K, PS5 Slim, Sky Stream box) from `.local/oliver-devices/` into `app/assets/devices/` for the Device Photos theme. Run the script with `--remove` before `npm run export:public` if the resulting widget might be shared.

Photo pages, authors and licence observations are in [asset sources](../../../docs/asset-sources.md). Generation instructions are in [asset generation](../../../docs/assets.md). Full-size originals remain outside the repository.
