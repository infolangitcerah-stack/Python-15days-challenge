# refresh-readme-index.ps1
$days = (Get-ChildItem -Directory challenges | Sort-Object Name)
$rows = foreach ($d in $days) {
  $n = $d.Name.Substring(4)  # "01", "02", ...
  $desc = ""
  $readmePath = Join-Path $d.FullName "README.md"
  if (Test-Path $readmePath) {
    $heading = (Select-String -Path $readmePath -Pattern '^\s*#\s*(.+)' -List).Matches.Value
    if ($heading) { $desc = ($heading -replace '^\s*#\s*','').Trim() }
  }
  "| $n | [challenges/$($d.Name)](challenges/$($d.Name)/) | $desc |"
}

$index = "## Index`n| Day | Folder | Description |`n|---:|:-------|:------------|`n" + ($rows -join "`n")

# Read README and replace or append the Index section
$content = Get-Content README.md -Raw
if ($content -match '(?ms)^## Index\b.*?(?=^\#|\Z)') {
  $new = [regex]::Replace($content, '(?ms)^## Index\b.*?(?=^\#|\Z)', $index)
} else {
  $new = $content.TrimEnd() + "`n`n" + $index + "`n"
}
$new | Set-Content README.md -Encoding UTF8
