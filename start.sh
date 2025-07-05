#!/bin/bash
set -euo pipefail

# Color output (simplified)
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

log() {
    echo -e "${BLUE}[$(date +'%Y-%m-%d %H:%M:%S')]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[$(date +'%Y-%m-%d %H:%M:%S')]${NC} $1"
}

log_error() {
    echo -e "${RED}[$(date +'%Y-%m-%d %H:%M:%S')]${NC} $1"
}

# Database connection check
if [ -z "${DATABASE_URL:-}" ]; then
    log_error "DATABASE_URL is not set"
    exit 1
fi

log "Starting server setup..."

# Function to test database connectivity
test_db_connection() {
    psql "$DATABASE_URL" -c "SELECT 1;" >/dev/null 2>&1
}

# Wait for database
log "Waiting for database connection..."
max_attempts=30
attempt=1
wait_time=1

while [ $attempt -le $max_attempts ]; do
    if test_db_connection; then
        log_success "Database is ready"
        break
    fi
    
    [ $attempt -eq $max_attempts ] && { log_error "Database connection failed"; exit 1; }
    
    log "Waiting ${wait_time}s (attempt $attempt/$max_attempts)"
    sleep $wait_time
    
    wait_time=$((wait_time < 5 ? wait_time * 2 : 5))
    attempt=$((attempt + 1))
done

# Database setup
log "Configuring database..."
if [ "${NODE_ENV:-development}" = "production" ]; then
    bun run db:migrate || { log_error "Migration failed"; exit 1; }
    log_success "Migrations applied"
else
    bun run db:push || { log_error "Schema push failed"; exit 1; }
    log_success "Schema updated"
fi

log_success "Server starting..."
exec bun run dev