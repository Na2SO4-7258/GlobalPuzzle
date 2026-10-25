param([Parameter(Mandatory = $true)][string]$Document)

$ErrorActionPreference = 'Stop'
$source = Get-Item -LiteralPath $Document
$output = Join-Path $source.DirectoryName 'build'
$env:Path = (@($env:Path -split ';' | Where-Object {
    $_ -and (Test-Path -LiteralPath $_ -PathType Container)
}) -join ';')
$tex = (Get-Command pdflatex.exe -ErrorAction Stop).Source
$bib = (Get-Command bibtex.exe -ErrorAction Stop).Source

Push-Location -LiteralPath $source.DirectoryName
try {
    New-Item -ItemType Directory -Path $output -Force | Out-Null
    $texArgs = @('-synctex=1', '-interaction=nonstopmode', '-file-line-error',
        '-halt-on-error', '-recorder', "-output-directory=$output", $source.Name)
    & $tex @texArgs
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

    $passes = 1
    $citations = Get-ChildItem -LiteralPath $output -Filter '*.aux' -Recurse |
        Select-String -SimpleMatch '\citation{'
    if ($citations) {
        & $bib "build/$($source.BaseName)"
        if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
        $passes = 3
    } else {
        $bbl = Join-Path $output ($source.BaseName + '.bbl')
        if (Test-Path -LiteralPath $bbl) { Remove-Item -LiteralPath $bbl }
    }

    for ($pass = 0; $pass -lt $passes; $pass++) {
        & $tex @texArgs
        if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
    }
    exit 0
} finally {
    Pop-Location
}
