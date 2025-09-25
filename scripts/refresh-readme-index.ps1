# refresh-readme-index.ps1
\ = "15days-challenge"

\ = (Get-ChildItem -Directory \ | Sort-Object Name)
\ = foreach (\ in \) {
  \ = \.Name.Substring(4)  # "01", "02", ...
  \ = ""
  \ = Join-Path \.FullName "README.md"
  if (Test-Path \) {
    \ = (Select-String -Path \ -Pattern "^\s*#\s*(.+)" -List).Matches.Value
    if (\) { \ = (\ -replace "^\s*#\s*","").Trim() }
  }
  "| \ | [\/\](\/\/) | \ |"
}

\ = "## Index
| Day | Folder | Description |
|---:|:-------|:------------|
" + (\ -join "
")

\# Python 15 Days Challenge

Consolidated daily challenges with history preserved.

## Index
| Day | Folder | Description |
|---:|:-------|:------------|
| 01 | [15days-challenge/day_01](15days-challenge/day_01/) | Day-1 Python Project 🐍 |
| 02 | [15days-challenge/day_02](15days-challenge/day_02/) | 🚀 Day 2 - Python Challenge |
| 03 | [15days-challenge/day_03](15days-challenge/day_03/) | Day 3 Python Challenge |
| 04 | [15days-challenge/day_04](15days-challenge/day_04/) | 🚀 Day 4 - Python Challenge |
| 05 | [15days-challenge/day_05](15days-challenge/day_05/) | 🚀 Day 5 - Python Challenge |
| 06 | [15days-challenge/day_06](15days-challenge/day_06/) | Day 6 - Python Challenge |
| 07 | [15days-challenge/day_07](15days-challenge/day_07/) | 🏋️ Day 7 - Python Challenge |
| 08 | [15days-challenge/day_08](15days-challenge/day_08/) | Day 8 – Currency Converter 💱 |
| 09 | [15days-challenge/day_09](15days-challenge/day_09/) | Day 9 – Quiz Game App ❓ |
| 10 | [15days-challenge/day_10](15days-challenge/day_10/) | Day 10 – Python Challenge |
| 11 | [15days-challenge/day_11](15days-challenge/day_11/) | 🍔 Restaurant Order & Billing App |
| 12 | [15days-challenge/day_12](15days-challenge/day_12/) | 🎮 Futuristic Tic-Tac-Toe ❌⭕ |
| 13 | [15days-challenge/day_13](15days-challenge/day_13/) | 🪨📜✂️ Rock, Paper, Scissors Game |
| 14 | [15days-challenge/day_14](15days-challenge/day_14/) |  |

 = Get-Content README.md -Raw
if (\# Python 15 Days Challenge

Consolidated daily challenges with history preserved.

## Index
| Day | Folder | Description |
|---:|:-------|:------------|
| 01 | [15days-challenge/day_01](15days-challenge/day_01/) | Day-1 Python Project 🐍 |
| 02 | [15days-challenge/day_02](15days-challenge/day_02/) | 🚀 Day 2 - Python Challenge |
| 03 | [15days-challenge/day_03](15days-challenge/day_03/) | Day 3 Python Challenge |
| 04 | [15days-challenge/day_04](15days-challenge/day_04/) | 🚀 Day 4 - Python Challenge |
| 05 | [15days-challenge/day_05](15days-challenge/day_05/) | 🚀 Day 5 - Python Challenge |
| 06 | [15days-challenge/day_06](15days-challenge/day_06/) | Day 6 - Python Challenge |
| 07 | [15days-challenge/day_07](15days-challenge/day_07/) | 🏋️ Day 7 - Python Challenge |
| 08 | [15days-challenge/day_08](15days-challenge/day_08/) | Day 8 – Currency Converter 💱 |
| 09 | [15days-challenge/day_09](15days-challenge/day_09/) | Day 9 – Quiz Game App ❓ |
| 10 | [15days-challenge/day_10](15days-challenge/day_10/) | Day 10 – Python Challenge |
| 11 | [15days-challenge/day_11](15days-challenge/day_11/) | 🍔 Restaurant Order & Billing App |
| 12 | [15days-challenge/day_12](15days-challenge/day_12/) | 🎮 Futuristic Tic-Tac-Toe ❌⭕ |
| 13 | [15days-challenge/day_13](15days-challenge/day_13/) | 🪨📜✂️ Rock, Paper, Scissors Game |
| 14 | [15days-challenge/day_14](15days-challenge/day_14/) |  |

 -match "(?ms)^## Index\b.*?(?=^\#|\Z)") {
  \ = [regex]::Replace(\# Python 15 Days Challenge

Consolidated daily challenges with history preserved.

## Index
| Day | Folder | Description |
|---:|:-------|:------------|
| 01 | [15days-challenge/day_01](15days-challenge/day_01/) | Day-1 Python Project 🐍 |
| 02 | [15days-challenge/day_02](15days-challenge/day_02/) | 🚀 Day 2 - Python Challenge |
| 03 | [15days-challenge/day_03](15days-challenge/day_03/) | Day 3 Python Challenge |
| 04 | [15days-challenge/day_04](15days-challenge/day_04/) | 🚀 Day 4 - Python Challenge |
| 05 | [15days-challenge/day_05](15days-challenge/day_05/) | 🚀 Day 5 - Python Challenge |
| 06 | [15days-challenge/day_06](15days-challenge/day_06/) | Day 6 - Python Challenge |
| 07 | [15days-challenge/day_07](15days-challenge/day_07/) | 🏋️ Day 7 - Python Challenge |
| 08 | [15days-challenge/day_08](15days-challenge/day_08/) | Day 8 – Currency Converter 💱 |
| 09 | [15days-challenge/day_09](15days-challenge/day_09/) | Day 9 – Quiz Game App ❓ |
| 10 | [15days-challenge/day_10](15days-challenge/day_10/) | Day 10 – Python Challenge |
| 11 | [15days-challenge/day_11](15days-challenge/day_11/) | 🍔 Restaurant Order & Billing App |
| 12 | [15days-challenge/day_12](15days-challenge/day_12/) | 🎮 Futuristic Tic-Tac-Toe ❌⭕ |
| 13 | [15days-challenge/day_13](15days-challenge/day_13/) | 🪨📜✂️ Rock, Paper, Scissors Game |
| 14 | [15days-challenge/day_14](15days-challenge/day_14/) |  |

, "(?ms)^## Index\b.*?(?=^\#|\Z)", \)
} else {
  \ = \# Python 15 Days Challenge

Consolidated daily challenges with history preserved.

## Index
| Day | Folder | Description |
|---:|:-------|:------------|
| 01 | [15days-challenge/day_01](15days-challenge/day_01/) | Day-1 Python Project 🐍 |
| 02 | [15days-challenge/day_02](15days-challenge/day_02/) | 🚀 Day 2 - Python Challenge |
| 03 | [15days-challenge/day_03](15days-challenge/day_03/) | Day 3 Python Challenge |
| 04 | [15days-challenge/day_04](15days-challenge/day_04/) | 🚀 Day 4 - Python Challenge |
| 05 | [15days-challenge/day_05](15days-challenge/day_05/) | 🚀 Day 5 - Python Challenge |
| 06 | [15days-challenge/day_06](15days-challenge/day_06/) | Day 6 - Python Challenge |
| 07 | [15days-challenge/day_07](15days-challenge/day_07/) | 🏋️ Day 7 - Python Challenge |
| 08 | [15days-challenge/day_08](15days-challenge/day_08/) | Day 8 – Currency Converter 💱 |
| 09 | [15days-challenge/day_09](15days-challenge/day_09/) | Day 9 – Quiz Game App ❓ |
| 10 | [15days-challenge/day_10](15days-challenge/day_10/) | Day 10 – Python Challenge |
| 11 | [15days-challenge/day_11](15days-challenge/day_11/) | 🍔 Restaurant Order & Billing App |
| 12 | [15days-challenge/day_12](15days-challenge/day_12/) | 🎮 Futuristic Tic-Tac-Toe ❌⭕ |
| 13 | [15days-challenge/day_13](15days-challenge/day_13/) | 🪨📜✂️ Rock, Paper, Scissors Game |
| 14 | [15days-challenge/day_14](15days-challenge/day_14/) |  |

.TrimEnd() + "

" + \ + "
"
}
\ | Set-Content README.md -Encoding UTF8
