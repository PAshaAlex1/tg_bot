# Скрипт для создания коммита и отправки на GitHub

Write-Host "=== Инициализация git репозитория ===" -ForegroundColor Green

# Проверка наличия .git
if (-not (Test-Path .git)) {
    Write-Host "Инициализация git репозитория..." -ForegroundColor Yellow
    git init
} else {
    Write-Host "Git репозиторий уже инициализирован" -ForegroundColor Green
}

Write-Host "`n=== Добавление файлов ===" -ForegroundColor Green
git add .

Write-Host "`n=== Создание коммита ===" -ForegroundColor Green
$commitMessage = "feat: итерация 2 - простейший бот с командой /start"
git commit -m $commitMessage

Write-Host "`n=== Проверка remote ===" -ForegroundColor Green
$remote = git remote -v
if (-not $remote) {
    Write-Host "Remote репозиторий не настроен." -ForegroundColor Yellow
    Write-Host "Для отправки на GitHub выполните:" -ForegroundColor Yellow
    Write-Host "  git remote add origin <URL_вашего_репозитория>" -ForegroundColor Cyan
    Write-Host "  git branch -M main" -ForegroundColor Cyan
    Write-Host "  git push -u origin main" -ForegroundColor Cyan
} else {
    Write-Host "Remote репозиторий найден:" -ForegroundColor Green
    Write-Host $remote
    Write-Host "`nОтправка на GitHub..." -ForegroundColor Yellow
    git push
}

Write-Host "`n✓ Готово!" -ForegroundColor Green

