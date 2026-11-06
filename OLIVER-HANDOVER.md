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
  actual boxes (see "Device photos — what they are"), now sitting on rich
  card art like Apple TV home-screen icons (see "Apple TV-style cards"
  below).
- **Apple TV-style cards.** The device tiles are large rounded cards
  whose artwork fills the tile — a cinematic living room behind Apple TV,
  a neon game canyon behind PS5, a floodlit stadium behind Sky — with the
  photo of the actual box on top. The focused card lifts (slightly bigger,
  strong shadow, white ring) and the others dim. In Device Photos a strong,
  wide halo follows focus: the focused device's backdrop, brightened to
  about three-quarters, on a 1920×880 layer centred on the focused tile
  and faded to transparent at its far edges by a CSS radial-gradient
  mask (ellipse 940×420, full strength to 60%), so the glow clearly
  extends behind the neighbouring cards while still fading out before
  the screen edges and keeping the hero above clean. (An earlier version
  swapped the whole screen background, Top Shelf-style; a later one was
  a smaller 1600×760 halo that Oliver found too subtle — it read as if
  the glow lived only inside the focused card, because its full-strength
  core was barely bigger than the card and the backdrop was dimmed to
  about half.) Futuristic reuses the same cards (with a cyan lift) but
  keeps its nebula background; Art Mode gets only the lift, so the JFK
  photo stays the picture; Minimal stays text-only and 90s TV keeps its
  bevelled plastic buttons.
- **Bigger Home tiles.** Tiles are 400×280 (was 288×200) in icon+label
  mode, 400×140 in text mode (Minimal), with bigger labels (44px, was
  36px) and bigger device photos. The dock sits a little higher so the
  tiles are not so low on the screen. Three tiles plus Art Mode / All apps
  / Settings and the clock still fit 1920×1080 with no clipping or overlap.
- **A hero at the top of every theme, and a Tonight strip under the
  dock.** The 24-hour clock is now big (enlarged by a transform, so the
  measured digit widths still work), with today's date and a
  time-appropriate greeting ("Good morning, Oliver") underneath, so the
  top half of the screen is no longer empty. The Tonight strip names each
  box and its HDMI port, or that a port still needs picking ("Tonight:
  Apple TV 4K · HDMI 2 — PS5 · pick a port — Sky · pick a port"). The
  strip is hidden in the 90s TV theme, where the TV set's bottom band
  occupies that strip. Tiles were not made bigger again — the hero, the
  strip and the backgrounds fill the space instead.
- **Backgrounds for the four non-Art themes (see below).** Minimal gets
  your Petty #43 B&W photo, now bright enough to actually see (about half
  brightness, was about a third); Device Photos gets a lit dark gradient
  with a brighter shelf glow; Futuristic gets a brighter nebula and a
  stronger perspective grid; 90s TV gets a brighter Memphis wash inside
  the CRT glass. Art Mode Overlay is unchanged (JFK photo full-screen).
  Each background is one pre-rendered 1920×1080 JPEG — no live blur, no
  animation, so it stays fast on Tizen. (A bug in the background maker was
  also fixed: its vignette was darkening the centre of every background
  instead of the edges, which is why they all read as a dark void.)
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
   focused tile. Background: your Petty #43 B&W photo, dimmed to about
   half and darkened further behind the tile row so the white labels stay
   readable — the car is clearly visible now. Still calm, still monochrome.
2. **Device Photos** — Apple TV-style cards (see above): each Home tile
   is a large rounded card with rich artwork filling it and the photo of
   the actual box on top (Apple TV 4K + remote over a cinematic living
   room, PS5 Slim + controller over a neon game canyon, Sky Q box over a
   floodlit stadium). The focused card lifts with a white ring and strong
   shadow, the others dim, and a wide halo of that device's backdrop
   glows behind the whole dock row around the focused card, fading out
   as it spreads away from it, while the theme background shows through
   at the edges. The card art
   and halos are AI-generated generic scenes (no copyrighted poster art,
   no logos); the device photos are the local-only PNGs below. Needs the
   local-only device photos and card art installed (below); without the
   card art the tiles fall back to plain dark cards, without the photos
   to their labels.
3. **Futuristic** — pre-rendered dark nebula background (cyan and purple
   clouds, stars, a glowing horizon and a faint perspective grid), cyan
   glass focus plate and clock glow. Static paint only, no animation, still
   readable from the sofa. Its device tiles reuse the same Apple TV-style
   cards (rich art, device photo, focused lift with a cyan ring) but the
   background stays the nebula — it does not swap with focus.
4. **90s TV** — a physical 90s CRT television set filling the whole
   screen: chunky plastic bezel with rounded corners, speaker grilles down
   both sides, corner screws, a CLEANFRAME brand badge, a red power button
   with a red standby LED, a VHS slot, a tuning knob and CH/VOL buttons
   along the bottom, and the launcher living inside the curved CRT glass.
   Inside the glass: the muted Memphis-pattern background (soft magenta
   circle, teal triangle, yellow shapes), a green channel OSD ("CH 03 ·
   AV1"), stronger scanlines, a vignette and a slight glass reflection,
   and chunky bevelled plastic tiles with drop shadows and uppercase
   labels in the same magenta/purple/teal/yellow palette. The type stays
   the bundled sans — a real pixel font would break the TV's measured
   label widths, so the retro feel comes from the set, the colours and the
   glass, not the typeface. The bezel is a local-only PNG (see below);
   without it the theme falls back to the Memphis background with
   scanlines.
5. **Art Mode Overlay** — the JFK diner photo fills the screen and the
   launcher sits on top as a minimal overlay. Unfocused tiles dim so the
   photo reads as art when idle. The focused tile lifts slightly with a
   soft shadow; there is no card art and no background swap, so the photo
   stays the picture. If the local-only photos are not installed
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
the Device Photos theme with each device focused:
`.local/qa/themes/theme-devices-focus-appletv.png`,
`.local/qa/themes/theme-devices-focus-ps5.png`,
`.local/qa/themes/theme-devices-focus-sky.png`, plus
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
- Prepared device card art + focus backdrops + halo PNGs (9 files): `.local/oliver-cards/`
  with `MANIFEST.json`. Made by `.local/make-card-art.py` (Pillow) from
  three AI-generated backdrops in `.local/card-gen-raw/` (cinematic living
  room, neon game canyon, floodlit stadium — generic scenes, no
  copyrighted poster art, no logos): each device gets an 800×560 card
  (centre crop, light pool behind the black box, dark scrim under the
  label), a 1920×1080 focus backdrop (brightened to about three-quarters,
  darker top and bottom band) that the runtime shows as the wide halo
  through a CSS mask, and a 1920×880 halo PNG (the same glow with the
  fade baked into the alpha channel, kept for a future switch away from
  the mask). Installed by the same apply script — card art to
  `app/assets/devices/`, focus backdrops to `app/assets/theme-backgrounds/`.
  Also local-only and never committed.
  (The generator writes via a temp file and only replaces on success, and
  skips files that already match the manifest — this VM intermittently
  refuses shell-spawned writes with EPERM, and a failed write used to
  leave a truncated asset behind.)
- Prepared theme backgrounds (4 JPEGs): `.local/oliver-backgrounds/` with
  `MANIFEST.json`. Made by `.local/make-backgrounds.py` (Pillow): Minimal
  from your Petty #43 B&W original in `~/workspace/your_files/frame-art/`,
  the other three drawn procedurally. Installed by the same apply script
  into `app/assets/theme-backgrounds/`. If a background file is missing,
  that theme falls back to its flat colour/gradient — the launcher never
  breaks on a missing background.
- CRT bezel for the 90s TV theme (1 PNG): `.local/oliver-retro/` with
  `MANIFEST.json`. Made by `.local/make-retro-bezel.py` (Pillow, drawn
  procedurally — bezel, grilles, screws, badge, power button, LED, VHS
  slot, knob, CH/VOL buttons — with the glass cut out to transparent).
  Installed by the same apply script into
  `app/assets/theme-backgrounds/retro-bezel.png`. Also local-only and never
  committed.
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
- `.local/verify-oliver.mjs` (own checks) — **109/109 passed**: fresh install
  (Minimal Black & White, dark Dock, three HDMI tiles in order, 24-hour
  clock, JFK wallpaper), hero (today's date, time-appropriate greeting,
  clock enlarged by transform) and Tonight strip (names all three boxes,
  shows "pick a port" unmapped and "HDMI 2" once mapped), HDMI mapping
  (chooser names the device, picking HDMI 2 calls `setSource(2)`, mapping
  saved and survives reload, mapped tile switches directly), all four photo
  wallpapers render, and all five themes applied through the real Settings
  UI (look values, stage class, device PNGs loading, gradient/scanline/
  photo checks, theme backgrounds loading at 1920×1080, the new larger
  tile sizes with device photos scaled up, hero + Tonight strip in every
  theme, CRT bezel/OSD/bevelled tiles/glass effects in the 90s TV theme,
  persistence back on Home and across reload), plus the Apple TV-style
  cards (rich card art at 800×560, focused card lifts with a white ring,
  unfocused cards dim) and the wide focus halo (1920×880 layer centred
  on the focused tile, radial-gradient mask 940×420 full strength to 60%,
  core reaching the neighbouring cards' centres, hero staying clean above
  it, following focus across all three devices).
- `npm run check:public` — passed (bounded secret audit; see below).
- Public export built from a clean checkout (photos removed first):
  `dist/CleanFrame-public-unsigned.wgt`, SHA-256
  `c2788c958af9ba3cb395d5be44d510a5dc14f88f28095894a06be3f6a6073fde`,
  15,791,830 bytes, 152 entries, only the 15 upstream wallpapers, no
  Oliver photos, no device photos, no theme backgrounds and no CRT bezel.
  The themes, the hero, the Tonight strip, the bigger tiles, the card
  code and the halo are in the package (checked: `PRESETS`, `focusBg`,
  `card-art`, `HALO_W`, `applyFocusBackdrop` in `main.js`, theme classes,
  background rules, `.card-art` and the radial-gradient halo mask in
  `style.css`, `tw: 400` in the dock geometry).
  Unsigned — signing needs your Samsung account and Mac.

### Apple TV-style cards (6 Nov 2026) — built and verified

- `npm run check` — passed (ESLint, `check.py`, 10/10 device tests),
  run through the direct binaries (`./node_modules/.bin/eslint app`,
  `python3 scripts/check.py`, `node --test scripts/test-device.mjs`).
- `CLEANFRAME_PUBLIC_FONTS=1 npm run check:browser` — **432 checks,
  0 failures**.
- `.local/verify-oliver.mjs` — **109/109 passed** (see above). It
  produced the three focus screenshots
  (`.local/qa/themes/theme-devices-focus-appletv.png`,
  `theme-devices-focus-ps5.png`, `theme-devices-focus-sky.png`) and
  confirmed the halo follows focus per device, the focused card lifts
  with a white ring, and the other themes still work.
- `python3 scripts/check-public.py` — passed (219 candidate files).
- One real bug caught by the screenshots: the Futuristic theme showed
  the device PNGs at natural size, overflowing the tiles (the
  `.device-photo img` fit rule was scoped to Device Photos only). Fixed
  by sharing the fit rule and the 340×150 mark sizing with Futuristic,
  and the verify check now asserts the rendered PNG fits inside the
  tile (≤340×150). Re-shot `theme-future.png` shows all three boxes
  correctly on their cards.

### Stronger halo (6 Nov 2026) — the 1600×760 version was too subtle

- Oliver's read was right: the old halo's full-strength core (45% of a
  700×330 mask ellipse) was barely bigger than the 400×280 card itself,
  and the backdrop was dimmed to about half, so the glow read as if it
  lived only inside the focused card.
- Now: 1920×880 layer, mask ellipse 940×420 full strength to 60%
  (core 564px, so it covers the neighbouring cards' centres 416px
  away), backdrop brightened to about three-quarters (top shade 0.38→
  0.22, bottom band 0.5→0.35). The layer top (284) sits above the
  hero's bottom edge, but the mask is ~85% faded there, so the hero
  stays clean. Still a halo, not a full-screen swap: it fades to
  transparent at the far edges. Baked-alpha PNG halos in
  `.local/oliver-cards/` were regenerated at the same 1920×880 geometry
  (centre alpha 255, core 0.60) for a future switch, but the shipped
  version still uses the CSS mask — same rendering path the shelf and
  list fades already use, no new files to install.
- Two check fixes along the way, both in the checks, not the app:
  Chromium serialises the mask as `rgb(0, 0, 0) 60%` (no `ellipse`
  keyword), and the far neighbour on an end tile sits outside the
  full-strength core but inside the 940px fade radius, so the
  neighbour check now asserts the adjacent card is in the core and
  every card is inside the fade.
- Checks after the change: verify 109/109, browser suite 432/0, public
  export rebuilt (SHA `c2788c95…` above), assets reinstalled, committed
  locally on `oliver-launcher` (still NOT pushed).

### VM filesystem breakage, 6 Nov 2026 ~10:41–12:14 — recovered

- The VM intermittently refused all shell-spawned file writes with
  `Operation not permitted` (Python, `cp`, `git`, Node, Chromium),
  while the shell's own built-ins still wrote. Chromium also died at
  launch while this lasted. Hundreds of retries failed; the outage
  lasted until ~12:14, when writes came back and Chromium launched
  again (v156.0.8078.4).
- What it broke along the way: a `--remove` run failed halfway and left
  `SOURCES.json` and `catalog.js` truncated to 0 bytes (restored by hand
  to their exact upstream bytes, git-hash verified: SOURCES.json
  `56c5d216…`, catalog.js `041c61f4…`), and a card-art run truncated
  `hdmi-appletv-card.jpg` to 0 bytes (regenerated once writes returned;
  SHA-256 matches the original manifest entry exactly, `5b51db1f…`).
  The generator now writes via a temp file and only replaces on success,
  and skips files that already match the manifest, so a failed write can
  no longer leave a truncated asset behind.
- Everything in the Blocked list is now done: assets reinstalled and
  checked (28/28, 3/3, 4/4, 1/1, 6/6, no 0-byte files), verify 109/109,
  browser suite 432/0, public export rebuilt (SHA `c2788c95…` above),
  assets reinstalled afterwards, and the work committed locally on
  `oliver-launcher` (see "Steps you still do" — still NOT pushed).
