# =====================================================================
#  GT2101 — engineering-drawings-schematics tidy
#  Written 4 September 2026.  ONE-OFF SCRIPT — delete it when done.
#
#  HOW TO RUN IT SAFELY
#  --------------------
#  1. Leave $DryRun = $true below.  Right-click the file →
#     "Run with PowerShell".  It will PRINT everything it would do
#     and change NOTHING.
#  2. Read the output.  If you are happy, change $DryRun to $false
#     and run it again.
#
#  It will never overwrite an existing file, and it skips anything
#  it cannot find — so running it twice is harmless.
#  Nothing here is deleted.  Deletions are listed at the bottom as
#  comments for you to do by hand, deliberately.
# =====================================================================

$DryRun = $false          # <--- change to $false when you are ready

$root = "C:\Users\User\Documents\GitHub\gale-electronics.github.io\GT2101\engineering-drawings-schematics"

# ---------------------------------------------------------------- helpers
function Do-Rename($relFrom, $newName) {
    $from = Join-Path $root $relFrom
    $to   = Join-Path (Split-Path $from -Parent) $newName
    if (-not (Test-Path -LiteralPath $from)) { Write-Host "  skip (not found) : $relFrom" -ForegroundColor DarkGray; return }
    if (Test-Path -LiteralPath $to)          { Write-Host "  SKIP (target exists) : $newName" -ForegroundColor Yellow; return }
    Write-Host "  rename : $relFrom" -ForegroundColor Cyan
    Write-Host "        -> $newName"
    if (-not $DryRun) { Rename-Item -LiteralPath $from -NewName $newName }
}

function Do-Move($relFrom, $relToDir, $newName) {
    $from  = Join-Path $root $relFrom
    $toDir = Join-Path $root $relToDir
    $to    = Join-Path $toDir $newName
    if (-not (Test-Path -LiteralPath $from))  { Write-Host "  skip (not found) : $relFrom" -ForegroundColor DarkGray; return }
    if (-not (Test-Path -LiteralPath $toDir)) { Write-Host "  SKIP (no target folder) : $relToDir" -ForegroundColor Yellow; return }
    if (Test-Path -LiteralPath $to)           { Write-Host "  SKIP (target exists) : $relToDir\$newName" -ForegroundColor Yellow; return }
    Write-Host "  move   : $relFrom" -ForegroundColor Magenta
    Write-Host "        -> $relToDir\$newName"
    if (-not $DryRun) { Move-Item -LiteralPath $from -Destination $to }
}

Write-Host ""
if ($DryRun) { Write-Host "*** DRY RUN — nothing will be changed ***" -ForegroundColor Green }
else         { Write-Host "*** LIVE RUN — files will be renamed and moved ***" -ForegroundColor Red }
Write-Host ""

# ================================================================== BOARD 2
Write-Host "board-2-touch-timing" -ForegroundColor White
Do-Rename "board-2-touch-timing\2Layout.pdf"       "Board-2-Layout.pdf"
Do-Rename "board-2-touch-timing\Board-2BSchem.pdf" "Board-2B-Schem.pdf"

# ================================================================== BOARD 3
# The furthest behind — four filenames still contain spaces.
# NOTE: "Board 3B back/front" are photographs (.jpeg), while 3A-3D are
# schematic SHEETS (.pdf).  Per board-3-fvar-gate.md there is a third
# spare board legended GT201/3275ST ISSUE B, so these are taken to be
# photographs of that board.  ** If that is wrong, say so — a filename
# is exactly where a wrong claim survives longest. **
Write-Host ""
Write-Host "board-3-fvar-gate" -ForegroundColor White
Do-Rename "board-3-fvar-gate\3ASchem.pdf"           "Board-3A-Schem.pdf"
Do-Rename "board-3-fvar-gate\3BSchem.pdf"           "Board-3B-Schem.pdf"
Do-Rename "board-3-fvar-gate\3CSchem.pdf"           "Board-3C-Schem.pdf"
Do-Rename "board-3-fvar-gate\3DSchem.pdf"           "Board-3D-Schem.pdf"
Do-Rename "board-3-fvar-gate\3Layout.pdf"           "Board-3-Layout.pdf"
Do-Rename "board-3-fvar-gate\Board 3 back.jpeg"     "Board-3-back-3275ST.jpeg"
Do-Rename "board-3-fvar-gate\Board 3 front.jpeg"    "Board-3-front-3275ST.jpeg"
Do-Rename "board-3-fvar-gate\Board 3B back.jpeg"    "Board-3-issueB-back-3275ST.jpeg"
Do-Rename "board-3-fvar-gate\Board 3B front.jpeg"   "Board-3-issueB-front-3275ST.jpeg"
Do-Rename "board-3-fvar-gate\board-3-back-pcb.png"  "Board-3-back-pcb-3275ST.png"
Do-Rename "board-3-fvar-gate\board-3-front-pcb.png" "Board-3-front-pcb-3275ST.png"

# ================================================================== BOARD 5
Write-Host ""
Write-Host "board-5-power" -ForegroundColor White
Do-Rename "board-5-power\board-5-pcb-back.png"  "Board-5-back-pcb-3285NH.png"
Do-Rename "board-5-power\board-5-pcb-front.png" "Board-5-front-pcb-3285NH.png"

# ============================================= PCB SCANS — one convention
# Your photographs already agree everywhere:  Board-N-{back|front}-{partno}
# The PCB scans do not.  board-2 has  Board-2-back-pcb-3272ST.png
#                        board-1 & 4 have  Board-N-pcb-back.png
# Adopting board-2's, because it matches the photo convention AND carries
# the part number.  These four bring boards 1 and 4 into line.
Write-Host ""
Write-Host "PCB scans — matching the photo convention" -ForegroundColor White
Do-Rename "board-1-display\Board-1-pcb-back.png"  "Board-1-back-pcb-3155ST.png"
Do-Rename "board-1-display\Board-1-pcb-front.png" "Board-1-front-pcb-3155ST.png"
Do-Rename "board-4-servo\Board-4-pcb-back.png"    "Board-4-back-pcb-3276ST.png"
Do-Rename "board-4-servo\Board-4-pcb-front.png"   "Board-4-front-pcb-3276ST.png"

# ========================================================= MISFILED PAPERS
# Two documents are in folders that describe something else.
Write-Host ""
Write-Host "misfiled documents" -ForegroundColor White

#  Disk-2B-Power-Driver.pdf describes the SEPARATE MOTOR PCB, not board 2.
#  archive-provenance.md documents this: it is where the old
#  "is disk 2 one board or two?" confusion came from.  In a folder now
#  correctly named touch-timing, it reads as if it describes touch-timing.
Do-Move "board-2-touch-timing\Disk-2B-Power-Driver.pdf" "motor-overview" "Disk-2B-Power-Driver.pdf"

#  backplane.pdf is the FANATSON backplane sheet — the source document
#  behind flexicon-backplane-map.md.  Nothing to do with the motor.
#  flexicon-connector/ is already the backplane folder.
Do-Move "motor-overview\backplane.pdf" "flexicon-connector" "Backplane-3281NH.pdf"

# ================================================== flexicon-1.2 file type
# It has no extension, so index.html's allowed-extensions filter hides it
# and that 2 MB photo never appears on the page.  This reads the file's
# magic bytes and tells you what it actually is — it does NOT rename it.
Write-Host ""
Write-Host "flexicon-1.2 — what type is it?" -ForegroundColor White
$f12 = Join-Path $root "flexicon-connector\flexicon-1.2"
if (Test-Path -LiteralPath $f12) {
    $b = Get-Content -LiteralPath $f12 -Encoding Byte -TotalCount 4
    $sig = ($b | ForEach-Object { $_.ToString("X2") }) -join " "
    $type = switch -Regex ($sig) {
        "^FF D8"       { "JPEG  -> rename to  flexicon-1.2.jpeg" }
        "^89 50 4E 47" { "PNG   -> rename to  flexicon-1.2.png"  }
        default        { "unknown ($sig) — open it and see" }
    }
    Write-Host "  first bytes: $sig"
    Write-Host "  looks like : $type" -ForegroundColor Green
} else { Write-Host "  not found" -ForegroundColor DarkGray }

Write-Host ""
Write-Host "Done." -ForegroundColor Green
if ($DryRun) { Write-Host "That was a dry run. Set `$DryRun = `$false to apply." -ForegroundColor Green }
Write-Host ""

# =====================================================================
#  NOT DONE BY THIS SCRIPT — delete these by hand, deliberately
#  ---------------------------------------------------------------
#  Verified safe (I checked each one):
#
#    flexicon-connector\raymon.jpeg
#        byte-identical to remora.jpeg (MD5 ea07ffa0...). Keep remora.
#
#    flexicon-connector\IMG_0275.jpeg
#        byte-identical to top-pico-mount-front.jpeg (MD5 1614cbe2...).
#        Keep the descriptive name.
#
#    motor-overview\motor-findings.md
#        A 22 Aug scrape of the published technical-notes page (its
#        frontmatter has canonical:, og: tags, Jekyll generator). The
#        live page is a full rewrite and a superset. The only thing it
#        held that the live page had lost — the two NMB example part
#        numbers M1N6FB08C / M1N10FB08G — is now restored there.
#
#  Your call, not verified:
#
#    motor-overview\bottom.zip   (17.8 MB)
#        Not a listed extension, so invisible on the published page.
#        GT2101_Motor_Controller_PCB_Bottom.jpg sits beside it — check
#        whether the zip is just that photo's source before keeping
#        17.8 MB in git history for ever.
#
#  Still open, needs your answer, NOT a file operation:
#
#    board-5-power\Motor-PSU-board-3285NH.jpeg
#    board-5-power\Motor-PSU-front-3285NH.jpeg
#        The -3285NH suffix asserts these ARE board 5. If they are a
#        separate motor PSU, that is a false claim baked into a filename.
# =====================================================================
