# rename-gt2101-files.ps1
# Renames GT2101 archive files to a consistent scheme.
#
# HOW TO RUN
#   1. Put this file in the repo root - the folder containing GT2101\ and GS401\
#   2. Right-click it -> Run with PowerShell
#      (or open PowerShell there and run:  .\rename-gt2101-files.ps1 )
#
# It prints every rename, skips anything already renamed, and warns about
# anything it cannot find. It never deletes and never overwrites.
#
# To see what WOULD happen without changing anything, run:
#   .\rename-gt2101-files.ps1 -WhatIf

[CmdletBinding(SupportsShouldProcess = $true)]
param()

$base = Join-Path $PSScriptRoot "GT2101\engineering-drawings-schematics"

if (-not (Test-Path $base)) {
    Write-Host "Cannot find $base" -ForegroundColor Red
    Write-Host "Put this script in the repo root, next to the GT2101 folder." -ForegroundColor Red
    exit 1
}

$renames = @(
    # ---- board 1 -------------------------------------------------------
    @("disk-1-display-interface\1ASchem.pdf",         "board-1-schematic-sheet-a.pdf")
    @("disk-1-display-interface\1BSchem.pdf",         "board-1-schematic-sheet-b.pdf")
    @("disk-1-display-interface\1Layout.pdf",         "board-1-layout.pdf")
    @("disk-1-display-interface\Board 1 front.jpeg",  "board-1-component-side.jpeg")
    @("disk-1-display-interface\Board 1 back.jpeg",   "board-1-copper-side.jpeg")
    @("disk-1-display-interface\board-1-pcb-front.png", "board-1-component-side-scan.png")
    @("disk-1-display-interface\pcb-back.png",        "board-1-copper-side-scan.png")

    # ---- board 2 -------------------------------------------------------
    @("disk-2ab-servo-motor-drive\2ASchem.pdf",       "board-2-schematic-sheet-a.pdf")
    @("disk-2ab-servo-motor-drive\2BSchem.pdf",       "board-2-schematic-sheet-b.pdf")
    @("disk-2ab-servo-motor-drive\2Layout.pdf",       "board-2-layout.pdf")
    @("disk-2ab-servo-motor-drive\Board 2 front.jpeg","board-2-component-side.jpeg")
    @("disk-2ab-servo-motor-drive\Board 2 back.jpeg", "board-2-copper-side.jpeg")
    @("disk-2ab-servo-motor-drive\Helipot.jpeg",      "board-2-helipot.jpeg")

    # ---- board 3 -------------------------------------------------------
    # NOTE: "Board 3B" was the SECOND PLAIN SPARE, not the ISSUE B board.
    # The genuine ISSUE B board is the pair of .png scans.
    @("disk-3-optical-sensor\3ASchem.pdf",            "board-3-schematic-sheet-a.pdf")
    @("disk-3-optical-sensor\3BSchem.pdf",            "board-3-schematic-sheet-b.pdf")
    @("disk-3-optical-sensor\3CSchem.pdf",            "board-3-schematic-sheet-c.pdf")
    @("disk-3-optical-sensor\3DSchem.pdf",            "board-3-schematic-sheet-d.pdf")
    @("disk-3-optical-sensor\3Layout.pdf",            "board-3-layout.pdf")
    @("disk-3-optical-sensor\Board 3 front.jpeg",     "board-3-spare-1-component-side.jpeg")
    @("disk-3-optical-sensor\Board 3 back.jpeg",      "board-3-spare-1-copper-side.jpeg")
    @("disk-3-optical-sensor\Board 3B front.jpeg",    "board-3-spare-2-component-side.jpeg")
    @("disk-3-optical-sensor\Board 3B back.jpeg",     "board-3-spare-2-copper-side.jpeg")
    @("disk-3-optical-sensor\board-3-front-pcb.png",  "board-3-issue-b-component-side.png")
    @("disk-3-optical-sensor\board-3-back-pcb.png",   "board-3-issue-b-copper-side.png")

    # ---- board 4 -------------------------------------------------------
    @("disk-4-reference-oscillator\4Schem.pdf",       "board-4-schematic.pdf")
    @("disk-4-reference-oscillator\4Layout.pdf",      "board-4-layout.pdf")
    @("disk-4-reference-oscillator\Board 4 front.jpeg","board-4-component-side.jpeg")
    @("disk-4-reference-oscillator\Board 4 back.jpeg","board-4-copper-side.jpeg")

    # ---- board 5 -------------------------------------------------------
    # "Board 5 back.jpeg" is NOT board 5 - it is the toroidal mains transformer.
    @("disk-5-power-supply\5Schem.pdf",               "board-5-schematic.pdf")
    @("disk-5-power-supply\5Layout.pdf",              "board-5-layout.pdf")
    @("disk-5-power-supply\Board 5 front.jpeg",       "board-5-component-side.jpeg")
    @("disk-5-power-supply\Board 5 back.jpeg",        "mains-transformer-toroidal.jpeg")
    @("disk-5-power-supply\Motor PSU board.jpeg",     "gt201-3185nh-b-copper-side.jpeg")

    # ---- motor ---------------------------------------------------------
    @("motor-overview\motSchem.pdf",                  "motor-controller-schematic.pdf")
    @("motor-overview\motpcbLayout.pdf",              "motor-controller-layout.pdf")
    @("motor-overview\backplane.pdf",                 "backplane-tracing.pdf")
)

$done = 0; $skipped = 0; $missing = 0

foreach ($pair in $renames) {
    $oldRel = $pair[0]
    $newName = $pair[1]
    $oldPath = Join-Path $base $oldRel
    $newPath = Join-Path (Split-Path $oldPath -Parent) $newName

    if (Test-Path $newPath) {
        Write-Host "  already done : $newName" -ForegroundColor DarkGray
        $skipped++
        continue
    }
    if (-not (Test-Path $oldPath)) {
        Write-Host "  NOT FOUND    : $oldRel" -ForegroundColor Yellow
        $missing++
        continue
    }
    if ($PSCmdlet.ShouldProcess($oldRel, "rename to $newName")) {
        Rename-Item -LiteralPath $oldPath -NewName $newName
        Write-Host "  renamed      : $oldRel  ->  $newName" -ForegroundColor Green
        $done++
    }
}

# The misspelled turntable page
$bad = Join-Path $PSScriptRoot "GT2101\turntable\index.hmtl"
if (Test-Path $bad) {
    $good = Join-Path $PSScriptRoot "GT2101\turntable\index-old.html"
    if (-not (Test-Path $good)) {
        if ($PSCmdlet.ShouldProcess("GT2101\turntable\index.hmtl", "rename to index-old.html")) {
            Rename-Item -LiteralPath $bad -NewName "index-old.html"
            Write-Host "  renamed      : turntable\index.hmtl  ->  index-old.html" -ForegroundColor Green
            $done++
        }
    }
}

Write-Host ""
Write-Host "$done renamed, $skipped already done, $missing not found." -ForegroundColor Cyan
Write-Host "Nothing was deleted. Check the site builds, then commit." -ForegroundColor Cyan
