# PowerShell script for running Docker Compose on Windows
# Run this script from PowerShell as Administrator

param(
    [string]$Action = "up",
    [switch]$Build = $false,
    [switch]$Detach = $true,
    [switch]$Help = $false
)

# Colors for output
$Red = [System.ConsoleColor]::Red
$Green = [System.ConsoleColor]::Green
$Yellow = [System.ConsoleColor]::Yellow
$Blue = [System.ConsoleColor]::Blue

function Write-ColorOutput($ForegroundColor) {
    $fc = $host.UI.RawUI.ForegroundColor
    $host.UI.RawUI.ForegroundColor = $ForegroundColor
    if ($args) {
        Write-Output $args
    } else {
        $input | Write-Output
    }
    $host.UI.RawUI.ForegroundColor = $fc
}

function Show-Help {
    Write-ColorOutput $Blue "Docker Compose Helper for Windows"
    Write-Host ""
    Write-Host "Usage: .\run-windows.ps1 [OPTIONS] [ACTION]"
    Write-Host ""
    Write-Host "Actions:"
    Write-Host "  up      - Start services (default)"
    Write-Host "  down    - Stop and remove services"
    Write-Host "  logs    - View logs"
    Write-Host "  build   - Build images"
    Write-Host "  restart - Restart services"
    Write-Host "  ps      - List running services"
    Write-Host ""
    Write-Host "Options:"
    Write-Host "  -Build    - Force rebuild images"
    Write-Host "  -Detach   - Run in background"
    Write-Host "  -Help     - Show this help"
    Write-Host ""
    Write-Host "samples:"
    Write-Host "  .\run-windows.ps1                    # Start services"
    Write-Host "  .\run-windows.ps1 -Build -Detach     # Build and start in background"
    Write-Host "  .\run-windows.ps1 down               # Stop services"
    Write-Host "  .\run-windows.ps1 logs               # View logs"
}

if ($Help) {
    Show-Help
    exit 0
}

# Check if Docker is installed and running
try {
    docker --version | Out-Null
    Write-ColorOutput $Green "Docker is installed"
} catch {
    Write-ColorOutput $Red "Docker is not installed or not in PATH"
    Write-Host "Please install Docker Desktop for Windows from https://www.docker.com/products/docker-desktop"
    exit 1
}

# Check if docker-compose is available
try {
    docker-compose --version | Out-Null
    Write-ColorOutput $Green "Docker Compose is available"
} catch {
    try {
        docker compose version | Out-Null
        Write-ColorOutput $Green "Docker Compose (plugin) is available"
        # Use docker compose (plugin) instead of docker-compose
        $env:COMPOSE_COMMAND = "docker compose"
    } catch {
        Write-ColorOutput $Red "Docker Compose is not available"
        exit 1
    }
}

if (-not $env:COMPOSE_COMMAND) {
    $env:COMPOSE_COMMAND = "docker-compose"
}

# Check if .env file exists, if not create from sample
if (-not (Test-Path ".env")) {
    if (Test-Path ".env.sample") {
        Write-ColorOutput $Yellow "No .env file found, copying from .env.sample"
        Copy-Item ".env.sample" ".env"
    } else {
        Write-ColorOutput $Yellow "No .env file found, creating default one"
        @"
# Database Configuration
POSTGRES_DB=serverdb
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your-secure-password
POSTGRES_PORT=5432

# Server Configuration
SERVER_PORT=3000
NODE_ENV=production

# Application Configuration
DATABASE_URL=postgresql://postgres:your-secure-password@db:5432/serverdb
JWT_SECRET=your-super-secret-jwt-key-change-this-in-production
"@ | Out-File -FilePath ".env" -Encoding UTF8
        Write-ColorOutput $Yellow "Please edit .env file with your configuration"
    }
}

# Build command flags
$buildFlag = if ($Build) { "--build" } else { "" }
$detachFlag = if ($Detach) { "-d" } else { "" }

Write-ColorOutput $Blue "Running Docker Compose action: $Action"

switch ($Action.ToLower()) {
    "up" {
        Write-ColorOutput $Green "Starting services..."
        if ($buildFlag -and $detachFlag) {
            Invoke-Expression "$env:COMPOSE_COMMAND --env-file .env up $buildFlag $detachFlag"
        } elseif ($buildFlag) {
            Invoke-Expression "$env:COMPOSE_COMMAND --env-file .env up $buildFlag"
        } elseif ($detachFlag) {
            Invoke-Expression "$env:COMPOSE_COMMAND --env-file .env up $detachFlag"
        } else {
            Invoke-Expression "$env:COMPOSE_COMMAND --env-file .env up"
        }
    }
    "down" {
        Write-ColorOutput $Yellow "Stopping services..."
        Invoke-Expression "$env:COMPOSE_COMMAND --env-file .env down"
    }
    "logs" {
        Write-ColorOutput $Blue "Viewing logs..."
        Invoke-Expression "$env:COMPOSE_COMMAND --env-file .env logs -f"
    }
    "build" {
		Write-ColorOutput $Blue "Building images..."
		Invoke-Expression "$env:COMPOSE_COMMAND --env-file .env build"
	}
    "restart" {
        Write-ColorOutput $Yellow "Restarting services..."
        Invoke-Expression "$env:COMPOSE_COMMAND --env-file .env restart"
    }
    "ps" {
        Write-ColorOutput $Blue "Listing services..."
        Invoke-Expression "$env:COMPOSE_COMMAND --env-file .env ps"
    }
    default {
        Write-ColorOutput $Red "Unknown action: $Action"
        Show-Help
        exit 1
    }
}

if ($LASTEXITCODE -eq 0) {
    Write-ColorOutput $Green "Command completed successfully"
} else {
    Write-ColorOutput $Red "Command failed with exit code $LASTEXITCODE"
    exit $LASTEXITCODE
} 