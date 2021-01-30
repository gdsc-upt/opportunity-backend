WHITE='\033[0m'
RED=$(tput setaf 1)
GREEN=$(tput setaf 2)
YELLOW=$(tput setaf 3)

print_success() {
  echo -e "${GREEN}$1${WHITE}"
}

print_error() {
  echo -e "${RED}$1${WHITE}"
}

print_warn() {
  echo -e "${YELLOW}$1${WHITE}"
}

print_success "Running black..."
black src
print_success "Done black!"

print_success 'Running pylint...'
pylint src
print_success 'Done pylint!'

print_success 'Running pycodestyle...'
pycodestyle --exclude=migrations --max-line-length=88 src
print_success 'Done pycodestyle!'
