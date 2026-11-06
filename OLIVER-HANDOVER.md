# CleanFrame65 — handover for Oliver

A custom launcher for your 65" Samsung Frame 2025 (QE65LS03FAUXXU), built on
upstream CleanFrame v0.7.0. One build, five switchable themes, your HDMI
boxes on Home, your photos as wallpapers.

**Only the browser preview was checked. Nothing here has run on a real TV.**
Do not treat any of this as verified on your Frame until you have installed
it and used it there.

## The durable home vs the scratch copy

- **Durable home:** your fork, https://github.com/0liverBirch/CleanFrame65,
  branch `oliver-launcher`. That is where this work belongs.
- **Scratch copy:** `~/workspace/cleanframe-oliver/` on this machine. It is
  only a preview copy. If it is lost, the branch on your fork is the copy
  that matters.

## What was changed vs upstream, and why

- **Home tiles: Apple TV 4K, PS5, Sky.** Upstream shows streaming apps.
  Your three boxes are HDMI shortcuts, not Tizen apps, so they are never
  sent to `launchApp`. A tile with no remembered port opens the TV's real
  Inputs chooser and says which device it is for. Pick the port there and
  the tile remembers it. No port numbers are assumed anywhere.
- **24-hour clock.** Upstream is 12-hour. Yours shows 24-hour, no seconds,
  no AM/PM.
- **Five switchable themes in Settings (see below).** A fresh install starts
  on Minimal Black & White: dark Dock, text-only tiles, no photo wallpaper.
- **Your photos as wallpapers.** JFK at the diner (your favourite), Mustang
  at the villa, Superbird in the desert, Petty #43. Prepared at 1920×1080
  with the pre-rendered glass materials CleanFrame needs. They are
  local-only and never committed (see "Your photos and device photos").
- **Device photos for the Device Photos theme.** Transparent PNGs of the
  actual boxes (see "Device photos — what they are").
- **Bigger Home tiles.** Tiles are 400×280 (was 288×200) in icon+label
  mode, 400×140 in text mode (Minimal), with bigger labels (44px, was
  36px) and bigger device photos. The dock sits a little higher so the
  tiles are not so low on the screen. Three tiles plus Art Mode / All apps
  / Settings and the clock still fit 1920×1080 with no clipping or overlap.
- **Backgrounds for the four non-Art themes (see below).** Minimal gets
  your Petty #43 B&W photo dimmed right down; Device Photos gets a dark
  shelf gradient; Futuristic gets a pre-rendered nebula/grid; 90s TV gets
  a muted Memphis wash. Art Mode Overlay is unchanged (JFK photo
  full-screen). Each background is one pre-rendered 1920×1080 JPEG — no
  live blur, no animation, so it stays fast on Tizen.
- **A clear route back.** Settings → Samsung has Samsung Home, TV settings
  and Inputs. The remote's Back key always works.

Remote navigation (arrows / OK / Back), saved preferences and the ES5
runtime are all preserved. Nothing here uses live blur or animation, so it
stays fast on Tizen.

## The five themes

Settings → **Theme** (first row in Settings). Pick one, press OK, the whole
look changes in one save. Your choice is remembered across restarts.

1. **Minimal Black & White** — the fresh-install default. Monochrome only,
   no photo wallpaper, text-only tiles, a plain white outline around the
   focused tile. Background: your Petty #43 B&W photo, dimmed to about a
   third and darkened further behind the tile row so the white labels stay
   readable. Still calm, still monochrome.
2. **Device Photos** — each Home tile shows a photo of the actual box
   (Apple TV 4K + remote, PS5 Slim + controller, Sky Q box) on a dark
   gradient background with a soft shelf glow behind the tile row, so the
   boxes do not float in a void. Needs the local-only device photos
   installed (below); without them the tiles fall back to their labels.
3. **Futuristic** — pre-rendered dark nebula background (cyan and purple
   clouds, stars, a glowing horizon and a faint perspective grid), cyan
   glass focus plate and clock glow. Static paint only, no animation, still
   readable from the sofa.
4. **90s TV** — retro CRT/VHS feel: a muted Memphis-pattern background
   (soft magenta circle, teal triangle, yellow shapes) in the same
   magenta/teal/yellow palette, magenta and purple focus plate with a
   chunky teal border, yellow menus, uppercase labels, a teal frame around
   the screen and static scanlines. The type stays the bundled sans — a real
   pixel font would break the TV's measured label widths, so the retro feel
   comes from colour, borders and scanlines.
5. **Art Mode Overlay** — the JFK diner photo fills the screen and the
   launcher sits on top as a minimal overlay. Unfocused tiles dim so the
   photo reads as art when idle. If the local-only photos are not installed
   it uses the current wallpaper instead.

Changing Background, Layout or Focus by hand afterwards still works. It does
not clear the stored theme — Settings keeps showing the last theme you
picked. A profile saved before themes existed shows as **Custom** in the
Theme row; if its look happens to match a theme exactly, that theme is shown
instead.

Screenshots from the browser preview (in this local copy only, not in the
repo): `.local/qa/themes/theme-minimal.png`,
`.local/qa/themes/theme-devices.png`, `.local/qa/themes/theme-future.png`,
`.local/qa/themes/theme-retro.png`, `.local/qa/themes/theme-art.png`, plus
`.local/qa/oliver/fresh-minimal-dock.png` (fresh install) and
`.local/qa/oliver/photo-jfk-diner.png`.

## Preview on your Mac

```sh
cd ~/workspace/cleanframe-oliver   # or wherever you cloned the fork
npm ci
python3 scripts/apply-oliver-assets.py   # installs your photos, device photos and theme backgrounds (below)
npm run dev:public
```

Open http://localhost:4795/home/ in a browser. Use the arrow keys, Enter
and Escape — it behaves like the TV remote. To try a theme: Settings (top
right) → Theme → pick one → OK → Back, Back to Home.

To preview a theme without clicking through Settings, the preview URL is
the same for all five; switch in Settings as above.

## Your photos and device photos (local-only)

Your photos and the device photos are **not in the repo**. The fork is
public; committing them would publish them.

- Prepared wallpapers (28 files): `.local/oliver-wallpapers/` with
  `MANIFEST.json` (sizes + SHA-256).
- Prepared device photos (3 PNGs): `.local/oliver-devices/` with
  `MANIFEST.json`.
- Prepared theme backgrounds (4 JPEGs): `.local/oliver-backgrounds/` with
  `MANIFEST.json`. Made by `.local/make-backgrounds.py` (Pillow): Minimal
  from your Petty #43 B&W original in `~/workspace/your_files/frame-art/`,
  the other three drawn procedurally. Installed by the same apply script
  into `app/assets/theme-backgrounds/`. If a background file is missing,
  that theme falls back to its flat colour/gradient — the launcher never
  breaks on a missing background.
- Install: `python3 scripts/apply-oliver-assets.py`
- Check state: `python3 scripts/apply-oliver-assets.py --check`
- Remove: `python3 scripts/apply-oliver-assets.py --remove`

Remove restores the upstream catalogues. **Run `--remove` before
`npm run export:public` if the resulting `.wgt` might be shared** — the
public export zips everything in `app/`, so an export built while the
photos are installed would contain them. The copied files are covered by
`.gitignore`, so `git status` stays clean and they cannot be committed by
accident. The script verifies every file against its manifest before
copying; if a file is missing or changed it refuses and says which one.

If you clone the fork fresh on another Mac, make these three `.local/`
folders there first: the wallpapers are prepared from your Frame-art
originals in `~/workspace/your_files/frame-art/` (JFK diner first), the
device photos are the three PNGs in `.local/oliver-devices/`, and the theme
backgrounds are made by `python3 .local/make-backgrounds.py` (needs the
Petty #43 B&W original in the Frame-art folder). The
preparation steps are in `.local/cutout-devices.py` (device photos) and the
earlier wallpaper preparation used Pillow `ImageOps.fit` to 1920×1080 plus
upstream `node scripts/build-materials.mjs`.

### Device photos — what they are

There are no clean, licensable transparent product photos of these three
boxes to download, so the three images are AI-generated studio shots of the
actual products, cut out to transparent PNGs:

- **Apple TV 4K + Siri Remote** — accurate (black puck, silver clickpad
  remote). It renders smaller than the other two on a tile because the
  remote stands tall, making the image nearly square. A wider re-shoot is
  possible if it bothers you.
- **PS5 Slim + DualSense** — accurate Slim (diagonal split, white plates).
  This render is the **disc-edition** Slim. Say if yours is the digital
  edition and I will swap it. The console stands on a dark floor shadow
  that is part of the image; it blends into the dark theme.
- **Sky Q box** — accurate Sky Q 2TB box (Sky logo, Q button, green LED).
  If your Sky box is a different model (Sky Stream, Sky Glass, older Sky+),
  say so and I will match it.

A faint shadow remnant is visible under the Apple TV box if you look at the
full-size PNG closely; it is not visible at tile size.

## Steps you still do on your Mac + TV, in order

Do these on your Mac (M-04237, Node v22.13.1 / npm 10.9.2). Nothing below
needs me; stop and ask if a step does not match your screen.

### 1. Push the branch to your fork

```sh
cd <your clone of 0liverBirch/CleanFrame65>
git checkout oliver-launcher
git push -u origin oliver-launcher
```

The local commit on this branch was made with a clearly local/agent git
identity, not yours. Re-author it if you want your name on it
(`git commit --amend --reset-author` before pushing, or just leave it).

Only these files are committed: `.gitignore`, `README.md`,
`app/assets/wallpapers/README.md`, `app/main.js`, `app/style.css`,
`docs/interaction-behaviour.md`, `scripts/apply-oliver-assets.py`,
`scripts/check-browser.mjs`, `OLIVER-HANDOVER.md`. The local-only
`SOURCES.json` / `catalog.js` changes are **not** committed — a clean clone
would fail its checks without the photo files, so they stay local-only.

### 2. Developer Mode on the TV

1. TV: Home → Apps → App Settings (the gear).
2. Open the numeric pad, press **1, 2, 3, 4, 5**, then Done if shown. The
   Developer Mode popup appears.
3. Set Developer Mode → **On**. Enter your **Mac's local IP address** as
   Host PC IP, then save.
4. Restart the TV as it instructs (power-cycle at the wall if it asks for
   one). Reopen Apps and check Developer Mode is shown as on.

Your Mac and TV must be on the same Wi-Fi for this and for install.

### 3. Samsung certificates (author + distributor)

You need a Samsung account. In Tizen Studio (Certificate Manager) or the
Samsung VS Code extension:

1. Create a **new signing profile** for yourself. Do not reuse anyone
   else's.
2. Create an **author certificate** (this signs the app as yours) and a
   **distributor certificate** with **Public privilege**, adding your TV's
   DUID (Unique Device ID — the TV shows it in the support menu, or the
   certificate tool's connected-device selector finds it).
3. Select the profile in `.local/signing.json` (copy
   `signing.example.json` first). That file is gitignored.
4. **Back up `~/SamsungCertificate/<profile>`** somewhere safe (USB stick
   or encrypted backup). If you lose the author certificate you cannot
   update this app later without uninstalling it first.

### 4. Build, sign, install, launch

```sh
npm run package              # builds and signs the .wgt with your profile
npm run tv:install && npm run tv:launch
```

First launch: map each tile. Press OK on **Apple TV 4K** → the TV's Inputs
chooser opens → pick the HDMI port your Apple TV is on. Repeat for **PS5**
and **Sky**. The ports are then remembered per tile.

### 5. How to delete it

TV: Home → Apps → App Settings → select CleanFrame → Delete. That removes
the app only; it does not touch anything else on the TV.

### 6. SKIP the Home-button remap — for now

Upstream CleanFrame can remap the TV's Home button to open the launcher,
but it is undocumented and can break after a firmware update. We are
deliberately **not** doing it first. Use the launcher from Apps, and the
Samsung Home route inside it (Settings → Samsung → Samsung Home), until you
have lived with it and decide the remap is worth the risk. Treat any
Home/startup change as a separate decision with its own recovery plan.

## Risks, in plain language

- **This is not Samsung software and not verified on a real TV yet.** It
  was checked in a desktop browser only. It might look or behave
  differently on your Frame, and the first install might need fixes.
- **Use at your own risk.** A third-party launcher can misbehave, freeze
  or need deleting (step 5 above). It does not change the TV's firmware.
- **Warranty:** installing a developer app through Developer Mode is a
  normal Samsung developer feature, but if the TV ever needs warranty
  service, delete the app and turn Developer Mode off first.
- **Certificates expire.** Samsung distributor certificates last a limited
  time (typically a year). When it expires, the app stops launching until
  you renew the certificate and reinstall.
- **Firmware updates can change things.** A Samsung update could change
  the Home button behaviour (which is why we skip the remap), the Inputs
  chooser, or how apps launch. If the launcher breaks after an update, the
  fix is to delete it and check for an updated build.
- **TV restarts.** The TV may restart during install. That is expected.

## Still missing from you

- A photo of Settings → Support → About This TV (crop the serial number
  out before sending). This confirms the exact model, firmware and Tizen
  version — 9.0 is still assumed from the 2025 LS03F model, not confirmed.
- Your TV's IP address and your Mac's IP address (needed for Developer
  Mode and install).
- Which HDMI port is Apple TV / PS5 / Sky (you pick these on the TV at
  first launch anyway, so this is only for the record).
- Confirmation you have Claude Code installed on your Mac, or that you
  want the manual Tizen SDK steps instead.
- Which theme you like best once you have tried them in the preview. The
  fresh-install default is Minimal Black & White; say if you would rather
  it opened on Art Mode Overlay (JFK photo) or Device Photos instead.

## Checks run (6 Nov 2026, browser only, mock Tizen, no TV contacted)

- `npm run check` — passed (ESLint, wallpaper/material checks, 10/10
  device tests).
- `CLEANFRAME_PUBLIC_FONTS=1 npm run check:browser` — **432 checks,
  0 failures** (upstream suite plus the new Theme group checks).
- `.local/verify-oliver.mjs` (own checks) — **48/48 passed**: fresh install
  (Minimal Black & White, dark Dock, three HDMI tiles in order, 24-hour
  clock, JFK wallpaper), HDMI mapping (chooser names the device, picking
  HDMI 2 calls `setSource(2)`, mapping saved and survives reload, mapped
  tile switches directly), all four photo wallpapers render, and all five
  themes applied through the real Settings UI (look values, stage class,
  device PNGs loading, gradient/scanline/photo checks, persistence back on
  Home and across reload).
- `npm run check:public` — passed (bounded secret audit; see below).
- Public export built from a clean checkout (photos removed first):
  `dist/CleanFrame-public-unsigned.wgt`, SHA-256
  `425ce1f43eac736562aa81916061afa8b0e36f7d315a3e2b3d07a14f77bcad0d`,
  15,787,775 bytes, 152 entries, only the 15 upstream wallpapers, no
  Oliver photos and no device photos. The themes are in the package
  (checked: `PRESETS` in `main.js`, theme classes in `style.css`).
  Unsigned — signing needs your Samsung account and Mac.
