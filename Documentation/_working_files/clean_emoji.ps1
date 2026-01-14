# Clean emoji and special characters from documentation files

function Clean-DocFile {
    param([string]$FilePath)
    
    Write-Host "Cleaning $FilePath..."
    $content = Get-Content $FilePath -Encoding UTF8 -Raw
    
    # Replace corrupted emojis
    $content = $content -creplace 'Ÿ"˜', '[DOCS]'
    $content = $content -creplace 'ðŸ', '[BATCH]'
    $content = $content -creplace '1ï¸âƒ£', '[1]'
    $content = $content -creplace '2ï¸âƒ£', '[2]'
    $content = $content -creplace '3ï¸âƒ£', '[3]'
    $content = $content -creplace '4ï¸âƒ£', '[4]'
    $content = $content -creplace '5ï¸âƒ£', '[5]'
    $content = $content -creplace '6ï¸âƒ£', '[6]'
    $content = $content -creplace '7ï¸âƒ£', '[7]'
    $content = $content -creplace '8ï¸âƒ£', '[8]'
    $content = $content -creplace '9ï¸âƒ£', '[9]'
    $content = $content -creplace 'ðŸ"Ÿ', '[10]'
    $content = $content -creplace '10ï¸âƒ£', '[10]'
    $content = $content -creplace '11ï¸âƒ£', '[11]'
    $content = $content -creplace '12ï¸âƒ£', '[12]'
    $content = $content -creplace 'ðŸ"¹', '-'
    $content = $content -creplace 'Pðico', 'Pico'
    
    # Save
    $content | Set-Content $FilePath -Encoding UTF8
    Write-Host "Done cleaning $FilePath"
}

# Clean both files
Clean-DocFile "d:\MFF\Pico\Documentation\Docs_0001_0100.md"
Clean-DocFile "d:\MFF\Pico\Documentation\Docs_0101_0200_NEW.md"

Write-Host "`n[OK] Both files cleaned successfully!"
