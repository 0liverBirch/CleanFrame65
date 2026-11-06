"""Install Oliver's personal assets into a local checkout: Frame-art wallpapers
and Device Photos for the Device Photos theme.

The four photos (JFK at the diner, Mustang at the villa, Superbird in the
desert, Petty #43) and the three device photos (Apple TV 4K + remote, PS5
Slim + controller, Sky Q box) are Oliver's own images. They are NOT in this
repository: this fork is public, and committing them would publish his
personal photos.

Prepared files live in the gitignored folders `.local/oliver-wallpapers/`
(28 files: background, thumbnail, panel backdrop and the four registered
glass materials per photo) and `.local/oliver-devices/` (3 transparent PNGs),
each with a MANIFEST.json of sizes and SHA-256 hashes. Those folders are
local-only: they are made on Oliver's Mac from his own Frame-art collection
in `~/workspace/your_files/frame-art/` (see OLIVER-HANDOVER.md), and they are
never pushed to GitHub.

Usage, from the repository root:

    python3 scripts/apply-oliver-assets.py           # install
    python3 scripts/apply-oliver-assets.py --check    # report state only
    python3 scripts/apply-oliver-assets.py --remove   # undo the install

Install copies the prepared files into app/assets/wallpapers/,
app/assets/materials/ and app/assets/devices/, and inserts the four entries
at the top of app/assets/wallpapers/SOURCES.json and
app/assets/wallpapers/catalog.js. The copied files are covered by
.gitignore, so `git status` stays clean and they cannot be committed by
accident. Run `npm run check` afterwards.

Remove deletes the copied files and drops the four catalogue entries again,
restoring the upstream catalogues. Do that before `npm run export:public`
if the resulting .wgt might be shared: the public export zips everything in
app/, so an export built while the photos are installed would contain them.
"""

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WALLPAPER_SOURCE = ROOT / '.local/oliver-wallpapers'
DEVICE_SOURCE = ROOT / '.local/oliver-devices'
WALLPAPERS = ROOT / 'app/assets/wallpapers'
MATERIALS = ROOT / 'app/assets/materials'
DEVICES = ROOT / 'app/assets/devices'

PHOTOS = [
    ('jfk-diner', 'JFK at the diner'),
    ('mustang-villa', 'Mustang at the villa'),
    ('superbird-desert', 'Superbird in the desert'),
    ('petty-43', 'Petty #43'),
]
IDS = [photo[0] for photo in PHOTOS]

# Files per photo: background, thumbnail and panel go to wallpapers/;
# the four registered materials go to materials/.
WALLPAPER_FILES = ['{id}.jpg', '{id}-thumb.jpg', '{id}-panel.jpg']
MATERIAL_FILES = ['{id}-field-blur.jpg', '{id}-field-frost.jpg',
                  '{id}-field-clear.jpg', '{id}-study-soft.jpg']

# Device Photos theme: transparent PNGs of the actual boxes, one per tile.
DEVICE_FILES = ['appletv-4k.png', 'ps5-slim.png', 'sky-q.png']


def wallpaper_files():
    for id_, _name in PHOTOS:
        for pattern in WALLPAPER_FILES:
            yield pattern.format(id=id_), WALLPAPERS
        for pattern in MATERIAL_FILES:
            yield pattern.format(id=id_), MATERIALS


def device_files():
    for name in DEVICE_FILES:
        yield name, DEVICES


def file_hash(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_source(source, files):
    """Check every prepared file is present and matches MANIFEST.json."""
    missing, bad = [], []
    manifest_path = source / 'MANIFEST.json'
    manifest = {}
    if manifest_path.is_file():
        manifest = json.loads(manifest_path.read_text()).get('files', {})
    else:
        print('No MANIFEST.json in ' + str(source) + '; copying by filename only.')
    for name, _dest in files:
        path = source / name
        if not path.is_file():
            missing.append(name)
            continue
        if name in manifest:
            want = manifest[name]
            if path.stat().st_size != want['bytes'] or file_hash(path) != want['sha256']:
                bad.append(name)
    return missing, bad


def sources_entry(id_, name):
    return {'id': id_, 'name': name, 'src': 'assets/wallpapers/' + id_ + '.jpg',
            'thumb': 'assets/wallpapers/' + id_ + '-thumb.jpg', 'pos': '50% 50%',
            'tone': 'light', 'credit': 'Oliver Birch',
            'source': 'Personal Frame art collection'}


CATALOG_TEMPLATE = """  {{
    "id": "{id}",
    "name": "{name}",
    "src": "assets/wallpapers/{id}.jpg",
    "thumb": "assets/wallpapers/{id}-thumb.jpg",
    "tone": "light",
    "ut": {{
      "tr": "mist",
      "br": "mist"
    }},
    "frostVeil": 0.2,
    "listColumn": 0,
    "dockQuiet": false,
    "clockMist": false
  }},
"""

START_MARKER = '  /* Oliver wallpapers: local-only, installed by scripts/apply-oliver-assets.py. */\n'
END_MARKER = '  /* End Oliver wallpapers. */\n'


def catalog_block():
    entries = ''.join(CATALOG_TEMPLATE.format(id=id_, name=name) for id_, name in PHOTOS)
    return START_MARKER + entries + END_MARKER


def install():
    if not WALLPAPER_SOURCE.is_dir():
        print('Missing source folder: ' + str(WALLPAPER_SOURCE))
        print('Prepare it from Oliver\'s Frame-art originals (see OLIVER-HANDOVER.md).')
        return 1
    missing, bad = verify_source(WALLPAPER_SOURCE, list(wallpaper_files()))
    if missing:
        print('Missing prepared files in ' + str(WALLPAPER_SOURCE) + ': ' + ', '.join(missing))
        return 1
    if bad:
        print('Files do not match MANIFEST.json (re-prepare them): ' + ', '.join(bad))
        return 1
    devices_ok = DEVICE_SOURCE.is_dir()
    if devices_ok:
        missing, bad = verify_source(DEVICE_SOURCE, list(device_files()))
        if missing:
            print('Missing prepared files in ' + str(DEVICE_SOURCE) + ': ' + ', '.join(missing))
            return 1
        if bad:
            print('Files do not match MANIFEST.json (re-prepare them): ' + ', '.join(bad))
            return 1
    else:
        print('No device photos in ' + str(DEVICE_SOURCE)
              + '; installing wallpapers only. The Device Photos theme will fall back to monograms until they are prepared.')
    catalog_path = WALLPAPERS / 'catalog.js'
    catalog_text = catalog_path.read_text()
    marker = 'window.CleanFrameWallpapers = [\n'
    if marker not in catalog_text:
        print('catalog.js does not contain the expected gallery marker; refusing to edit it.')
        return 1
    for name, dest in wallpaper_files():
        dest.mkdir(parents=True, exist_ok=True)
        (dest / name).write_bytes((WALLPAPER_SOURCE / name).read_bytes())
    if devices_ok:
        for name, dest in device_files():
            dest.mkdir(parents=True, exist_ok=True)
            (dest / name).write_bytes((DEVICE_SOURCE / name).read_bytes())
    sources_path = WALLPAPERS / 'SOURCES.json'
    entries = json.loads(sources_path.read_text())
    have = {entry['id'] for entry in entries}
    added = [sources_entry(id_, name) for id_, name in PHOTOS if id_ not in have]
    if added:
        sources_path.write_text(json.dumps(added + entries, indent=2) + '\n')
    if START_MARKER not in catalog_text:
        catalog_path.write_text(catalog_text.replace(marker, marker + catalog_block(), 1))
    print('Installed ' + str(len(list(wallpaper_files()))) + ' prepared wallpaper files'
          + (' and ' + str(len(DEVICE_FILES)) + ' device photos.' if devices_ok else '.'))
    if added:
        print('Added to SOURCES.json: ' + ', '.join(entry['id'] for entry in added))
    print('Catalogue entries: ' + ', '.join(IDS))
    print('These files are gitignored and must not be committed. Run npm run check.')
    return 0


def remove():
    removed = 0
    for name, dest in list(wallpaper_files()) + list(device_files()):
        path = dest / name
        if path.is_file():
            path.unlink()
            removed += 1
    sources_path = WALLPAPERS / 'SOURCES.json'
    entries = json.loads(sources_path.read_text())
    kept = [entry for entry in entries if entry['id'] not in IDS]
    if len(kept) != len(entries):
        sources_path.write_text(json.dumps(kept, indent=2) + '\n')
    catalog_path = WALLPAPERS / 'catalog.js'
    text = catalog_path.read_text()
    if START_MARKER in text and END_MARKER in text:
        before, rest = text.split(START_MARKER, 1)
        _block, after = rest.split(END_MARKER, 1)
        catalog_path.write_text(before + after)
    print('Removed ' + str(removed) + ' installed files and the four catalogue entries.')
    return 0


def check():
    source_ok = WALLPAPER_SOURCE.is_dir()
    _missing, _bad = (['(source folder missing)'] if not source_ok
                      else verify_source(WALLPAPER_SOURCE, list(wallpaper_files())))
    installed, absent = [], []
    for name, dest in wallpaper_files():
        (installed if (dest / name).is_file() else absent).append(name)
    sources = json.loads((WALLPAPERS / 'SOURCES.json').read_text())
    present_sources = [id_ for id_ in IDS if any(e['id'] == id_ for e in sources)]
    catalog = (WALLPAPERS / 'catalog.js').read_text()
    catalog_ok = START_MARKER in catalog
    print('Wallpaper source: ' + ('present' if source_ok else 'MISSING') + ' ' + str(WALLPAPER_SOURCE))
    print('Installed wallpaper files: ' + str(len(installed)) + '/28; missing: ' + str(len(absent)))
    if absent:
        print('  missing: ' + ', '.join(absent))
    print('SOURCES.json entries: ' + (', '.join(present_sources) if present_sources else '(none)'))
    print('catalog.js block: ' + ('present' if catalog_ok else 'absent'))
    wallpapers_ok = (not absent and not _missing and not _bad
                     and len(present_sources) == len(IDS) and catalog_ok)
    device_source_ok = DEVICE_SOURCE.is_dir()
    _dm, _db = ([] if not device_source_ok
                else verify_source(DEVICE_SOURCE, list(device_files())))
    device_installed = [name for name, dest in device_files() if (dest / name).is_file()]
    device_note = ''
    if device_source_ok and (_dm or _db):
        device_note = '; manifest mismatches: ' + ', '.join(_dm + _db)
    print('Device photo source: ' + ('present' if device_source_ok else 'not prepared (theme falls back to monograms)'))
    print('Installed device photos: ' + str(len(device_installed)) + '/' + str(len(DEVICE_FILES)) + device_note)
    devices_ok = (not device_source_ok) or (len(device_installed) == len(DEVICE_FILES) and not _dm and not _db)
    return 0 if (wallpapers_ok and devices_ok) else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Report state without changing anything')
    parser.add_argument('--remove', action='store_true', help='Undo the install')
    args = parser.parse_args()
    if args.check:
        return check()
    if args.remove:
        return remove()
    return install()


if __name__ == '__main__':
    sys.exit(main())
