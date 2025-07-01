#!/bin/bash
# Bash script for running Docker Compose on macOS/Linux
# Make executable with: chmod +x run-unix.sh

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Default values
ACTION="up"
BUILD_FLAG=""
DETACH_FLAG="-d"
SHOW_HELP=false

# Function to display colored output
log() {
    echo -e "${BLUE}[$(date +'%Y-%m-%d %H:%M:%S')]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[$(date +'%Y-%m-%d %H:%M:%S')]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[$(date +'%Y-%m-%d %H:%M:%S')]${NC} $1"
}

log_error() {
    echo -e "${RED}[$(date +'%Y-%m-%d %H:%M:%S')]${NC} $1"
}

show_help() {
    echo -e "${BLUE}🐳 Docker Compose Helper for macOS/Linux${NC}"
    echo ""
    echo "Usage: ./run-unix.sh [OPTIONS] [ACTION]"
    echo ""
    echo "Actions:"
    echo "  up      - Start services (default)"
    echo "  down    - Stop and remove services"
    echo "  logs    - View logs"
    echo "  build   - Build images"
    echo "  restart - Restart services"
    echo "  ps      - List running services"
    echo "  clean   - Remove all containers, networks, and volumes"
    echo ""
    echo "Options:"
    echo "  --build, -b     - Force rebuild images"
    echo "  --detach, -d    - Run in background"
    echo "  --help, -h      - Show this help"
    echo ""
    echo "Examples:"
    echo "  ./run-unix.sh                    # Start services"
    echo "  ./run-unix.sh --build --detach   # Build and start in background"
    echo "  ./run-unix.sh down               # Stop services"
    echo "  ./run-unix.sh logs               # View logs"
    echo "  ./run-unix.sh clean              # Clean up everything"
}

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --build|-b)
            BUILD_FLAG="--build"
            shift
            ;;
        --detach|-d)
            DETACH_FLAG="-d"
            shift
            ;;
        --help|-h)
            SHOW_HELP=true
            shift
            ;;
        up|down|logs|build|restart|ps|clean)
            ACTION="$1"
            shift
            ;;
        *)
            log_error "Unknown option: $1"
            show_help
            exit 1
            ;;
    esac
done

if [[ "$SHOW_HELP" == true ]]; then
    show_help
    exit 0
fi

# Check if Docker is installed and running
if ! command -v docker &> /dev/null; then
    log_error "❌ Docker is not installed or not in PATH"
    log_error "Please install Docker from https://docs.docker.com/get-docker/"
    exit 1
fi

log_success "✅ Docker is installed"

# Check if docker-compose is available
COMPOSE_COMMAND=""
if command -v docker-compose &> /dev/null; then
    COMPOSE_COMMAND="docker-compose"
    log_success "✅ Docker Compose is available"
elif docker compose version &> /dev/null; then
    COMPOSE_COMMAND="docker compose"
    log_success "✅ Docker Compose (plugin) is available"
else
    log_error "❌ Docker Compose is not available"
    exit 1
fi

# Check if Docker daemon is running
if ! docker info &> /dev/null; then
    log_error " Docker daemon is not running"
    log_error "Please start Docker and try again"
    exit 1
fi

# Check if .env file exists, create default if not
if [[ ! -f ".env" ]]; then
    if [[ -f ".env.example" ]]; then
        log_warning "⚠️  No .env file found, copying from .env.example"
        cp ".env.example" ".env"
    else
        log_warning "⚠️  No .env file found, creating default one"
        cat > .env << EOF
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
EOF
        log_warning "📝 Please edit .env file with your configuration"
    fi
fi

log "🚀 Running Docker Compose action: $ACTION"

case "$ACTION" in
    up)
        log_success "🟢 Starting services..."
        $COMPOSE_COMMAND --env-file .env up $BUILD_FLAG $DETACH_FLAG
        ;;
    down)
        log_warning "🟡 Stopping services..."
        $COMPOSE_COMMAND --env-file .env down
        ;;
    logs)
        log "📋 Viewing logs..."
        $COMPOSE_COMMAND --env-file .env logs -f
        ;;
    build)
        log "🔨 Building images..."
        $COMPOSE_COMMAND --env-file .env build
        ;;
    restart)
        log_warning "🔄 Restarting services..."
        $COMPOSE_COMMAND --env-file .env restart
        ;;
    ps)
        log "📊 Listing services..."
        $COMPOSE_COMMAND --env-file .env ps
        ;;
    clean)
        log_warning "🧹 Cleaning up containers, networks, and volumes..."
        $COMPOSE_COMMAND --env-file .env down -v --remove-orphans
        docker system prune -f
        log_success "✅ Cleanup completed"
        ;;
    *)
        log_error "❌ Unknown action: $ACTION"
        show_help
        exit 1
        ;;
esac

if [[ $? -eq 0 ]]; then
    log_success "✅ Command completed successfully"
    
    # Show helpful information after successful 'up' command
    if [[ "$ACTION" == "up" && "$DETACH_FLAG" == "-d" ]]; then
        echo ""
        log "Services are running in the background"
        log " Server: http://localhost:${SERVER_PORT:-3000}"
        log " Database: localhost:${POSTGRES_PORT:-5432}"
        log "View logs: ./run-unix.sh logs"
        log "Stop services: ./run-unix.sh down"
    fi
else
    log_error "❌ Command failed with exit code $?"
    exit $?
fi 