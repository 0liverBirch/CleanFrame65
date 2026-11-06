# Interaction behaviour — 0.7.0

## Home

- Dock: Left/Right scrolls the apps without wrapping. Up enters the top-right controls, starting with Art Mode or the last selected control. Left/Right moves between Art Mode, All apps and Settings. Down or Back returns to the selected app. The clock is at the top left.
- List: Up/Down scrolls the apps without wrapping. Right enters the bottom-right controls, aligned with the clock above. Up/Down moves between Art Mode, All apps and Settings. Left or Back returns to the selected app. The list fades at both ends as it scrolls.
- OK opens the selected item. Focus alone never launches an app.
- Icons-only apps and controls reveal their names when focused. App presentation and control presentation are independent.
- Back from the app list or Dock opens a choice to stay or open Samsung Home.
- A panel keeps focus within its own controls. Back closes one panel at a time.
- Returning to the running launcher keeps the selected app or panel item. There is no auto-return timer. Held OK and Back keys act once until the key is released.

## Settings and appearance

Settings opens a grouped overview: Background, Layout, Typography, Focus, Apps on Home and Samsung. OK opens a group. Appearance groups use a two-pane screen with visible choices on the left and the committed Home preview on the right.

| Group | Choices |
| --- | --- |
| Background | Photo, Light, Dark; Wallpaper and Rotation when Photo is active |
| Layout | List or Dock; independent Text, Icons or Both choices for apps and Home controls |
| Typography | Manrope, Neue Montreal, Mori, Pangram Sans, Geist and Newsreader, when available |
| Focus | Type or Glass; Soft, Frost or Clear tint material |
| Apps on Home | Membership and arrangement editor |
| Samsung | Samsung Home, TV settings and Inputs |

Up/Down moves between rows. Left/Right moves between choices in a horizontal row. Focus alone changes neither the preview nor saved preferences in these appearance groups. Wallpaper has its own temporary photo preview, described below. OK applies the focused value. A checkmark identifies the applied value; the filled plate identifies remote focus. Applying the current value does not write again.

Material applies to a photographic Dock, or Glass focus on a photographic List. Inactive material choices remain visible with an explanation and are skipped during navigation. Their stored value is retained. Wallpaper and rotation are also inactive on flat backgrounds.

A font or photo change applies only after its resources are ready and storage succeeds. A load or storage failure keeps the previous appearance and checkmark, with a Try again action. Back cancels a pending change, leaves the group and keeps completed changes. Late load callbacks cannot apply a cancelled choice. There is no Save button. Returning to a group restores its last choice focus; returning to Settings restores its category focus. Rotation is nested within Background, and Back returns to its Rotation row.

The selected font applies to Home app names, the clock and Home controls, including Newsreader. Settings, All apps, the Home editor and status text retain Manrope. The preview shows the committed Home appearance and its clock continues to update. Pangram faces are available in Nathan's private build when the local files are present; their binaries are not included in the public source. An unavailable optional face is omitted. If the baseline font is slow or missing, Home remains usable with a local fallback and can recover when the font loads.

## Streaming apps

The nine default apps keep their known native IDs. Other installed consumer apps can also be added to Home. Launching uses the public `tizen.application.launch` API with the app's native ID. Missing apps and denied launches produce a real error. No web player, placeholder success page or account credential is embedded.

## All apps

The panel reads `tizen.application.getAppsInfo` on entry and shows the filtered consumer apps alphabetically. Samsung's visibility flag alone also exposes system utilities, so EP packages, background services, ad players, account utilities, placeholders and duplicates are omitted. Known brands use bundled marks. Other apps use their local installed icon, with initials as a fallback.

The five-column grid scrolls with remote focus. OK launches an app; its On Home badge shows membership. Up from the first row reaches Apps on Home, which opens the editor. An API failure shows a retry and keeps saved Home choices. Browser previews report that installed-app discovery and launching require the TV.

## Apps on Home

Open the editor from Settings or All apps. On Home shows the current order on the left. Not on Home shows Recently removed first, followed by other installed apps on the right. Home holds one to nine apps.

- Reorder: OK on an app name picks it up. Up/Down moves it. OK places it and saves the order. Back puts an unplaced app back without saving that move.
- Remove: Right from an app name reaches Remove from Home. OK saves the removal and moves focus to the same app in Recently removed. The app stays installed.
- Add: OK on an app in Not on Home adds it and saves. A recently removed app returns to its previous position within the editing session; another app is added at the end. Focus follows the app to its Remove from Home control, so another OK can reverse the addition.
- Undo reverses a completed addition, removal or reorder from the current editing session. Done or Back closes the editor and keeps completed changes. Undo history ends when the editor closes.

Removing the last Home app or adding a tenth app is prevented. A failed storage write keeps the committed choices and order, with a retry message. Saved native app IDs and names survive a restart or a failed catalogue refresh.

## Art Mode and Samsung screens

Art Mode sends an application control to the installed `org.tizen.art-app`, with `mode=fullscreen` and `requester=mobile`. This aims to enter native Art Mode with its current artwork, without toggling power or changing the selected artwork.

This mode comes from [research on Samsung's Art app](https://github.com/TheFab21/ha-samsungtv-smart/blob/master/notes/QN55LS03FAFXZA/ART_MODE_DECOMPILED.md), on another Tizen 9 Frame model. It is an internal Samsung contract, not a documented public Art API. Its visible behaviour on this exact firmware must be confirmed on the TV.

Samsung Home explicitly launches the original `com.samsung.tv.csfs` app, independently of the new Home assignment. The earlier `com.samsung.tv.coba.newhome` component did not open Smart Hub visibly and is no longer the escape target. TV settings still uses `com.samsung.tv.coba.setting`. Exact on-device destinations are recorded in docs/tv-status.md; launch callbacks alone are not visual proof. There is no blind power-key fallback.

All calls have bounded response handling. A failure leaves CleanFrame usable. No simulated device success views remain. Browser validation cannot confirm the visible Samsung destination.

Installed-app discovery allows up to 20 seconds for large TV catalogues; launch controls retain an 8-second limit. Opening All apps or the editor refreshes the catalogue while retaining saved Home choices. No discovery polling runs during hidden startup.

## HDMI inputs

Settings → Samsung → Inputs opens the HDMI chooser. The adapter reads the TV’s actual connected and disconnected source records, including sleeping devices that may be listed as disconnected. It does not guess a universal port count or add a fourth default Home control. Missing APIs, denied access and discovery failure produce an unavailable/error state rather than invented ports. The active source comes from the synchronous `tvwindow.getSource()` return value.

Up/Down selects an input. OK requests that exact source; Back returns to Samsung Settings. Retry after a failed load rereads the available sources. A routing error remains an error, and a failed handoff leaves the launcher usable. Timed-out or cancelled requests cannot start a later routing or viewer action; a native request already sent to the TV may itself be uncancellable.

Selecting a source, opening Samsung’s viewer, seeing the expected HDMI picture and waking a CEC device are separate results. The portable implementation does not import firmware-specific viewer payloads or claim to wake a sleeping device. No input discovery or polling runs during hidden startup.

## Preferences and wallpaper

The launcher stores appearance, Home order, recently removed apps, the last launched Home app, wallpaper and rotation locally. List and Dock share these preferences. The existing `cleanframe.home.v1` key is retained, with a fallback read from `cleanframe.shore.v1`. Legacy List maps to Dark + List + Type; Glass Dock and Glass Grid map to Photo + Dock + Glass. App order, wallpaper, rotation and the last Home app are preserved.

The gallery contains 15 bundled wallpapers. Settings → Background → Wallpaper keeps the two-pane Settings frame. Up/Down browses a vertical thumbnail list without wrapping; the right-hand Home preview shows the candidate while the surrounding Settings backdrop stays on the applied photo. OK applies the focused photo and stays in Wallpaper. The tick marks the applied photo and preview status distinguishes unsaved browsing. Back restores the latest applied photo, cancels pending loading and returns to Background’s Wallpaper row. Photo and material assets change as one complete bundle; a failed load restores the applied preview and offers retry. Preview loading waits briefly for remote focus to settle. OK during loading queues application for that photo; another browse move or Back cancels it. Browsing never saves, and repeated OK on the applied photo does not write again.

Settings → Background → Rotation offers Fixed, Each time Home opens, Every 5 minutes, Every 15 minutes and Every hour. Each time Home opens advances once when the launcher loads; a return to the already-running launcher does not advance it. Timed rotation counts only visible Photo Home time in either List or Dock. Panels, flat backgrounds and time spent in other apps pause the cycle. Changing the photo or rotation mode starts a new interval.

Launcher wallpaper is separate from native Art Mode. Runtime photos, materials and available fonts are local assets; they do not require the Mac or a network download.

## Sources

- [Samsung Application API](https://developer.samsung.com/smarttv/develop/api-references/tizen-web-device-api-references/application-api.html): installed-app discovery and application control.
- [Samsung application termination guide](https://developer.samsung.com/smarttv/develop/guides/fundamentals/terminating-applications.html): exiting is not treated as a deterministic Samsung Home route.

The native Home operation and startup configuration from 19 October remain separate from this app update. Home from Netflix was confirmed for that configuration; power-on after Netflix remains provisional. Streaming apps retain their own Back navigation. Netflix did not exit on repeated Back in the observed test, so there was no app-exit destination to verify. No global Back interception or key-filter hook was installed. See [TV status](tv-status.md) for device evidence; this behaviour specification is not an installation or visual-verification record for 0.6.0.

## Themes (Oliver fork)

Settings has a Theme group, first in the list, with five presets in one
build: Minimal Black & White, Device Photos, Futuristic, 90s TV and Art Mode
Overlay. Choosing one applies its whole look (background, layout, app and
control display, font, focus style, material and, for Art Mode Overlay, the
JFK diner wallpaper) in a single save, and the last-applied preset is kept in
saved preferences (`preset` in `cleanframe.home.v1`). A fresh install starts
on Minimal Black & White: dark Dock, text-only tiles, no photo wallpaper.
Changing Background, Layout or Focus afterwards keeps working exactly as
before; it does not clear the stored preset, so Settings keeps showing the
last theme chosen. Saved profiles from before themes existed have no preset
and show as Custom.

Every theme on the Dock home has a hero at the top: the 24-hour clock
enlarged by a transform (the clock stays 48px in the layout, because its
digit cells are measured at that size), today's date, and a time-appropriate
greeting. Below the dock, a Tonight strip names each Home box and its HDMI
port, or that a port still needs picking ("Tonight: Apple TV 4K · HDMI 2 —
PS5 · pick a port — Sky · pick a port"). The strip is Dock-only and hidden
in the 90s TV theme, where the CRT bezel occupies that strip of screen.
Tiles were not made bigger again to fill the space; the backgrounds, hero
and strip do that instead. Remote navigation is unchanged: the hero and the
strip are not focusable.

- Minimal Black & White is monochrome only: a dimmed Petty #43 B&W photo
  as the background (darkened further behind the tile row), text-only
  tiles, a plain white focus outline instead of a glass plate.
- Device Photos is the Apple TV-style theme: each Home tile is a large
  rounded card whose rich artwork fills the tile — a cinematic living
  room behind the Apple TV 4K + remote, a neon game canyon behind the
  PS5 Slim + controller, a floodlit stadium behind the Sky Q box — with
  the transparent photo of the actual box on top. The focused card lifts
  (slightly larger, strong drop shadow, white ring) while the others sit
  flatter and dimmer, and a subtle halo follows focus: that device's
  pre-rendered backdrop on a 1600x760 layer, centred on the focused
  tile and faded to transparent at its edges by a CSS radial-gradient
  mask (gone about 500px past the card edge), so the glow is local to
  the card and the theme background shows through at the screen edges
  while the hero above stays clean (instant swap, no animation). The
  PNGs, card art and backdrops are local-only, installed by
  `scripts/apply-oliver-assets.py` from `.local/oliver-devices/` and
  `.local/oliver-cards/` (made by `.local/make-card-art.py` from
  AI-generated backdrops — no copyrighted poster art); if any file is
  missing, that tile falls back to a plain dark card and the halo stays
  off, and navigation is unaffected.
- Futuristic is a static neon/glass look: a pre-rendered dark nebula
  background (cyan/purple clouds, stars, glowing horizon, faint perspective
  grid), cyan focus plate and clock glow. No live blur, no animation. Its
  device tiles reuse the same Apple TV-style cards (rich card art, device
  photo on top, focused lift with a cyan ring) but keep the nebula
  background — the backdrop does not swap here.
- 90s TV is a physical 90s CRT television set filling the whole screen:
  a pre-rendered 1920x1080 PNG of a chunky plastic bezel (speaker grilles,
  corner screws, brand badge, red power button and standby LED, VHS slot,
  tuning knob, CH/VOL buttons) with the glass cut out to transparent, so
  the launcher lives inside the CRT glass. Inside the glass: the muted
  Memphis-pattern background, a stronger scanline overlay with a vignette
  and a diagonal glass reflection, a green channel OSD ("CH 03 · AV1") and
  chunky bevelled plastic tiles with drop shadows and uppercase labels in
  the magenta/purple/teal/yellow palette. The caption and utils move inside
  the glass; the Tonight strip is hidden because the bezel's bottom band
  occupies that strip. The bezel PNG is local-only, made by
  `.local/make-retro-bezel.py` and installed by
  `scripts/apply-oliver-assets.py` from `.local/oliver-retro/`; without it
  the theme falls back to the Memphis background with CSS scanlines only.
  The type stays the bundled sans (a pixel font would break the measured
  label geometry), so the retro feel comes from the set, the colours and
  the glass, not the typeface.
- Art Mode Overlay fills the screen with the JFK diner photo (or the
  current wallpaper if the local-only photos are not installed) and puts the
  launcher on top as a minimal overlay: unfocused tiles dim so the photo
  reads as art when idle. The focused tile lifts slightly with a soft
  shadow; there is no card art and no backdrop swap, so the photo stays
  the picture. Minimal stays text-only and 90s TV keeps its bevelled
  plastic buttons; neither gets the card treatment.

Theme styling is static CSS under the `th-<preset>` stage class; it never
uses live blur or backdrop filters. The four non-Art themes paint one
pre-rendered 1920x1080 JPEG on the `.scene` layer, local-only and installed
by `scripts/apply-oliver-assets.py` from `.local/oliver-backgrounds/`
(made by `.local/make-backgrounds.py`); if a background file is missing,
that theme falls back to its flat colour/gradient. The backgrounds are
deliberately bright enough to read as a picture, not a void: the vignette
helper in `.local/make-backgrounds.py` darkens the edges, never the centre
(an earlier version had it backwards and dimmed the middle of every
background). Home tiles are 400x280 in icon+label mode and 400x140 in text
mode, with the dock bottom at y=880 on the 1920x1080 stage; remote
navigation and the browser checks are unaffected.

## HDMI shortcuts (Oliver fork)

Home can hold three HDMI shortcut tiles — Apple TV 4K, PS5 and Sky — in that
order on a fresh install. They are not Tizen apps and have no launchable app
ID, so they are never sent to `launchApp`. A tile with no remembered port
opens Settings → Samsung → Inputs, the TV's real input chooser, and says
which device it is for. Choosing a port there switches to it and remembers
the port for that tile in saved preferences (`hdmi` in `cleanframe.home.v1`).
A tile with a remembered port switches straight to it with `setSource`. No
port numbers are assumed anywhere: until Oliver picks a port on the TV,
nothing is mapped. If a tile is removed from Home it appears under Recently
removed in the editor and can be added back from there. The Samsung Apple TV
app is still available in All apps; the Home tile is the Apple TV 4K box.

## Clock and rendering

Both layouts show the TV's local time in 24-hour format, without seconds. It updates at the minute boundary and on return to the launcher. No date or clock panel is shown.

Photographic materials and blurred panel backgrounds are generated before packaging and stay aligned with the full-screen image. Photo colour and contrast metadata are also prepared offline. Navigation does not sample image pixels, run an optics engine or apply live backdrop blur. Flat backgrounds use matching light or dark panel colours. Focus feedback uses transforms and opacity; reduced motion removes animated scaling and movement while retaining opacity feedback.

Hidden prelaunch can install a fully loaded wallpaper bundle without waiting for an animation frame. A valid loaded image remains usable if detached-image decoding rejects. A failed startup bundle retries when the launcher becomes visible; an active wallpaper preview keeps its candidate. Font recovery clears fallback measurements and cached markup. This readiness fallback uses a completed load and nonzero image dimensions; it does not prove a TV has painted the image, and an accepted bundle is not automatically decoded again on return. These paths have browser regression coverage; physical cold-boot behaviour still needs owner observation.
